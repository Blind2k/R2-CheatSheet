#!/bin/bash
# This script is meant to be compatible with Debian (Kali) machines

BASHRC="/home/$(logname)/.bashrc"

function install_python_environment(){
    echo "[*] Installing pyenv..."
    sudo apt update && sudo apt install -y \
        build-essential \
        libssl-dev \
        zlib1g-dev \
        libbz2-dev \
        libreadline-dev \
        libsqlite3-dev \
        curl \
        libncursesw5-dev \
        xz-utils \
        tk-dev \
        libffi-dev \
        liblzma-dev \
        python3-openssl \
        git

    curl https://pyenv.run | bash

    {
      echo ""
      echo "# Python Library Manager"
      echo 'export PYENV_ROOT="$HOME/.pyenv"'
      echo 'export PATH="$PYENV_ROOT/bin:$PATH"'
      echo 'eval "$(pyenv init --path)"'
      echo 'eval "$(pyenv init - bash)"'
    } >> "$BASHRC"

    export PYENV_ROOT="$HOME/.pyenv"
    export PATH="$PYENV_ROOT/bin:$PATH"
    eval "$(pyenv init --path)"
    eval "$(pyenv init - bash)"

    pyenv install 3.10.7
    pyenv global 3.10.7
}

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

function create_r2_shortcut(){
    SCRIPT_DIR="$(dirname "$(realpath "$0")")"
    echo "$SCRIPT_DIR/R2-CheatSheet"

    if ! grep -q 'alias r2cs=' "$BASHRC"; then
        {
          echo ""
          echo "# Alias for R2-Cheat Sheet"
          echo "alias r2cs=\"cd $SCRIPT_DIR/R2-CheatSheet; source r2cs_env/bin/activate && python r2cs.py\""
        } >> "$BASHRC"
        echo "[+] Alias 'r2cs' added to $BASHRC"
    else
        echo "[*] Alias 'r2cs' already exists in $BASHRC"
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

    echo "[*] Creating virtual environment..."
    python3 -m venv r2cs_env

    echo "[*] Adding shortcut to .bashrc..."
    create_r2_shortcut

    echo "[+] Install complete!"
    echo "Open terminator and type \"r2cs\" to run the tool!"
}

# --- Main ---
if [ "$(id -u)" -eq 0 ]; then
    update_system
    sudo apt-get install -y terminator git

    if validate_python_version; then
        install_r2
    else
        echo "[!] Python 3.10 or higher is required. Trying to install pyenv..."
        install_python_environment

        if validate_python_version; then
            install_r2
        else
            echo "[!] Failed installing Python. Sorry, your version is too low."
            exit 1
        fi
    fi
else
    echo "Please run this script with Bash and as super user"
    echo "sudo bash $(pwd)/install_r2-cs.bash"
    exit 1
fi
