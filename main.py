from constants import bot_token , bot_username
from telegram import Document, Sticker, Update
from telegram.ext import MessageHandler, CommandHandler,Application
from telegram.ext import ContextTypes,filters,CallbackContext,ConversationHandler
#from typing import Final


USER_STATE = {}
#start
#---------------------------------------------------------------------
#---------------------------------------------------------------------
async def start_Command(update: Update,context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello there!Let's start chatting")
    USER_STATE[update.effective_user.id] = 0
#---------------------------------------------------------------------
#---------------------------------------------------------------------
def handle_response(text:str)->str:
    return text
    
def handle_response_sticker(content: Sticker)->Sticker:
    return content

def handle_response_document(content: Document)->Document:
    return Document
#---------------------------------------------------------------------
#---------------------------------------------------------------------
# Handler for the state
async def handle_user_state1(update: Update, context: ContextTypes.DEFAULT_TYPE, status):
    print("worked3")
    user_id = update.effective_user.id
    user_data = context.user_data.get(user_id, {})  # Get user-specific dictionary
    
    message = update.message.text
    if status == 1:
        print("worked4")
        user_data['key1'] = 'value1'  # Store a key-value pair for the user
        print("worked5")
        await update.message.reply_text("کیه؟")
        return 2
        #USER_STATE[update.effective_user.id] = await handle_user_state1(update,context,2)
    elif status == 2:
        await update.message.reply_text(f"{message} کیه؟")
        return 3
        #USER_STATE[update.effective_user.id] = await handle_user_state1(update,context,3)
    elif status == 3:
        await update.message.reply_text(":)")
        return 0
        #USER_STATE[update.effective_user.id] = await handle_user_state1(update,context,0)
#---------------------------------------------------------------------
#---------------------------------------------------------------------
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message
    if 'تق تق' in message.text.strip().lower():
        print(update.effective_user.id, " called taq taq")
        USER_STATE[update.effective_user.id] = 1
        print("worked1")
    state = USER_STATE.get(update.effective_user.id, 0)

    if state == 0:
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
            await update.message.reply_text(message)
            print('Bot: ',response)
    else:
       print("worked2")
       USER_STATE[update.effective_user.id] = await handle_user_state1(update, context, state)

#---------------------------------------------------------------------
#---------------------------------------------------------------------
#error handler
async def error(update: Update,context:ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')
#---------------------------------------------------------------------
#---------------------------------------------------------------------
#main
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