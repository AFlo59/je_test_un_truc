import logging
import os
from typing import List, Optional


def ensure_log_directory_exists(log_dir: str = "logs") -> None:
    """
    Vérifie si le dossier de logs existe, sinon le crée.

    :param log_dir: Chemin du dossier de logs (par défaut: "logs").
    """
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
        print(f"Dossier '{log_dir}' créé avec succès.")


def setup_logger(
    name: str,
    log_file: Optional[str] = None,
    level: int = logging.INFO,
    console: bool = True,
    file_only: bool = False,
    file_format: str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    console_format: str = "%(asctime)s - %(levelname)s - %(message)s",
) -> logging.Logger:
    """
    Configure un logger modulaire pour fichier, console, ou les deux.

    :param name: Nom du logger.
    :param log_file: Chemin du fichier de log (optionnel).
    :param level: Niveau de log (logging.DEBUG, logging.INFO, etc.).
    :param console: Active la sortie console (par défaut: True).
    :param file_only: Désactive la console si True (par défaut: False).
    :param file_format: Format des logs dans le fichier.
    :param console_format: Format des logs dans la console.
    :return: Instance du logger configuré.
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Supprime les handlers existants pour éviter les doublons
    if logger.hasHandlers():
        logger.handlers.clear()

    # Formatter pour les logs fichier et console
    formatter_file = logging.Formatter(file_format)
    formatter_console = logging.Formatter(console_format)

    # Assurer que le dossier logs existe
    if log_file:
        log_dir = os.path.dirname(log_file) or "logs"
        ensure_log_directory_exists(log_dir)

        # Handler pour le fichier
        file_handler = logging.FileHandler(log_file, mode="a")  # Mode "append"
        file_handler.setLevel(level)
        file_handler.setFormatter(formatter_file)
        logger.addHandler(file_handler)

    # Handler pour la console
    if console and not file_only:
        console_handler = logging.StreamHandler()
        console_handler.setLevel(level)
        console_handler.setFormatter(formatter_console)
        logger.addHandler(console_handler)

    return logger


def setup_multi_logger(
    name: str,
    log_files: List[str],
    level: int = logging.INFO,
    console: bool = True,
    file_format: str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    console_format: str = "%(asctime)s - %(levelname)s - %(message)s",
) -> logging.Logger:
    """
    Configure un logger multi-fichiers et console.

    :param name: Nom du logger.
    :param log_files: Liste des chemins de fichiers de log.
    :param level: Niveau de log (logging.DEBUG, logging.INFO, etc.).
    :param console: Active la sortie console (par défaut: True).
    :param file_format: Format des logs dans les fichiers.
    :param console_format: Format des logs dans la console.
    :return: Instance du logger configuré.
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Supprime les handlers existants pour éviter les doublons
    if logger.hasHandlers():
        logger.handlers.clear()

    # Formatter pour les logs fichier et console
    formatter_file = logging.Formatter(file_format)
    formatter_console = logging.Formatter(console_format)

    # Assurer que chaque fichier de log est prêt
    for log_file in log_files:
        log_dir = os.path.dirname(log_file) or "logs"
        ensure_log_directory_exists(log_dir)

        # Handler pour chaque fichier
        file_handler = logging.FileHandler(log_file, mode="a")  # Mode "append"
        file_handler.setLevel(level)
        file_handler.setFormatter(formatter_file)
        logger.addHandler(file_handler)

    # Handler pour la console
    if console:
        console_handler = logging.StreamHandler()
        console_handler.setLevel(level)
        console_handler.setFormatter(formatter_console)
        logger.addHandler(console_handler)

    return logger
