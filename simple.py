import telebot

# โทเค็นบอทของคุณ
BOT_TOKEN = "YOUR_BOT_TOKEN"

# สร้างตัวอย่างบอท
bot = telebot.TeleBot(BOT_TOKEN)

# ฟังก์ชันการทำงานเมื่อมีคนส่งข้อความ
@bot.message_handler(func=lambda message: True)
def handle_message(message):
  # ตอบกลับข้อความ
  bot.reply_to(message, "สวัสดี! คุณส่งข้อความอะไรมา")

# เริ่มการทำงานของบอท
bot.polling()
