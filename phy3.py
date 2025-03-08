import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from gtts import gTTS
from googletrans import Translator
import os
import html
from time import sleep

# توكن البوت
bot = telebot.TeleBot("7837405948:AAFrC5UZTSqxR8tVmGcOyyoxcB8SpjZJmmE")

# إعدادات عامة
CHANNEL_USERNAME = "@Shahmplus"
ADMIN_ID = 6848908141
LANGUAGES = {
    'ar': 'العربية',
    'en': 'الإنجليزية',
    'fr': 'الفرنسية',
    'tr': 'التركية',
    'ru': 'الروسية',
    'zh-cn': 'الصينية',
    'es': 'الإسبانية',
    'ko': 'الكورية',
    'ja': 'اليابانية',
    'hi': 'الهندية'
}
user_settings = {}
user_ids_file = "user_ids.txt"
banned_users_file = "banned_users.txt"

# تحميل البيانات
if not os.path.exists(user_ids_file):
    open(user_ids_file, "w").close()
if not os.path.exists(banned_users_file):
    open(banned_users_file, "w").close()

with open(user_ids_file, "r") as f:
    user_ids = set(f.read().splitlines())
with open(banned_users_file, "r") as f:
    banned_users = set(f.read().splitlines())

# الاشتراك الإجباري
def is_subscribed(user_id):
    try:
        status = bot.get_chat_member(CHANNEL_USERNAME, user_id).status
        return status in ['member', 'administrator', 'creator']
    except Exception:
        return False

def is_banned(user_id):
    return str(user_id) in banned_users

# قائمة الرئيسية
def main_menu():
    markup = InlineKeyboardMarkup()
    markup.row(
        InlineKeyboardButton("تغيير اللغة 🌍", callback_data="change_language"),
        InlineKeyboardButton("تغيير السرعة ⏩", callback_data="change_speed")
    )
    markup.row(
        InlineKeyboardButton("مطور البوت", url="https://t.me/o_p_g"),
        InlineKeyboardButton("- تخص المطور -👨‍💻", callback_data="admin" if ADMIN_ID == 6848908141 else "none")
    )
    return markup

def return_button():
    return InlineKeyboardMarkup().add(InlineKeyboardButton("⬅️ العودة إلى القائمة الرئيسية", callback_data="main_menu"))

# بدء المحادثة
@bot.message_handler(commands=['start'])
def start_message(message):
    user_id = message.from_user.id
    if is_banned(user_id):
        bot.send_message(user_id, "🚫 تم حظرك من استخدام هذا البوت.")
        return

    # التحقق من المستخدم الجديد
    if str(user_id) not in user_ids:
        user_name = html.escape(message.from_user.full_name)  # تأمين النص من مشاكل HTML
        user_link = f"<a href='tg://user?id={user_id}'>{user_name}</a>"
        
        with open(user_ids_file, "a") as f:
            f.write(f"{user_id}\n")
        user_ids.add(str(user_id))

        # إرسال إشعار إلى المطور
        bot.send_message(
            ADMIN_ID,
            f"🔔 عضو جديد انضم إلى البوت:\n{user_link}\n\n🆔 <code>{user_id}</code>",
            parse_mode='HTML'
        )

    # التحقق من الاشتراك في القناة
    if not is_subscribed(user_id):
        bot.send_message(user_id, f"⚠️ يجب عليك الاشتراك في القناة أولًا:\n{CHANNEL_USERNAME}")
    else:
        bot.send_message(
            user_id,
            "- هلا بيك\n- تم تصميم هذا البوت لتعليم النطق وترجمة النصوص.\n- صنع بحب @O_P_G",
            reply_markup=main_menu()
        )

# ترجمة النصوص
def translate_text(text, target_lang='ar'):
    translator = Translator()
    translation = translator.translate(text, dest=target_lang)
    return translation.text

# تحويل النص إلى رسالة صوتية بصيغة ogg
def text_to_speech(text, lang='en', filename='voice.ogg'):
    tts = gTTS(text=text, lang=lang)
    tts.save(filename)

# التعامل مع الرسائل النصية من المستخدمين
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_id = message.from_user.id
    text = message.text

    if not is_subscribed(user_id):
        bot.send_message(user_id, f"⚠️ يجب عليك الاشتراك في القناة أولًا:\n{CHANNEL_USERNAME}")
        return

    if text:
        # توليد رسالة صوتية للنص المدخل بصيغة ogg
        original_text_filename = 'original_text.ogg'
        text_to_speech(text, lang=user_settings.get(user_id, {}).get('lang', 'en'), filename=original_text_filename)

        # ترجمة النص إلى العربية
        translated_text = translate_text(text, 'ar')

        # توليد رسالة صوتية للنص المترجم بصيغة ogg
        translated_text_filename = 'translated_text.ogg'
        text_to_speech(translated_text, lang='ar', filename=translated_text_filename)

        # إرسال الرسائل الصوتية
        bot.send_audio(user_id, open(original_text_filename, 'rb'), caption="🔊 النص المدخل")
        bot.send_audio(user_id, open(translated_text_filename, 'rb'), caption="🔊 الترجمة إلى العربية")

        # حذف الملفات الصوتية بعد إرسالها
        os.remove(original_text_filename)
        os.remove(translated_text_filename)

# تشغيل البوت
while True:
    try:
        print('البوت قيد التشغيل......')
        bot.polling(non_stop=True)
    except Exception as e:
        print(f"Error: {e}")
        sleep(15)
