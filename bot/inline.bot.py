
from config import BOT_TOKEN  # Token aus config.py importieren

def main():
    TOKEN = BOT_TOKEN
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(InlineQueryHandler(inline_query))
    updater.start_polling()
    print("Bot läuft... (Drücke STRG+C zum Beenden)")
    updater.idle()
