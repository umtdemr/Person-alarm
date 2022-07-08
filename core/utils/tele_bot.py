from nis import cat
import telegram
from django.conf import settings


class TelegramBot():
    _bot = telegram.Bot(settings.T_TOKEN)

    def __init__(self) -> None:
        self._bot = telegram.Bot(settings.T_TOKEN)
    
    def get_bot(self) -> telegram.Bot:
        return self._bot

    def get_me(self):
        return self._bot.get_me()
    
    def send_photo(self, path: str, reply_message_id: int = None, caption: str = ""):
        opened_file = open(path, 'rb')
        message = self._bot.send_photo(
            chat_id=settings.T_USER,
            photo=opened_file,
            caption=caption,
            reply_to_message_id=reply_message_id
        )
        opened_file.close()
        return message

    def send_text(self, text: str, reply_message_id: int = None):
        return self._bot.send_message(
            chat_id=settings.T_USER,
            text=text,
            reply_to_message_id=reply_message_id
        )
