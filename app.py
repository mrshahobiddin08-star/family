import streamlit as st
import requests
from datetime import datetime

# Sahifa sozlamalari
st.set_page_config(page_title="Raqamli Mahalla", page_icon="🏛️", layout="centered")

# SOZLAMALAR - TO'G'RIDAN-TO'G'RI KOD ICHIDA
BOT_TOKEN = "8850573618:AAFHnfum5nKAEUL-JPvcQX7Emp_raHKj-K0"
CHAT_ID = "-1004373849569"  # Guruh ID raqami

st.markdown("""
<style>
    .stApp { background: linear-gradient(135deg, #0b1a10, #050d08); }
    .mahalla-header {
        background: linear-gradient(145deg, #112d1b, #0c1f13);
        border: 2px solid #1a4228;
        border-radius: 15px;
        padding: 30px;
        text-align: center;
        margin-bottom: 30px;
    }
    .mahalla-title { color: #4cd964; font-size: 2.2rem; font-weight: 800; }
    .stTextInput input, .stTextArea textarea, .stSelectbox div[data-baseweb="select"] {
        background-color: #0c1f13 !important; border: 1px solid #1a4228 !important; color: #fafafa !important;
    }
    div.stButton > button {
        background: linear-gradient(135deg, #4cd964, #28a745) !important;
        color: white !important; font-weight: bold !important; font-size: 18px !important; width: 100%;
    }
    
    /* REKLAMA BLOCKI UCHUN MAXSUS NEON USLUB */
    .reklama-box {
        background: linear-gradient(145deg, #1f1c11, #14120a);
        border: 2px dashed #d4af37; /* Oltin rangli chiziqli ramka */
        border-radius: 12px;
        padding: 20px;
        text-align: center;
        margin-top: 40px;
        box-shadow: 0 0 15px rgba(212, 175, 55, 0.2);
    }
    .reklama-text {
        color: #fafafa;
        font-size: 15px;
        line-height: 1.6;
        margin-bottom: 15px;
    }
    .reklama-link {
        display: inline-block;
        padding: 8px 16px;
        border-radius: 6px;
        color: white !important;
        text-decoration: none !important;
        font-weight: bold;
        margin: 5px;
        font-size: 14px;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='mahalla-header'><div class='mahalla-title'>🏛️ OLIY MAHALLA RAQAMLI PORTALI</div></div>", unsafe_allow_html=True)

def send_tg(name, phone, m_type, text):
    vaqt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    message = (
        f"🔔 YANGI MUROJAAT! 🔔\n\n"
        f"👤 Fuqaro: {name}\n"
        f"📞 Telefon: {phone}\n"
        f"📂 Turi: {m_type}\n"
        f"📝 Matni: {text}\n\n"
        f"📅 Vaqt: {vaqt}"
    )
    
    url = f"https://telegram.org{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": int(CHAT_ID),
        "text": message
    }
    
    try:
        r = requests.post(url, data=payload)
        return r.status_code == 200
    except:
        return False

# Forma
f_name = st.text_input("Ism va Familiyangiz:")
f_phone = st.text_input("Telefon raqamingiz:")
f_type = st.selectbox("Murojaat turi:", ["Mahalla obodonlashtirish", "Ijtimoiy yordam", "Boshqa muammolar"])
f_text = st.text_area("Murojaat matni:")

if st.button("Murojaatni Rasman Yuborish 🚀"):
    if f_name.strip() == "" or f_phone.strip() == "" or f_text.strip() == "":
        st.error("❌ Maydonlarni to'ldiring!")
    else:
        with st.spinner("Yuborilmoqda..."):
            status = send_tg(f_name, f_phone, f_type, f_text)
            if status:
                st.balloons()
                st.success("✅ Murojaatingiz guruhga muvaffaqiyatli yuborildi!")
            else:
                st.error("❌ Xatolik yuz berdi. Iltimos, qayta urinib ko'ring.")

# 📣 REKLAMA BO'LIMI (SAYTNING ENG PASTIDA CHIROYLI KO'RINADI)
st.markdown("""
<div class='reklama-box'>
    <p class='reklama-text'>
        💡 <b>Sizga ham shunday turdagi zamonaviy veb-saytlar yoki Telegram botlar kerakmi?</b><br>
        Murojaat qiling, xizmatlar juda <b>hamyonbop narxlarda</b> va yuqori sifatda ko'rsatiladi!
    </p>
    <a href='https://instagram.com' target='_blank' class='reklama-link' style='background-color: #e1306c;'>📸 Instagram: mr.shahobiddin5</a>
    <a href='https://t.me' target='_blank' class='reklama-link' style='background-color: #0088cc;'>✈️ Telegram: @matem_agent</a>
</div>
""", unsafe_allow_html=True)
