from scripts.setup_logger import setup_logger
from io import StringIO
import os
import sys

def test_logger_file_and_console(tmp_path):
    log_file = tmp_path / "file_and_console.log"
    buffer = StringIO()
    sys.stdout = buffer
    logger = setup_logger(name="file_console_logger", log_file=str(log_file), console=True)
    logger.info("Message INFO dans fichier et console.")
    sys.stdout = sys.__stdout__
    assert os.path.exists(log_file), "Le fichier de log n'a pas été créé."
    with open(log_file, "r") as file:
        assert "Message INFO dans fichier et console." in file.read()
    assert "Message INFO dans fichier et console." in buffer.getvalue()
