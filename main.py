from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler,MessageHandler, ContextTypes, filters
import time

TOKEN = "7198080460:AAEmAEqdlyC53Cuc3yJcIm7fLIui-T_WU7g"

# Command Handlers
async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')


# Message Handlers
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(update.message.text)


def get_app():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("hello", hello))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    return app


if __name__ == "__main__":
    app = get_app()
    print("Polling..")
    app.run_polling(10)