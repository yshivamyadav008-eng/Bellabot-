"""Command handlers for Bellabot"""

from telegram import Update
from telegram.ext import ContextTypes
import logging

logger = logging.getLogger(__name__)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle /start command"""
    user = update.effective_user
    await update.message.reply_text(
        f"Hi {user.mention_markdown_v2()\! Welcome to Bellabot\!\n\n"
        f"Use /help to see available commands\.",
        parse_mode='MarkdownV2'
    )
    logger.info(f"User {user.id} started the bot")


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle /help command"""
    help_text = (
        "*Available Commands:*\n\n"
        "/start \- Start the bot\n"
        "/help \- Show this help message\n"
        "/ping \- Check if bot is alive\n\n"
        "Just send me a message and I\'ll echo it back\!"
    )
    await update.message.reply_text(help_text, parse_mode='MarkdownV2')
    logger.info(f"User {update.effective_user.id} requested help")
