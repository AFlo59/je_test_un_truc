import os
import logging
from io import StringIO
from scripts.setup_logger import setup_multi_logger


def test_setup_multi_file_and_console(tmp_path):
    buffer = StringIO()
    log_file1 = tmp_path / "multi1.log"
    log_file2 = tmp_path / "multi2.log"

    # Ajouter un handler pour capturer les logs de la console
    stream_handler = logging.StreamHandler(buffer)
    stream_handler.setFormatter(logging.Formatter("%(message)s"))

    # Configurer le logger
    logger = setup_multi_logger(name="multi_logger", log_files=[str(log_file1), str(log_file2)], console=True)
    logger.addHandler(stream_handler)  # Attacher le handler de flux

    logger.warning("Message WARNING dans plusieurs fichiers et console.")
    
    # Vérification des fichiers
    for log_file in [log_file1, log_file2]:
        assert os.path.exists(log_file), f"Le fichier {log_file} n'a pas été créé."
        with open(log_file, "r") as file:
            log_content = file.read()
            assert "Message WARNING dans plusieurs fichiers et console." in log_content, (
                f"Le message attendu n'est pas dans le fichier. Contenu actuel : {log_content}"
            )
    
    # Vérification de la console
    captured = buffer.getvalue().strip()
    assert "Message WARNING dans plusieurs fichiers et console." in captured, "Le message n'a pas été capturé dans la console."
