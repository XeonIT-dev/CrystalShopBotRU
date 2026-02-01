#!/bin/bash

set -e

SCRIPT_DIR="$(pwd)"
REPO_DIR="$SCRIPT_DIR"
VENV_DIR="$REPO_DIR/.venv"
REPO_URL="https://github.com/XeonIT-dev/CrystalShopBotRU.git"


update_system() {
    echo "🔄 Обновление системы..."
    
    if [ -f /etc/os-release ]; then
        . /etc/os-release
    fi
    
    case "${ID_LIKE:-$ID}" in
        "debian"|"ubuntu")
            echo "📦 Debian/Ubuntu: apt update && apt upgrade"
            sudo apt update && sudo apt upgrade -y
            sudo apt autoremove -y
            ;;
        "arch")
            echo "📦 Arch Linux: pacman -Syu"
            sudo pacman -Syu --noconfirm
            ;;
        "fedora")
            echo "📦 Fedora: dnf upgrade"
            sudo dnf upgrade -y
            sudo dnf autoremove -y
            ;;
        *)
            echo "⚠️  Дистрибутив не поддерживается: $ID"
            return 1
            ;;
    esac
    echo "✅ Система обновлена!"
}


echo "🚀 Быстрая установка CrystalShopBotRU"

update_system

ping -c 4 8.8.8.8 > /dev/null || { echo "❌ Нет интернета!"; exit 1; }

git pull

python3 -m venv "$VENV_DIR"
source "$VENV_DIR/bin/activate"

pip install --upgrade pip
pip install -r requirements.txt
clear

echo "🚀 Запуск бота..."
sleep 3
clear
python3 main.py


