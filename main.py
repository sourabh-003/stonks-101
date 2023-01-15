import telebot
import logging
import bse
import creds



# Set up the logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logging.info('Starting Bot...')


bot = telebot.TeleBot(creds.token)

@bot.message_handler(['start'])
def start(message):
    bot.reply_to(message, "Hello, this is Stonks 101, check out the functionalities of the bot in the menu")

@bot.message_handler(['help'])
def help(message):
    bot.reply_to(message, """
    The available functions are:
/topgainers: High performing stocks
/toplosers: Low performing stocks
/stockprice: Check live prices
/companycode: Search for the company code
     """)

@bot.message_handler(['topgainers'])
def topgainers(message):
    ret = bse.topgainers()
    bot.reply_to(message, ret)

@bot.message_handler(['toplosers'])
def toplosers(message):
    ret = bse.toplosers()
    bot.reply_to(message, ret)



@bot.message_handler(['stockprice'])
def stockprice(message):
    try:
        bot.reply_to(message,"""Enter the company code eg. HDFC, SBIN , TITAN, BHEL etc.: """)
        @bot.message_handler()
        def custom(message):
            msg = message.text
            ret = bse.stockprice(msg)
            bot.reply_to(message,ret)

    
    except:
        bot.reply_to(message,"Not found, possibly because of wrong fields entered")
    
    

@bot.message_handler(['stockhistory'])
def stockhistory(message):
    markup = telebot.types.InlineKeyboardMarkup()

    # Create the buttons
    button1 = telebot.types.InlineKeyboardButton("1M", callback_data="1M")
    button2 = telebot.types.InlineKeyboardButton("3M", callback_data="3M")
    button3 = telebot.types.InlineKeyboardButton("6M", callback_data="6M")

    # Add the buttons to the markup
    markup.add(button1, button2, button3)

    # Send the message with the inline keyboard
    bot.send_message(message.chat.id, "Please select the duration:", reply_markup=markup)
    @bot.callback_query_handler(func=lambda call: True)
    def callback_inline(call):
        if call.message:
            if call.data == "1M":
                time = "1M"
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="You selected 1M.")
            elif call.data == "3M":
                time = "3M"
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="You selected 3M.")

            elif call.data == "6M":
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="You selected 6M.")
                time = "6M"
        

            
            bot.reply_to(message,"""Enter the company code eg. HDFC, SBIN , TITAN, BHEL etc.: """)
            @bot.message_handler()
            def custom(message):
                msg = message.text
                ret = bse.stockhistory(msg,call.data)
                bot.reply_to(message,ret)
           
    
                   


@bot.message_handler(['companycode'])
def companycode(message):
    bot.reply_to(message, "click on this link: bseindia.com/corporates/List_Scrips.html")

bot.polling()
