import os
import shutil
import tarfile
from datetime import datetime


def archive_logs(log_files, archive_folder="archive"):
    """
    Archive et compresse plusieurs fichiers de logs dans un sous-dossier horodaté.

    :param log_files: Liste des chemins des fichiers de logs à archiver.
    :param archive_folder: Dossier principal pour les archives.
    :return: Chemin du fichier d'archive créé ou None si aucun fichier valide.
    """
    # Vérification ou création du dossier principal
    if not os.path.exists(archive_folder):
        os.makedirs(archive_folder)
        print(f"Dossier '{archive_folder}' créé avec succès.")

    # Création d'un sous-dossier horodaté
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    sub_folder = os.path.join(archive_folder, f"logs_{timestamp}")
    os.makedirs(sub_folder)

    # Copier les fichiers dans le sous-dossier
    valid_files = []
    for log_file in log_files:
        if os.path.exists(log_file):
            shutil.copy(log_file, sub_folder)
            valid_files.append(log_file)
            print(f"Fichier '{log_file}' copié dans '{sub_folder}'.")
        else:
            print(f"Attention : Fichier '{log_file}' introuvable et ignoré.")

    # Si aucun fichier valide, supprimer le sous-dossier et retourner None
    if not valid_files:
        shutil.rmtree(sub_folder)
        print(f"Pas de fichiers valides. Sous-dossier temporaire '{sub_folder}' supprimé.")
        return None

    # Compression du sous-dossier
    archive_path = os.path.join(archive_folder, f"logs_{timestamp}.tar.gz")
    with tarfile.open(archive_path, "w:gz") as tar:
        for root, _, files in os.walk(sub_folder):
            for file in files:
                file_path = os.path.join(root, file)
                tar.add(file_path, arcname=os.path.relpath(file_path, sub_folder))
        print(f"Fichiers compressés dans l'archive '{archive_path}'.")

    # Suppression du sous-dossier après compression
    shutil.rmtree(sub_folder)
    print(f"Sous-dossier temporaire '{sub_folder}' supprimé.")

    return archive_path
