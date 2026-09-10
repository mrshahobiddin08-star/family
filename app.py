import streamlit as st
import pandas as pd
import os
from datetime import datetime

# Sahifa sozlamalari - Premium to'q yashil va oltin rangli dizayn
st.set_page_config(page_title="Raqamli Mahalla", page_icon="🏛️", layout="centered")

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
    .premium-reklama {
        background: linear-gradient(135deg, #151912, #0d110a); border: 3px solid #ffcc00;
        border-radius: 16px; padding: 30px; text-align: center; margin-top: 50px;
        box-shadow: 0 0 25px rgba(255, 204, 0, 0.4);
    }
    .reklama-badge {
        background-color: #ffcc00; color: #000; font-size: 12px; font-weight: 900;
        padding: 4px 12px; border-radius: 50px; text-transform: uppercase; display: inline-block; margin-bottom: 15px;
    }
    .premium-text { color: #ffffff; font-size: 18px; font-weight: 700; margin-bottom: 20px; }
    .premium-btn {
        display: inline-flex; align-items: center; justify-content: center; gap: 10px;
        padding: 14px 28px; border-radius: 10px; color: white !important; text-decoration: none !important;
        font-weight: 700; margin: 8px;
    }
    .btn-insta { background: linear-gradient(135deg, #f09433, #bc1888); }
    .btn-tg { background: linear-gradient(135deg, #229ED9, #0088cc); }
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='mahalla-header'><div class='mahalla-title'>🏛️ OLIY MAHALLA RAQAMLI PORTALI</div></div>", unsafe_allow_html=True)

# Ma'lumotlarni bepul va mustahkam CSV bazaga saqlash mantiqi
def save_data(name, phone, m_type, text):
    file_name = "murojaatlar_baza.csv"
    vaqt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    yangi_ariza = pd.DataFrame([[vaqt, name, phone, m_type, text]], columns=["Vaqt", "Ism Familiya", "Telefon", "Murojaat Turi", "Murojaat Matni"])
    
    if os.path.exists(file_name):
        yangi_ariza.to_csv(file_name, mode='a', header=False, index=False, encoding='utf-8')
    else:
        yangi_ariza.to_csv(file_name, mode='w', header=True, index=False, encoding='utf-8')

# Forma komponentlari
f_name = st.text_input("Ism va Familiyangiz:")
f_phone = st.text_input("Telefon raqamingiz:")
f_type = st.selectbox("Murojaat turi:", ["Mahalla obodonlashtirish", "Ijtimoiy yordam va nafaqalar", "Boshqa muammolar"])
f_text = st.text_area("Murojaat matni (Batafsil yozing):")

if st.button("Murojaatni Rasman Yuborish 🚀"):
    if f_name.strip() == "" or f_phone.strip() == "" or f_text.strip() == "":
        st.error("❌ Iltimos, barcha maydonlarni to'liq to'ldiring!")
    else:
        with st.spinner("Yuborilmoqda..."):
            # Ma'lumotni 100% kafolatli saqlash
            save_data(f_name, f_phone, f_type, f_text)
            st.balloons()
            st.success("✅ Murojaatingiz muvaffaqiyatli qabul qilindi va mahalla onlayn bazasiga rasman kiritildi!")

# 📊 KELIB TUSHGAN ARIZALARNI ARIZA EGASI KO'RISHI UCHUN PANELI
st.write("")
st.divider()
with st.expander("📊 Kelib tushgan onlayn murojaatlar ro'yxati (Baza)"):
    if os.path.exists("murojaatlar_baza.csv"):
        df = pd.read_csv("murojaatlar_baza.csv", encoding='utf-8')
        st.dataframe(df, use_container_width=True)
    else:
        st.info("Hozircha onlayn murojaatlar mavjud emas. Birinchi bo'lib arizani yuboring!")

# 📣 REKLAMA PANEL
st.markdown("""
<div class='premium-reklama'>
    <div class='reklama-badge'>Tijoriy Taklif 🔥</div>
    <div class='premium-text'>Sizga ham xuddi shunday turdagi zamonaviy, tezkor va avtomatlashtirilgan veb-saytlar yoki loyihalar kerakmi?</div>
    <div style='text-align: center;'>
        <a href='https://instagram.com' target='_blank' class='premium-btn btn-insta'>📸 Instagram: mr.shahobiddin5</a>
        <a href='https://t.me' target='_blank' class='premium-btn btn-tg'>✈️ Telegram: @matem_agent</a>
    </div>
</div>
""", unsafe_allow_html=True)
