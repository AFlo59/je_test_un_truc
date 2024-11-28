from scripts.setup_logger import setup_multi_logger
import os

def test_multi_logger(tmp_path):
    log_files = [tmp_path / "file1.log", tmp_path / "file2.log"]
    logger = setup_multi_logger(name="multi_logger", log_files=[str(f) for f in log_files], console=False)
    logger.warning("Message WARNING multi-loggers.")
    for log_file in log_files:
        assert os.path.exists(log_file), f"Le fichier {log_file} n'a pas été créé."
        with open(log_file, "r") as file:
            assert "Message WARNING multi-loggers." in file.read()
