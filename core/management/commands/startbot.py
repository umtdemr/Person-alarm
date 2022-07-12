from telegram import (
    Update
)
from telegram.ext import (
    Updater, 
    CommandHandler,
    CallbackContext
)
from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

from core.models import TelegramData



def start(update: Update, context: CallbackContext):
    update.message.reply_text('bot başladı')


def get_sensors_data(update: Update, context: CallbackContext):
    telegram_data_obj = TelegramData.objects.first()
    update.message.reply_text(f"""
        alev: {telegram_data_obj.fire_info}
    """)


class Command(BaseCommand):
    help = 'Starts telegram bot for getting sensors data'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Bot is starting...'))

        updater = Updater(settings.T_TOKEN, use_context=True)
        dp = updater.dispatcher

        dp.add_handler(CommandHandler("start", start))
        dp.add_handler(CommandHandler("data", get_sensors_data))

        updater.start_polling()
        updater.idle()
