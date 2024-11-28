import os
import pytest
from scripts.setup_logger import ensure_log_directory_exists


def test_create_logs_directory(tmp_path):
    # Utiliser un chemin temporaire pour éviter de modifier le système
    log_dir = tmp_path / "logs"
    ensure_log_directory_exists(str(log_dir))
    assert log_dir.exists() and log_dir.is_dir(), "Le dossier de logs n'a pas été créé correctement."
