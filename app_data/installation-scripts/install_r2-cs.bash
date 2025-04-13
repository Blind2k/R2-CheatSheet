#!/bin/bash
# This script is meant to be compatible with Debian (Kali) machines

BASHRC="/home/$(logname)/.bashrc"

function validate_python_version(){
    echo "[*] Checking Python version..."
    PYTHON_VERSION=$(python3 -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')
    REQUIRED_VERSION="3.10"

    if [[ "$(printf '%s\n' "$REQUIRED_VERSION" "$PYTHON_VERSION" | sort -V | head -n1)" == "$REQUIRED_VERSION" && "$PYTHON_VERSION" != "$REQUIRED_VERSION" ]]; then
        return 0  # Python is newer
    elif [[ "$PYTHON_VERSION" == "$REQUIRED_VERSION" ]]; then
        return 0  # Exact match
    else
        return 1  # Too old
    fi
}

function update_system(){
    echo "[+] Updating front-end package list..."
    sudo apt update -y

    echo "[+] Updating back-end package list..."
    sudo apt-get update -y
}

function install_r2(){
    PYTHON_VERSION=$(python3 -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')
    echo "[+] Python version OK: $PYTHON_VERSION"

    echo "[*] Cloning repository..."
    git clone https://github.com/Blind2k/R2-CheatSheet.git
    cd "R2-CheatSheet"

    echo "[+] Install complete!"
    echo "Open terminator and type \"r2cs\" to run the tool!"
}

# --- Main ---
update_system
sudo apt-get install -y terminator git

if validate_python_version; then
    install_r2
    {
      echo ""
      echo "# Alias for R2-Cheat Sheet"
      echo "alias r2cs=\"cd $(pwd)/R2-CheatSheet; source r2cs_env/bin/activate && python r2cs.py\""
    } >> ~/.bashrc
else
    echo "[!] Failed installing Python. Sorry, your version is too low."
fi
