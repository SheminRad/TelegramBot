#from constants import bot_token , bot_username
from telegram import Document, Sticker, Update
from telegram.ext import MessageHandler, CommandHandler,Application,ContextTypes,filters
from typing import Final
from constants import bot_token, bot_username,api_hash,api_id


async def start_Command(update: Update,context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply.text("Hello there!Let's start chatting")

def handle_response(text:str)->str:
    if 'تق تق' in text:
        return 'کیه؟'
    else:
        return text
    
def handle_response(content: Sticker)->Sticker:
    return content

def handle_response(content: Document)->Document:
    return Document


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message

    # Extract message content based on message type
    if message.text:  # Text message
        content = message.text
    elif message.sticker:  # Sticker message
        content = message.sticker
    elif message.document:  # Document (including GIF) message
        content = message.document
    else:
        content = "Received a message of unsupported type"

    response = handle_response(content)
    print('Bot:', response)
    if message.text:
        await update.message.reply_text(response)
    elif message.sticker:
        await update.message.reply_sticker(response)
    else:
        await update.message.reply_document(response)


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


