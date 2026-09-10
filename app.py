import streamlit as st
import requests
import json
import os
from datetime import datetime

# Telegram bot sozlamalari (O'zingizning botingiz ma'lumotlari)
TELEGRAM_BOT_TOKEN = "8850573618:AAFHnfum5nKAEUL-JPvcQX7Emp_raHKj-K0"
TELEGRAM_CHAT_ID = "-1004373849569"


# Sahifa sozlamalari - Milliy zamonaviy dizayn
st.set_page_config(page_title="Raqamli Mahalla - Murojaatlar Tizimi", page_icon="🏛️", layout="centered")

# Maxsus CSS va JavaScript effektlari (To'q yashil va oltin ranglar uyg'unligi + Klaviatura tovushlari)
st.markdown("""
<style>
    /* Umumiy fon va mahalla muhitiga mos ranglar */
    .stApp {
        background: linear-gradient(135deg, #0b1a10, #050d08);
    }
    
    /* Chiroyli sarlavha paneli */
    .mahalla-header {
        background: linear-gradient(145deg, #112d1b, #0c1f13);
        border: 2px solid #1a4228;
        border-radius: 15px;
        padding: 30px;
        text-align: center;
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
        margin-bottom: 30px;
    }
    
    .mahalla-title {
        color: #4cd964;
        font-size: 2.2rem;
        font-weight: 800;
        margin-bottom: 10px;
        text-shadow: 0 0 15px rgba(76, 217, 100, 0.4);
    }
    
    .mahalla-subtitle {
        color: #d4af37; /* Oltin rang */
        font-size: 1.1rem;
        font-weight: 500;
    }
    
    /* Inputlar va Textarea uslubi */
    .stTextInput input, .stTextArea textarea, .stSelectbox div[data-baseweb="select"] {
        background-color: #0c1f13 !important;
        border: 1px solid #1a4228 !important;
        color: #fafafa !important;
        border-radius: 8px !important;
        padding: 12px !important;
    }
    
    .stTextInput input:focus, .stTextArea textarea:focus {
        border-color: #4cd964 !important;
        box-shadow: 0 0 10px rgba(76, 217, 100, 0.3) !important;
    }

    /* Professional Yuborish tugmasi */
    div.stButton > button {
        background: linear-gradient(135deg, #4cd964, #28a745) !important;
        color: white !important;
        font-weight: bold !important;
        font-size: 18px !important;
        padding: 14px 28px !important;
        border-radius: 10px !important;
        border: none !important;
        box-shadow: 0 5px 20px rgba(76, 217, 100, 0.4) !important;
        transition: all 0.3s ease !important;
        width: 100%;
    }
    
    div.stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 8px 25px rgba(76, 217, 100, 0.6) !important;
        background: linear-gradient(135deg, #5ce675, #34b953) !important;
    }
</style>

<!-- Klaviatura va bosish tovushlari (Audio effekt) uchun JavaScript -->
<script>
    // Maxsus chiroyli click va yozish tovushlari uchun audio ob'ektlari
    const typeSound = new Audio('https://mixkit.co');
    const clickSound = new Audio('https://mixkit.co');
    
    typeSound.volume = 0.2;
    clickSound.volume = 0.5;

    // Saytdagi barcha yozish maydonlariga audio ulash
    document.addEventListener('input', function(e) {
        if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA') {
            typeSound.currentTime = 0;
            typeSound.play().catch(err => console.log("Audio yoqilmadi"));
        }
    });

    // Tugma bosilganda chiroyli tovush chiqarish
    document.addEventListener('click', function(e) {
        if (e.target.tagName === 'BUTTON' || e.target.closest('button')) {
            clickSound.currentTime = 0;
            clickSound.play().catch(err => console.log("Audio yoqilmadi"));
        }
    });
</script>
""", unsafe_allow_html=True)

# TEPADAGI MULTIMEDIALI INTERFEYS
st.markdown("""
<div class='mahalla-header'>
    <div class='mahalla-title'>🏛️ OLIY MAHALLA RAQAMLI PORTALI</div>
    <div class='mahalla-subtitle'>Fuqarolar murojaatlari, takliflari va muammolarini onlayn qabul qilish tizimi</div>
</div>
""", unsafe_allow_html=True)

# Ma'lumotlarni Telegramga yuborish funksiyasi
def send_murojaat_telegram(name, phone, m_type, text):
    vaqt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    message = (
        f"🔔 *YANGI MUROJAAT KELIB TUSHDI!* 🔔\n\n"
        f"📅 *Vaqt:* {vaqt}\n"
        f"👤 *Fuqaro:* {name}\n"
        f"📞 *Telefon:* {phone}\n"
        f"📂 *Murojaat turi:* {m_type}\n\n"
        f"📝 *Murojaat matni:* \n_{text}_"
    )
    url = f"https://telegram.org{TELEGRAM_BOT_TOKEN}/sendMessage"
    try:
        requests.post(url, json={"chat_id": TELEGRAM_CHAT_ID, "text": message, "parse_mode": "Markdown"})
        return True
    except:
        return False

# Ma'lumotlarni Bepul Bazaga (GitHub ichidagi maxsus faylga) saqlash mantiqi
def save_to_database(name, phone, m_type, text):
    vaqt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    yangi_data = {"vaqt": vaqt, "ism_familiya": name, "telefon": phone, "murojaat_turi": m_type, "matn": text}
    
    file_name = "murojaatlar_baza.json"
    data_list = []
    
    if os.path.exists(file_name):
        try:
            with open(file_name, "r", encoding="utf-8") as f:
                data_list = json.load(f)
        except:
            data_list = []
            
    data_list.append(yangi_data)
    
    with open(file_name, "w", encoding="utf-8") as f:
        json.dump(data_list, f, ensure_ascii=False, indent=4)

# ANKETA FORMASI
with st.container():
    st.markdown("<p style='color: #4cd964; font-weight: 600; font-size: 18px;'>📝 Murojaat shaklini to'ldiring:</p>", unsafe_allow_html=True)
    
    f_name = st.text_input("Ism va Familiyangiz:", placeholder="Masalan: Abdullayev Jamshid")
    f_phone = st.text_input("Telefon raqamingiz:", placeholder="Masalan: +998 90 123 45 67")
    
    f_type = st.selectbox(
        "Murojaat yoki taklif turi:",
        [
            "Mahalla obodonlashtirish (Yo'l, Svet, Gaz, Suv)",
            "Ijtimoiy yordam va nafaqalar",
            "Tadbirkorlik yoki Yoshlar tashabbusi",
            "Mahalla raisiga shaxsiy taklif/shikoyat",
            "Boshqa muammolar"
        ]
    )
    
    f_text = st.text_area("Murojaat yoki taklifingiz matni (Batafsil yozing):", placeholder="Muammo yoki taklifingizni bu yerga qoldiring...")
    
    st.write("")
    
    # YUBORISH TUGMASI
    if st.button("Murojaatni Rasman Yuborish 🚀"):
        if f_name.strip() == "" or f_phone.strip() == "" or f_text.strip() == "":
            st.error("❌ Iltimos, barcha maydonlarni to'liq to'ldiring!")
        else:
            with st.spinner("Murojaat tizimga kiritilmoqda..."):
                # Telegramga yuborish
                tg_status = send_murojaat_telegram(f_name, f_phone, f_type, f_text)
                # Bazaga (GitHub'ga) saqlash
                save_to_database(f_name, f_phone, f_type, f_text)
                
                if tg_status:
                    st.balloons()
                    st.success("✅ Murojaatingiz muvaffaqiyatli qabul qilindi! Mahalla mas'ul xodimi va Telegram botga rasman yetkazildi.")
                else:
                    st.warning("⚠️ Murojaat bazaga saqlandi, biroq botga yuborishda xatolik yuz berdi.")

# ADMIN PANEL (Faqat loyiha egasi arizalarni saytning o'zida ko'rishi uchun qulaylik)
st.write("")
st.divider()
with st.expander("📊 Kelib tushgan murojaatlar ro'yxati (Admin uchun)"):
    if os.path.exists("murojaatlar_baza.json"):
        with open("murojaatlar_baza.json", "r", encoding="utf-8") as f:
            baza_read = json.load(f)
            st.json(baza_read)
    else:
        st.info("Hozircha hech qanday onlayn murojaatlar mavjud emas.")
