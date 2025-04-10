import streamlit as st
import time

st.set_page_config(page_title="Bunk Calculator", page_icon="🎓", layout="centered")

with st.container():
    st.markdown("""
        <style>
            .main {
                background-color: #f8f9fa;
                padding: 30px;
                border-radius: 15px;
                box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.1);
                font-family: 'Segoe UI', sans-serif;
            }
            .stButton>button {
                border-radius: 10px;
                font-weight: bold;
            }
            footer {visibility: hidden;}
        </style>
    """, unsafe_allow_html=True)

    st.markdown("<h1 style='text-align: center;'>📊 Smart Bunk Calculator</h1>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center; color: gray;'>Stay above 75% — without doing the math</h4>", unsafe_allow_html=True)

    st.divider()

    total_classes = st.number_input("📘 Total Classes Conducted", min_value=1)
    attended_classes = st.number_input("✅ Classes Attended", min_value=0, max_value=total_classes)

    if total_classes > 0:
        percentage = (attended_classes / total_classes) * 100
        st.markdown(f"### 🎯 Your Attendance: **{percentage:.2f}%**")

        st.progress(min(int(percentage), 100))

        if percentage >= 75:
            safe_bunks = int(((attended_classes / 0.75) - total_classes))
            st.success(f"✨ You're safe! You can bunk **{safe_bunks}** more class(es).")
        else:
            required = int(((0.75 * total_classes) - attended_classes))
            st.warning(f"⚠️ Attend at least **{required}** more class(es) to reach 75%.")

