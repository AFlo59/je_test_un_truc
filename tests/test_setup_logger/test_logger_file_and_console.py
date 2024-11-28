import logging
import sys
from io import StringIO
import os
from scripts.setup_logger import setup_logger

def test_logger_file_and_console(tmp_path):
    log_file = tmp_path / "file_and_console.log"
    buffer = StringIO()
    handler = logging.StreamHandler(buffer)
    handler.setFormatter(logging.Formatter("%(message)s"))

    logger = setup_logger(
        name="file_console_logger",
        log_file=str(log_file),
        console=True,
        level=logging.INFO,
        console_format="%(message)s",
        file_format="%(message)s"
    )
    logger.addHandler(handler)  # Ajouter le handler pour capturer le flux
    logger.info("Message INFO dans fichier et console.")

    # Vérification du fichier
    assert os.path.exists(log_file), "Le fichier de log n'a pas été créé."
    with open(log_file, "r") as file:
        log_content = file.read()
        assert "Message INFO dans fichier et console." in log_content, (
            f"Le message attendu n'est pas dans le fichier. Contenu actuel : {log_content}"
        )

    # Vérification de la console
    captured = buffer.getvalue().strip()
    assert "Message INFO dans fichier et console." in captured, "Le message n'a pas été capturé dans la console."
