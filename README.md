# Bellabot

A Telegram bot built with Python and the python-telegram-bot library.

## Features

- Responsive to user commands
- Modular architecture for easy extensibility
- Error handling and logging

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yshivamyadav008-eng/Bellabot-.git
cd Bellabot-
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Configuration

1. Create a `.env` file in the project root:
```
TELEGRAM_BOT_TOKEN=your_bot_token_here
```

2. Get your bot token from [BotFather](https://t.me/botfather) on Telegram

## Running the Bot

```bash
python main.py
```

## Project Structure

```
Bellabot-/
├── main.py              # Entry point of the bot
├── config.py            # Configuration settings
├── handlers/            # Command and message handlers
│   ├── __init__.py
│   ├── commands.py      # Command handlers
│   └── messages.py      # Message handlers
├── utils/               # Utility functions
│   ├── __init__.py
│   └── helpers.py       # Helper functions
├── requirements.txt     # Python dependencies
├── .env                 # Environment variables (not in repo)
├── .gitignore           # Git ignore file
└── README.md            # This file
```

## License

MIT License - feel free to use this project
