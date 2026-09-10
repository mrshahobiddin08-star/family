import streamlit as st
import requests
from datetime import datetime

# Sahifa sozlamalari
st.set_page_config(page_title="Raqamli Mahalla", page_icon="🏛️", layout="centered")

# SOZLAMALAR - SHAXSIY PROFILGA 100% KAFOLATLANGAN SHAKLDA ULASH
BOT_TOKEN = "8850573618:AAFHnfum5nKAEUL-JPvcQX7Emp_raHKj-K0"
CHAT_ID = "6937805047"  # Shahobiddinning shaxsiy profil ID raqami

st.markdown("""
<style>
    /* Umumiy fon va mahalla uslubi */
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
        background-color: #0c1f13 !important; 
        border: 1px solid #1a4228 !important; 
        color: #fafafa !important;
    }
    
    div.stButton > button {
        background: linear-gradient(135deg, #4cd964, #28a745) !important;
        color: white !important; 
        font-weight: bold !important; 
        font-size: 18px !important; 
        width: 100%;
    }

    /* 🌟 DAXSHATLI PREMIUM NEON REKLAMA BLOKI 🌟 */
    .premium-reklama {
        background: linear-gradient(135deg, #151912, #0d110a);
        border: 3px solid #ffcc00;
        border-radius: 16px;
        padding: 30px;
        text-align: center;
        margin-top: 50px;
        box-shadow: 0 0 25px rgba(255, 204, 0, 0.4), inset 0 0 15px rgba(255, 204, 0, 0.1);
        position: relative;
        overflow: hidden;
    }
    
    .reklama-badge {
        background-color: #ffcc00;
        color: #000;
        font-size: 12px;
        font-weight: 900;
        padding: 4px 12px;
        border-radius: 50px;
        text-transform: uppercase;
        letter-spacing: 1px;
        display: inline-block;
        margin-bottom: 15px;
        box-shadow: 0 0 10px rgba(255, 204, 0, 0.5);
    }

    .premium-text {
        color: #ffffff;
        font-size: 18px;
        font-weight: 700;
        line-height: 1.6;
        margin-bottom: 20px;
        text-shadow: 0 0 8px rgba(255, 255, 255, 0.2);
    }
    
    .premium-subtext {
        color: #a2bca6;
        font-size: 15px;
        margin-bottom: 25px;
    }

    /* Premium Aloqa Tugmalari */
    .premium-btn {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        gap: 10px;
        padding: 14px 28px;
        border-radius: 10px;
        color: white !important;
        text-decoration: none !important;
        font-weight: 700;
        font-size: 15px;
        margin: 8px;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
    }
    
    .btn-insta {
        background: linear-gradient(135deg, #f09433 0%, #e6683c 25%, #dc2743 50%, #cc2366 75%, #bc1888 100%);
    }
    .btn-insta:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 25px rgba(220, 39, 67, 0.5);
    }

    .btn-tg {
        background: linear-gradient(135deg, #229ED9, #0088cc);
    }
    .btn-tg:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 25px rgba(0, 136, 204, 0.5);
    }
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='mahalla-header'><div class='mahalla-title'>🏛️ OLIY MAHALLA RAQAMLI PORTALI</div></div>", unsafe_allow_html=True)

def send_tg(name, phone, m_type, text):
    vaqt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    message = (
        f"🔔 *YANGI MUROJAAT REKORDI!* 🔔\n\n"
        f"👤 *Fuqaro:* {name}\n"
        f"📞 *Telefon:* {phone}\n"
        f"📂 *Murojaat turi:* {m_type}\n"
        f"📝 *Murojaat matni:* \n_{text}_\n\n"
        f"📅 *Vaqt:* {vaqt}"
    )
    url = f"https://telegram.org{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": int(CHAT_ID), "text": message, "parse_mode": "Markdown"}
    try:
        r = requests.post(url, data=payload)
        return r.status_code == 200
    except:
        return False

# Forma komponentlari
f_name = st.text_input("Ism va Familiyangiz:")
f_phone = st.text_input("Telefon raqamingiz:")
f_type = st.selectbox("Murojaat turi:", ["Mahalla obodonlashtirish", "Ijtimoiy yordam va nafaqalar", "Boshqa muammolar"])
f_text = st.text_area("Murojaat matni (Batafsil yozing):")

if st.button("Murojaatni Rasman Yuborish 🚀"):
    if f_name.strip() == "" or f_phone.strip() == "" or f_text.strip() == "":
        st.error("❌ Iltimos, barcha maydonlarni to'ldiring!")
    else:
        with st.spinner("Yuborilmoqda..."):
            status = send_tg(f_name, f_phone, f_type, f_text)
            if status:
                st.balloons()
                st.success("✅ Murojaatingiz muvaffaqiyatli qabul qilindi va mahalla tizimiga rasman uzatildi!")
            else:
                st.error("❌ Xatolik yuz berdi. Iltimos, botingizga Telegramda /start berganingizni tekshiring.")

# 📣 🌟 YANGILANGAN EKLYUZIV PREMIUM REKLAMA PANEL 🌟
st.markdown("""
<div class='premium-reklama'>
    <div class='reklama-badge'>Tijoriy Taklif 🔥</div>
    <div class='premium-text'>
        Sizga ham xuddi shunday turdagi zamonaviy, tezkor va avtomatlashtirilgan veb-saytlar yoki Telegram botlar kerakmi?
    </div>
    <div class='premium-subtext'>
        Murojaat qiling! Istalgan murakkablikdagi loyihalarni <b>eng hamyonbop narxlarda</b> va qisqa muddatda tayyorlab beramiz.
    </div>
    <div style='text-align: center;'>
        <a href='https://instagram.com' target='_blank' class='premium-btn btn-insta'>
            📸 Instagram: mr.shahobiddin5
        </a>
        <a href='https://t.me' target='_blank' class='premium-btn btn-tg'>
            ✈️ Telegram: @matem_agent
        </a>
    </div>
</div>
""", unsafe_allow_html=True)
