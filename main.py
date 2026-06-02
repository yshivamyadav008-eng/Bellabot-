#!/usr/bin/env python3
"""
Bellabot - A Telegram Bot
Main entry point for the bot
"""

import logging
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from config import TELEGRAM_BOT_TOKEN, DEBUG
from handlers.commands import start, help_command
from handlers.messages import handle_message

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO if not DEBUG else logging.DEBUG
)
logger = logging.getLogger(__name__)


def main():
    """Start the bot"""
    # Create the Application
    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

    # Add command handlers
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('help', help_command))

    # Add message handler
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Run the bot
    logger.info("Bot started. Press Ctrl+C to stop.")
    application.run_polling(allowed_updates=['message', 'edited_message'])


if __name__ == '__main__':
    main()
