"""Helper utilities for Bellabot"""

import logging

logger = logging.getLogger(__name__)


def format_user_info(user):
    """Format user information for display"""
    return f"{user.first_name} {user.last_name or ''} (@{user.username or 'N/A'})"


def log_action(user_id, action, details=None):
    """Log bot actions"""
    message = f"User {user_id}: {action}"
    if details:
        message += f" - {details}"
    logger.info(message)
