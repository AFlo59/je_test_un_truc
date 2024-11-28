import logging
from scripts.setup_logger import setup_logger

# Configurer le logger
logger = setup_logger(
    name="all_levels_logger",
    log_file="logs/all_levels.log",  
    level=logging.DEBUG,            
    console=True                    
)

# Logs de test pour chaque niveau
logger.debug("Ceci est un message DEBUG (niveau 10).")
logger.info("Ceci est un message INFO (niveau 20).")
logger.warning("Ceci est un message WARNING (niveau 30).")
logger.error("Ceci est un message ERROR (niveau 40).")
logger.critical("Ceci est un message CRITICAL (niveau 50).")
