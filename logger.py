from loguru import logger
from pathlib import Path

for handler_id in list(logger._core.handlers.keys()):
    logger.remove(handler_id)

LOG_PATH = Path(r"C:\Users\anahi\VS_code\F5\taximetro\proyecto1_Anahi") / "taxi.log"
logger.add(LOG_PATH, rotation="1 MB", retention="1 week")