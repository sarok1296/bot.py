import os
from telegram import Update
from telegram.ext import Application, MessageHandler, CommandHandler, ContextTypes, filters

TOKEN = os.environ.get("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "سڵاو 👋\n"
        "بۆتەکە چالاکە.\n\n"
        "وێنەیەک بنێرە بۆ دەستپێکردنی پشکنین."
    )

async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📷 وێنەکەت وەرگیرا.\n"
        "🔎 لە وەشانی داهاتوودا پشکنینی وێنە، OCR و ڕاپۆرتی بەڵگە زیاد دەکرێت."
    )

def main():
    if not TOKEN:
        raise RuntimeError("BOT_TOKEN is not configured")

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.PHOTO, handle_photo))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main() 
