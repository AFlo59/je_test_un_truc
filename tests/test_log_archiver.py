import os
import tarfile
import pytest
from pathlib import Path
from scripts.log_archiver import archive_logs


@pytest.fixture
def setup_logs(tmp_path):
    """
    Fixture pour préparer un environnement de test avec des fichiers de logs.
    """
    log_dir = tmp_path / "logs"
    log_dir.mkdir()

    # Créez des fichiers de logs factices
    log1 = log_dir / "log1.log"
    log1.write_text("Log 1 content")

    log2 = log_dir / "log2.log"
    log2.write_text("Log 2 content")

    empty_log = log_dir / "empty.log"
    empty_log.touch()  # Fichier vide

    return {
        "log_dir": log_dir,
        "log_files": [str(log1), str(log2)],
        "empty_log": str(empty_log),
    }


def test_create_archive_folder(tmp_path):
    """
    Teste la création du dossier archive si inexistant.
    """
    archive_folder = tmp_path / "archive"
    log_files = []  # Aucun fichier pour ce test

    archive_logs(log_files, archive_folder=str(archive_folder))

    assert archive_folder.exists(), "Le dossier 'archive' n'a pas été créé."


def test_archive_nonexistent_logs(tmp_path):
    """
    Teste l'archivage de fichiers de logs inexistants.
    """
    archive_folder = tmp_path / "archive"
    non_existent_logs = [str(tmp_path / "nonexistent.log")]

    archive_path = archive_logs(non_existent_logs, archive_folder=str(archive_folder))

    # Vérifier qu'aucune archive n'est créée
    assert archive_path is None, "Une archive a été créée alors qu'il ne devrait pas."
    assert archive_folder.exists(), "Le dossier 'archive' n'a pas été créé."
    archive_files = list(archive_folder.glob("*.tar.gz"))
    assert len(archive_files) == 0, "Un fichier d'archive a été créé alors qu'il ne devrait pas."


def test_archive_empty_log(tmp_path, setup_logs):
    """
    Teste l'archivage d'un fichier de log vide.
    """
    archive_folder = tmp_path / "archive"
    empty_log = [setup_logs["empty_log"]]

    archive_path = archive_logs(empty_log, archive_folder=str(archive_folder))

    assert Path(archive_path).exists(), "Le fichier d'archive n'a pas été créé."
    with tarfile.open(archive_path, "r:gz") as tar:
        members = tar.getnames()
        assert len(members) == 1, "L'archive ne contient pas exactement un fichier."
        assert "empty.log" in members[0], "Le fichier vide n'est pas présent dans l'archive."


def test_archive_multiple_logs(tmp_path, setup_logs):
    """
    Teste l'archivage de plusieurs fichiers de logs.
    """
    archive_folder = tmp_path / "archive"
    log_files = setup_logs["log_files"]

    archive_path = archive_logs(log_files, archive_folder=str(archive_folder))

    assert Path(archive_path).exists(), "Le fichier d'archive n'a pas été créé."
    with tarfile.open(archive_path, "r:gz") as tar:
        members = tar.getnames()

        # Vérifie que l'archive contient exactement les fichiers attendus
        expected_files = [os.path.basename(log_file) for log_file in log_files]
        archived_files = [os.path.basename(member) for member in members]
        assert len(members) == len(expected_files), "L'archive ne contient pas le bon nombre de fichiers."
        for expected_file in expected_files:
            assert expected_file in archived_files, f"{expected_file} est manquant dans l'archive."



def test_successful_archive(tmp_path, setup_logs):
    """
    Teste que l'archivage réussit et produit une archive valide.
    """
    archive_folder = tmp_path / "archive"
    log_files = setup_logs["log_files"]

    archive_path = archive_logs(log_files, archive_folder=str(archive_folder))

    assert Path(archive_path).exists(), "Le fichier d'archive n'a pas été créé."
    assert archive_path.endswith(".tar.gz"), "L'archive n'a pas le bon format."
    with tarfile.open(archive_path, "r:gz") as tar:
        assert tar.getmembers(), "L'archive est vide."
