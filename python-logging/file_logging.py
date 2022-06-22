import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    filename="./logs/file_logging.log"
)

logger = logging.getLogger(__name__)

for i in range(1, 11):
    logger.info(f"{i}: Custom Logging Message.")

