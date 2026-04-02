from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
import os

TOKEN = os.getenv("TOKEN")

# START MENU
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📖 Study Notes", callback_data='notes')],
        [InlineKeyboardButton("📝 Quiz", callback_data='quiz')],
        [InlineKeyboardButton("🎯 Competitive Journey", callback_data='comp')],
        [InlineKeyboardButton("ℹ️ About", callback_data='about')]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "Welcome to Sikshangan 📚\nChoose an option:",
        reply_markup=reply_markup
    )

# BUTTON HANDLER
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    # STUDY NOTES
    if query.data == "notes":
        keyboard = [
            [InlineKeyboardButton(f"Class {i}", callback_data=f"notes_class_{i}")]
            for i in range(4, 13)
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.message.reply_text("Select Class:", reply_markup=reply_markup)

    # QUIZ
    elif query.data == "quiz":
        keyboard = [
            [InlineKeyboardButton(f"Class {i}", callback_data=f"quiz_class_{i}")]
            for i in range(4, 13)
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.message.reply_text("Select Class for Quiz:", reply_markup=reply_markup)

    # COMPETITIVE
    elif query.data == "comp":
        await query.message.reply_text("Competitive section coming soon 🚀")

    # ABOUT
    elif query.data == "about":
        await query.message.reply_text("Sikshangan Bot 📚\nYour smart study partner.")

    # SUBJECT SELECTION (NOTES)
    elif "notes_class_" in query.data:
        cls = query.data.split("_")[-1]
        keyboard = [
            [InlineKeyboardButton("Math", callback_data=f"notes_{cls}_math")],
            [InlineKeyboardButton("English", callback_data=f"notes_{cls}_eng")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.message.reply_text(f"Class {cls} - Choose Subject:", reply_markup=reply_markup)

    # SUBJECT SELECTION (QUIZ)
    elif "quiz_class_" in query.data:
        cls = query.data.split("_")[-1]
        keyboard = [
            [InlineKeyboardButton("Math", callback_data=f"quiz_{cls}_math")],
            [InlineKeyboardButton("English", callback_data=f"quiz_{cls}_eng")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.message.reply_text(f"Class {cls} Quiz - Choose Subject:", reply_markup=reply_markup)

    # FINAL PLACEHOLDER
    elif "notes_" in query.data:
        await query.message.reply_text("Notes will be added here 📄")

    elif "quiz_" in query.data:
        await query.message.reply_text("Quiz will be added here 📝")


app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button))

app.run_polling()
