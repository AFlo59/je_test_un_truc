import os
from scripts.setup_logger import ensure_log_directory_exists

def test_create_logs_directory(tmp_path):
    log_dir = tmp_path / "logs"
    ensure_log_directory_exists(log_dir)
    assert os.path.exists(log_dir), "Le dossier logs n'a pas été créé."
