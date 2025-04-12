#!/bin/bash

function update_system(){
  echo "[+] Updating front-end package list..."
  sudo apt update -y

  echo "[+] Updating back-end package list..."
  sudo apt-get update -y
}

function install_r2(){
  echo "[*] Checking Python version..."

  PYTHON_VERSION=$(python3 -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')

  REQUIRED_VERSION="3.10"

  # Compare versions
  if [[ "$(printf '%s\n' "$REQUIRED_VERSION" "$PYTHON_VERSION" | sort -V | head -n1)" != "$REQUIRED_VERSION" ]]; then
    echo "[!] Python 3.10 or higher is required. Found: $PYTHON_VERSION"
    return 1

  else
    echo "[+] Python version OK: $PYTHON_VERSION"

    echo "[*] Cloning repository..."
    git clone https://github.com/Blind2k/R2-CheatSheet.git

    cd "$USER_HOME/R2-CheatSheet"

    echo "[*] Creating virtual environment..."
    python3 -m venv r2cs_env

    echo "[*] Adding shortcut to .bashrc..."
    echo "" >> "/home/$(logname)/.bashrc"
    echo "# Alias for R2-Cheat Sheet" >> "/home/$(logname)/.bashrc"
    echo "alias r2cs=\"source $(pwd)/r2cs_env/bin/activate && python $(pwd)/r2cs.py\"" >> "/home/$(logname)/.bashrc"

    echo "[+] Install complete!."
    echo "Open terminator and type \"r2cs\" to run the tool!"
  fi
}


if [ "$(id -u)" -eq 0 ]; then
  update_system
  sudo apt-get install -y terminator git || { echo "Something went wrong while installing terminaor."; }
  sudo apt-get install -y git || { echo "Something went wrong while installing git."; }
  install_r2

else
    echo "Please run this script with Bash and as super user"
    echo "sudo bash $(pwd)/install_r2-cs.bash"
    exit 1
fi
