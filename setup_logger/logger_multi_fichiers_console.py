import logging
from scripts.setup_logger import setup_multi_logger

# Configurer le logger multi-fichiers
logger = setup_multi_logger(
    name="multi_all_levels_logger",
    log_files=["logs/all_levels_file1.log", "logs/all_levels_file2.log"],
    level=logging.DEBUG,             
    console=True                     
)

# Logs de test pour chaque niveau
logger.debug("Multi-log DEBUG (niveau 10).")
logger.info("Multi-log INFO (niveau 20).")
logger.warning("Multi-log WARNING (niveau 30).")
logger.error("Multi-log ERROR (niveau 40).")
logger.critical("Multi-log CRITICAL (niveau 50).")
