#This code use Python 3.10.2 or up
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import os 

Theme_color = "#4169e1"
Font_color = "#ffffff"
#-----------------------------------------------------------------------------------------------------------
try :
    userlang = os.popen('systeminfo | findstr /B /C:"System Locale"').read()
    def textviewer(outtrans) :
        #دالة عرض النص في مكان خارجي
        roottext = Tk()
        roottext.resizable(False,False)
        if 'Arabic' in userlang :
            roottext.title("مستعرض النص")
        else:
            roottext.title("Text browser")

        roottext.geometry("700x300")
        text = Text(roottext , font = ("Tajawal" , 15))
        text.insert(INSERT, outtrans)
        text.insert(END, "")
   
        text.pack()
        roottext.mainloop()

    def message_error(title1 , text1) :
            #دالة عرض الرسائل الموجه للمستخدم
            error_404 = Tk()
            error_404.title(title1)
            error_404.geometry("220x50")
            epx = Label(error_404,text = text1).pack()
            def close_epx() :
                error_404.destroy()
            if 'Arabic' in userlang :
                epx_button = Button(error_404,text = "موافق" , command = close_epx).pack()
            else :
                epx_button = Button(error_404,text = "OK" , command = close_epx).pack()
            error_404.mainloop()

    try :

        #كود اداة نطق الكلمات
        import pyttsx3
        wel = pyttsx3.init()
        voices = wel.getProperty("voices")
        wel.setProperty("voices", voices[0].id)
        pyttsx_error = 0

    except :
        pyttsx_error = 1
        
    try : 
        from gtts import gTTS
        gtts_error = 0
    except :
        gtts_error = 1

    try :
        from translate import Translator
        trans_error = 0
    except :
        trans_error = 1

    try :
        from pyperclip import copy
        pyperclip_error = 0
    except :
        pyperclip_error = 1
   
    Data = {"x" : "احد حروف الغة الانجليزية" , "your" : "كاف الملكية" , "xebec" : "وهي سفينة صغيرة استخدمت قديماً" , "xenon" : "وهي احدى العناصر الغازية الثقيلة" , "xenophobe" : "المصاب برهاب الاجانب" , "xenophobia" : "رهاب الاجانب : الخوف من الاجانب" , "xerphilous" : "نامٍ في الجفاف" , "xerophyte" : "النبات الصحراوي" , "xmas" : "عيد الميلاد" , "x-ray" : "اشعة اكس" , "x ray" : "اشعة اكس" , "xray" : "اشعة اكس" , "x ray photograph" : "صورة بالاشعة السينية" , "x-ray photograph" : "صورة بالاشعة السينية" , "x ray photograph" : "صورة بالاشعة السينية" , "xylem" : "الجزء الخشبي من النبات" , "xylgraphy" : "فن النقش على الخشب" , "xylophone" : "اكسلفون : الة مسيقية" , "y" : "احدى حروف الغة الانجليزية" , "yacht" : "اليخت : مركب بحري" , "yachting" : "الابحار باليخوت" , "yak" : "ثور التبت الضخم" , "yam" : "جزء من البطاطا" , "yank" : "يخلق - ينزع - يقتلع" , "yankee" : "اليانكي" , "yap" : "ينبح - يثرثر - نُباح" , "yard" : "الياردة - فناء - ساحة - زريبة" , "yardstick" : "اداة قياس بالياردة - محك" , "yarn" : "غزل(نسيج)- حكاية - يروي حكاية" , "yarrow" : "احدى اوراق النبات تسمى الالفية" , "yawl" : "مركب - نباح - ينبح", "yawn" : "ينفتح - يتثاءب - فجوة - ثغرة - حفرة" , "yawning" : "تثائب - واسع" , "yea" : "نعم - ليس هذا فحسب - بل" , "yean" : "تلد او تنتج" , "year" : "سنة - عام - شيخوخة" , "yearbook" : "كتاب ينشر سنوياً" , "yearling" : "حيوان عمره سنة" , "yearly" : "سنوي - سنويا" , "yearn" : "يتوق الى - يشفق على", "yeast" : "خميرة - رغوة - زبد" , "yeasty" : "فارغ - تافه - مزبد" , "yell" : "يصرخ - يصيح - صرخة" , "yellow" : "الون الاصفر - صفار البيض - شاحب" , "yellowish" : "مصفر - ضارب الى الصفرة" , "yellowness" : "الصفرة" , "yellowtail" : "اصفر الذيل", "yellowy" : "مصفر - ضارب الى الصفرة" , "yelp" : "يعوي - ينبح - عواء - نباح" , "yen" : "وهي العملة اليابانية" , "yeoman" : "ضابط صغير يقوم باعمال مكتبية", "yeomanry" : "احد صغار مالكي الارض" , "yes" : "نعم - بلى - اجل" , "yesterday" : "امس - بالامس - البارحة" , "yesternight" : "اليلة البارحة" , "yet" : "ايضاً - حتى - بل - علاوة على ذلك" , "yiddish" : "لهجة من لهجات الغة" , "yield" : "محصول - يمنح - يحدث - يخضع" , "yoga" : "يوغا" , "yoke" : "اعلى التنورة - عبودية - صلة" , "yokel" : "الفلاح - الريفي - الحلف" , "yon" : "هناك - هنالك - مرئي - ابعد" , "yonder" : "هناك - هنالك - مرئي - ابعد" , "yonde" : "هناك - هنالك - مرئي - ابعد" , "yore" : "الايام الحالية" , "you" : "انت - انتم- انتن - انتِ - انتما" , "young" : " قليل الخبرة - صغير - الشباب - ناشئ" , "younger" : "اصغر - الاصغر" , "youngest" : "الاصغر" , "youngling" : "صغير - الصغير" , "youngster" : "شاب - طفل" , "yourself" : "نفسك - بنفسك " , "youth" : "فتى - شاب - الشباب" , "youthful" : "شاب - غض - طري - قوي - نشيط" , "yowl" : "يعوي - يموء - يصرخ محتجاً - مواء" , "yucca" : "اليكة : نبات من الفصيلة الزنبقية" , "yours" : "لك - لكما  - لكِ - لكن - لكم " , "yugoslav" : "يوغسلافي" , "yule" : "عيد الميلاد : عيد ميلاد المسيح" , "yemen" : "دولة اليمن" , "z" : "احد الاحرف الانجليزية" , "zeal" : "حماسة" , "zealot" : "متحمس - متعصب" , "zealotry" : "حماسة مفرطة - تعصب" , "zealous" : "متحمس - حماسي" , "zealously" : "بحماسة", "zebra" : "حمار الوحش" , "zebu" : "وهو احدى الحيوانات من الفصيلةالبقرية" , "zeitgeist" : "روح العصر" , "zenith" : "السمت - اوج - ذروة" , "zephyr" : "نسيم عليل" , "zeppelin" : "منطاد - منطاد زبلن" , "zero" : "الصفر - شخص تافه" , "zero hour" : "ساعة الصفر" , "zest" : "المنكه - استمتاع شديد - تلذذ - حيوية" , "zuse" : "زيوس : كبير الهة اليونان" , "zigzag" : "خط متعرج - بتعرج - متعرج - يعرج" , "zinc" : "معدن الزنك او الخارصين" , "zincography" : "الحفر او الطباعة بالزنكوغراف", "zinc ointment" : "مرهم الزنك" , "zinc oxid" : "اكسيد الزنك", "zinnia" : "الزينية : نبات جميل الزهر" , "zionism" : "الصهيونية ، الحركة الصهيونية" , "zionist" : "صهيوني" , "zip" : "المعنى في الانجليزية : ازيز- حيوية" , "zip fastener" : "السحاب - الزمام المنزلق" , "zipper" : "السحاب - الزمام المنزلق", "zippy" : "رشيق مفعم باحيوية والنشاط" , "zither" : "وهو احدى الالات المسيقية" , "zloty" : "وحدة النقد البولندية" , "zodiac" : "دائرة البروج" , "zodiacal" : "دائرة البروج" , "zonal" : "منطقي - نطاقي" , "zone" : "منطقة - يقسم الى مناطق - يحيط او يطوق" , "zoo" : "حديقة الحيوان - حديقة الحيوانات" , "zoogeography" : "الجغرافيا الحيوانية" , "zoography" : "الجغرافيا الحيوانية - علم الحيوان الوصفي", "zoolatry" : "عبادة الحيوان اوالحيوانات" , "zoological" : "صفة بمعنى : حيواني" , "zoologically" : "من الوجهة الحيونية - حيوانياً" , "zoological garden" : "حديقة حيوان" , "zoologist" : "العالم بالحيوان" , "zoology" : "علم الحيوان - حيوانات منطقة ما" , "zoom" : "يئز ازيزاً متواصلاً ، يصدر صوت ازيز - ارتفاع مباشرة" , "zoophagous" : "لاحم - اكل لحم الحيوانات" , "zoophyte" : "الحيوان النباتي", "zooplasty" : "الجراحة التعويضية الحيوانية" , "zoroastrian" : "الزراد شتي : شخص يدين بالديانة الزرادشتية" , "zoroastrianism" : "الزرادشتية :ديانة فارسية قديمة", "zulu" : "لغة الزولو", "zwieback" : "البقسماط :جزءمن الخبز يقسم الى شرائح ثم يحمص في الفرن" , "zygote" : "الاقحة : خلية تنشأ من اندماج مشيجين" , "zymology" : "الزيمولوجيا : علم يبحث في الخمائر" , "zymosis" : "تخمر - اختمار" , "zymotic" : "تخمري - اختماري - مخمر - معدٍ" , "q" : "الحرف 17 من الغة الانجليزية" , "quack" :"يصيح - مشعوذ - صوت البط" , "quackery" : "شعوذة" , "quadrangle":"رباعي الزوايا اوالاضلاع" , "quadrangular":"رباعي الزوايا" , "quadrant":"الربعية: اداة تستخدم لقياس الارتفاع - ربع دائرة" ,"quadrate":"مربع او شبه مربع" , "quadratic":"تربيعي(في الرياضيات)" , "quadrilateral":"رباعي الاضلاع" , "quadruped":"رباعي الارجل" , "quadruple":"رباعي - يضاعف او يتضاعف اربع مرات","quaff":"يشرب جرعات كبيرة" , "quagmire":"مستنقع - ورطة" , "quail":"طائر السلوى - طائر السماني - يذبل - يجبن","quaint":"طريف" ,"quake":"يهتز - يرتجف - يتزلزل - هزة - زلزال - رجفة" , "qualification":"اهلية - مؤهل" , "qualified":"موهل - كفو" , "quality":"خاصة - يحدد - يلطف - يخفف - يفوض - يؤهل" , "qualm":"غثيان - ارتياب","quandary":"مأزق - ورطة","quantitative":"كمي - مقداري","quantity":"كمية - كمية كبيرة","quarantine":"حجر -حجر صحي" , "quarrel":"نزاع - شجار - يتنازع" , "quarrelsom":"مشاكس - محب للنزاع" , "quarry":"طريدة - مقلع للحجارة" , "quart":"الكوارت : وحدة قياسية تساوي ربع جلون","quarter":"ربع - فصل - ربع سنة - ربع دولار - نقطة - جهة","quarterdeck":"سطح موخر المركب","quarterly":"فصلي - فصلياً - الفصلية : مجلة تصدر اربع مرات في العام","quartermaster":"الرئيس البحري - امين الامدادات والتموين في الجيش" ,"quartz":"حجر المرو - حجر الكوراتز" , "quash":"يلغي - يسحق - يقمع" , "quasi":"الى درجة ما - شبه","quaver":"يرتعش - يتدهج - يتكلم او يغني بتدهج " , "quay":"رصيف الميناء" , "queasy":"مغثي - مصاب بالغثيان" , "queen":"ملكة" , "queer":"غريب - غير مألوف" , "quell":"يقمع - يخضع - يهدئ" , "quench":"يطفئ - يقمع - يُخمد" , "querulous":"كثير التشكي - دائم الشكوى  - نَكِد" , "query":"سؤال - يتسائل - يشك في" ,"quest":"تحقيق - بحث - تنقيب" , "question":"سؤال - قضية - استجواب - تعذيب شك" , "questionable":"موضع شك - مشكوك فيه" , "questionnaire":"استفتاء" , "queue":"ضفيرة - رتل - صف طابور" ,"quibble":"مراوغة - مواربة - يوارغ - يوارب" , "quick":"سريع - ذكي - نزق - بسرعة - الاحياء - جوهر" , "quicken":"يثير - يسرع - ينشط" , "quickie":"المتعجل:كل ما يتعجل في صناعته سواء اكان فيلم اوكتاب اوغيره" , "quickly":"بسرعة - بعجلة" , "quickness":"سرعة - عجلة" , "quicksand":"الرمل الين" , "quicksilver":"زئبق" , "quick-tempered":"حاد الطبع" , "quick tempered":"حاد الطبع" , "quick-witted":"حاد الذكاء" ,  "quick witted":"حاد الذكاء" , "quid":"مضغة التبغ - التمباك" , "quiescent":"هامد - ساكن - هادئ" , "quiet":"هدوئ - سكون - مطمئن البال - يهدأ - هادئ" , "quietude":"هدوء - سكون - طمأنينة" , "quietus":"تسديد للدين - الراحة - الموت" , "quill":"ريشة - شوكة من اشواك القنفذ" , "quilt":"لحاف - مضربة" , "quince":"شجر السفرجل - ثمار السفرجل" , "quinine":"الكينين : مادة شديدة المرارة تستخدم لعلاج الملاريا" , "quinsy":"التهاب الوزتين المتقيح" , "quintal":"الكنتال - القنطار" , "quintessence":"جوهر" , "quintuplet":"الخماسية : خمسة من نوع واحد - خمس توائم" , "quip":"ملاحظة ساخرة او ظريفة" , "quire":"رزمة ورق مؤلفة من 24 ورقة" , "quirk":"خاصية - خصوصية -  صفة مميزة" , "quit":"يسلك - يترك - يكف عن" , "quite":"الى حد بعيد - ًتماماً - فعلا" , "quits":"متخالصان - متعادلان" , "quittance":"ابراء دين او التزام - تعويض - سند الابراء" , "quiver":"جعبة - يهتز - يرتعش - يرتجف" , "quixotic":"وهمي" , "quiz":"امتحان موجز - يسخر من - يمتحن" , "quizzical":"غريب - هزلي - ساخر - مازح - فضولي" , "quoit":"حلقة الرمي : حلقة معدنية ترمى لتطوق وتد غرس في الارض" , "quondam":"سابق" , "quorum":"عدد الاعضاء الذين يتعين حضورهم لتصبح الجلسة قانونية" , "quota":"نصيب - حصة نسبية" , "quotable":"جدير بان يستشهد به" , "quotation":"الشاهد - جملة او فقرة مقتبسة - الاقتباس : الاستشهاد ب - سعر" , "quotation marks":"علامات الاقتباس" , "quotation-marks":"علامات الاقتباس" , "quote":"يقتبس - يستشهد - علامة اقتباس" , "quoth":"قال" , "quotidion":"يومي - مبتذل - عادي" , "quotient":"خارج القسمة - حاصل" , "quran":"القران الكريم" , "qu'ran":"القران الكريم" , "qursh":"القرش : 1/20 من الريال السعودي" ,"k" : "احد احرف الغة الانجليزية" , "kaffir" : "الكفيري  :  هضو في مجموعة الشعوب الناطقة بلغة بانتو في جنوب افريقيا" , "kalser" : "قيصر - امبراطور" , "kale" : "كرنب - مال - دراهم" , "kangaroo" : "الكنغر" , "katydid" : "الجندب الامريكي" , "keel" : "يقلب - ينقلب" , "keen" : "ماضٍ - قاطع - باتر - قوي - حاد" , "keep" : "يفي - يصون - يحمي - يبقي - يدون" , "keeper" : "الحافظ - القائم على" , "keeping" : "حفظ - عناية - اعالة" , "keepsake" : "تذكار - هدية للذكرى" , "keg" : "برميل صغير" , "ken" : "يدرك - يعرف - مدى البصر" , "kennel" : "وجار الكلب - قناو" , "kerb" : "حاجز حجري عند حافة الطريق" , "kerchief" : "حجاب - وشاح - منديل" , "kernel" : "نواة - حبة القمح - جوهر الشئ او لبه" , "kerosine" : "الكيروسين" , "kerosene" : "الكيروسين" , "kettle" : "غلاية - غلاية الشاي" , "kettledrum" : "طبلة" , "key" : "مفتاح" , "keyboard" : "لوحة المفاتيح" , "keyhole" : "موضع وضع المفتاح في القفل" , "keynote" : "الفكرة الاساسية" , "keystone" : "مرتكز" , "khaki" : "بذلة عسكرية" , "khan" : "زعيم" , "khedive" : "امير مصر" , "kick" : "يرفس - رفسة - مفاجأة" , "kickshaw" : "طعام مترف" , "kid" : "طفل" , "kidnap" : "يخطف" , "kidney" : "مزاج" , "kidney bean" : "لوبياء" , "kill" : "يقتل - يوقف - يذبح" , "killer" : "السفاح - القاتل" , "kiln" : "التنور" , "kilo" : "كيلوغرام - كيلومتر" , "kilocycle" : "الكيلوسيكل  :  الف دورة" , "kilogram" : "كيلوغرام" , "kiloliter" : "الكيلولتر - متر مكعب" , "kilometer" : "الكيلو متر - الف متر" , "kilowatt" : "الف واط" , "kilt" : "تنورة رجالية  اسكتلندية" , "kimono" : "الكيمون  :  ثوب فضفاض" , "kin" : "عشيرة - اقرباء المرء" , "kind" : "نوع - صنف - حنون - لطيف - كريم" , "kindergarten" : "روضة اطفال" , "kindle" : "يتوهج - يثير - يضيء" , "kindless" : "فظ - قاسٍ - غليظ" , "kindliness" : "عطف" , "kindly" : "عطوف - بعطف - بارتياح - لطفا" , "kindness" : "عطف - رقة في الفؤاد" , "kindred" : "انسباء - اسرة - عشيرة - شقيق" , "kinetic" : "حركي - ناشط" , "kinetic energy" : "علم الحركة" , "king" : "ملك" , "kingdom" : "مملكة - عالم" , "kingfisher" : "طائر الرفراف" , "kink" : "عقدة في الحبل - غرابة اطوار" , "kinsfolk" : "انسباء - اقرباء" , "kinship" : "قرابة - نسب" , "kinsman" : "احد الاقرباء - القريب" , "kinswoman" : "احد القريبات" , "kiosk" : "كشك  :  محل بيع صغير" , "kipper" : "سمكة رنكة مملحة ومدخنة" , "kiss" : "قبلة - يقبل" , "kit" : "عدة - طقم ادوات - كمنجة صغيرة" , "kitchen" : "مطبخ" , "kitchenware" : "ادوات الطبخ" , "kite" : "طائرة ورقية - الحدأة" , "kith" : "اصدقاء - انسباء - جيران" , "kitten" : "هرة صغيرة" , "kiwi" : "الكيوي  :  اسم يطلق على طائر نيوزلندي وعلى فاكهة خضراء" , "knack" : "براعة - حيلة - موهبة" , "knapsack" : "حيقبة ظهر يحملها الجنود" , "knave" : "الوغد - الولد في لعبة الورق" , "knavery" : "خداع - احتيال - مكر" , "knead" : "يعجن - يدلك" , "knee" : "الركبة" , "kneecap" : "عظم اعلى الركبة" , "kneel" : "يركع - يسجد" , "knell" : "نعي" , "knelt" : "ركع - سجد" , "knew" : "عَلِمَ" , "knife" : "سكين" , "knight" : "الفارس - الفرس في الشطرنج" , "knighthood" : "فروسية - فرسان" , "knightly" : "فروسي" , "knit" : "يعقد - يربط - يجبر - يقتلع حاجبيه - يحبك" , "knitting" : "عقد - ربط - حبك" , "knob" : "مسكة باب مزخرفة - هضبة مدورة" , "knock" : "يقرع - يصطدم بشيء - يخبط - يعيب - ينتقد" , "knocker" : "القارع - مقرعة الباب" , "knockout" : "الضربة الحاسمة" , "knoll" : "هضبة صغيرة مدورة" , "knot" : "عقدة - مشكلة - رباط" , "knotty" : "مليء بالعقد - صعب" , "know" : "يعلم - يعرف" , "knowing" : "معرفة" , "knowledge" : "معرفة - علم - اطلاع" , "knuckle" : "البرجمة  :  احد مفاصل الاصبع" , "koran" : "القران الكريم",'j':'الحرف العاشر من الابجدية الانجليزية','jap':'يخز - يطعن - يلطم - يلكم - لكمة','jabber':'يثرثر - ثرثرة - يتكلم  بشكل غير واضح','jack':'رافعة - علم صغير -الولد في لعبة الورق','jackal':'ابن اوى','jackass':'حمار - مغفل - غبي','jackdaw':'غراب الزيتون','jacket':'سترة - جاكيت - غلاف','jade':'منهوك القوى - فرس','jackscrew':'المرفاع اللولبي','jag':'نتوء حاد','jaguar':'نمر امريكي مرقط','jail':'سجن - يسجن','jailbird':'السجين - المجرم المزمن','jailer':'السجان','jailor':'السجان','jam':'مربى - مربى الفاكهة - يسحق - يضغط - يثبت باحكام','jamboree':'مهرجان - مهرجان للكشافة','janitor':'الحاجب - البواب','january':'ياناير','japan':'اليابان','japanese':'شخص ياباني - الغة اليابانية','jar':'يتنافر - يضايق - يرج - ارتجاج - صدمة','jargon':'لغة مطربة غير مفهومة','jasmine':'الياسمين','jasper':'اليشب : حجر كريم','jaundice':'مرض اليرقان','jaunt':'رحلة قصيرة','jaunty':'انيق - مرح','java':'الجافا : لغة برمجة كائنية التوجه','javelin':'رمح','jaw':'فك - حنك','jawbone':'عظم الفك - الفك السفلي','jay':'ابو زريق : طائر يشبه الغراب','jazz':'موسيقى الجاز','jealous':'غيور - حسود - حريص - يقظ','jealousy':'غيره - حسد - حرص - يقظة','jeep':'سيارة الجيب','jeer':'يسخر - ملاحظة ساخرة','jejune':'تافه او صبياني','jelly':'حلوى الهلام او الجيليه','jellyfish':'قنديل البحر','jeopard':'يعرض للخطر','jeopardize':'يعرض للخطر','jeopardy':'خطر','jerk':'ارتعاش عصبي - يرتج','jerkin':'سترة طويلة لا كمين لها','jersey':'قميص صوفي','jerusalem':'القدس  - بيت المقدس','jessamine':'ياسمين','jest':'نكتة - دعابة - مزاح - يسخر','jesus':'النبي عيسى عليه السلام','jet':'الكهرمان الاسود - نافورة - انبثاق','jet airplane':'طائرة نفاثة','jet-airplane':'الطائره النفاثة','jet engine':'المحرك النفاث','jet-engine':'المحرك النفاث','jetty':'محط السفن في البحر','jew':'يهودي : احد اليهود','jewel':'جوهرة - حجر كريم','jeweler':'صائع الحلي او المجوهرات','jewelry':'حلى - مجوهرات','jewellery':'مجوهرات','jewess':'يهودية : فتاة او امراة يهودية','jewish':'يهودي - عبري','jip':'شراع السارية الامامية','jiff':'لحظة','jiffy':'لحظة','jig':'رقصة الجيغ - يهزهز','jilt':'الناكثة : امراة تنكث بالعقد الذي قطعته لحبيبها','jingle':'يجلجل - يخشخش - جلجلة - خشخشة','jingo':'وطني متطرف','jitters':'نرفزة - اهتياج عصبي','jop':'عمل - مهمة - وظيفة','jobber':'سمسار - وسيط','jokey':'فارس خيل السباق','jocose':'فكاهي','jocular':'مزوح - مازح','jocularity':'مزاح - مزحة','jocund':'مرح','jog':'يهز - يدفع برفق - ينبه - يتذبذب','joggle':'يهز برفق -  يهتز - يتمايل','join':'يربط - يضم - يصل - يلحق - يتصل','joiner':'نجار','joinery':'النجارة : عمل النجار','joint':'مفصل - قطعة لحم للشوي - يقطع - مشترك - متشارك','jointed':'ذو مفاصل','jointly':'بالاشتراك او بالتعاون مع','joke':'نكتة - دعابة - مزاح','joker':'الجوكر في ورقة العب - الشخص المزوحي او المنكت','jollity':'ابتهاج صاخب','jolly':'ابتهاج - مرح','jolt':'ضربة - صدمة - ينتخع - رجة - يرتج','jonquil':'نبات النرجس الاسلي','jostle':'وزن ذرة - يدون باختصار - مذكرة موجزة','jotting':'تذكرة موجزة','journal':'دفتر اليومية - يوميات - جريدة - مجلة','journalism':'الصحافة','journalist':'صحفي - كاتب يوميات','journalistc':'صحفي','journey':'يقوم برحلة - رحلة','journeyman':'عامل بارع','joust':'يصارع بالسيف - يصارع','jovial':'مرح - جذل','joviality':'مرحٌ - جذلٌ','jowl':'الفك الاسفل - الحد','joy':'ابتهاج - يبتهج','joyful':'مبتهج - بهيج - سار','joyless':'كثيب','joyous':'مبتهج - بهيج - سار','jubilant':'شديد الابتهاج','jubilee':'يوبيل','jubilation':'ابتهاج','judaism':'اليهودية : ديانة اليهود','judge':'يحكم على - يحاكم - يقدر - يعتبر - يقضي - قاض','judgment':'قضاء - رأي -  قرار محكمة','judgement':'قضاء - يحكم على - قرار محكمة - راي','judicial':'قضائي - حصيف','judiciary':'قضائي - النظام القضائي - القضاة - السلطة القضائية','judicious':'حكيم - حصيف','judo':'الجودو : المصارعة اليابانية','jug':'ابريق - سجن','juggle':'يشعوذ - يتلاعب ب - يخدع','juggler':'المشعوذ - المحتال - المتلاعب ب','jugular vein':'الوريد الوداجي في العنق','juice':'عصير - عصارة','juicy':'كثير العصارة - ممتع','jujube':'علكة - قرص محلى','julep':'الجلاب - شراب مسكر','july':'شهر يوليو','jumble':'يخلط - اختلاط - اشياء مختلطة بغير نظام','jumb':'يقفز - قفز - وثبة - حاجز - ارتفاع مفاجئ','jemper':'الجمبر : اداة تستخدم في الوحة الام - سترة العمال','jumby':'متقلب - عصبي','junction':'نقطة اتصال - اتصال - وصل - ملتقى طرق - صلة','june':'يونيو','junior':'الاصغر - الادنى - اقل اهمية اهمية','juniper':'العرعر : شجر صنوبري','junk':'سلعة مستعملة او بالية - مخدرات - شيئ تافه','junket':'حفلة - رحلة - حلوى هلامية','junta':'مجلس سياسي - لجنة سياسية','junto':'الزمرة : مجموعة من الاشخاص يجمعهم هدف واحد','jupiter':'المشتري','juridical':'قضائي - قانوني - شرعي','jurisprudence':'قانون - مجموعة قوانين - فلسفة التشريع','juror':'المحلف :  عضو في هيئة المحلفين','jury':'هيئة المحلفين','just':'صحيح - مضبوط - دقيق - منصف - مستقيم - تماما - لحظات - مباشرة - جدا','justice':'عدل - عدالة - حق - استقامة  - قاض','justifiable':'ممكن تبريره','justification':'ممكن تبريره','justificatory':'تبريري - تسويغي','justify':'يبرر','jut':'نتوء','juvenile':'يافع - حدث - صبياني - اليافع','juvenile court':'محكمة الاحداث','juvenile-court':'محكمة الاحداث','juvenile delinquent':'مجرم يافع','juvenile-delinquent':'مجرم يافع','joxtapose':'يضع شيئ بجانب اخر','juxtaposition':'وضع شيئ بجانب اخر' , 'yolk' : "صفار البيض" , 'ye' : "انتَ - انتِ"}
    new_data_con ={}

    def open_creator() :
        cre = Tk()
        if 'Arabic' in userlang :
            cre.title("محرر قواعد البيانات")
        else:
            cre.title("Database Editor")

        cre.config(background = Theme_color)
        cre.geometry("378x400")
        cre.resizable(False,False)

        cref = Frame(cre, bg="#d4d4d4" , width=380 , height=450).place(x = 0 , y = 60)
        creapp_name = Label(cre,text = "zezn Translate" , bg = Theme_color , fg = Font_color , font=("Tajol",22))
        creapp_name.place(x = 10, y = 11 )

        cre_input = Frame(cre, bg = Theme_color , width = "333" , height = "160")
        cre_input.place(x = 24 , y = 100)
      
        l1 = Label(text = "{")
        p1 = Label(text = "")
        def add_to_data_base():
            l1["text"] =  l1["text"].replace("}" , "") + "," + "'" + cre_cre_e1.get() + "'" + ":" + "'" + cre_cre_e2.get() + "'" + "}"
            l1["text"] = l1["text"].replace("{," , "{")
            cre_cre_e1.delete(0, END)
            cre_cre_e2.delete(0, END)
         
        def save():
            try :
                tosave = open(p1["text"],mode = "w",encoding = "utf-8")
                tosave.write(l1["text"])
                tosave.close()
            except :
                p1["text"]= filedialog.asksaveasfilename()
                try :
                    tosave = open(p1["text"],mode = "x",encoding = "utf-8")
                    tosave.write(l1["text"])
                    tosave.close()
                except :
                    tosave = open(p1["text"],mode = "w",encoding = "utf-8")
                    tosave.write(l1["text"])
                    tosave.close()

        def open_Data_Base():
            p1["text"]= filedialog.askopenfilename()
            cre_pa_1 = open(p1["text"],mode = "r",encoding='utf-8')
            l1["text"] = cre_pa_1.read()  
            cre_pa_1.close()

        def save_as():
            p1["text"]= filedialog.asksaveasfilename()
            try :
                tosave = open(p1["text"],mode = "x",encoding = "utf-8")
                tosave.write(l1["text"])
                tosave.close()
            except :
                tosave = open(p1["text"],mode = "w",encoding = "utf-8")
                tosave.write(l1["text"])
                tosave.close()

        if 'Arabic' in userlang :    
            cre_cre_l1 = Label(cre_input ,bg=Theme_color ,text =  ": انشاء كلمة في قاعدة البيانات",fg = Font_color).place(x = 176 , y = 10) 
            cre_cre_l2 =Label(cre_input,text = ": الكلمة",bg = Theme_color,fg = Font_color).place(x = 260 , y = 45)
            cre_cre_l3 =Label(cre_input,text = ": معناها",bg = Theme_color,fg = Font_color).place(x = 259 , y = 85)
            cre_cre_b1 = ttk.Button(cre_input,text ="حفظ",command = add_to_data_base).place(x = 245 , y = 125)

        else :
            cre_cre_l1 = Label(cre_input ,bg=Theme_color ,text =  "Add a word to the database :",fg = Font_color).place(x = 10 , y = 10)
            cre_cre_l2 =Label(cre_input,text = "Words :",bg = Theme_color,fg = Font_color).place(x = 10 , y = 45)
            cre_cre_l3 =Label(cre_input,text = "Meaning :",bg = Theme_color,fg = Font_color).place(x = 10 , y = 85)
            cre_cre_b1 = ttk.Button(cre_input,text ="Add",command = add_to_data_base).place(x = 20 , y = 125)

        cre_cre_e1 = ttk.Entry(cre_input,width = 30)
        cre_cre_e1.place(x = 70 , y = 45)

        cre_cre_e2 = ttk.Entry(cre_input,width = 30)
        cre_cre_e2.place(x = 70 , y = 85)

        cre_se = Frame(cre, bg = Theme_color , width = "333" , height = "60")
        cre_se.place(x = 24 , y = 300)

        if 'Arabic' in userlang :
            cre_car_b1 =ttk.Button(
                cre_se
                ,text ="فتح"
                ,command = open_Data_Base
            ).place(x = 230 , y = 17)

            cre_car_b2 =ttk.Button(
                cre_se
                ,text ="حفظ"
                ,command = save
            ).place(x = 130 , y = 17)

            cre_car_b3 =ttk.Button(
                cre_se
                ,text ="حفظ باسم"
                ,command = save_as
            ).place(x = 30 , y = 17)

        else:
            cre_car_b1 =ttk.Button(
                cre_se
                ,text ="Open db"
                ,command = open_Data_Base
            ).place(x = 230 , y = 17)

            cre_car_b2 =ttk.Button(
                cre_se
                ,text ="Save"
                ,command = save
            ).place(x = 130 , y = 17)

            cre_car_b3 =ttk.Button(
                cre_se
                ,text ="Save As"
                ,command = save_as
            ).place(x = 30 , y = 17)
            
        cre.mainloop()

    sayer_file_path = ""
    sayer_text = ""

    def snders() :
        if (gtts_error == 0) :
            sayer = Tk()

            if "Arabic" in userlang :
                sayer.geometry("310x180")
                sayer.title("تحويل النص الى صوت")
            else :
                sayer.geometry("310x155")
                sayer.title("Convert TXT to Mp3")

            sayer.resizable(False,False)
            sayer.config(background = "#202020")

            sayer_file_path = Label()
            sayer_text = Label()

            def sayer_btcommand1():
                global sayer_file_path
                global sayer_text

                sayer_file_path["text"] = filedialog.askopenfilename()
                sayer_var1 = open(sayer_file_path["text"] , mode="r" , encoding="utf-8")
                sayer_text["text"] = sayer_var1.read()
                sayer_var1.close()

            if "Arabic" in userlang :
                sayer_l4 = Label(sayer,text = ": لغة المستند" , bg="#202020" , fg = "#ffffff").place(x = 234 , y = 50)
                vals = ["Arabic" , "English" , "Fransh"]
                sayer_compo = ttk.Combobox(sayer,values=vals , width = 30)
                sayer_compo.place(x = 10 , y = 50)
            else :
                sayer_l4 = Label(sayer,text = "Text Lang :" , bg="#202020" , fg = "#ffffff").place(x = 17 , y = 50)
                vals = ["Arabic" , "English" , "Fransh"]
                sayer_compo = ttk.Combobox(sayer,values=vals , width = 30)
                sayer_compo.place(x = 100 , y = 50)

            def sayer_save():
                sayer_path_to_save = filedialog.asksaveasfilename()
                try :
                    if (sayer_compo.get() == vals[0]):

                        audio = gTTS(text=sayer_text["text"].replace(".mp3","") , lang = "ar" , slow=False)
                        audio.save(sayer_path_to_save.replace(".mp3","").replace(".","") + ".mp3")

                    elif (sayer_compo.get() == vals[1]) :

                        audio = gTTS(text=sayer_text["text"].replace(".mp3","") , lang = "en" , slow=False)
                        audio.save(sayer_path_to_save.replace(".mp3","").replace(".","") + ".mp3")
    
                    elif (sayer_compo.get() == vals[2]) :

                        audio = gTTS(text=sayer_text["text"].replace(".mp3","") , lang = "fr" , slow=False)
                        audio.save(sayer_path_to_save.replace(".mp3","").replace(".","") + ".mp3")

                except :
                    if "Arabic" in userlang :
                        message_1 = messagebox.showinfo("Error","يرجى الاتصال بالانترنت")
                    else :
                        message_1 = messagebox.showinfo("Error" , "Please get online")

            if "Arabic" in userlang :
                sayer_bt1 = ttk.Button(sayer,text = "فتح ملف النص" , command = sayer_btcommand1 , width = 15).place(x = 200 , y = 20 + 70)
                sayer_bt2 = ttk.Button(sayer,text = "حفظ الملف الصوتي" , command = sayer_save).place(x = 20 , y = 20 + 70)
                sayer_l1 = Label(sayer,text = "<-----|" , bg="#202020" , fg = "#ffffff").place(x = 140 , y = 20 + 70)

            else :
                sayer_bt1 = ttk.Button(sayer,text = "Open TXT file" , command = sayer_btcommand1 , width = 15).place(x = 200 , y = 20 + 70)
                sayer_bt2 = ttk.Button(sayer,text = "Save Mp3 file" , command = sayer_save).place(x = 20 , y = 20 + 70)
                sayer_l1 = Label(sayer,text = "<-----------|" , bg="#202020" , fg = "#ffffff").place(x = 115 , y = 20 + 70)


            if "Arabic" in userlang :

                sayer_lm1 = Label(sayer,text = "عندما تقوم بتحويل مستندات عربية الى ملفات صوتية قم " , bg="#202020" , fg = "red").place(x = 30 , y = 60 + 70)
                sayer_lm2 = Label(sayer,text = "بتشكيل النص ليتم نطقه بالشكل الصحيح" , bg="#202020" , fg = "red").place(x = 106 , y = 80 + 70)

            else :
                sayer_lm1 = Label(sayer,text = " - This app need Internet" , bg="#202020" , fg = "red" , font=("Bold",10)).place(x = 10 , y = 60 + 70)

            sayer_l0 = Label(sayer,text = "Convert txt To mp3" , height=2 , fg = "#ffffff" , bg = "#454567").pack(fill =X)

            sayer.mainloop()
        else: 
            message_error("Error","gTTS يرجى تثبيت")

    def take_data_b():

        tdb=Tk()
        if 'Arabic' in userlang :
            tdb.title("ربط قاعدة بيانات")
        else :
            tdb.title("Connect to the database")

        tdb.geometry("378x250")
        tdb.resizable(False,False)
        tdb.config(background= Theme_color)

        wtdb = Frame(tdb, bg="#d4d4d4" , width=380 , height=190).place(x = 0 , y = 60)

        tdbapp_name = Label(tdb,text = "zezn Translate" , bg = Theme_color , fg = Font_color , font=("Tajol",22))
        tdbapp_name.place(x = 10, y = 11 )
        path_entry = Label(tdb,fg = "blue" , width=42)
        path_entry.place(x = 20 , y = 100 + 60)
        
        if 'Arabic' in userlang :
            tdb_l_1 = Label(tdb,text = ": اسم الغة" ,  bg = "#d4d4d4").place(x = 315 , y = 100)
            tdb_ent_1 = ttk.Entry(tdb,width=45)
            tdb_ent_1.place(x = 20 , y = 100)
        else :
            tdb_l_1 = Label(tdb,text = "Language Name :" ,  bg = "#d4d4d4" ).place(x = 17 , y = 100)
            tdb_ent_1 = ttk.Entry(tdb,width=40)
            tdb_ent_1.place(x = 120 , y = 100)

        Path_Data_Base_1 = Label()

        def tdb_chose_data_base() :
            Path_Data_Base_1["text"] = filedialog.askopenfilename()
            path_entry["text"] = Path_Data_Base_1["text"]

        button_chose = Button(tdb,text = "..." , command = tdb_chose_data_base , width = 4).place(x = 330 , y = 100 + 60)

        def tdb_condb() :
            global new_data_con
            tdb_t_1 = open(Path_Data_Base_1["text"] ,mode = "r",encoding='utf-8')
            tdb_t_2 = tdb_t_1.read()
            new_data_con = eval(str(tdb_t_2))
            tdb_t_1.close()
            DataBaseMenu.entryconfigure(2,label = tdb_ent_1.get() , command = chose_lang_new)
            tdb.destroy()

        btn_oktc = Button(tdb,text = "OK" , width = "38", font=('Tajawal',12) , fg = Font_color , bg = "grey" , command=tdb_condb).place(x = 20 , y = 150 + 50)
        tdb.mainloop()

    # كود انشاء التطبيق
    app = Tk()
    app.title("zezn Translate")
    app.geometry("378x565")
    app.config(background= Theme_color)
    app.resizable(False,False)
   
    chose_language = Label(text = "english")
    
    def about() :
        if 'Arabic' in userlang : 
            messa1 = messagebox.showinfo("About" , "تم تطوير هذا البرنامج عن طريق زيزن سوفتوير بواسطة المطور زياد الحموي")
        else :
            messa1 = messagebox.showinfo("About" , "This program was developed by zezn Software by the developer Ziad Al-Hamwi")

    window = Frame(app, bg="#d4d4d4" , width=380 , height=548)
    window.place(x = 0 , y = 60)

    arlangs = ['الغة العربية' , 'الغة الروسية' , 'الغة الكندية' , 'الغة الفرنسية']
    enlangs = ['Arabic language' , 'French language' , 'Russian language' , 'Canadian language']
    if 'Arabic' in userlang :
        miclabel1 = Label(bg = "#d4d4d4", text = ": الى لغة")
        miccompo = ttk.Combobox(width = 40 , values=arlangs)
    else:
        miclabel1 = Label(bg = "#d4d4d4", text = "To language :")
        miccompo = ttk.Combobox(width = 37 , values=enlangs)

    def chose_lang_microsoftapi() :
        chose_language["text"] = "microsoft"
        if 'Arabic' in userlang :
            miclabel1.place(x = 310 , y = 75)
            miccompo.place(x = 23 , y = 75)
        else :
            miclabel1.place(x = 20 , y = 75)
            miccompo.place(x = 111 , y = 75)

    def chose_lang_asng() :
        chose_language["text"] = "english"
        miclabel1.place(x = 1000 , y = 1000)
        miccompo.place(x = 1000 , y = 1000)

    def chose_lang_new() :
        chose_language["text"] = "new"
        miclabel1.place(x = 1000 , y = 1000)
        miccompo.place(x = 1000 , y = 1000)
    
    if 'Arabic' in userlang :
        menubar = Menu(app)
        DataBaseMenu = Menu(menubar , tearoff=0)
        menubar.add_cascade(label = "الغات المتوفرة" , menu = DataBaseMenu )
        DataBaseMenu.add_command(label = 'الاتصال بقاعدة بيانات ميكروسوفت' , command = chose_lang_microsoftapi )
        DataBaseMenu.add_command(label = 'English To Arabic  (offline)' , command = chose_lang_asng )
        DataBaseMenu.add_command(label = '...' , command = take_data_b )

        AppMenu = Menu(menubar , tearoff=0)
        menubar.add_cascade(label = "تطبيقات اضافية" , menu = AppMenu )
        AppMenu.add_command(label = 'منشئ قواعد البيانات' , command = open_creator)
        AppMenu.add_command(label = 'محول النصوص الى ملفات صوتية' , command = snders )

        aboutMenu = Menu(menubar , tearoff=0)
        menubar.add_cascade(label = "عن المطور" , menu = aboutMenu )
        aboutMenu.add_command(label = 'عن المطور' , command = about )

        app.config(menu = menubar)

    else :
        menubar = Menu(app)
        DataBaseMenu = Menu(menubar , tearoff=0)
        menubar.add_cascade(label = "Languages" , menu = DataBaseMenu )
        DataBaseMenu.add_command(label = 'Connect to a Microsoft database' , command = chose_lang_microsoftapi )
        DataBaseMenu.add_command(label = 'English To Arabic (offline)' , command = chose_lang_asng )
        DataBaseMenu.add_command(label = '...' , command = take_data_b )

        AppMenu = Menu(menubar , tearoff=0)
        menubar.add_cascade(label = "Other applications" , menu = AppMenu )
        AppMenu.add_command(label = 'Database Editor' , command = open_creator)
        AppMenu.add_command(label = 'Convert txt to mp3' , command = snders )

        aboutMenu = Menu(menubar , tearoff=0)
        menubar.add_cascade(label = "About" , menu = aboutMenu )
        
        aboutMenu.add_command(label = 'About the developer' , command = about )

        app.config(menu = menubar)

    app_name = Label(text = "zezn Translate" , bg = Theme_color , fg = Font_color , font=("Tajol",22))
    app_name.place(x = 10, y = 11)

    widows_input = Frame(window, bg = Theme_color , width = "333" , height = "135")
    widows_input.place(x = 24 , y = 50)

    if 'Arabic' in userlang :
        mess = Label(widows_input,text = " : ادخل الكلمة المراد ترجمتها" , bg = Theme_color , fg = Font_color)
        mess.place(x = 180 , y = 25)
    else :
        mess = Label(widows_input,text = "Enter a word to translate it :" , bg = Theme_color , fg = Font_color)
        mess.place(x = 15 , y = 25)        

    Ent = ttk.Entry(widows_input, width = 40)
    Ent.place(x = 44 , y = 60)

    def read() :
        if pyttsx_error == 0 :
            wel.say(Ent.get().replace("<" , "").replace(">" , "").replace("!",""))
            wel.runAndWait()
        else :
            message_error("Pyttsx3" , "Pyttsx3 يرجى تثبيت مكتبة")
    
    widows_outpot = Frame(window, bg = Theme_color , width = "333" , height = "135")
    widows_outpot.place(x = 24 , y = 220)

    def clear() :
        tran_view["text"] = "-"
        tran_view["fg"] = Font_color   
        tran_view.place(x = 30 , y = 30 + 28)

    mtranslation = ''

    def trans() :
        global mtranslation
        if (chose_language["text"] == "english") :
            Enter = str(Ent.get()).casefold()
            try : 
                trans_1234 = Data[Enter]
                if len(trans_1234) < 52 :
                    tran_view["text"] = trans_1234
                
                elif len(trans_1234) > 52 :
                    if 'Arabic' in userlang :
                        tran_view["text"] = "لعرض الترجمة اضغط على زر عرض الترجمة في مكان خارجي"
                    else :
                        tran_view["text"] = "Tap the button to view subtitles outside"

                elif len(trans_1234) == 52 :
                    if 'Arabic' in userlang :
                        tran_view["text"] = "لعرض الترجمة اضغط على زر عرض الترجمة في مكان خارجي"
                    else :
                        tran_view["text"] = "Tap the button to view subtitles outside"
                  
            except :
                if 'Arabic' in userlang :
                    tran_view["text"] = "تتعذر الترجمة ، كلمة غير متوفرة"
                else :
                    tran_view["text"] = "word is not available"
            
        elif (chose_language["text"] == "new") :
            Enter = str(Ent.get()).casefold()
            try :
                trans_1234 = new_data_con[Enter]
                if len(trans_1234) < 52 :
                    tran_view["text"] = trans_1234
              
                elif len(trans_1234) > 52 :
                    if 'Arabic' in userlang :
                        tran_view["text"] = "لعرض الترجمة اضغط على زر عرض الترجمة في مكان خارجي"
                    else :
                        tran_view["text"] = "Tap the button to view subtitles outside"
                   
                elif len(trans_1234) == 52 :
                    if 'Arabic' in userlang :
                        tran_view["text"] = "لعرض الترجمة اضغط على زر عرض الترجمة في مكان خارجي"
                    else :
                        tran_view["text"] = "Tap the button to view subtitles outside"
                                
            except :
                if 'Arabic' in userlang :
                    tran_view["text"] = "تتعذر الترجمة ، كلمة غير متوفرة"
                else :
                    tran_view["text"] = "word is not available"

        elif (chose_language["text"] == 'microsoft') :
            Enter = str(Ent.get()).casefold()
            try:
                mtranslator= Translator(to_lang=miccompo.get().replace("Arabic language","ar").replace("French language","fr").replace("Russian language","ru").replace("Canadian language","ca").replace("الغة العربية","ar").replace("الغة الفرنسية","fr").replace("الغة الروسية","ru").replace("الغة الكندية","ca"))
                mtranslation = mtranslator.translate(Enter) 
                if (len(mtranslation) == 50) or (len(mtranslation) < 50) :   
                    tran_view["text"] = mtranslation
                else :
                    if 'Arabic' in userlang :
                        tran_view["text"] = "لعرض الترجمة اضغط على زر عرض الترجمة في مكان خارجي"
                    else :
                        tran_view["text"] = "Tap the button to view subtitles outside"
            except :
                if 'Arabic' in userlang :
                    var2 = messagebox.showinfo("error","يرجى الاتصال بالانترنت")
                else :
                    var2 = messagebox.showinfo("error","Please go online")

    def view_trans_out() :
        if (chose_language["text"] == "english") : 
            try :
                Enter = str(Ent.get()).casefold()
                textviewer(Data[Enter])
            except :
                pass
        elif (chose_language["text"] == "new"):
            try :
                Enter = str(Ent.get()).casefold()
                textviewer(new_data_con[Enter])
            except :
                pass

        elif (chose_language["text"] == "microsoft"):
            try :
                textviewer(mtranslation)
            except :
                pass

    def copytranslate():
        if (chose_language["text"] == "english") : 
            try :
                Enter = str(Ent.get()).casefold()
                copy(Data[Enter])
            except :
                pass
        elif (chose_language["text"] == "new"):
            try :
                Enter = str(Ent.get()).casefold()
                copy(new_data_con[Enter])
            except :
                pass

        elif (chose_language["text"] == "microsoft"):
            try :
                copy(mtranslation)
            except :
                pass

    if 'Arabic' in userlang :
        copbtn = ttk.Button(widows_outpot,text = "نسخ الترجمة",command=copytranslate)
        copbtn.place(x = 244 , y = 100)
        trs = Button(command = trans , width = 12 , height = 1 , text = "ترجمة الكلمة" , font=('Tahoma',12) , fg = Font_color , bg = "grey")
        btn_view_out = Button(text = "عرض  ترجمة الكلمة في مكان خارجي" , width = "35", font=('Tahoma',12) , fg = Font_color , bg = "grey" , command=view_trans_out)
        cle = Button(command = clear , width = 11 , height = 1 , text = "clear" , font=('Tahoma',12) , fg = Font_color , bg = "grey").place(x = 227+13 , y = 440 + 15)
        mess2 = Label(widows_outpot,text = " : الترجمة" , bg = Theme_color , fg = Font_color)
        mess2.place(x = 270 , y = 20)
        tran_view = Label(widows_outpot,text = "-" , bg = Theme_color , fg = Font_color)
        tran_view.place(x = 15 , y = 30 + 28)
        readbutton = Button(window, text = "نطق" , command = read , height = 1 , font=('Tahoma',12) , fg = Font_color , bg = "grey", width = 7 )

    else:
        copbtn = ttk.Button(widows_outpot,text = "copy",command=copytranslate)
        copbtn.place(x = 27 , y = 100)
        trs = Button(command = trans , width = 12 , height = 1 , text = "Translate" , font=('Tahoma',12) , fg = Font_color , bg = "grey")
        btn_view_out = Button(text = "View word translation in an outdoor location" , width = "35", font=('Tahoma',12) , fg = Font_color , bg = "grey" , command=view_trans_out)
        cle = Button(command = clear , width = 11 , height = 1 , text = "clear" , font=('Tahoma',12) , fg = Font_color , bg = "grey").place(x = 227+13 , y = 440 + 15)
        mess2 = Label(widows_outpot,text = " Translate :" , bg = Theme_color , fg = Font_color)
        mess2.place(x = 15 , y = 20)
        tran_view = Label(widows_outpot,text = "-" , bg = Theme_color , fg = Font_color)
        tran_view.place(x = 20 , y = 30 + 28)
        readbutton = Button(window, text = "say" , command = read , height = 1 , font=('Tahoma',12) , fg = Font_color , bg = "grey", width = 7 )
    
    trs.place(x = 27 , y = 440 + 15)
    readbutton.place(x = 155 ,y = 395)
    btn_view_out.place(x = 27 , y = 440 + 80 - 20)

    def languagec() :
        global userlang
        langc = Tk()
        if 'Arabic' in userlang :
            langc.title("لغة البرنامج")
            lagcl1 = Label(langc , bg = '#202020' , fg = '#ffffff' , text = ': اختر لغة').place(x = 140 , y= 10)
        else :
            langc.title("App Language")
            lagcl1 = Label(langc , bg = '#202020' , fg = '#ffffff' , text = 'Select a language :').place(x = 10 , y= 10)

        langc.config(background = '#202020')
        langc.resizable(False,False)
        langc.geometry('200x150')
        langclist1 = ['Arabic' , 'Engish']
        langccom = ttk.Combobox(langc,values=langclist1)

        def langbtn1c():
            global userlang
            langc_var1 = langccom.get()
            if langc_var1 == 'Arabic' :
                userlang ='Arabic'
                menubar.entryconfigure(1,label = 'الغات المتوفرة')
                DataBaseMenu.entryconfigure(0,label = 'الاتصال بقاعدة بيانات ميكروسوفت')
                menubar.entryconfigure(2,label = 'تطبيقات اضافية')
                AppMenu.entryconfigure(0,label = 'منشئ قواعد البيانات')
                AppMenu.entryconfigure(1,label = 'محول النصوص الى ملفات صوتية')
                menubar.entryconfigure(3,label = 'عن المطور')
                aboutMenu.entryconfigure(0,label = 'عن المطور')
                aboutMenu.entryconfigure(1,label = 'لغة البرنامج')
                readbutton.config(text = 'نطق')
                trs.config(text = 'ترجمة الكلمة')
                btn_view_out.config(text = 'عرض الترجمة في مكان خارجي')
                mess2.place(x = 270 , y = 20)
                mess2.config(text = ': الترجمة')
                mess.config(text = " : ادخل الكلمة المراد ترجمتها")
                mess.place(x = 180 , y = 25)
                miclabel1.config(text = ": الى لغة")
                miccompo.config(width = 40)
                if (chose_language["text"] == "microsoft") :
                    miclabel1.place(x = 310 , y = 75)
                    miccompo.place(x = 23 , y = 75)
                miccompo.config(values=arlangs)
                copbtn.place(x = 244 , y = 100)
                copbtn.config(text = "نسخ الترجمة")

            elif langc_var1 == 'Engish' :
                userlang ='English'
                menubar.entryconfigure(1,label = 'Languages')
                DataBaseMenu.entryconfigure(0,label = 'Connect to a Microsoft database')
                menubar.entryconfigure(2,label = 'Other applications')
                AppMenu.entryconfigure(0,label = 'Database Editor')
                AppMenu.entryconfigure(1,label = 'Convert txt to mp3')
                menubar.entryconfigure(3,label = 'About')
                aboutMenu.entryconfigure(0,label = 'About the developer')
                aboutMenu.entryconfigure(1,label = 'App Language')
                readbutton.config(text = 'say')
                trs.config(text = 'Translate')
                btn_view_out.config(text = 'View word translation in an outdoor location')
                mess2.place(x = 15 , y = 20)
                mess2.config(text = 'Translate :')
                mess.config(text = "Enter a word to translate it :")
                mess.place(x = 15 , y = 25)  
                miclabel1.config(text = "To Language :")
                miccompo.config(width = 37)
                if (chose_language["text"] == "microsoft") :
                    miclabel1.place(x = 20 , y = 75)
                    miccompo.place(x = 111 , y = 75)
                miccompo.config(values=enlangs)
                copbtn.place(x = 27 , y = 100)
                copbtn.config(text = "copy")
            langc.destroy()

        langcbtn1 = ttk.Button(langc,text = 'OK',command = langbtn1c).place(x = 60 , y = 90)
        langccom.place(x = 28 , y = 50)
        langc.mainloop()
    
    if 'Arabic' in userlang :
        aboutMenu.add_command(label = 'لغة البرنامج' , command = languagec)
    else :
        aboutMenu.add_command(label = 'App Language' , command = languagec)
    app.mainloop()

except: 
    userlang = os.popen('systeminfo | findstr /B /C:"System Locale"').read()
    try:
        app.destroy()
    except :
        pass
    error_window = Tk()
    error_window.title("zezn Translate")  
    error_window.geometry("378x190")
    error_window.config(background= Theme_color) 
    error_window.resizable(False,False)
    app_name_e = Label(error_window,text = "zezn Translate" , bg = Theme_color , fg = Font_color , font=("Tajol",22))
    app_name_e.place(x = 20, y = 11)
    window_er = Frame(error_window, bg="#d4d4d4" , width=380 , height=548)
    window_er.place(x = 0 , y = 60)
    
    if 'Arabic' in userlang :
        message_e = Label(window_er,text = "حصل خطأ في شفرة التطبيق" , bg = "#d4d4d4" , fg = "#000000",font=("Tahoma" , 15))
        message_e.place(x = 65, y = 15)
        closeerror = Button(error_window, text = "حسناً" , command = error_window.destroy , height = 1 , font=('Tahoma',12) , fg = Font_color , bg = "grey", width = 13 )
        closeerror.place(x = 130 ,y = 130)
    else :
        message_e = Label(window_er,text = "An error occurred in the application code" , bg = "#d4d4d4" , fg = "#000000",font=("Tahoma" , 15))        
        message_e.place(x = 5, y = 15)

        closeerror = Button(error_window, text = "OK" , command = error_window.destroy , height = 1 , font=('Tahoma',12) , fg = Font_color , bg = "grey", width = 13 )
        closeerror.place(x = 130 ,y = 130)

    error_window.mainloop()