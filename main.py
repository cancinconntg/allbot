import telebot

TOKEN = "" #@BotFather
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def start(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Mandame un privado con '/join {0}'".format(chat_id))

@bot.message_handler(commands=["join"])
def join(message):
    print "group: " + message.text.replace("/join","").replace(" ","")
    user_id = str(message.from_user.id)
    id_file = open("id.txt","a+")
    id_list = id_file.readlines()
    estar = False
    print user_id, id_list  
    for i in id_list:
        if i.replace("\n","") == user_id:
            estar = True
    if not estar:
        id_file.write("{0}\n".format(user_id))
    id_file.close()

@bot.message_handler(commands=["all@allTestBot","all"])
def all(message):
    ctext = message.text.replace("/all ","")
    id_list = open("id.txt","r").readlines()
    for i in id_list:
        user_id = i.replace("\n","")
        #bot.send_message(int(user_id), text)
        bot.send_message(int(user_id), "@" + str(message.from_user.username) + " (*" + message.chat.title + "*): " + ctext + "\n", parse_mode = 'Markdown')
        
@bot.message_handler(commands=["data"])
def data(message):
    print(message)

bot.polling()
