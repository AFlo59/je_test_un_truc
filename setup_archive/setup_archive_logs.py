from scripts.log_archiver import archive_logs

# Liste des fichiers de logs à archiver
log_files = ["logs/log1.log", "logs/log2.log"]

# Appel de la fonction archive_logs
archive_path = archive_logs(log_files)
print(f"Archive créée : {archive_path}")