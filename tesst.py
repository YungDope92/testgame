import telebot
from telebot import types

# Replace with your actual bot token
TOKEN = '6547449335:AAFNYjGkppLT3cnR6GhHzgLpIgQcb-iixn0'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Welcome to the 3D Game! Click /play to start playing.")

@bot.message_handler(commands=['play'])
def play_game(message):
    game_url = "https://your-game-url.com"  # Replace with your actual game URL
    markup = types.InlineKeyboardMarkup()
    btn = types.InlineKeyboardButton("Play 3D Game", url=game_url)
    markup.add(btn)
    bot.send_message(message.chat.id, "Click below to play the 3D Game!", reply_markup=markup)

bot.polling()
