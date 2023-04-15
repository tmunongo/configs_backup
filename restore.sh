#!/bin/bash

# Define the module directories and their backup directories
MODULES=(
    "i3"
    "neofetch"
    "polybar"
)
BACKUP_DIR="$HOME/Documents/backup"

# Loop through each module and restore the most recent backup
for MODULE in "${MODULES[@]}"; do
    # Get the most recent backup folder
    BACKUP=$(ls -td "$BACKUP_DIR/$MODULE"/*/ | head -n 1)

    # Copy the contents of the backup folder to the module directory
    cp -r "$BACKUP"* "$HOME/.config/$MODULE/"
done

echo "Restoration complete."
