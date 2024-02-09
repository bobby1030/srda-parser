import os, logging

# set up logging
logger = logging.getLogger("backend")
logger.setLevel(os.environ.get("LOG_LEVEL", "INFO"))

handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s"))

logger.addHandler(handler)