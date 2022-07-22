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

from core.models import TelegramData, SiteSettings


def parse_danger_area_data(args):
    x = int(args[args.index("x") + 1])
    y = int(args[args.index("y") + 1])
    w = int(args[args.index("w") + 1])
    h = int(args[args.index("h") + 1])
    return [x, y, x + w, y + h]


def handler_help(update: Update, context: CallbackContext):
    update.message.reply_text(""" 
        Person alarm bot    
        /danger x 100 y 20 w 200 h 400 : tehlikeli alanı belirtmek için.
    """)

def start(update: Update, context: CallbackContext):
    update.message.reply_text('bot başladı')


def get_sensors_data(update: Update, context: CallbackContext):
    telegram_data_obj = TelegramData.objects.first()
    update.message.reply_text(f"""
        alev: {telegram_data_obj.fire_info}
    """)

def draw_danger_area(update: Update, context: CallbackContext):
    try:
        danger_area = parse_danger_area_data(context.args)
        try:
            settings_obj = SiteSettings.objects.first()
            settings_obj.rect_x = danger_area[0]
            settings_obj.rect_y = danger_area[1]
            settings_obj.rect_w = danger_area[2]
            settings_obj.rect_h = danger_area[3]
            settings_obj.save()
            update.message.reply_text('Tehlikeli alan oluşturuldu')
        except Exception:
            update.message.reply_text('Veritabanına kaydedilirken hata...')
    except Exception:
        update.message.reply_text('Parse edilirken hata. Örnek: /danger x 100 y 100 w 100 h 100')


class Command(BaseCommand):
    help = 'Starts telegram bot for getting sensors data'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Bot is starting...'))

        updater = Updater(settings.T_TOKEN, use_context=True)
        dp = updater.dispatcher

        dp.add_handler(CommandHandler("help", handler_help))
        dp.add_handler(CommandHandler("start", start))
        dp.add_handler(CommandHandler("data", get_sensors_data))
        dp.add_handler(CommandHandler("danger", draw_danger_area))

        updater.start_polling()
        updater.idle()
