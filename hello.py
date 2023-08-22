from telegram import Update
from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler, Filters, CallbackContext

# State constants
USER_STATE1, USER_STATE2, USER_STATE3 = range(3)

# Entry point for the conversation
def start_command(update: Update, context: CallbackContext):
    update.message.reply_text("Hello! Let's start a conversation. Send 'next' to proceed.")
    return USER_STATE1

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
        return

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
    #stored_value = user_data.get('key1', 'No value')
    #return ConversationHandler.END
   
    #update.message.reply_text("Send 'finish' to end the conversation.")

if __name__ == '__main__':
    updater = Updater(token='YOUR_BOT_TOKEN', use_context=True)
    dispatcher = updater.dispatcher
    
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start_command)],
        states={
            USER_STATE1: [MessageHandler(Filters.text, handle_user_state1)],
            USER_STATE2: [MessageHandler(Filters.text, handle_user_state2)],
            USER_STATE3: [MessageHandler(Filters.text, handle_user_state3)]
        },
        fallbacks=[]
    )
    
    dispatcher.add_handler(conv_handler)
    
    updater.start_polling()
    updater.idle()
