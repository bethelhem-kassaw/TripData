import os
from dotenv import load_dotenv
from telegram.ext import *
from telegram import Update

# Load environment variables from .env
load_dotenv()

# Access the API key
api_key = os.environ.get("BOT_TOKEN")


# def start(update: Updater, context: CommandHandler):
#     """Greets the user and explains the bot's functionality"""
#     update.message.reply_text(
#         "Hi! Enter your name and I'll store it for now."
#     )

# def get_name(update: Updater, context: CommandHandler):
#     """Logs the user's entered name to the console and replies with success message"""
#     name = update.message.text.strip()
#     print(f"User entered name: {name}")
#     update.message.reply_text(f"Successfully added your name: {name}!")


async def start_command(update:Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello there can you please enter a Hiking group  telegram username by replying to this message as /name and then your group name')


async def get_name(update:Update, context: ContextTypes.DEFAULT_TYPE):
    name = update.message.text.strip()[6:]
    print(f"User entered name: {name}")
    await update.message.reply_text(f"Successfully added your name: {name}!")



async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')

def main():
    print('Starting bot...')
    app = Application.builder().token(api_key).build()
    
   
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("name", get_name))
    
    app.add_error_handler(error)
    print('polling...')
    app.run_polling(poll_interval=3)
    


main()