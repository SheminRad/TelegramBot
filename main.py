from constants import bot_token , bot_username
from telegram import Document, Sticker, Update
from telegram.ext import MessageHandler, CommandHandler,Application,ContextTypes,filters,CallbackContext,ConversationHandler
#from typing import Final


USER_STATE1, USER_STATE2, USER_STATE3, LAST_STATE = range(4)


# Handler for the first state
def handle_user_state1(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    user_data = context.user_data.get(user_id, {})  # Get user-specific dictionary
    
    message = update.message.text
    if message == 'تق تق':
        user_data['key1'] = 'value1'  # Store a key-value pair for the user
        update.message.reply_text("کیه؟")
        return USER_STATE2
    else:
        return LAST_STATE

# Handler for the second state
def handle_user_state2(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    user_data = context.user_data.get(user_id, {})
    
    message = update.message.text
    #stored_value = user_data.get('key1', 'No value')  # Retrieve the stored value
    update.message.reply_text( message + "کیه")
    return USER_STATE3
    

def handle_user_state3(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    user_data = context.user_data.get(user_id, {})
    
    message = update.message.text
    update.message.reply_text(":)")

async def start_Command(update: Update,context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply.text("Hello there!Let's start chatting")
    return USER_STATE1 

def handle_response(text:str)->str:
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
        await update.message.reply_text(response)
    print('Bot: ',response)
    #await update.message.reply_text(response)
async def error(update: Update,context:ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')

if __name__ == '__main__':
    print('Starting bot...')
    app = Application.builder().token(bot_token).build()

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start_Command)],
        states={
            USER_STATE1: [MessageHandler(filters.TEXT, handle_user_state1)],
            USER_STATE2: [MessageHandler(filters.TEXT, handle_user_state2)],
            USER_STATE3: [MessageHandler(filters.TEXT, handle_user_state3)],
            LAST_STATE: [MessageHandler(filters.TEXT, handle_message)]
        },
        fallbacks=[]
    )
    #Commands
    app.add_handler(CommandHandler('start', start_Command)) 

    #Messages
    app.add_handler(MessageHandler(filters.ALL, handle_message))

    #Errors
    app.add_error_handler(error)

    print('Polling...')
    app.run_polling(poll_interval=3)


