
from telegram.ext import Updater, MessageHandler, Filters
import requests
import os

# Token do bot e URL do Webhook (configure no Render como variáveis de ambiente)
TOKEN = os.getenv("BOT_TOKEN")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")

def handle_new_member(update, context):
    for member in update.message.new_chat_members:
        data = {
            "user_id": member.id,
            "name": member.full_name,
            "username": member.username,
            "chat_id": update.message.chat_id
        }
        requests.post(WEBHOOK_URL, json=data)

updater = Updater(TOKEN, use_context=True)
dp = updater.dispatcher
dp.add_handler(MessageHandler(Filters.status_update.new_chat_members, handle_new_member))

updater.start_polling()
updater.idle()
