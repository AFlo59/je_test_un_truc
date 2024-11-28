#!/usr/bin/env bats

setup() {
  # Créer un environnement temporaire pour les tests
  export TEST_DIR=$(mktemp -d)
  export LOG_DIR="$TEST_DIR/logs"
  export LOG_FILE="$LOG_DIR/schedule.log"
  mkdir -p "$TEST_DIR"
  cp schedule.sh "$TEST_DIR/"
  cd "$TEST_DIR"
}

teardown() {
  # Nettoyage de l'environnement temporaire
  rm -rf "$TEST_DIR"
}

@test "Création du dossier de logs si inexistant" {
  run bash schedule.sh
  [ "$status" -eq 0 ]
  [ -d "$LOG_DIR" ]
  [ -f "$LOG_FILE" ]
  grep "Création du dossier $LOG_DIR." "$LOG_FILE"
}

@test "Exécution de install.sh si venv absent" {
  touch install.sh
  chmod +x install.sh
  echo "echo 'Installation simulée'" > install.sh
  run bash schedule.sh
  [ "$status" -eq 0 ]
  grep "Environnement virtuel non trouvé" "$LOG_FILE"
  grep "Installation simulée" "$LOG_FILE"
}

@test "Activation de l'environnement virtuel existant" {
  mkdir venv
  run bash schedule.sh
  [ "$status" -eq 0 ]
  grep "Environnement virtuel trouvé" "$LOG_FILE"
}

@test "Erreur pour système d'exploitation non supporté" {
  run bash -c 'OS=UnsupportedOS bash schedule.sh'
  [ "$status" -ne 0 ]
  grep "Système d'exploitation non pris en charge" "$LOG_FILE"
}

@test "Archivage des logs après exécution" {
  touch archive_logs.sh
  chmod +x archive_logs.sh
  echo "echo 'Archivage simulé'" > archive_logs.sh
  run bash schedule.sh
  [ "$status" -eq 0 ]
  grep "Archivage des logs terminé" "$LOG_FILE"
  grep "Archivage simulé" "$LOG_FILE"
}
