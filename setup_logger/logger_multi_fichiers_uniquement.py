import logging
from scripts.setup_logger import setup_multi_logger

logger = setup_multi_logger(
    name="multi_logger",
    log_files=["logs/app1.log", "logs/app2.log"],  
    level=logging.WARNING,                        
    console=False                                 
)

# Logs de test pour chaque niveau
logger.debug("Ceci est un message DEBUG (niveau 10).")
logger.info("Ceci est un message INFO (niveau 20).")
logger.warning("Ceci est un message WARNING (niveau 30).")
logger.error("Ceci est un message ERROR (niveau 40).")
logger.critical("Ceci est un message CRITICAL (niveau 50).")
