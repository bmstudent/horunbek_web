# Bot API tokeni
API_TOKEN = 'YOUR_API_TOKEN'

# Sizga habar yuborish uchun botga xabar yuborilganda trigger qilinadigan funksiya
def notify(update, context):
    user_message = update.message.text  # Xabar matnini oling
    user = update.message.from_user.username  # Foydalanuvchi nomini oling
    print(f"Xabar yuborildi: {user} - {user_message}")

    # Sizga xabar yuborish
    context.bot.send_message(chat_id="YOUR_CHAT_ID", text=f"Yangi xabar: {user} - {user_message}")

# Asosiy funksiya
def main():
    updater = Updater(API_TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # Xabar yuborilganida trigger qilinadigan handler
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, notify))

    # Botni ishga tushirish
    updater.start_polling()
    updater.idle()

if name == 'main':
    main()