import streamlit as st

# Sayt sarlavhasi va sozlamalari
st.set_page_config(page_title="Bizning Baxtli Oilamiz", page_icon="👨‍👩‍👧‍👦", layout="centered")

# Bosh sahifa matnlari
st.title("👨‍👩‍👧‍👦 Bizning Baxtli Oilamizga Xush Kelibsiz!")
st.write("Bu bizning internetdagi ilk oilaviy rasmiy saytimiz!")

st.header("❤️ Bizning maqsadimiz")
st.write("Bir-birimizni qo'llab-quvvatlash, hamisha birga bo'lish va baxtli xotiralarni jamlash.")

# Aloqa yoki tilaklar bo'limi
st.subheader("✍️ Oilamizga o'z tilaklaringizni yozib qoldiring:")
user_wish = st.text_input("Sizning ismingiz va tilagingiz:")

if st.button("Yuborish"):
    if user_wish:
        st.success(f"Rahmat! Sizning tilagingiz qabul qilindi: '{user_wish}'")
    else:
        st.warning("Iltimos, avval tilakni yozing.")  
