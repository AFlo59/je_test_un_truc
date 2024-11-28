#!/usr/bin/env bats

# Initialisation avant chaque test
setup() {
  # Créer un répertoire temporaire pour isoler les tests
  export TEST_DIR=$(mktemp -d)
  export LOG_DIR="$TEST_DIR/logs"
  export LOG_FILE="$LOG_DIR/install.log"
  export VENV_DIR="$TEST_DIR/venv"
  export REQUIREMENTS_FILE="$TEST_DIR/requirements.txt"
  export SCRIPT_NAME="$TEST_DIR/setup.sh"
  
  # Copier le script setup.sh dans le répertoire temporaire
  cp setup.sh "$TEST_DIR/setup.sh"
  
  cd "$TEST_DIR"
}

# Nettoyage après chaque test
teardown() {
  rm -rf "$TEST_DIR"
}

@test "Création du dossier logs si inexistant" {
  run bash setup.sh
  [ "$status" -eq 0 ]
  [ -d "$LOG_DIR" ] # Vérifier que le dossier logs a été créé
  [ -f "$LOG_FILE" ] # Vérifier que le fichier log existe
  grep -q "Logger initialisé" "$LOG_FILE"
}

@test "Activation de l'environnement virtuel si absent" {
  run bash setup.sh
  [ "$status" -eq 0 ]
  [ -d "$VENV_DIR" ] # Vérifier que le venv a été créé
  grep -q "Exécution de la commande : python3 -m venv $VENV_DIR" "$LOG_FILE"
}

@test "Installation des dépendances depuis requirements.txt" {
  echo "pytest" > "$REQUIREMENTS_FILE"
  run bash setup.sh
  [ "$status" -eq 0 ]
  grep -q "pip install -r $REQUIREMENTS_FILE" "$LOG_FILE"
}

@test "Détection correcte du système d'exploitation" {
  run bash setup.sh
  [ "$status" -eq 0 ]
  grep -q "Détection de l'OS" "$LOG_FILE"
}

@test "Gestion des droits d'exécution pour setup.sh" {
  chmod -x "$SCRIPT_NAME"
  run bash setup.sh
  [ "$status" -eq 0 ]
  grep -q "Droits d'exécution accordés à $SCRIPT_NAME" "$LOG_FILE"
  [ -x "$SCRIPT_NAME" ] # Vérifier que le script est maintenant exécutable
}

@test "Erreur pour un système d'exploitation non pris en charge" {
  run bash -c 'OS=UnsupportedOS bash setup.sh'
  [ "$status" -ne 0 ]
  grep -q "Système d'exploitation non pris en charge" "$LOG_FILE"
}

@test "Exécution complète du script avec succès" {
  touch "$REQUIREMENTS_FILE"
  run bash setup.sh
  [ "$status" -eq 0 ]
  grep -q "Script d'installation terminé avec succès" "$LOG_FILE"
}
