from scripts.setup_logger import setup_logger
from io import StringIO
import sys

def test_logger_console_only():
    buffer = StringIO()
    sys.stdout = buffer
    logger = setup_logger(name="console_logger", log_file=None, console=True)
    logger.info("Message INFO dans la console uniquement.")
    sys.stdout = sys.__stdout__
    assert "Message INFO dans la console uniquement." in buffer.getvalue()
