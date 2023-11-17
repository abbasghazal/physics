import telebot
import random
from telebot import types

bot = telebot.TeleBot('6333831584:AAFc-akfiQZK9yAq5h9dM_GeiEC1rgZlBN0')

@bot.message_handler(commands=['start'])
def start(message):
	markup = types.InlineKeyboardMarkup(row_width=2)
	saif1 = types.InlineKeyboardButton('مختبرات', callback_data='مختبرات')
	saif2 = types.InlineKeyboardButton('ملازم المواد', callback_data='ملازم المواد')
	saif3 = types.InlineKeyboardButton('تحفيز', callback_data='تحفيز')
	saif4 = types.InlineKeyboardButton('اشياء تفيدك', callback_data='اشياء تفيدك')
	markup.add(saif1, saif2, saif3,saif4)
	bot.send_message(message.chat.id, '''🔰السلام عليكم ورحمة الله وبركاته عزيزي الطالب
⭕ اهلا بك في بوت المرحلة الثانية لقسم الفيزياء 
🔰شكر خاص الى مجموعة من طلاب قسم الفيزياء 
⭕هذا البوت من تطوير 
𝑨𝑩𝑩𝑨𝑺 𝑮𝑯𝑨𝒁𝑾𝑨𝑵
لتواصل: @SHAHM4
قناتي: @BGGlG ''', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
 message = call.message
 chat_id = message.chat.id
 if call.data == 'مختبرات':
  markup = types.InlineKeyboardMarkup(row_width=1)
  btn1 = types.InlineKeyboardButton('ملزمة كهربائية عملي', callback_data='ملزمة كهربائية عملي')
  btn2 = types.InlineKeyboardButton('ملزمة بصريات', callback_data='ملزمة بصريات')
  btn3 = types.InlineKeyboardButton('ملزمة برمجة', callback_data='ملزمة برمجة')
  btn4 = types.InlineKeyboardButton('شرح التجارب', callback_data='شرح التجارب')
  btn5=types.InlineKeyboardButton(text='عودة🔙',callback_data='back')
  markup.add(btn1, btn2, btn3,btn4,btn5)
  bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="اليك ملازم مختبرات المرحلة الثانية ", reply_markup=markup)
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
   btn7=types.InlineKeyboardButton(text='عودة🔙',callback_data='back')
   markup.add(btn1,btn2, btn3, btn4, btn5, btn6,btn7) 
   bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='هنا راح تاخذ شيء يفيدك بهالمرحلة وبحياتك اليومية', reply_markup=markup)
 elif call.data =='قوانين':
   bot.send_message(call.message.chat.id, text='قريبا تتم اضافته')
 elif call.data =='اسئلة فاينل':
   bot.send_message(call.message.chat.id, text='قريبا تتم اضافته')
 elif call.data =='اسئلة شهرية':
   bot.send_message(call.message.chat.id, text='قريبا تتم اضافته')    
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
    saif4 = types.InlineKeyboardButton('اشياء تفيدك', callback_data='اشياء تفيدك')
    markup.add(saif1, saif2, saif3, saif4)
    return markup





print('shahm')

bot.infinity_polling()