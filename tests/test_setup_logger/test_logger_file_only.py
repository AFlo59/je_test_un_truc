import os
from scripts.setup_logger import setup_logger

def test_logger_file_only(tmp_path):
    log_file = tmp_path / "file_only.log"
    logger = setup_logger(name="file_logger", log_file=str(log_file), console=False)
    logger.debug("Message DEBUG dans le fichier uniquement.")
    assert os.path.exists(log_file), "Le fichier de log n'a pas été créé."
    with open(log_file, "r") as file:
        assert "Message DEBUG dans le fichier uniquement." in file.read()
