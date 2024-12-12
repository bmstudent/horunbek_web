import logging
from aiogram import Bot, Dispatcher, executor, types

# Telegram bot tokenini shu yerga joylashtiring
API_TOKEN = 'YOUR_BOT_API_TOKEN'

# Loglar uchun sozlama
def logging_setup():
    logging.basicConfig(level=logging.INFO, 
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Bot va dispatcher yaratish
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Admin ID si (o'zingizni Telegram ID raqamingizni kiriting)
ADMIN_ID = 'YOUR_TELEGRAM_ID'

# Foydalanuvchi /start bosganda ishlaydigan funksiya
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    # Foydalanuvchini kutib olish xabari
    await message.reply("Salom! Bu bot orqali siz bilan bog'lanish mumkin!")

    # Adminni xabardor qilish
    admin_message = f"Yangi foydalanuvchi ulandi: {message.from_user.full_name} (ID: {message.from_user.id})"
    await bot.send_message(chat_id=ADMIN_ID, text=admin_message)

# Xabarni jo'natish uchun universal funksiya
async def notify_admin(event_text):
    await bot.send_message(chat_id=ADMIN_ID, text=event_text)

# Botni ishga tushirish
if __name__ == '__main__':
    logging_setup()
    executor.start_polling(dp, skip_updates=True)
