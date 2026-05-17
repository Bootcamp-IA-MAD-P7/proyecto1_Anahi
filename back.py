import asyncio
import readchar
from taxi import Taxi, RATE_MOVING, RATE_STOPPED

from rich import print
from rich.console import Console
from rich_gradient import Gradient

console = Console()

meter = Taxi()

VALID_COMMANDS = {"i", "m", "p", "f", "s"}

async def count_fare():
    while meter.journey_active:
        await asyncio.sleep(1)
        if meter.journey_active:
            meter.taximeter()
            console.print(f"Coste del viaje: {meter.fare:.2f}€", style="#B088C8")

async def get_input():
    loop = asyncio.get_event_loop()
    while True:
        key = await loop.run_in_executor(None, readchar.readkey)
        key = key.strip().casefold()
        if key in VALID_COMMANDS:
            print(key)   # echo so user sees what they pressed
            return key

async def handle_input():
    console.print(
    Gradient(
        "¡Hola!Gracias por usar el servicio de taxi\n"
        "Por favor, elige uno de los siguientes comandos:",
        rainbow=True
        )
    )
    console.print(
    Gradient(
        "\nComandos:"
        "\n  (i) Iniciar viaje"
        "\n  (m) Volver a moverse"
        "\n  (p) Hacer una parada"
        "\n  (f) Finalizar el viaje"
        "\n  (s) Salir",
        rainbow=True
        )
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
                    console.print("Ya hay un trayecto activo.", style="bold cyan")
                else:
                    meter.start_journey()
                    print("Trayecto iniciado. Tarifa en marcha.")
                    asyncio.create_task(count_fare())
            case "m":
                if not meter.journey_active:
                    console.print("No hay trayecto activo. Pulsa [i] para iniciar.", style="bold cyan")
                else:
                    meter.set_moving()
                    print("Taxi en movimiento.")

            case "p":
                if not meter.journey_active:
                    console.print("No hay trayecto activo. Pulsa [i] para iniciar.", style="bold cyan")
                else:
                    meter.set_stopped()
                    console.print("Taxi parado. El taxímetro sigue corriendo.", style="#FFB8CC")

            case "f":
                if not meter.journey_active:
                    console.print("No hay trayecto activo.", style="bold cyan")
                else:
                    final = meter.end_journey()
                    console.print(Gradient(f"\n Trayecto finalizado. Total: €{final:.2f}", rainbow=True))
                    console.print(Gradient(" Pulsa (i) para nuevo trayecto o (s) para salir.\n", rainbow=True))

            case "s":
                if meter.journey_active:
                    meter.end_journey()
                console.print(Gradient("\n¡Muchas gracias!\n", rainbow=True))
                break

async def main():
    await handle_input()