import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    await update.message.reply_text(
        f"Привет {user.first_name}! 🤖\n"
        "Я AI-генератор контента. Просто напиши тему, и я создам:\n"
        "• Посты для соцсетей\n• Тексты для блога\n• Описания товаров\n"
        "Напиши что хочешь, например: 'пост про кофе для Instagram'"
    )

# Обработка текстовых сообщений
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    
    # Простой ответ (замените на вызов AI API)
    ai_response = f"🔮 Вот что я создал по запросу '{user_message}':\n\n"
    ai_response += "🌟 Уникальный контент будет здесь!\n\n"
    ai_response += "💡 Хочешь больше возможностей? Напиши /premium"
    
    await update.message.reply_text(ai_response)

# Команда /premium
async def premium(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🚀 Премиум версия включает:\n"
        "• Безлимитная генерация\n• 10+ типов контента\n• Приоритетная очередь\n"
        "💳 Стоимость: 299 руб/месяц\n"
        "📧 Для подключения: @your_username"
    )

def main():
    # Получаем токен из переменных окружения Railway
    token = os.getenv('TELEGRAM_BOT_TOKEN')
    
    if not token:
        logger.error("Токен бота не найден!")
        return

    # Создаем приложение
    application = Application.builder().token(token).build()
    
    # Добавляем обработчики
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("premium", premium))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    # Запускаем бота
    application.run_polling()

if __name__ == '__main__':
    main()
