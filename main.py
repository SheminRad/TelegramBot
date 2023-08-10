#from constants import bot_token , bot_username
from telegram import Update
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

async def handle_meassage(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')

    if message_type == 'group':
        if bot_token in text:
            new_text: str = text.replace(bot_token,'').strip()
            response: str = handle_response(new_text)
        else:
            return
    else:
        response: str = handle_response(text)

    print('Bot: ',response)
    await update.message.reply_text(response)


async def error(update: Update,context:ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')

if __name__ == '__main__':
    print('Starting bot...')
    app = Application.builder().token(bot_token).build()

    #Commands
    app.add_handler(CommandHandler('start', start_Command)) 

    #Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_meassage))

    #Errors
    app.add_error_handler(error)

    print('Polling...')
    app.run_polling(poll_interval=3)


