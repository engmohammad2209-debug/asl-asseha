import tkinter as tk
from tkinter import scrolledtext

def get_smart_response(user_input):
    text = user_input.strip().lower()
    
    # 1. العنوان والموقع
    if any(w in text for w in ["عنوان", "موقع", "مكان", "وين", "فرع", "زيونة", "ربيعي", "مجمع"]):
        return ("📍 موقع شركة أصل الصحة للخدمات العلاجية:\n"
                "- بغداد - زيونة - شارع الربيعي - مجمع الليرة\n"
                "- هاتف التواصل: 07703305095\n"
                "- أوقات العمل: من الساعة 9:00 صباحاً حتى 8:00 مساءً")

    # 2. الدول والخدمات العلاجية
    elif any(w in text for w in ["خدمات", "تفاصيل", "سفر", "علاج", "دول", "هند", "تركيا", "مستشفى", "اطباء", "دكتور", "متابعة"]):
        return ("🏥 خدمات السفر العلاجي والدول المتاحة:\n"
                "نوفر رحلات علاجية متكاملة إلى أفضل مستشفيات (الهند / تركيا):\n"
                "• حجز أفضل المستشفيات والأطباء الاستشاريين المعتمدين.\n"
                "• استخراج الدعوات الطبية ومتابعة الفيزا.\n"
                "• استقبال من المطار ومترجم خاص يرافق المريض طوال فترة العلاج.\n"
                "• حجز الفنادق والسكن المناسب للمريض ومرافقيه.\n"
                "• متابعة دقيقة للمريض منذ وصوله إلى بلد العلاج وطوال فترة إقامته، وحتى بعد عودته إلى العراق بسلامة.")

    # 3. إرسال التقارير والأسعار
    elif any(w in text for w in ["سعر", "اسعار", "أسعار", "تكلفة", "عملية", "كشفية", "تقرير", "تحاليل", "رنين", "اشعة"]):
        return ("📋 لمعرفة تكلفة العلاج والعمليات:\n"
                "يرجى إرسال التقارير الطبية الخاصة بالمريض (صور أشعة، رنين، تحاليل حديثة).\n"
                "سيتم عرضها مباشرة على الأطباء الاختصاص في (الهند أو تركيا) لتزويدكم بالخطة العلاجية والتكلفة التقديرية بدقة خلال 24 ساعة.")

    # 4. التواصل عبر الواتساب
    elif any(w in text for w in ["واتساب", "واتس", "رقم", "تواصل", "خدمة", "مباشر", "اتصال", "هاتف"]):
        return ("📲 للتواصل المباشر وإرسال التقارير عبر الواتساب:\n"
                "- رقم الهاتف: 07703305095\n"
                "- رابط المحادثة المباشرة: https://wa.me/9647703305095\n"
                "فريق خدمة العملاء جاهز للإجابة على كافة استفساراتكم.")

    # 5. الترحيب والتحية
    elif any(w in text for w in ["هلا", "هلو", "السلام", "مرحبا", "سلام", "صباح", "مساء", "أهلا"]):
        return ("أهلاً وسهلاً بك في شركة أصل الصحة للخدمات العلاجية! 🌹\n"
                "كيف يمكننا مساعدتك اليوم؟ تفضل بطرح سؤالك مباشرة.")

    # 6. الخروج أو الشكر
    elif any(w in text for w in ["خروج", "شكرا", "شكراً", "مع السلامة", "باي"]):
        return "EXIT"

    # الرد الافتراضي
    else:
        return ("عذراً، لم أفهم استفسارك بدقة.\n"
                "يمكنك كتابة سؤالك بكلمات مثل:\n"
                "• موقع الشركة\n"
                "• خدمات العلاج بالخارج والمتابعة\n"
                "• التكلفة والتقارير الطبية\n"
                "• رقم الواتساب والتواصل")

def send_message(event=None):
    msg = entry_box.get().strip()
    if not msg:
        return
        
    chat_history.config(state=tk.NORMAL)
    chat_history.insert(tk.END, f"أنت: {msg}\n\n", "user")
    entry_box.delete(0, tk.END)
    
    response = get_smart_response(msg)
    if response == "EXIT":
        chat_history.insert(tk.END, "البوت: شكراً لتواصلك مع شركة أصل الصحة. نتمنى لك دوام الصحة والعافية! ❤️\n\n", "bot")
    else:
        chat_history.insert(tk.END, f"البوت:\n{response}\n\n", "bot")
        
    chat_history.config(state=tk.DISABLED)
    chat_history.yview(tk.END)

# إنشاء النافذة وتنسيق المظهر
root = tk.Tk()
root.title("شركة أصل الصحة - المساعد الذكي للخدمات العلاجية")
root.geometry("520x600")
root.configure(bg="#f4f6f9")

# منطقة المحادثة
chat_history = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Segoe UI", 10), bg="#ffffff", fg="#333333")
chat_history.pack(padx=12, pady=12, fill=tk.BOTH, expand=True)

chat_history.tag_config("user", foreground="#0056b3", justify="right", font=("Segoe UI", 10, "bold"))
chat_history.tag_config("bot", foreground="#1e7e34", justify="right")

welcome_msg = (
    "أهلاً بك في شركة أصل الصحة للخدمات العلاجية! 🏥\n"
    "اسألني مباشرة عن أي موضوع، مثل:\n\n"
    "🔹 موقع وعنوان الشركة\n"
    "🔹 الدول والخدمات العلاجية والمتابعة (الهند / تركيا)\n"
    "🔹 الاستفسار عن الأسعار وإرسال التقارير\n"
    "🔹 رقم الواتساب والتواصل المباشر\n"
    "--------------------------------------------------\n"
)
chat_history.insert(tk.END, welcome_msg, "bot")
chat_history.config(state=tk.DISABLED)

# إدخال النص والأزرار
entry_frame = tk.Frame(root, bg="#f4f6f9")
entry_frame.pack(padx=12, pady=(0, 12), fill=tk.X)

send_button = tk.Button(entry_frame, text="إرسال", command=send_message, bg="#007bff", fg="white", font=("Segoe UI", 10, "bold"), relief=tk.FLAT)
send_button.pack(side=tk.RIGHT, padx=(6, 0))

entry_box = tk.Entry(entry_frame, font=("Segoe UI", 11), justify="right", relief=tk.SOLID, bd=1)
entry_box.pack(side=tk.LEFT, fill=tk.X, expand=True, ipady=4)
entry_box.bind("<Return>", send_message)

root.mainloop()