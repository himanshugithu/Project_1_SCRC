
import telebot
from gtts import gTTS
import os
import socket
import subprocess
import oneM2Mget
# Replace with your bot token
BOT_TOKEN = ''
bot = telebot.TeleBot(BOT_TOKEN)

# Function to convert text to speech and play it
def text_to_speech(text, language='en', filename='output.mp3', play=True):
    tts = gTTS(text=text, lang=language, slow=False)
    tts.save(filename)
    if play:
        os.system(f"mpg321 {filename}")  # Play the audio file

# Define a function to handle the /start command
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hello! Use /play to play predefined text or /playcustom to play custom text.")

# Define a function to handle the /play command (predefined text)
@bot.message_handler(commands=['play'])
def play_audio(message):
    response_data = oneM2Mget.getTemperature()
    con_value = response_data
    predefined_text = f"Welcome to Smart City Living Lab. We have deployed over three hundred sensor nodes all over the campus and we also have wi sun backbone network in place. The current value of CO2 is {con_value[1]}, temperature is {con_value[2]}, and humidity is {con_value[3]}."
    # predefined_text = "Hello, Welcome to Smart city living lab, have a nice day."
    bot.reply_to(message, "Playing predefined text.")
    text_to_speech(predefined_text)

# Define a function to handle the /playcustom command (custom text)
@bot.message_handler(commands=['playcustom'])
def play_custom_audio(message):
    # Extract the text after the "/playcustom:" command
    if ':' in message.text:
        custom_text = message.text.split(":", 1)[1].strip()  # Extract text after the colon
        if custom_text:
            bot.reply_to(message, f"Playing custom text: {custom_text}")
            text_to_speech(custom_text)  # Play the custom text
        else:
            bot.reply_to(message, "No custom text provided after /playcustom.")
    else:
        bot.reply_to(message, "Please provide custom text using /playcustom:your text")

# Function to get the IP address
def get_ip_address():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip_address = s.getsockname()[0]
        s.close()
        return ip_address
    except Exception as e:
        return "Unable to get IP address: {}".format(str(e))

# Function to check Wi-Fi connection status
def check_wifi_connection():
    try:
        result = subprocess.run(['iwgetid'], stdout=subprocess.PIPE)
        wifi_info = result.stdout.decode('utf-8')
        if wifi_info:
            return "Connected to WiFi network: {}".format(wifi_info.strip())
        else:
            return "Not connected to any WiFi network"
    except Exception as e:
        return "Unable to determine WiFi connection status: {}".format(str(e))

# Define a function to handle the /ip command
@bot.message_handler(commands=['ip'])
def send_ip_info(message):
    ip_address = get_ip_address()
    wifi_status = check_wifi_connection()
    bot.reply_to(message, f"IP Address: {ip_address}\nWiFi Status: {wifi_status}")

@bot.message_handler(commands=['reboot'])
def reboot_rpi(message):
    bot.reply_to(message, "Reboot successful....")
    os.system("sudo reboot")

@bot.message_handler(func=lambda message: True)
def handle_data(message):
    data = message.text
    bot.reply_to(message, f"Received data: {data}")

# Start the bot
bot.polling()
