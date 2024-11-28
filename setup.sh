#!/bin/bash

# Variables
LOG_DIR="logs"
LOG_FILE="$LOG_DIR/install.log"
VENV_DIR="venv"
REQUIREMENTS_FILE="requirements.txt"
SCRIPT_NAME="setup.sh"

# Initialisation du logger Python
initialize_logger() {
    python3 - <<END
import os
import logging
from scripts.setup_logger import setup_logger

log_dir = "$LOG_DIR"
log_file = "$LOG_FILE"

if not os.path.exists(log_dir):
    os.makedirs(log_dir)

global logger
logger = setup_logger(name="install_logger", log_file=log_file, level=logging.DEBUG, console=True)

logger.debug("Logger initialisé. Les logs seront enregistrés dans la console et dans $LOG_FILE.")
END
}

# Fonction pour exécuter une commande et rediriger la sortie vers le logger
log_command() {
    local command="$1"
    local output
    output=$($command 2>&1) # Capture la sortie standard et d'erreur
    python3 - <<END
import logging
from scripts.setup_logger import setup_logger

log_file = "$LOG_FILE"
logger = setup_logger(name="install_logger", log_file=log_file, level=logging.DEBUG, console=True)

logger.info("Exécution de la commande : $command")
logger.info("""$output""")
END
}

# Fonction pour s'accorder les droits d'exécution
self_chmod() {
    if [ ! -x "$SCRIPT_NAME" ]; then
        chmod +x "$SCRIPT_NAME"
        python3 - <<END
import logging
from scripts.setup_logger import setup_logger

log_file = "$LOG_FILE"
logger = setup_logger(name="install_logger", log_file=log_file, level=logging.DEBUG, console=True)

logger.info("Droits d'exécution accordés à $SCRIPT_NAME.")
END
    fi
}

# Fonction pour vérifier l'environnement virtuel
setup_virtual_environment() {
    if [ ! -d "$VENV_DIR" ]; then
        log_command "python3 -m venv $VENV_DIR"
    fi
    log_command "source $VENV_DIR/bin/activate"
}

# Fonction pour installer les dépendances
install_dependencies() {
    if [ ! -f "$REQUIREMENTS_FILE" ]; then
        log_command "touch $REQUIREMENTS_FILE"
    fi
    log_command "pip install --upgrade pip"
    log_command "pip install -r $REQUIREMENTS_FILE"
}

# Fonction pour détecter le système d'exploitation
detect_os() {
    local os
    os=$(uname)
    python3 - <<END
import logging
from scripts.setup_logger import setup_logger

log_file = "$LOG_FILE"
logger = setup_logger(name="install_logger", log_file=log_file, level=logging.DEBUG, console=True)

logger.info("Détection de l'OS : $os")
END

    if [[ "$os" == "Linux" ]]; then
        log_command "echo Système Linux détecté."
    elif [[ "$os" == "Darwin" ]]; then
        log_command "echo Système macOS détecté."
    elif [[ "$os" == "MINGW"* || "$os" == "CYGWIN"* ]]; then
        log_command "echo Système Windows détecté."
    else
        log_command "echo Système d'exploitation non pris en charge."
        exit 1
    fi
}

# Lancement du script
initialize_logger
self_chmod
detect_os
setup_virtual_environment
install_dependencies
log_command "echo Script d'installation terminé avec succès."
