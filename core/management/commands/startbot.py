from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

from telegram import (
    Update
)
from telegram.ext import (
    Updater, 
    CommandHandler,
    CallbackContext
)


def start(update: Update, context: CallbackContext):
    update.message.reply_text('bot başladı')


class Command(BaseCommand):
    help = 'Starts telegram bot for getting sensors data'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Bot is starting...'))

        updater = Updater(settings.T_TOKEN, use_context=True)
        dp = updater.dispatcher

        dp.add_handler(CommandHandler("start", start))

        updater.start_polling()
        updater.idle()
