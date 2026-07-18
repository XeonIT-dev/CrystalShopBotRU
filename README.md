# 💎 CrystalShopBotRU v.1.0.1-beta


![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![aiogram](https://img.shields.io/badge/aiogram-async-green?logo=telegram&logoColor=white)
![Telegram](https://img.shields.io/badge/Telegram-Bot-2CA5E0?logo=telegram&logoColor=white)
![Crypto](https://img.shields.io/badge/Crypto-Payments-orange?logo=bitcoin&logoColor=white)
![SQLite](https://img.shields.io/badge/Database-SQLite-003B57?logo=sqlite&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-success)


---
## Version v.1.0.1-beta
---


## 📌 Описание


**CrystalShopBotRU** — это универсальный Telegram-бот-магазин, написанный на Python с использованием библиотеки **aiogram**.

Он предоставляет полноценный консольный интерфейс для владельцев магазинов, позволяющий настраивать и управлять Telegram-магазином:  
от ввода платёжных данных до добавления товаров и кастомизации сообщений бота.

Бот интегрирован с **CrystalPAY** для удобной оплаты криптовалютой.


--------------------------------------------------------------


## ✨ Возможности


### 🔧 Управление и администрирование
| Возможность | Описание |
|------------|----------|
| Консольное управление | Полная настройка магазина через интерфейс командной строки |
| Удалённый контроль | Запуск и остановка бота напрямую из Telegram |


---


### 💳 Платёжная система
| Возможность | Описание |
|------------|----------|
| CrystalPAY | Интеграция с платёжной системой CrystalPAY |
| Криптовалютные платежи | Приём оплаты в криптовалюте |
| SDK CrystalPAY | Встроенный SDK для работы с API CrystalPAY |


---


### 📦 Управление товарами
| Возможность | Описание |
|------------|----------|
| Карточки товаров | Создание и управление товарами |
| Редактирование | Изменение названий, описаний и цен |
| Результаты покупки | Выдача контента после успешной оплаты |


---


### 🤖 Telegram-интерфейс
| Возможность | Описание |
|------------|----------|
| Inline-клавиатуры | Интерактивные кнопки внутри сообщений |
| Reply-клавиатуры | Кнопки быстрого ответа |
| aiogram | Асинхронная обработка событий |


---


### 🎨 Контент и кастомизация
| Возможность | Описание |
|------------|----------|
| Тексты магазина | Название, приветственные сообщения, раздел «О нас» |
| Контакты поддержки | Настройка контактной информации |


---


### 🗄 Хранение данных
| Возможность | Описание |
|------------|----------|
| SQLite | Локальное хранение пользователей и настроек |


---


### 🛠 Сервисные функции
| Возможность | Описание |
|------------|----------|
| Режим обслуживания | Уведомление пользователей о технических работах |
| Безопасное выключение | Удалённая остановка бота |


--------------------------------------------------------------


## 🐧 Установка (Linux Manual)

│
├──🟠 Ubuntu / Debian

```bash
sudo apt update
sudo apt install -y python3 python3-pip git
git clone https://github.com/XeonIT-dev/CrystalShopBotRU.git
cd CrystalShopBotRU
source .venv/bin/activate
pip3 install -r requirements.txt
python3 main.py
```

│
├──🔵 Arch Linux

```bash
sudo pacman -Syu --needed python python-pip git
git clone https://github.com/XeonIT-dev/CrystalShopBotRU.git
cd CrystalShopBotRU
source .venv/bin/activate
pip install -r requirements.txt
python main.py
```

│
├──🔴 Fedora

```bash
sudo dnf install -y python3 python3-pip git
git clone https://github.com/XeonIT-dev/CrystalShopBotRU.git
cd CrystalShopBotRU
source .venv/bin/activate
pip3 install -r requirements.txt
python3 main.py
```

--------------------------------------------------------------

## 🐧⚙️  Установка (Linux Autoinstall)

```bash
git clone https://github.com/XeonIT-dev/CrystalShopBotRU.git
cd CrystalShopBotRU
chmod +x start.sh
./start.sh
```

--------------------------------------------------------------

## 🪟 Установка (Windows Portable EXE)

```powershell
# 1. Скачайте архив с portable EXE из раздела Releases или сам .exe файл
# 2. Распакуйте в любую папку
# 3. Запустите CrystalShopBotRU.exe
.\CrystalShopBotRU.exe
```

## 🚀 Использование

После настройки выберите пункт:

[1] Запустить бота

Бот станет активным в Telegram и начнёт обрабатывать заказы.

--------------------------------------------------------------

## 🧰 Используемые технологии

🐍 Python
🤖 aiogram
🌐 requests
🗃 sqlite3

--------------------------------------------------------------

## 🗂 Структура проекта
```bash
├── crystalpay_sdk.py       # SDK для работы с API CrystalPAY
├── license.txt             # Лицензия проекта
├── main.py                 # Главный файл настройки и запуска бота
├── requirements.txt        # Зависимости Python
├── service.py              # Запуск бота в режиме обслуживания
├── Keyboards/              # Клавиатуры Telegram
│   ├── inline_keyboard.py
│   └── reline.py
├── handlers/               # Обработчики событий
│   └── user_handlers.py
├── initializer/            # Инициализация БД
│   └── initializer_db.py
├── main_config/            # Конфигурации
│   ├── Token_conf.py
│   ├── code_death.py
│   ├── config.py
│   ├── photo_path.py
│   └── reviews.py
└── payment/                # Платежи
    └── pay.py
```
--------------------------------------------------------------

## 📜 Лицензия

Проект распространяется под лицензией MIT.
Подробнее см. файл LICENSE

--------------------------------------------------------------

## 💖 Поддержать проект


☕ **Yoomoney/СБП/Банковские карты РФ**
- [Yoomoney](https://yoomoney.ru/to/4100119458290881)


⭐ **Поддержка на GitHub**
- Ставь ⭐ проекту, делись с друзьями и оставляй отзывы

--------------------------------------------------------------

> Любая поддержка помогает улучшать функционал, добавлять новые возможности и сохранять проект актуальным!
