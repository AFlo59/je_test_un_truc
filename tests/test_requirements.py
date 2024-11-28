import os

def test_requirements_file_exists():
    assert os.path.exists("requirements.txt"), "Le fichier requirements.txt est manquant."