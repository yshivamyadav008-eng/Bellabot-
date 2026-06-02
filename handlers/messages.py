"""Message handlers for Bellabot"""

from telegram import Update
from telegram.ext import ContextTypes
import logging

logger = logging.getLogger(__name__)


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle regular text messages"""
    user = update.effective_user
    message_text = update.message.text
    
    logger.info(f"Message from {user.id}: {message_text}")
    
    # Simple echo response
    await update.message.reply_text(
        f"You said: {message_text}"
    )
