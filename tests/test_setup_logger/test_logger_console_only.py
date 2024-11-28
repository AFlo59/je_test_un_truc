import logging
import sys
from io import StringIO
from scripts.setup_logger import setup_logger

def test_logger_console_only():
    buffer = StringIO()
    handler = logging.StreamHandler(buffer)
    handler.setFormatter(logging.Formatter("%(message)s"))

    logger = setup_logger(
        name="console_logger",
        log_file=None,
        console=True,
        level=logging.INFO,
        console_format="%(message)s"
    )
    logger.addHandler(handler)  # Ajouter le handler pour capturer le flux
    logger.info("Message INFO dans la console uniquement.")

    captured = buffer.getvalue().strip()
    assert "Message INFO dans la console uniquement." in captured, "Le message n'a pas été capturé dans la console."
