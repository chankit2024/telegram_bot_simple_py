import telebot

# Token
BOT_TOKEN = "YOUR_BOT_TOKEN"

# Create Bot
bot = telebot.TeleBot(BOT_TOKEN)

# Receive Message
@bot.message_handler(func=lambda message: True)
def handle_message(message):
  # Reply Message
  bot.reply_to(message, "Hello !!")

# Start Bot
bot.polling()
