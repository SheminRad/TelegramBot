#from constants import bot_token , bot_username
from asyncore import dispatcher
from telegram import Document, Sticker, Update
from telegram.ext import MessageHandler, CommandHandler,Application,ContextTypes,filters
from typing import Final
from constants import bot_token, bot_username,api_hash,api_id
import telethon.sync 
from telethon.sync import TelegramClient
import emoji

async def start_Command(update: Update,context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply.text("Hello there!Let's start chatting")

def handle_response(text:str)->str:
    if 'تق تق' in text:
        with TelegramClient.conversation(...) as conv:
            conv.send_message('کیه؟')
            hello = conv.get_response()

            conv.send_message(Update.message.text + 'کیه؟')
            conv.send_message(':smile:')
            name = conv.get_response().raw_text
    else:
        return text
    
def handle_response_sticker(content: Sticker)->Sticker:
    return content

def handle_response_document(content: Document)->Document:
    return Document

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message

    if message.text:
        response = handle_response(message.text)
        await update.message.reply_text(response)
    elif message.sticker:
        response = handle_response_sticker(message.sticker)
        await update.message.reply_sticker(response)
    elif message.document:
        response = handle_response_document(message.document)
        await update.message.reply_document(response)
    else:
        response = "Received a message of unsupported type"
        await update.message.reply_text(response)

async def error(update: Update,context:ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')

if __name__ == '__main__':
    print('Starting bot...')
    app = Application.builder().token(bot_token).build()

    #Commands
    app.add_handler(CommandHandler('start', start_Command)) 
   
    #Messages
    app.add_handler(MessageHandler(filters.ALL, handle_message))
    #Errors
    app.add_error_handler(error)

    print('Polling...')
    app.run_polling(poll_interval=3)


