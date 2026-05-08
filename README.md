# Taximeter 
CLI taximeter simulator built in Python using asyncio and OOP.

## Structure
```
proyecto1_Anahi/
├── taxi.py        # Taxi class — pure fare logic
├── back.py        # async engine — timing and user input
├── main.py        # entry point
├── pyproject.toml
└── uv.lock
```

## How It Works
The project is split into 3 layers:
**taxi.py** Contains the Taxi class. It holds the state of the taximeter (fare, journey status, movement status) and the methods to modify it.  
**back.py** Contains the async engine. It runs two coroutines concurrently via asyncio.gather: 
- Fare counter - Calls meter.taximeter() every second.
- Input handler - Listens for user commands. User input is captured keystroke by keystroke using readchar, with no Enter required.
**main.py** Entry point. It starts the event loop with asyncio.run(main()).

## Interface
The terminal interface uses Rich and rich-gradient to display colorful menus and improve the visual experience of the application.

## Requirements 
- Python 3.10+
- [uv](https://github.com/astral-sh/uv)

## Installation
````bash
git clone https://github.com/Bootcamp-IA-MAD-P7/proyecto1_Anahi.git
cd proyecto1_Anahi
uv sync
````
 
## Usage
 
```bash
uv run main.py
```

## Commands
| Key | Action |
|-----|--------|
| `i` | Start journey |
| `m` | Set moving |
| `p` | Set stationary |
| `f` | End journey |
| `s` | Quit |