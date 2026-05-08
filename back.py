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
    print("🚕 Gracias por usar el taxímetro!")
    print(
    "\nComandos:"
    "\n  [i] Iniciar viaje"
    "\n  [m] Comenzar a moverse"
    "\n  [p] Hacer una parada"
    "\n  [f] Finalizar el viaje"
    "\n  [s] Salir\n"
    )

