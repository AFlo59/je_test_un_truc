from scripts.setup_logger import setup_logger

logger = setup_logger(
    name="app_logger",
    log_file="logs/app.log",   
    level="logging.INFO",
    console=False               
)

logger.debug("Multi-log DEBUG (niveau 10).")
logger.info("Multi-log INFO (niveau 20).")
logger.warning("Multi-log WARNING (niveau 30).")
logger.error("Multi-log ERROR (niveau 40).")
logger.critical("Multi-log CRITICAL (niveau 50).")
