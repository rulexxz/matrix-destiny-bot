from telegram import Update
from datetime import datetime
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

# ==========================
# ВСТАВЬ СЮДА ТОКЕН БОТА
# ==========================
TOKEN = "8890250236:AAFBzcIzl0yBxqwCFbHhljug4MD9HbGr1B8"

# ==========================
# СЮДА ПОТОМ ВСТАВИМ ID АННЫ
# ==========================
ANNA_ID = 450982711


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(update.effective_user.id)

    await update.message.reply_text(
        "🌿 Благодарю за доверие!\n\n"
        "Чтобы записаться на разбор, пожалуйста, отправьте:\n\n"
        "1. Ваше имя.\n"
        "2. Дату рождения.\n"
        "3. Ваш главный вопрос.\n\n"
        "✨ Вопрос может звучать в свободной форме."
    )


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user

    now = datetime.now()
    current_time = now.strftime("%d.%m.%Y %H:%M")
    text = (
        f"🔮 НОВАЯ ЗАЯВКА — МАТРИЦА СУДЬБЫ\n"
        f"━━━━━━━━━━━━━━━━━━\n\n"
        f"🕒 Дата: {current_time}\n\n"
        f"👤 Имя: {user.full_name}\n"
        f"🆔 Telegram ID: {user.id}\n"
        f"📱 Username: @{user.username if user.username else 'нет'}\n\n"
        f"💬 Заявка клиента:\n\n"
        f"{update.message.text}\n\n"
        f"━━━━━━━━━━━━━━━━━━"
    )

    if ANNA_ID != 0:
        await context.bot.send_message(chat_id=ANNA_ID, text=text)

    await update.message.reply_text(
        "💫 Спасибо!\n\n"
        "Ваша заявка принята.\n\n"
        "В ближайшее время Анна лично ознакомится с вашим запросом "
        "и свяжется с вами для согласования консультации.\n\n"
        "До встречи! 🌿\n\n"
        "*Стоимость консультации зависит от заданного вопроса.*",
        parse_mode="Markdown"
    )


def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Бот запущен!")

    app.run_polling()


if __name__ == "__main__":
    main()