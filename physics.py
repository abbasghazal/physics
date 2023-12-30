import telebot
import random
from time import sleep
from telebot import types
bot = telebot.TeleBot('6333831584:AAHr1e0wt_3V8bxSvj0GBBKkfmSZjqa7R8k')

@bot.message_handler(commands=['start'])
def start(message):
    dev = 'SHAHM4'
    ad='6066647930'
    with open("id.txt", "r") as file:
        ids = file.readlines()
        user_id = str(message.from_user.id)
        if user_id not in ids:
            with open("id.txt", "a") as file:
                file.write(user_id + "\n")
            bot.send_message(ad, f"مستخدم جديد:\nإسمه: {message.from_user.first_name} .\nيوزره: @{message.from_user.username} .\nأيديه: {message.from_user.id} .\n[المبرمج](t.me/{dev})")
            markup = types.InlineKeyboardMarkup(row_width=2)
            saif1 = types.InlineKeyboardButton('مختبرات', callback_data='مختبرات')
            saif2 = types.InlineKeyboardButton('ملازم المواد', callback_data='ملازم المواد')
            saif3 = types.InlineKeyboardButton('تحفيز', callback_data='تحفيز')
            saif4 = types.InlineKeyboardButton('ملاحظات وامتحانات', callback_data='اشياء تفيدك')
            markup.add(saif1, saif2, saif3, saif4)

            bot.send_message(message.chat.id, '''🔰السلام عليكم ورحمة الله وبركاته عزيزي الطالب
⭕ اهلا بك في بوت المرحلة الثانية لقسم الفيزياء 
🔰شكر خاص الى مجموعة من طلاب قسم الفيزياء 
⭕هذا البوت من تطوير 
𝑨𝑩𝑩𝑨𝑺 𝑮𝑯𝑨𝒁𝑾𝑨𝑵
لتواصل: @SHAHM4
قناتي: @BGGlG ''', reply_markup=markup)
@bot.message_handler(func=lambda message: message.text.lower() == 'غادر' and message.from_user.id ==6066647930)
def leavechat(message):
    bot.send_message(chat_id=message.chat.id,text='حسنا يا مطوري ساقوم بمغادرة المجموعة حسب طلبك')
    chatid = message.chat.id
    bot.leave_chat(chatid)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
 message = call.message
 chat_id = message.chat.id
 if call.data == 'مختبرات':
  markup = types.InlineKeyboardMarkup(row_width=2)
  btn1 = types.InlineKeyboardButton('ملزمة كهربائية عملي', callback_data='ملزمة كهربائية عملي')
  btn2 = types.InlineKeyboardButton('ملزمة بصريات عملي', callback_data='ملزمة بصريات')
  btn3 = types.InlineKeyboardButton('ملزمة برمجة عملي', callback_data='ملزمة برمجة')
  btn4=types.InlineKeyboardButton('التقارير',callback_data='تقارير')
  btn5 = types.InlineKeyboardButton('شرح التجارب', callback_data='شرح التجارب')
  btn6=types.InlineKeyboardButton(text='عودة🔙',callback_data='back')
  markup.add(btn1, btn2, btn3,btn4,btn5,btn6)
  bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="اليك ملازم المختبرات و تقارير المرحلة الثانية ", reply_markup=markup)
 elif call.data == 'تقارير':
   markup = types.InlineKeyboardMarkup(row_width=1)
   btn1 = types.InlineKeyboardButton('تقارير الكهربائية', callback_data='تقرير كهرو')
   btn2 = types.InlineKeyboardButton('تقارير البصريات', callback_data='تقرير بصر')
   btn3=types.InlineKeyboardButton(text='عودة🔙',callback_data='back')
   markup.add(btn1, btn2, btn3)
   bot.edit_message_text(chat_id=call.message.chat.id, message_id=call. message.message_id, text="اختر تقارير المختبر الذي تريده ", reply_markup=markup)
 elif call.data == 'تقرير بصر':
  markup = types.InlineKeyboardMarkup(row_width=1)
  btn1 = types.InlineKeyboardButton('رسم منحني بياني لبيان اصغر مسافة .....', callback_data='ت1')
  btn2 = types.InlineKeyboardButton('قياس البعد البؤري لعدسة مقعرة باستخدام عدسة محدبة...', callback_data='ت2')
  btn3 = types.InlineKeyboardButton('رسم خط بياني لاثبات ان التكبير بواسطة عدسة محدبة ....', callback_data='ت3')
  btn4=types.InlineKeyboardButton('مدخال مايكلسون',callback_data='ت4')
  btn5 = types.InlineKeyboardButton('تحفيز', callback_data='تحفيز')
  btn6=types.InlineKeyboardButton(text='عودة🔙',callback_data='back')
  markup.add(btn1, btn2, btn3,btn4,btn5,btn6)
  bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="اليك ملازم المختبرات و تقارير المرحلة الثانية الفصل الاول ", reply_markup=markup)
 elif call.data == 'تقرير كهرو':
  markup = types.InlineKeyboardMarkup(row_width=1)
  btn1 = types.InlineKeyboardButton('تحقيق قانون اوم في دوائر التيار المتناوب وايجاد حث ملف وسعة...', callback_data='ت5')
  btn2 = types.InlineKeyboardButton('المحولة', callback_data='ت6')
  btn3 = types.InlineKeyboardButton('قياس الممانعةZلدائرة RLCمتوالية الربط', callback_data='ت7')
  btn4=types.InlineKeyboardButton('ايجاد الرادة الحثية لملف وحثه باستخدام قانون اوم',callback_data='ت8')
  btn5 = types.InlineKeyboardButton('الحث المتبادلM', callback_data='ت9')
  btn6=types.InlineKeyboardButton('تحفيز',callback_data='تحفيز')
  btn7=types.InlineKeyboardButton(text='عودة🔙',callback_data='back')
  markup.add(btn1, btn2, btn3,btn4,btn5,btn6,btn7)
  bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="اليك ملازم المختبرات و تقارير المرحلة الثانية ", reply_markup=markup)
 elif call.data == 'ملزمة كهربائية عملي':
  markup = types.InlineKeyboardMarkup(row_width=1)
  btn1 = types.InlineKeyboardButton('مختبر كهربائية فصل اول', callback_data='مختبر كهربائية فصل اول')
  btn2 = types.InlineKeyboardButton('مختبر كهربائية فصل ثاني', callback_data='مختبر كهربائية فصل ثاني')
  btn3 = types.InlineKeyboardButton('تحفيز', callback_data='تحفيز')
  btn4=types.InlineKeyboardButton(text='عودة🔙',callback_data='back')
  markup.add(btn1, btn2, btn3,btn4)
  bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='اختار ملزمة الفصل الاول او الثاني حسب فصلك', reply_markup=markup)
 elif call.data == 'ملزمة بصريات':
  markup = types.InlineKeyboardMarkup(row_width=1)
  btn1 = types.InlineKeyboardButton('مختبر بصريات فصل اول', callback_data='مختبر بصريات فصل اول')
  btn2 = types.InlineKeyboardButton('مختبر بصريات فصل ثاني', callback_data='مختبر بصريات فصل ثاني')
  btn3 = types.InlineKeyboardButton('تحفيز', callback_data='تحفيز')
  btn4=types.InlineKeyboardButton(text='عودة🔙',callback_data='back')
  markup.add(btn1, btn2, btn3,btn4)
  bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='اختار ملزمة الفصل الاول او الثاني حسب فصلك', reply_markup=markup)
 elif call.data == 'ملزمة برمجة':
  markup = types.InlineKeyboardMarkup(row_width=1)
  btn1 = types.InlineKeyboardButton('مختبر برمجة فصل اول', callback_data='مختبر برمجة فصل اول')
  btn2 = types.InlineKeyboardButton('مختبر برمجة فصل ثاني', callback_data='مختبر برمجة فصل ثاني')
  btn3 = types.InlineKeyboardButton('تحفيز', callback_data='تحفيز')
  btn4=types.InlineKeyboardButton(text='عودة🔙',callback_data='back')
  markup.add(btn1, btn2, btn3,btn4)
  bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='اختار ملزمة الفصل الاول او الثاني حسب فصلك', reply_markup=markup)
 elif call.data=='مختبر برمجة فصل اول':
   markup = types.InlineKeyboardMarkup(row_width=1)
   btn1 = types.InlineKeyboardButton('ملزمة باور بوينت', callback_data='ملزمة باور بوينت')
   btn2 = types.InlineKeyboardButton('ملزمة الاكسل', callback_data='ملزمة الاكسل')
   btn3 = types.InlineKeyboardButton('تحفيز', callback_data='تحفيز')
   btn4=types.InlineKeyboardButton(text='عودة🔙',callback_data='back')
   markup.add(btn1, btn2, btn3,btn4)
   bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='اختار ملزمة الي تحتاجه', reply_markup=markup)
 elif call.data=='شرح التجارب':
   markup = types.InlineKeyboardMarkup(row_width=1)
   btn1 = types.InlineKeyboardButton('شرح تجارب الكهربائية', callback_data='شرح تجارب الكهربائية')
   btn2 = types.InlineKeyboardButton('شرح تجارب البصريات', callback_data='شرح تجارب البصريات')
   btn3 = types.InlineKeyboardButton('شرح تجارب البرمجه', callback_data='شرح البرمجه')
   btn4=types.InlineKeyboardButton('تحفيز',callback_data='تحفيز')
   btn5=types.InlineKeyboardButton(text='عودة🔙',callback_data='back')
   markup.add(btn1, btn2, btn3,btn4,btn5)
   bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='سيتم اضافة الشروحات قريبا عند توفر جميع الشروحات', reply_markup=markup) 	
 elif call.data == 'تحفيز':
        responses = ['صبراً سنُزهِر وسيعرفونَ مَن نحن .❗🤍', 'تعويضات الله مُذهلة تستحقُ الإنتظار🤍.......', 'الوصول إلى القمة امر سهل الصعوبة في الحفاظ عليه','"ان هذا الوقت سوف يمر، وان مرارة المذاکرة وتعبها، سوف يزول سريعًا "🗒🥛','"ڪَونوا على يقينٍ ڪل الصعاب ستمر بالنهاية"🤍✨',' وَتظل تسعَى جاهَدًا في همةٍ والله يُعطي من يشاء إذا شڪر ❤️.','- أحلامُك ليس لها أقدام لڪي تأتي إليك إسعى أنت إليها وبادِر واجتَهِد لنَيلها بِڪل جِد فإن لم تبدأ اليوم لن تبدأ أبدًا 🩺🤍.','ڪل الصعاب اللّٰه هينةٌطمئن فــــــــــــؤادكَ لا حزن ولا قلقُ 🦋.','𝟏𝟏:𝟏𝟏 ربُك عظيم سيُعطيك ماتتّمنى فصبرًا 💜✨','قد يتجاهلك العالم وتساندك آية: "لا تَحْزَنْ إِنَّ اللَّهَ مَعَنَا💜"','إن خير الله قادم فلا يُحزنك مُر الحياة💜','- نحن من طين ، يوجعنا الأذى ، يجرحنا صغير الشوك ، يجبرنا لطف الله','"ولعلها مسألة وقت وإنما هي عند الله قد قُضيت ."💜']  # قم بتحديد الردود العشوائية هنا
        ran = random.choice(responses)
        bot.send_message(call.message.chat.id, ran)
        bot.answer_callback_query(call.id, ran)
 elif call.data == 'مختبر برمجة فصل ثاني':
   bot.send_document(call.message.chat.id, document='https://t.me/bnosi3/869')
 elif call.data == 'ملزمة الاكسل':
   bot.send_document(call.message.chat.id, document='https://t.me/tkarer46/4?single')
 elif call.data == 'ملزمة باور بوينت':
   bot.send_document(call.message.chat.id, document='https://t.me/tkarer46/5?single')
 elif call.data == 'مختبر كهربائية فصل اول':
   bot.send_document(call.message.chat.id, document='https://t.me/tkarer46/2')
 elif call.data == 'مختبر بصريات فصل اول':
   bot.send_document(call.message.chat.id, document='https://t.me/tkarer46/8')
 elif call.data == 'ملازم المواد':
  markup = types.InlineKeyboardMarkup()
  btn1=types.InlineKeyboardButton('البصريات',callback_data='البصريات')
  btn2 = types.InlineKeyboardButton('البرمجة', callback_data='البرمجة')
  btn3 = types.InlineKeyboardButton('اجتثاث البعث', callback_data='اجتثاث البعث')
  btn4 = types.InlineKeyboardButton('منهج البحث', callback_data='منهج البحث')
  btn5 = types.InlineKeyboardButton('الانكليزي', callback_data='الانكليزي')
  btn6 = types.InlineKeyboardButton('علم النفس', callback_data='علم النفس')
  btn7 = types.InlineKeyboardButton('الرياضيات', callback_data='الرياضيات')
  btn8 = types.InlineKeyboardButton('الفلك', callback_data='الفلك')
  btn9 = types.InlineKeyboardButton('الادارة', callback_data='الادارة')
  btn10 = types.InlineKeyboardButton('الصوت', callback_data='الصوت')
  btn12 = types.InlineKeyboardButton('تحفيز', callback_data='تحفيز')
  btn11= types.InlineKeyboardButton('الكهربائية', callback_data='الكهربائية')
  btn13=types.InlineKeyboardButton(text='عودة🔙',callback_data='back')
  markup.add(btn1,btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10,btn11,btn12,btn13)
  bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='اختار ملزمة المادة التي تحتاجها ملاحضة الملازم كامله', reply_markup=markup)
 elif call.data == 'ت1':
  bot.send_document(call.message.chat.id, document='https://t.me/tkarer46/154?single')
 elif call.data == 'ت2':
  bot.send_document(call.message.chat.id, document='https://t.me/tkarer46/155?single')
 elif call.data == 'ت3':
  bot.send_document(call.message.chat.id, document='https://t.me/abrahimph/93?single')
 elif call.data == 'ت4':
  bot.send_document(call.message.chat.id, document='https://t.me/tkarer46/156?single')
 elif call.data == 'ت5':
  bot.send_document(call.message.chat.id, document='https://t.me/tkarer46/157?single')
 elif call.data == 'ت6':
  bot.send_document(call.message.chat.id, document='https://t.me/tkarer46/73')
 elif call.data == 'ت7':
  bot.send_document(call.message.chat.id, document='https://t.me/tkarer46/159?single')
 elif call.data == 'ت8':
  bot.send_document(call.message.chat.id, document='https://t.me/tkarer46/75')
 elif call.data == 'ت9':
  bot.send_document(call.message.chat.id, document='https://t.me/tkarer46/76')
 elif call.data == 'البصريات':
   bot.send_document(call.message.chat.id, document='https://t.me/kkjmo9/799?single')
 elif call.data =='منهج البحث':
  bot.send_document(call.message.chat.id, document='https://t.me/kkjmo9/477')
 elif call.data =='البرمجة':
   bot.send_message(call.message.chat.id, text='روح لقسم المختبرات واختار مختبر برمجة وحدد الملزمة الي محتاجها')	
 elif call.data =='الادارة':
   bot.send_document(call.message.chat.id, document='https://t.me/kkjmo9/549')
 elif call.data =='الفلك':
   bot.send_document(call.message.chat.id, document='https://t.me/kkjmo9/448?single')
 elif call.data =='علم النفس':
   bot.send_document(call.message.chat.id, document='https://t.me/kkjmo9/472')
 elif call.data =='الصوت':
   bot.send_document(call.message.chat.id, document='https://t.me/kkjmo9/545')
 elif call.data =='الكهربائية':
   bot.send_document(call.message.chat.id, document='https://t.me/utv2023/290')
   bot.send_message(call.message.chat.id,text='هذا فصل اول وفصل ثاني كهربائية كتابة الاء قاسم ')
 elif call.data=='الرياضيات':
     markup = types.InlineKeyboardMarkup()
     btn1=types.InlineKeyboardButton('الفصل الاول',callback_data='الفصل الاول')
     btn2 = types.InlineKeyboardButton('الفصل الثاني', callback_data='الفصل الثاني')
     btn3 = types.InlineKeyboardButton('الفصل الثالث', callback_data='الفصل الثالث')
     btn4 = types.InlineKeyboardButton('الفصل الرابع', callback_data='الفصل الرابع')
     btn5 = types.InlineKeyboardButton('الفصل الخامس', callback_data='الفصل الخامس')
     btn6=types.InlineKeyboardButton('تحفيز',callback_data='تحفيز')
     btn7=types.InlineKeyboardButton(text='عودة🔙',callback_data='back')
     markup.add(btn1,btn2, btn3, btn4, btn5, btn6,btn7) 
     bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='اختار الفصل الذي تريده من فصول الرياضيات', reply_markup=markup)
 elif call.data =='الفصل الاول':
   bot.send_document(call.message.chat.id, document='')
 elif call.data=='الانكليزي':
     markup = types.InlineKeyboardMarkup()
     btn1=types.InlineKeyboardButton('الوحدة الاولى',callback_data='الوحدة الاولى')
     btn2 = types.InlineKeyboardButton('الوحدة الثانية', callback_data='الوحدة الثانية')
     btn3 = types.InlineKeyboardButton('الوحدة الثالثة', callback_data='الوحدة الثالثة')
     btn4 = types.InlineKeyboardButton('الوحدة الرابعة', callback_data='الوحدة الرابعة')
     btn5 = types.InlineKeyboardButton('الوحدة الخامسة', callback_data='الوحدة الخامسة')
     btn6=types.InlineKeyboardButton('تحفيز',callback_data='تحفيز')
     btn7=types.InlineKeyboardButton(text='عودة🔙',callback_data='back')
     markup.add(btn1,btn2, btn3, btn4, btn5, btn6,btn7) 
     bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='اختار الوحدة الذي تريده من وحدات الانكليزي', reply_markup=markup)
 elif call.data =='الوحدة الاولى':
   bot.send_document(call.message.chat.id, document='https://t.me/kkjmo9/450?single')
 elif call.data =='الوحدة الثانية':
  bot.send_document(call.message.chat.id, document='https://t.me/kkjmo9/451?single')
 elif call.data =='الوحدة الثالثة':
   bot.send_document(call.message.chat.id, document='https://t.me/kkjmo9/452?single')
 elif call.data =='الوحدة الخامسة':
   bot.send_document(call.message.chat.id, document='https://t.me/kkjmo9/453?single')
   bot.send_message(call.message.chat.id,text='الجزء الاول')
  #elif call.data =='الوحدة الثالثة':
   bot.send_document(call.message.chat.id, document='https://t.me/kkjmo9/454?single')
   bot.send_message(call.message.chat.id,text='الجزء الثاني')
 elif call.data =='الوحدة الرابعة':
   bot.send_message(call.message.chat.id, text='ماكو وحدة رابعه شرفتني 😂')
 elif call.data=='شرح تجارب الكهربائية':
     markup = types.InlineKeyboardMarkup()
     btn1=types.InlineKeyboardButton('التجربة الاولى',callback_data='التجربة الاولى')
     btn2 = types.InlineKeyboardButton('التجربة الثانية', callback_data='التجربة الثانية')
     btn3 = types.InlineKeyboardButton('التجربة الثالثة', callback_data='التجربة الثالثة')
     btn4 = types.InlineKeyboardButton('التجربة الرابعة', callback_data='التجربة الرابعة')
     btn5 = types.InlineKeyboardButton('التجربة الخامسة', callback_data='الفصل الخامسة')
     btn6=types.InlineKeyboardButton('تحفيز',callback_data='تحفيز')
     btn7=types.InlineKeyboardButton(text='عودة🔙',callback_data='back')
     markup.add(btn1,btn2, btn3, btn4, btn5, btn6,btn7) 
     bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='اختار التجربة الي تريده من  شروحات تجارب الكهربائية سيتم اضافة الشروحات عند توفرها', reply_markup=markup)
 elif call.data=='شرح تجارب البصريات':
     markup = types.InlineKeyboardMarkup()
     btn1=types.InlineKeyboardButton('التجربة الاولى',callback_data='التجربة الاولى')
     btn2 = types.InlineKeyboardButton('التجربة الثانية', callback_data='التجربة الثانية')
     btn3 = types.InlineKeyboardButton('التجربة الثالثة', callback_data='التجربة الثالثة')
     btn4 = types.InlineKeyboardButton('التجربة الرابعة', callback_data='التجربة الرابعة')
     btn5 = types.InlineKeyboardButton('التجربة الخامسة', callback_data='الفصل الخامسة')
     btn6=types.InlineKeyboardButton('تحفيز',callback_data='تحفيز')
     btn7=types.InlineKeyboardButton(text='عودة🔙',callback_data='back')
     markup.add(btn1,btn2, btn3, btn4, btn5, btn6,btn7) 
     bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='اختار التجربة الي تريده من  شروحات تجارب البصريات سيتم اضافة الشروحات عند توفرها', reply_markup=markup)
 elif call.data == 'اشياء تفيدك':
   markup = types.InlineKeyboardMarkup()
   btn1=types.InlineKeyboardButton('قوانين',callback_data='قوانين')
   btn2 = types.InlineKeyboardButton('نصيحة', callback_data='نصيحة')
   btn3 = types.InlineKeyboardButton('اسئلة فاينل', callback_data='اسئلة فاينل')
   btn4 = types.InlineKeyboardButton('مفردات تفيدك', callback_data='مفردات تفيدك')
   btn5 = types.InlineKeyboardButton('اسئلة شهرية', callback_data='اسئلة شهرية')
   btn6=types.InlineKeyboardButton('تحفيز',callback_data='تحفيز')
   btn7=types.InlineKeyboardButton('امتحان',callback_data='امتحان')
   btn8=types.InlineKeyboardButton(text='عودة🔙',callback_data='back')
   markup.add(btn1,btn2, btn3, btn4, btn5, btn6,btn7,btn8) 
   bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='هنا راح تاخذ شيء يفيدك بهالمرحلة وبحياتك اليومية', reply_markup=markup)
 elif call.data =='قوانين':
   bot.send_message(call.message.chat.id, text='قريبا تتم اضافته')
 elif call.data =='اسئلة فاينل':
   markup = types.InlineKeyboardMarkup()
   btn1=types.InlineKeyboardButton('البصريات',callback_data='بصريات')
   btn2 = types.InlineKeyboardButton('البرمجة', callback_data='برمجة')
   btn3 = types.InlineKeyboardButton('اجتثاث البعث', callback_data='اجتثاث بعث')
   btn4 = types.InlineKeyboardButton('منهج البحث', callback_data='منهج بحث')
   btn5 = types.InlineKeyboardButton('الانكليزي', callback_data='انكليزي')
   btn6 = types.InlineKeyboardButton('علم النفس', callback_data='علم نفس')
   btn7 = types.InlineKeyboardButton('الرياضيات', callback_data='رياضيات')
   btn8 = types.InlineKeyboardButton('الفلك', callback_data='فلك')
   btn9 = types.InlineKeyboardButton('الادارة', callback_data='ادارة')
   btn10 = types.InlineKeyboardButton('الصوت', callback_data='صوت')
   btn12 = types.InlineKeyboardButton('تحفيز', callback_data='تحفيز')
   btn11= types.InlineKeyboardButton('الكهربائية', callback_data='كهربائية')
   btn13=types.InlineKeyboardButton(text='عودة🔙',callback_data='back')
   markup.add(btn1,btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10,btn11,btn12,btn13)
   bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='اختار المادة التي تريد اسئلة الفاينل لها قريبا تتم اضافة جميع الاسئلة', reply_markup=markup)
 elif call.data =='اسئلة شهرية':
   markup = types.InlineKeyboardMarkup()
   btn1=types.InlineKeyboardButton('البصريات',callback_data='بصريات1')
   btn2 = types.InlineKeyboardButton('البرمجة', callback_data='برمجة1')
   btn3 = types.InlineKeyboardButton('اجتثاث البعث', callback_data='اجتثاث بعث1')
   btn4 = types.InlineKeyboardButton('منهج البحث', callback_data='منهج بحث1')
   btn5 = types.InlineKeyboardButton('الانكليزي', callback_data='انكليزي1')
   btn6 = types.InlineKeyboardButton('علم النفس', callback_data='علم نفس1')
   btn7 = types.InlineKeyboardButton('الرياضيات', callback_data='رياضيات1')
   btn8 = types.InlineKeyboardButton('الفلك', callback_data='فلك1')
   btn9 = types.InlineKeyboardButton('الادارة', callback_data='ادارة1')
   btn10 = types.InlineKeyboardButton('الصوت', callback_data='صوت1')
   btn12 = types.InlineKeyboardButton('تحفيز', callback_data='تحفيز')
   btn11= types.InlineKeyboardButton('الكهربائية', callback_data='كهربائية')
   btn13=types.InlineKeyboardButton(text='عودة🔙',callback_data='back')
   markup.add(btn1,btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10,btn11,btn12,btn13)
   bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='اختار المادة التي تريد اسئلة الفاينل لها قريبا تتم اضافة جميع الاسئلة', reply_markup=markup)
 elif call.data =='بصريات1':
   bot.send_photo(call.message.chat.id, photo='https://t.me/physics980/232')
   bot.send_photo(call.message.chat.id,photo='https://t.me/bnosi3/245 ')
   bot.send_photo(call.message.chat.id, photo='https://t.me/bnosi3/244')
   bot.send_message(call.message.chat.id,text='اسئلة شهرية بصريات')
 elif call.data =='صوت1':
   bot.send_photo(call.message.chat.id, photo='https://t.me/abrahimph/159')
   bot.send_photo(call.message.chat.id,photo='https://t.me/abrahimph/156?single')
   bot.send_photo(call.message.chat.id, photo='https://t.me/abrahimph/154?single')
   bot.send_message(call.message.chat.id,text='اسئلة شهرية صوت')
 elif call.data =='رياضيات1':
   bot.send_photo(call.message.chat.id, photo='https://t.me/bnosi3/190')
   bot.send_photo(call.message.chat.id,photo='https://t.me/bnosi3/250')
   bot.send_photo(call.message.chat.id, photo='https://t.me/bnosi3/519')
   bot.send_photo(call.message.chat.id, photo='https://t.me/bnosi3/568')
   bot.send_photo(call.message.chat.id, photo='https://t.me/bnosi3/1186')
   bot.send_photo(call.message.chat.id, photo='https://t.me/bnosi3/1328')
   bot.send_photo(call.message.chat.id, photo='https://t.me/bnosi3/1388')
   bot.send_message(call.message.chat.id,text='اسئلة شهرية رياضييات')
 elif call.data =='فلك1':
   bot.send_document(call.message.chat.id, document='https://t.me/abrahimph/160')
   bot.send_message(call.message.chat.id,text='ملف اسئلة فلك')
 elif call.data =='ادارة1':
   bot.send_photo(call.message.chat.id, photo='https://t.me/bnosi3/307')
   bot.send_photo(call.message.chat.id, photo='https://t.me/bnosi3/317')
   bot.send_message(call.message.chat.id,text='اسئلة ادارة شهرية')
 elif call.data=='امتحان':
 	markup = types.InlineKeyboardMarkup()
 	btn1=types.InlineKeyboardButton('البصريات',callback_data='بص1')
 	btn2 = types.InlineKeyboardButton('البرمجة', callback_data='بر1')
 	btn3 = types.InlineKeyboardButton('اجتثاث البعث', callback_data='اج1')
 	btn4 = types.InlineKeyboardButton('منهج البحث', callback_data='من1')
 	btn5 = types.InlineKeyboardButton('الانكليزي', callback_data='ان1')
 	btn6 = types.InlineKeyboardButton('علم النفس', callback_data='عل1')
 	btn7 = types.InlineKeyboardButton('الرياضيات', callback_data='ري1')
 	btn8 = types.InlineKeyboardButton('الفلك', callback_data='فل1')
 	btn9 = types.InlineKeyboardButton('الادارة', callback_data='اد1')
 	btn10 = types.InlineKeyboardButton('الصوت', callback_data='صو1')
 	btn12 = types.InlineKeyboardButton('تحفيز', callback_data='تحفيز')
 	btn11= types.InlineKeyboardButton('الكهربائية', callback_data='كهرب1')
 	btn13=types.InlineKeyboardButton(text='عودة🔙',callback_data='back')
 	markup.add(btn1,btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10,btn11,btn12,btn13)
 	bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='اختار المادة الي تريد تمتحن بيها ', reply_markup=markup)
 elif call.data=='بص1':
   markup = types.InlineKeyboardMarkup(row_width=6)
   buttons = [types.InlineKeyboardButton(f'س{i}', callback_data=str(i)) for i in range(1, 100)]
   back_button = types.InlineKeyboardButton('عودة🔙', callback_data='back')
   buttons.append(back_button)
   markup.add(*buttons,back_button)
   bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='قم بالضغط على اي سؤال ليتم اختبارك ', reply_markup=markup)
 elif call.data =='1':
 	bot.send_message(call.message.chat.id,text='اذكر نص قانون سنيل')
 	sleep(1*60)
 	bot.send_message(call.message.chat.id,text='بعد الانتضار لمدة دقيقة اليك الاجابة')
 	sleep(2)
 	bot.send_message(call.message.chat.id,text='''عندما ينتقل الضوء من وسط إلى وسط آخر ذات كثافة مختلفة، يتغير زاوية انحراف الضوء الناتجة عن هذا التغيير في الوسط بنسبة معينة. ويمكن حساب هذه الزاوية باستخدام قانون سنيل ويمثلها العلاقة الرياضية التالية:

n₁sinθ₁ = n₂sinθ₂

حيث:
- n₁ و n₂ هما معاملات الانكسار للوسطين الأول والثاني على التوالي.
- θ₁ و θ₂ هما الزوايا بالنسبة للسطح بين الوسطين.
- sin تمثل دالة الجيب الزايدة عند زاوية محددة.''')
 elif call.data =='2':
 	bot.send_message(call.message.chat.id,text='''The wheel has 360 teeth, and so it must have 360 openings. Therefore, 

because the light passes through opening A but is blocked by the tooth immediately 

adjacent to A, the wheel must rotate through an angular displacement of (1/720) rev in 

the time interval during which the light pulse makes its round trip. From the definition 

of angular speed, that time interval is
''')
 	sleep(5)
 	bot.send_message(call.message.chat.id,text='بعد الانتضار لمدة 5 دقائق اليك الاجابة')
 	sleep(2)
 	bot.send_photo(call.message.chat.id,photo='https://t.me/abrahimph/164')
 elif call.data=='صو1':
 	markup = types.InlineKeyboardMarkup()
 	btn1=types.InlineKeyboardButton('فصل  1' ,callback_data='فصل ص1')
 	btn2= types.InlineKeyboardButton('فصل  2',callback_data='فصل ص 2')
 	btn3=types.InlineKeyboardButton('فصل 3',callback_data='فصل ص 3')
 	btn4=types.InlineKeyboardButton('عودة🔙',callback_data='back')
 	markup.add(btn1,btn2,btn3,btn4)
 	bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='اختار الفصل الذي ترغب الامتحان به', reply_markup=markup)
 elif call.data=='فصل ص 3':
 	markup = types.InlineKeyboardMarkup(row_width=2)
 	btn1=types.InlineKeyboardButton('نموذج PDF' ,callback_data='نموذج صpdf')
 	btn2= types.InlineKeyboardButton('سؤال &جواب',callback_data='فصل ص ا')
 	btn3=types.InlineKeyboardButton('اسئلة فكرية',callback_data='فكري ص')
 	btn4=types.InlineKeyboardButton('عودة🔙',callback_data='back')
 	markup.add(btn1,btn2,btn3,btn4)
 	bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='اختار الطريقة الي تعجبك', reply_markup=markup)
 elif call.data=='فكري ص':
 	markup = types.InlineKeyboardMarkup(row_width=3)
 	buttons = [types.InlineKeyboardButton(f'س فكري{i}', callback_data=str(i)) for i in range(200, 203)]
 	back_button = types.InlineKeyboardButton('عودة🔙', callback_data='back')
 	buttons.append(back_button)
 	markup.add(*buttons)
 	bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='قم بالضغط على اي سؤال ليتم اختبارك \nهذه الاسئلة خارجية ولكنها اتت في الامتحانات الشهرية لذلك قمنا بوضعها في خانه لوحدها', reply_markup=markup)
 elif call.data=='نموذج صpdf':
 	bot.send_message(call.message.chat.id,text='قريبا تتم اضافة الاسئلة والاجوبة على شكل PDF')
 elif call.data=='فصل ص ا':
   markup = types.InlineKeyboardMarkup(row_width=3)
   buttons = [types.InlineKeyboardButton(f'س{i}', callback_data=str(i)) for i in range(173, 200)]
   back_button = types.InlineKeyboardButton('عودة🔙', callback_data='back')
   buttons.append(back_button)
   markup.add(*buttons)
   bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='قم بالضغط على اي سؤال ليتم اختبارك ', reply_markup=markup)
 elif call.data =='173':
 	a='🟠 جواب سـ173 :'
 	bot.send_message(call.message.chat.id,text='''
 	سـ 173:
🟠 كيف يمكن التعبير عن تراكب حركتين توافقيتين لهما نفس التردد والطور في بعد واحد
 	''')
 	bot.send_photo(call.message.chat.id,photo='https://t.me/abrahimph/200',caption=a)
 elif call.data =='174':
 	a='🟠 جواب سـ174 :'
 	bot.send_message(call.message.chat.id,text='''
 	سـ 174
🟠 كيف يمكن التعبير عن تراكب حركتين توافقيتين لهما نفس التردد وبينهما فرق الطور (π)في بعد واحد
 	''')
 	bot.send_photo(call.message.chat.id,photo='https://t.me/abrahimph/201',caption=a)
 elif call.data =='175':
 	bot.send_message(call.message.chat.id,text='''
 	سـ175 :
ماهو مبدأ التراكب ؟
أو 
 على ماذا ينص مبدأ التراكب ؟
 	''')
 	#sleep(1*60)
 	#bot.send_message(call.message.chat.id,text='بعد الانتضار لمدة دقيقة اليك الاجابة')
 	#sleep(2)
 	bot.send_message(call.message.chat.id,text='''
 	جواب سـ175 :

🔸 مبدأ التراكب :
ينص هذا المبدأ على انه يمكن لحركتين اهتزازيتين او موجتين او اكثر ان تحدثا في نفس النقطة دون ان تاثر احداهما على الاخرى , وتكون الازاحة الانية في تلك النقطة عبارة عن المجموع الجبري للازاحات الانية للموجات المتراكبة ، وينطبق هذا المبدأ على الحركات التوافقية البسيطة .
 	''')
 elif call.data =='176':
 	bot.send_message(call.message.chat.id,text='سـ176\nاثبت ان حاصل تراكب اي حركتين توافقيتين بسيطتين .هو حركة توافقية بسيطة')
 	#sleep(5*60)
 	#bot.send_message(call.message.chat.id,text='بعد الانتضار لمدة 5دقيقة اليك الاجابة')
 	#sleep(2)
 	bot.send_photo(call.message.chat.id,photo='https://t.me/abrahimph/166')
 elif call.data =='177':
 	a='جواب سـ177'
 	bot.send_message(call.message.chat.id,text='''
 	سـ177 :
🔸 اثبت ان حاصل تراكب اي حركتين توافقيتين بسيطتين في بعد واحد ولهماء نفس التردد؟''')
 	bot.send_photo(call.message.chat.id,photo='https://t.me/abrahimph/174',caption=a)
 elif call.data =='178':
 	bot.send_message(call.message.chat.id,text='''
 	سـ178 :
🔸 ما المقصود بالـ( ضربات )؟''')
 	bot.send_message(call.message.chat.id,text='''
 	جواب سـ178 :

🔸 الضربات :
وهي نمط خاص من الحركة الدورية تحدث عندما يتاثر جسم آنياً بحركتين توافقيتين بسيطتين الفرق بين تردديهما قليل عندها تكون سعة الحركة الاهتزازية الناتجة للجسم تتناوب بين نهايتين عظمى وصغرى مع مرور الزمن.
 	''') 
 elif call.data =='179':
 	a='''سـ179 : 
جواب ( أولاً ).'''
 	b='''سـ179 :
جواب ( ثانياً )'''
 	bot.send_message(call.message.chat.id,text='''
 	سـ179 :

🟡 تراكب حركتين توافقيتين بسيطين في بعد واحد (ومختلفتين في التردد) (الضربات)
🔺 تنقسم الى :

أولاً : حساب الفترة الزمنية بين (اكبر)  سعتين متتاليتين في حالة الضربات.

ثانياً : حساب الفترة الزمنية بين(اصغر) سعتين متتاليتين في حالة الضربات.
 	''')
 	bot.send_photo(call.message.chat.id,photo='https://t.me/abrahimph/175',caption=a)
 	bot.send_photo(call.message.chat.id,photo='https://t.me/abrahimph/176',caption=b)
 elif call.data =='180':
 	a='''   سـ180 :
حل المثال .'''
 	bot.send_message(call.message.chat.id,text='''
 سـ180 :
🟣 مثال صفحة (10)
في تجربة على شكل ليساجو استعملت شوكتان رنين ، تردد الاولى(250Hz) ووجد ان شكل ليساجو الدائري يكمل بعد مرور (5s) كيف يمكن ايجاد شوكت التردد الثانية ؟
 	''')
 	bot.send_photo(call.message.chat.id,photo='https://t.me/abrahimph/177',caption=a)
 elif call.data =='181':
 	a='''سـ181 :
حل المثال .'''
 	bot.send_message(call.message.chat.id,text='''
 	سـ181 :
🟣 مثال صفحة (10)
احسب سرعة الصوت في غاز تولد فيه موجتان أطوالهما (100cm) و (101cm) ، 18 ضربة في 6 ثواني .
 	''')
 	bot.send_photo(call.message.chat.id,photo='https://t.me/abrahimph/179',caption=a)
 elif call.data =='182':
 	bot.send_message(call.message.chat.id,text='''سـ182 :
🔵 عرف شكل ليساجو ؟
 	''')
 	bot.send_message(call.message.chat.id,text='''جواب سـ182 :

🔵 شكل ليساجو :
هو المسار المنحني الذي يسلكه الجسيم الواقع تحت تأثير حركتين توافقيتين بسيطتين متعامدتين ويعتمد هذا الشكل على سعة وتردد كل من الحركتين وفرق الطور بينهما واذا كانت النسبة بين ترددي الحركتين مساوياََ لعدد صحيح وفرق الطور بينهما زاوية معينة فان شكل المسار يكون مغلقاََ .
 	''')
 elif call.data =='183':
 	bot.send_message(call.message.chat.id,text='''
 	سـ183 :
🟢 هناك أكثر من من طريقة لدراسة شكل المسار الذي يسلكه ذلك الجسيم ومن أهم تلك الطرق هي......... و...........
 	''')
 	bot.send_message(call.message.chat.id,text='''
 	جواب سـ183 :
🟢 الطريقة التحليلية و طريقة المحور الدوار.
 	''')
 elif call.data =='184':
 	a='🟠 جواب سـ184 :'
 	bot.send_message(call.message.chat.id,text='''
 	سـ184 :
🟤اشتق معادلة المسار المتحرك بتاثير حركتين توافقيتين بسيطتين متعامدتين لهما نفس التردد ومختلفتين بالسعة والطور ؟
 	''')
 	bot.send_photo(call.message.chat.id,photo='https://t.me/abrahimph/180',caption=a)
 elif call.data =='190':
 	bot.send_message(call.message.chat.id,text='''
 	سـ190 :
🟠لرسم المسار (أشكال ليساجو) الذي يسلكه الجسيم الواقع تحت تأثير حركتين هناك عدة خطوات عددها ؟
 	''')
 	a='''🟠 جواب سـ190 :'''
 	bot.send_photo(call.message.chat.id,photo='https://t.me/abrahimph/181',caption=a)
 elif call.data =='191':
 	bot.send_message(call.message.chat.id,text='''
 	سـ191:
 		🔷 ارسم مسار الجسيم بتأثير حركتين توافقيتين متعامدتين متساويتين بالتردد والطور (ثيتا=0 ) بطريقة المتجه الدوار .
 	''')
 	a='''جواب سـ191'''
 	bot.send_photo(call.message.chat.id,photo='https://t.me/abrahimph/182',caption=a)
 elif call.data =='192':
 	bot.send_message(call.message.chat.id,text='''
 	سـ192:
 		🔷 ارسم مسار الجسيم بتأثير حركتين توافقيتين متعامدتين متساويتين بالتردد وبينهما فرق طور (ثيتا= π/4) بطريقة المتجه الدوار .
 	''')
 	a='''جواب سـ192'''
 	bot.send_photo(call.message.chat.id,photo='https://t.me/abrahimph/183',caption=a)
 elif call.data =='193':
 	bot.send_message(call.message.chat.id,text='''
 	سـ193:
 	🔷 ارسم مسار الجسيم بتأثير حركتين توافقيتين متعامدتين متساويتين بالتردد وبينهما فرق طور (ثيتا=π/2) بطريقة المتجه الدوار .
 	''')
 	a='🟠 جواب سـ193 :'
 	bot.send_photo(call.message.chat.id,photo='https://t.me/abrahimph/190',caption=a)
 elif call.data =='194':
 	bot.send_message(call.message.chat.id,text='''
 	سـ194:
 		🔷 ارسم مسار الجسيم بتأثير حركتين توافقيتين متعامدتين متساويتين بالتردد وبينهما فرق طور (ثيتا= 3π/4) بطريقة المتجه الدوار .
 	''')
 	a='🟠 جواب سـ194 :'
 	bot.send_photo(call.message.chat.id,photo='https://t.me/abrahimph/191',caption=a)
 elif call.data =='185':
 	a='🟠 جواب سـ185 :'
 	bot.send_message(call.message.chat.id,text='''سـ185 :
 🔹 ما هو شكل المسار (اشكال ليساجو) الواقع بتاثير حركتين توافقيتين متعامدتين متساويتين بالتردد وفرق الطور بينهما يساوي (ثيتا = 0)؟''')
 #	sleep(2)
 	#bot.send_message(call.message.chat.id,text='بعد الانتضار لمدة 5دقيقة اليك الاجابة')
 	#sleep(2)
 	bot.send_photo(call.message.chat.id,photo='https://t.me/abrahimph/169',caption=a)
 elif call.data =='186':
 	a='🟠 جواب سـ186 :'
 	bot.send_message(call.message.chat.id,text='''
 	سـ186:
🔹ما هو شكل المسار (اشكال ليساجو) الواقع بتاثير حركتين توافقيتين متعامدتين متساويتين بالتردد وفرق الطور بينهما يساوي (ثيتا= π/4)؟
 	''')
 	#sleep(2)
 #	bot.send_message(call.message.chat.id,text='بعد الانتضار لمدة 5دقيقة اليك الاجابة')
 	#sleep(2)
 	bot.send_photo(call.message.chat.id,photo='https://t.me/abrahimph/170',caption=a)
 elif call.data =='187':
 	a='🟠 جواب سـ187:'
 	bot.send_message(call.message.chat.id,text='''
 	سـ187 :
🔹 ما هو شكل المسار (اشكال ليساجو) الواقع بتاثير حركتين توافقيتين متعامدتين متساويتين بالتردد وفرق الطور بينهما يساوي (ثيتا=π/2)؟
 	''')
 	bot.send_photo(call.message.chat.id,photo='https://t.me/abrahimph/171',caption=a)
 elif call.data =='188':
 	a='🟠 جواب سـ188 :'
 	bot.send_message(call.message.chat.id,text='''
 	سـ188 :
🔹 ما هو شكل المسار (اشكال ليساجو) الواقع بتاثير حركتين توافقيتين متعامدتين متساويتين بالتردد وفرق الطور بينهما يساوي(ثيتا= 3π/4)؟
 	''')
 	bot.send_photo(call.message.chat.id,photo='https://t.me/abrahimph/172',caption=a)
 elif call.data =='189':
 	a='🟠 جواب سـ189 :'
 	bot.send_message(call.message.chat.id,text='''
 	سـ189 :
🔹 ما هو شكل المسار (اشكال ليساجو) الواقع بتاثير حركتين توافقيتين متعامدتين متساويتين بالتردد وفرق الطور بينهما يساوي (ثيتا=π)؟
 	''')
 	bot.send_photo(call.message.chat.id,photo='https://t.me/abrahimph/173',caption=a)
 elif call.data =='195':
 	a='🟠 جواب سـ195 :'
 	bot.send_message(call.message.chat.id,text='''سـ195:
 	🔷 ارسم مسار الجسيم بتأثير حركتين توافقيتين متعامدتين متساويتين بالتردد وبينهما فرق طور (ثيتا=π) بطريقة المتجه الدوار 
 	''')
 	bot.send_photo(call.message.chat.id,photo='https://t.me/abrahimph/192',caption=a)
 elif call.data =='196':
 	a='🟠 جواب سـ196 :'
 	bot.send_message(call.message.chat.id,text='''
 	سـ196:
 		🔷 ارسم مسار الجسيم بتأثير حركتين توافقيتين متعامدتين متساويتين بالتردد وبينهما فرق طور (ثيتا= 5π/4) بطريقة المتجه الدوار .
 	''')
 	bot.send_photo(call.message.chat.id,photo='https://t.me/abrahimph/193',caption=a)
 elif call.data =='197':
 	a='🟠 جواب سـ197 :'
 	bot.send_message(call.message.chat.id,text='''
 	سـ197 :
🟡 ارسم مسار الجسيم بتأثير حركتين توافقيتين متعامدتين تردد أحدهما ضعف الأخرى وبينهما فرق طور (ثيتا=…..0،2π) بطريقة المتجه الدوار .
 	''')
 	bot.send_photo(call.message.chat.id,photo='https://t.me/abrahimph/194',caption=a)
 elif call.data =='198':
 	a='🟠 جواب سـ198 :'
 	bot.send_message(call.message.chat.id,text='''
 	سـ198 :
🟡 ارسم مسار الجسيم بتأثير حركتين توافقيتين متعامدتين تردد أحدهما ضعف الأخرى وبينهما فرق طور (ثيتا=π/4) بطريقة المتجه الدوار .
 	''')
 	bot.send_photo(call.message.chat.id,photo='https://t.me/abrahimph/195',caption=a)
 elif call.data =='199':
 	a='🟠 جواب سـ199 :'
 	bot.send_message(call.message.chat.id,text='''
 	سـ199 :
🟡 ارسم مسار الجسيم بتأثير حركتين توافقيتين متعامدتين تردد أحدهما ضعف الأخرى وبينهما فرق طور (ثيتا=π/2) بطريقة المتجه الدوار .
 	''')
 	bot.send_photo(call.message.chat.id,photo='https://t.me/abrahimph/196',caption=a)
 elif call.data =='200':
 	a='🟠 جواب سـ200 :'
 	bot.send_message(call.message.chat.id,text='''
 	سـ200:
🟠 جد تردد الحركة المركبة لكل مما ياتي 👇👇
 	''')
 	bot.send_photo(call.message.chat.id,photo='https://t.me/abrahimph/197',caption=a)
 elif call.data =='201':
 	a='🟠 جواب سـ201 :'
 	bot.send_message(call.message.chat.id,text='''
 	سـ201:
🟠 ارسم شكل ليساجو للحركة المركبة الناتجة عن اهتزازين متعامدين يمكن وضعهما في معادلتين
1-X= 10 cos(5πt)
2-Y= 10 cos(10πt+π/3)
 	''')
 	bot.send_photo(call.message.chat.id,photo='https://t.me/abrahimph/198',caption=a)
 elif call.data =='202':
 	a='🟠 جواب سـ202 :'
 	bot.send_message(call.message.chat.id,text='''
 	سـ202:
🟠 ارسم شكل ليساجو الناتج من تركيب الحركتين:
X=cos(2wt)
y=cos(2wt-π/4)
 	''')
 	bot.send_photo(call.message.chat.id,photo='https://t.me/abrahimph/199',caption=a)
 
 elif call.data=='كهرب1':
   markup = types.InlineKeyboardMarkup(row_width=6)
   buttons = [types.InlineKeyboardButton(f'س {i}', callback_data=str(i)) for i in range(201, 300)]
   back_button = types.InlineKeyboardButton('عودة🔙', callback_data='back')
   buttons.append(back_button)
   markup.add(*buttons)
   bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='قم بالضغط على اي سؤال ليتم اختبارك ', reply_markup=markup)
 elif call.data=='بر1':
   markup = types.InlineKeyboardMarkup(row_width=6)
   buttons = [types.InlineKeyboardButton(f'س {i}', callback_data=str(i)) for i in range(300, 350)]
   back_button = types.InlineKeyboardButton('عودة🔙', callback_data='back')
   buttons.append(back_button)
   markup.add(*buttons)
   bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='قم بالضغط على اي سؤال ليتم اختبارك ', reply_markup=markup)
 elif call.data == 'نصيحة':
    res = ['الصمت يعطي حسن الفهم',"ألا إنَّ الله تبارك وتعالى لا يُنْظر إلى صوركم، ولا إلى أموالكم، بل يُنْظر إلى قلوبكم وأعمالكم.","من كفَّ عن الدنيا زينت له الآخرة.","خيار الأصدقاء تزداد نقصًا.", "من سلك طريق الحق أشاكه كلاب الهوى.", "اُقْتُلوا الشَّهوَة بالتَّقوَى؛ فَإِنَّها أدوم مَرضي وأَخَوَفِ الدهورَ.","علامة عقلك أن لا تشبه فيه عجلة بالكركم.","أعمالكم معلَّقة بالنيات.","الناس أعداء ما جهلوا.","قلوب الناس معلقة بألسنتهم.","الزمِ الصدق تستبق جميع عمل."]
    ra = random.choice(res)
    bot.send_message(call.message.chat.id, ra)
 elif call.data == 'مفردات تفيدك':
    ress = [
        "معامل انكسار index",
        "Secondary focal length البعد البؤري الثانوي",
        "Primary focal length البعد البؤري الاولي",
        "convex lens عدسة محدبة",
        "concave lens عدسة مقعرة",
        "radius نصف القطر",
        "equal concave مقعر متساوي",
        "equal convex محدب متساوي",
        "farsightedness بعد النظر",
        "Nearsightedness قصر النظر",
        "astigmatism استكماتزم",
        "retina الشبكية",
        "spherical mirrors المرايا الكروية",
        "object جسم",
        "rays الاشعة",
        "refracted rays اشعة منكسرة",
        "reflected rays اشعة منعكسة",
        "falling rays اشعة ساقطة",
        "refraction انكسار",
        "reflection انعكاس",
        "luminous fringe هدب مضيء",
        "dark fringe هدب مظلم",
        "central fringe هدب مركزي",
        "naughty yung experien تجربة شقي يونغ",
        "Polarization الاستقطاب",
        "Linear polarization الاستقطاب الخطي",
        "Circular polarization الاستقطاب الدائري",
        "Radiation الاشعاع",
        "Snell's law قانون سنيل",
        "Huygens principle مبدأ هيوجنز",
        "image attributes صفات الصورة",
        "image height إرتفاع الصورة",
        "lens capacity or ability قدرة العدسة",
        "surface capacity قدرة السطح"
    ]
    raa = random.choice(ress)
    bot.send_message(call.message.chat.id, raa)
 elif call.data == "back":
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='''🔰السلام عليكم ورحمة الله وبركاته عزيزي الطالب
⭕ اهلا بك في بوت المرحلة الثانية لقسم الفيزياء 
🔰شكر خاص الى مجموعة من طلاب قسم الفيزياء 
⭕هذا البوت من تطوير 
𝑨𝑩𝑩𝑨𝑺 𝑮𝑯𝑨𝒁𝑾𝑨𝑵
لتواصل: @SHAHM4
قناتي: @BGGlG''', reply_markup=start(), parse_mode='Markdown')
def start():
    markup = types.InlineKeyboardMarkup(row_width=2)
    saif1 = types.InlineKeyboardButton('مختبرات', callback_data='مختبرات')
    saif2 = types.InlineKeyboardButton('ملازم المواد', callback_data='ملازم المواد')
    saif3 = types.InlineKeyboardButton('تحفيز', callback_data='تحفيز')
    saif4 = types.InlineKeyboardButton('ملاحظات وامتحانات', callback_data='اشياء تفيدك')
    markup.add(saif1, saif2, saif3, saif4)
    return markup
	

print('shahm')

bot.infinity_polling()
