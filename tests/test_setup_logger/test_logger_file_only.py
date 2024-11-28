import logging
import os
from scripts.setup_logger import setup_logger

def test_logger_file_only(tmp_path):
    log_file = tmp_path / "file_only.log"

    # Configure le logger avec le niveau DEBUG
    logger = setup_logger(
        name="file_logger",
        log_file=str(log_file),
        console=False,
        level=logging.DEBUG  # Assurez-vous que le niveau est DEBUG
    )
    logger.debug("Message DEBUG dans le fichier uniquement.")

    # Vérifie que le fichier de log contient le message
    assert os.path.exists(log_file), "Le fichier de log n'a pas été créé."
    with open(log_file, "r") as file:
        log_content = file.read()
        assert "Message DEBUG dans le fichier uniquement." in log_content, (
            f"Le message attendu n'est pas dans le fichier. Contenu actuel : {log_content}"
        )
