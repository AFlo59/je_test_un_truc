from scripts.setup_logger import setup_multi_logger

logger = setup_multi_logger(
    name="multi_logger",
    log_files=["logs/app1.log", "logs/app2.log"],  
    level="logging.WARNING",                        
    console=False                                 
)

logger.debug("Multi-log DEBUG (niveau 10).")
logger.info("Multi-log INFO (niveau 20).")
logger.warning("Multi-log WARNING (niveau 30).")
logger.error("Multi-log ERROR (niveau 40).")
logger.critical("Multi-log CRITICAL (niveau 50).")
