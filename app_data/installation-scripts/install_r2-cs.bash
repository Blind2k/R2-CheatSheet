#!/bin/bash

# Incase Python is already installed but less than version 3.10.
function install_python_environment(){
    echo "[*] Installing pyenv..."
    # Installing dependencies
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

    # Add pyenv to the shell
    echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
    echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
    echo 'eval "$(pyenv init --path)"' >> ~/.bashrc
    echo 'eval "$(pyenv init - bash)"' >> ~/.bashrc
    source ~/.bashrc

    pyenv install 3.10.7
    pyenv global 3.10.7
}

function validate_python_version(){
  echo "[*] Checking Python version..."
  PYTHON_VERSION=$(python3 -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')
  REQUIRED_VERSION="3.10"

  # Compare versions
  if [[ "$(printf '%s\n' "$REQUIRED_VERSION" "$PYTHON_VERSION" | sort -V | head -n1)" -eq "$REQUIRED_VERSION" ]]; then
    return 1
  else
    return 0
  fi
}

# Check for "r2cs" alias inside .bashrc. If not, create one.
function create_r2_shortcut(){
    SCRIPT_DIR="$(dirname "$(realpath "$0")")"
    BASHRC="/home/$(logname)/.bashrc"
    echo "$SCRIPT_DIR/R2-CheatSheet"

    if ! grep -q 'alias r2cs=' "$BASHRC"; then
      {
        echo ""
        echo "# Alias for R2-Cheat Sheet"
        # Creating dynamic alias depend on the user logon name as destination while the script is tested by dirname
        echo "alias r2cs=\"cd $SCRIPT_DIR/R2-CheatSheet; source /r2cs_env/bin/activate && python $SCRIPT_DIR/r2cs.py\""
      } >> "$BASHRC"
      echo "[+] Alias 'r2cs' added to $BASHRC"
    else
      echo "[*] Alias 'r2cs' already exists in $BASHRC"
    fi
}

# Simple updating before installation
function update_system(){
  echo "[+] Updating front-end package list..."
  sudo apt update -y

  echo "[+] Updating back-end package list..."
  sudo apt-get update -y
}

# Check that Python >= 3.10. If so, install environment
function install_r2(){
  echo "[+] Python version OK: $PYTHON_VERSION"

  echo "[*] Cloning repository..."
  git clone https://github.com/Blind2k/R2-CheatSheet.git
  cd "R2-CheatSheet"

  echo "[*] Creating virtual environment..."
  python3 -m venv r2cs_env

  echo "[*] Adding shortcut to .bashrc..."
  create_r2_shortcut

  echo "[+] Install complete!."
  echo "Open terminator and type \"r2cs\" to run the tool!"

}

if [ "$(id -u)" -eq 0 ]; then
  update_system
  sudo apt-get install -y terminator
  sudo apt-get install -y git
  is_valid=validate_python_version
  if [[ is_valid -eq 1 ]]; then
    install_r2
  else
    echo "[!] Python 3.10 or higher is required. Found: $PYTHON_VERSION"
    echo "[*] Trying to install pyenv"
    install_python_environment
    echo "[*] Trying to install pyenv"
    if [[ is_valid -eq 1 ]]; then
      install_r2
    else
      print "[!] Failed installing Python. Sorry but your python version is too low."
    fi # After trying to install pyenv
  fi # First attempt to install

else
    echo "Please run this script with Bash and as super user"
    echo "sudo bash $(pwd)/install_r2-cs.bash"
    exit 1
fi
