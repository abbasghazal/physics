import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from gtts import gTTS
from googletrans import Translator
import os
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
        user_link = f"<a href='tg://user?id={user_id}'>{message.from_user.full_name}</a>"
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

# قائمة التنقل والتحكم
@bot.callback_query_handler(func=lambda call: True)
def handle_callback_query(call):
    user_id = call.from_user.id

    if call.data == "main_menu":
        bot.edit_message_text("- هلا بيك\n- تم تصميم هذا البوت لتعليم النطق وترجمة النصوص.\n- صنع بحب @O_P_G", call.message.chat.id, call.message.message_id, reply_markup=main_menu())
    elif call.data == "change_language":
        markup = InlineKeyboardMarkup(row_width=2)
        buttons = [InlineKeyboardButton(name, callback_data=f"lang_{code}") for code, name in LANGUAGES.items()]
        for i in range(0, len(buttons), 2):
            markup.row(*buttons[i:i+2])
        markup.add(InlineKeyboardButton("⬅️ عودة", callback_data="main_menu"))
        bot.edit_message_text("- لقد قمت بالضغط على زر اللغات\n- ارسل النص باللغة التي تريد ان انطقه لك بها", call.message.chat.id, call.message.message_id, reply_markup=markup)
    elif call.data.startswith("lang_"):
        lang = call.data.split("_")[1]
        user_settings[user_id] = user_settings.get(user_id, {'lang': 'ar', 'speed': 1.0})
        user_settings[user_id]['lang'] = lang
        bot.answer_callback_query(call.id, f"✅ تم تغيير اللغة إلى {LANGUAGES[lang]}")
    elif call.data == "change_speed":
        markup = InlineKeyboardMarkup()
        speeds = ['0.5', '0.75', '1.0', '1.25', '1.5', '2.0']
        for speed in speeds:
            markup.add(InlineKeyboardButton(speed, callback_data=f"speed_{speed}"))
        markup.add(InlineKeyboardButton("⬅️ عودة", callback_data="main_menu"))
        bot.edit_message_text("- قمت بالضغط على زر التحكم بسرعة الصوت \n- اضغط على السرعة التي تحب ان تسمع الصوت بها", call.message.chat.id, call.message.message_id, reply_markup=markup)
    elif call.data.startswith("speed_"):
        speed = float(call.data.split("_")[1])
        user_settings[user_id] = user_settings.get(user_id, {'lang': 'ar', 'speed': 1.0})
        user_settings[user_id]['speed'] = speed
        bot.answer_callback_query(call.id, f"✅ تم تغيير السرعة إلى {speed}x")
    elif call.data == "admin" and user_id == ADMIN_ID:
        markup = InlineKeyboardMarkup()
        markup.add(
            InlineKeyboardButton("إحصائيات 📊", callback_data="stats"),
            InlineKeyboardButton("حظر مستخدم 🚫", callback_data="ban_user"),
        )
        markup.add(InlineKeyboardButton("⬅️ العودة", callback_data="main_menu"))
        bot.edit_message_text("هذه الازرار مخصصة للمطور فقط ", call.message.chat.id, call.message.message_id, reply_markup=markup)
    elif call.data == "stats" and user_id == ADMIN_ID:
        bot.answer_callback_query(call.id, f"👥 عدد المستخدمين: {len(user_ids)}")
    elif call.data == "ban_user" and user_id == ADMIN_ID:
        bot.send_message(ADMIN_ID, "🔒 أرسل ID المستخدم الذي تريد حظره:")
        bot.register_next_step_handler_by_chat_id(ADMIN_ID, ban_user)

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

def ban_user(message):
    try:
        user_id = message.text
        if user_id in user_ids and user_id not in banned_users:
            with open(banned_users_file, "a") as f:
                f.write(f"{user_id}\n")
            banned_users.add(user_id)
            bot.send_message(ADMIN_ID, f"🚫 تم حظر المستخدم: {user_id}")
        else:
            bot.send_message(ADMIN_ID, "⚠️ المستخدم غير موجود أو محظور بالفعل.")
    except Exception as e:
        bot.send_message(ADMIN_ID, f"❌ خطأ: {e}")

# تشغيل البوت
while True:
    try:
        print('البوت قيد التشغيل......')
        bot.polling(non_stop=True)
    except Exception as e:
        print(f"Error: {e}")
        sleep(15)
