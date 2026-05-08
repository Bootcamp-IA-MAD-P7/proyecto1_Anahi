import asyncio
import readchar
from taxi import Taxi, RATE_MOVING, RATE_STOPPED

meter = Taxi()

VALID_COMMANDS = {"i", "m", "p", "f", "s"}

async def count_fare():
    while meter.journey_active:
        await asyncio.sleep(1)
        if meter.journey_active:
            meter.taximeter()
            print(f"💰Coste del viaje: {meter.fare:.2f}€")

async def get_input():
    loop = asyncio.get_event_loop()
    while True:
        key = await loop.run_in_executor(None, readchar.readkey)
        key = key.strip().casefold()
        if key in VALID_COMMANDS:
            print(key)   # echo so user sees what they pressed
            return key

async def handle_input():
    print("🚕 Gracias por usar el taxímetro!\nPor favor, elige uno de los siguientes comandos: ")
    print(
    "\nComandos:"
    "\n  [i] Iniciar viaje"
    "\n  [m] Comenzar a moverse"
    "\n  [p] Hacer una parada"
    "\n  [f] Finalizar el viaje"
    "\n  [s] Salir\n"
    )
    while True:
        print(">> ", end="", flush=True)
        # end="" means don't add a newline after printing
        # flush=True forces the text to appear immediately
        # without it the >> might not show until something else prints
        command = await get_input()

        match command:
            case "i":
                if meter.journey_active:
                    print("  ⚠️  Ya hay un trayecto activo.")
                else:
                    meter.start_journey()
                    print("  ✅ Trayecto iniciado. Tarifa en marcha.")
                    asyncio.create_task(count_fare())
            case "m":
                if not meter.journey_active:
                    print("  ⚠️  No hay trayecto activo. Pulsa [i] para iniciar.")
                else:
                    meter.set_moving()
                    print("  🚗 Taxi en movimiento.")

            case "p":
                if not meter.journey_active:
                    print("  ⚠️  No hay trayecto activo. Pulsa [i] para iniciar.")
                else:
                    meter.set_stopped()
                    print("  🛑 Taxi parado. El taxímetro sigue corriendo.")

            case "f":
                if not meter.journey_active:
                    print("  ⚠️  No hay trayecto activo.")
                else:
                    final = meter.end_journey()
                    print(f"\n  🏁 Trayecto finalizado. Total: €{final:.2f}")
                    print("  Pulsa [i] para nuevo trayecto o [s] para salir.\n")

            case "s":
                if meter.journey_active:
                    meter.end_journey()
                print("\n  👋 ¡Hasta luego!\n")
                break

async def main():
    await handle_input()