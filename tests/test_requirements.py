import os


def test_requirements_file_exists():
    assert os.path.exists("requirements.txt"), "Le fichier requirements.txt est introuvable."

def test_requirements_not_empty():
    with open("requirements.txt", "r") as file:
        content = file.read().strip()
        assert len(content) > 0, "Le fichier requirements.txt est vide."
