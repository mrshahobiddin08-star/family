import streamlit as st
import requests
import json
import os
from datetime import datetime

# Sahifa sozlamalari
st.set_page_config(page_title="Raqamli Mahalla", page_icon="🏛️", layout="centered")

# Streamlit Secrets-dan ma'lumotlarni xavfsiz o'qish
try:
    BOT_TOKEN = st.secrets["telegram"]["bot_token"]
    CHAT_ID = st.secrets["telegram"]["chat_id"]
except:
    # Agar secrets o'qilmasa, kod ichidagidan foydalanish (Zaxira)
    BOT_TOKEN = "8850573618:AAFHnfum5nKAEUL-JPvcQX7Emp_raHKj-K0"
    CHAT_ID = "-1004373849569"

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
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='mahalla-header'><div class='mahalla-title'>🏛️ OLIY MAHALLA RAQAMLI PORTALI</div></div>", unsafe_allow_html=True)

def send_tg(name, phone, m_type, text):
    vaqt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    message = f"🔔 *YANGI MUROJAAT!* 🔔\n\n👤 *Fuqaro:* {name}\n📞 *Telefon:* {phone}\n📂 *Turi:* {m_type}\n📝 *Matni:* \n_{text}_"
    url = f"https://telegram.org{BOT_TOKEN}/sendMessage"
    try:
        r = requests.post(url, json={"chat_id": CHAT_ID, "text": message, "parse_mode": "Markdown"})
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
        status = send_tg(f_name, f_phone, f_type, f_text)
        if status:
            st.balloons()
            st.success("✅ Murojaatingiz guruhga muvaffaqiyatli yuborildi!")
        else:
            st.error("❌ Botga yuborishda xatolik. Guruhda bot admin ekanligini tekshiring!")
