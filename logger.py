from loguru import logger

logger.add("taxi.log", rotation="1 MB", retention="1 week")

