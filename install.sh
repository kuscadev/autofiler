#!/bin/bash

GREEN='\033[0;32]'
RED='\033[0;31]'
YELLOW='\033[1;33]'
NC='\033[0m'

SCRIPT_NAME="autofiler.py"
LINK_NAME="autofiler"
INSTALL_DIR=$(pwd)
PYTHON_EXEC=$(which python3)

echo -e "${YELLOW}--- AutoFiler Installation Wizard ---${NC}"

if [ ! -f "$SCRIPT_NAME" ]; then
    echo -e "${RED}[ERROR] $SCRIPT_NAME not found in this directory!${NC}"
    exit 1
fi

echo -e "📄 Granting execution permissions..."
chmod +x "$SCRIPT_NAME"
echo -e "${GREEN}[OK] Permissions granted.${NC}"

echo -e "🔗 Creating symlink for global access (sudo password may be required)..."
sudo ln -sf "$INSTALL_DIR/$SCRIPT_NAME" "/usr/local/bin/$LINK_NAME"

if [ $? -eq 0 ]; then
    echo -e "${GREEN}[OK] '$LINK_NAME' command added to system.${NC}"
else
    echo -e "${RED}[ERROR] Failed to create symlink.${NC}"
    exit 1
fi

CRON_CMD="$PYTHON_EXEC $INSTALL_DIR/$SCRIPT_NAME"
CRON_JOB="0 * * * * $CRON_CMD"

echo -e "⏰ Checking Cron Job status..."

(crontab -l 2>/dev/null | grep -F "$SCRIPT_NAME") >/dev/null

if [ $? -eq 0 ]; then
    echo -e "${YELLOW}[INFO] Cron job already exists. Skipping.${NC}"
else
    (crontab -l 2>/dev/null; echo "$CRON_JOB") | crontab -
    echo -e "${GREEN}[OK] Cron job added successfully (Runs every hour).${NC}"
fi

echo -e "${GREEN}✅ Installation Complete!${NC}"
echo -e "You can now run the tool by typing '${YELLOW}$LINK_NAME${NC}' in your terminal."