# Taxi meter

A rainbow-styled command-line taxi meter built with Python and asyncio.

## Features

- Real-time fare calculation with moving and stopped rates
- Colorful CLI interface using Rich and rich-gradient
- Journey history saved to `journey_history.txt`
- Structured logging to `taxi.log` via Loguru
- Configurable rates via `set_rates()`
- Unit tested with pytest

## Project Structure

```
proyecto1_Anahi/
├── main.py              # Entry point
├── back.py              # CLI logic and asyncio input handling
├── taxi.py              # Taxi class and fare logic
├── logger.py            # Loguru setup
├── test_taxi.py         # Unit tests
├── taxi.log             # Auto-generated log file
└── journey_history.txt  # Auto-generated journey history
```

## Requirements

- Python >= 3.14
- uv (package manager)

## Installation

```bash
git clone https://github.com/Bootcamp-IA-MAD-P7/proyecto1_Anahi.git
cd proyecto1_Anahi
uv sync
```

## Usage

```bash
uv run python main.py
```

## Commands

| Key | Action          |
|-----|-----------------|
| `i` | Start journey   |
| `m` | Set moving      |
| `p` | Pause           |
| `f` | End journey     |
| `s` | Exit            |

## Running Tests

```bash
uv run pytest test_taxi.py -v
```

## Tech Stack

- Python 3.14
- asyncio
- Rich + rich-gradient
- Loguru
- readchar
- pytest