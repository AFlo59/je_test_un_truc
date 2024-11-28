import os
from scripts.setup_logger import setup_multi_logger


def test_setup_multi_file_only(tmp_path):
    log_file1 = tmp_path / "multi1.log"
    log_file2 = tmp_path / "multi2.log"
    logger = setup_multi_logger(name="multi_logger", log_files=[str(log_file1), str(log_file2)], console=False)
    logger.warning("Message WARNING dans plusieurs fichiers.")
    
    # Vérification des fichiers
    for log_file in [log_file1, log_file2]:
        assert os.path.exists(log_file), f"Le fichier {log_file} n'a pas été créé."
        with open(log_file, "r") as file:
            assert "WARNING - Message WARNING dans plusieurs fichiers." in file.read(), f"Le message n'est pas dans {log_file}."
