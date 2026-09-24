import streamlit as st
from datetime import datetime
import os
import random
import time

# 1. Page Configuration
st.set_page_config(
    page_title="Happy Birthday Jasra! 💖",
    page_icon="💌",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 2. Custom CSS
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,500;1,600&family=Dancing+Script:wght@600&display=swap');

html, body, [class*="css"] { font-family: 'Playfair Display', serif; }
#MainMenu {visibility: hidden;} footer {visibility: hidden;} header {visibility: hidden;}

.stApp { background: linear-gradient(160deg, #fff5f7 0%, #ffe9ef 45%, #ffe0ec 100%); }

/* Floating hearts */
.hearts { position: fixed; top: 0; left: 0; width: 100%; height: 100%; overflow: hidden; pointer-events: none; z-index: 0; }
.heart { position: absolute; bottom: -50px; font-size: 1.6rem; opacity: 0.55; animation: rise linear infinite; }
@keyframes rise { 0% { transform: translateY(0) rotate(0deg); opacity: 0; } 10% { opacity: 0.6; } 100% { transform: translateY(-110vh) rotate(360deg); opacity: 0; } }

.glow-title {
    text-align: center; font-family: 'Dancing Script', cursive; font-size: 4.5rem; font-weight: 700;
    background: -webkit-linear-gradient(45deg, #d6416a, #ff9a9e, #d6416a); background-size: 200% 200%;
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    animation: pulse 3s ease-in-out infinite, shimmer 5s ease infinite; margin-bottom: 5px; margin-top: -30px;
}
@keyframes pulse { 0%, 100% { transform: scale(1); } 50% { transform: scale(1.04); } }
@keyframes shimmer { 0% { background-position: 0% 50%; } 50% { background-position: 100% 50%; } 100% { background-position: 0% 50%; } }

.subtitle { text-align: center; font-size: 1.3rem; color: #b5556b; font-style: italic; margin-top: -10px; }

/* FIXED TIMER FONT COLORS */
div[data-testid="stMetric"] {
    background: rgba(255, 255, 255, 0.7); backdrop-filter: blur(10px);
    border: 1px solid rgba(255, 111, 145, 0.4); border-radius: 20px; padding: 15px 10px; text-align: center;
    box-shadow: 0 4px 15px rgba(255, 111, 145, 0.15); transition: transform 0.3s ease;
}
div[data-testid="stMetric"]:hover { transform: translateY(-5px); }
[data-testid="stMetricLabel"], [data-testid="stMetricLabel"] p, [data-testid="stMetricLabel"] div, [data-testid="stMetricLabel"] span {
    color: #b5556b !important; font-size: 1.2rem !important; font-weight: 600 !important;
}
[data-testid="stMetricValue"], [data-testid="stMetricValue"] div {
    color: #d6416a !important; font-weight: 700 !important; font-size: 2.5rem !important;
}

/* FIX EXPANDER (PROMISES) & SPINNER (AUTHENTICATION) FONT COLORS */
div[data-testid="stExpander"] details summary p {
    color: #d6416a !important;
    font-size: 1.1rem !important;
    font-weight: 600 !important;
}
div[data-testid="stExpander"] details div p {
    color: #444444 !important;
    line-height: 1.6 !important;
}
div[data-testid="stSpinner"] * {
    color: #d6416a !important;
    font-weight: 600 !important;
    font-size: 1.1rem !important;
}

h2, h3 { color: #d6416a !important; text-align: center; }
hr { border: 0; height: 2px; background-image: linear-gradient(to right, rgba(0,0,0,0), rgba(255, 111, 145, 0.6), rgba(0,0,0,0)); margin: 2em 0; }

/* THE UNFOLDING BOARDING PASS */
.boarding-pass {
    background: #ffffff; border-left: 10px solid #d6416a; border-radius: 12px; padding: 25px;
    box-shadow: 0 15px 35px rgba(214, 65, 106, 0.2); animation: unfold 0.8s cubic-bezier(0.175, 0.885, 0.32, 1.275) forwards;
    transform-origin: top; margin: 20px 0;
}
@keyframes unfold { 0% { transform: scaleY(0) translateY(-20px); opacity: 0; } 100% { transform: scaleY(1) translateY(0); opacity: 1; } }
.ticket-header { color: #b5556b; font-weight: bold; font-size: 1.1rem; text-transform: uppercase; letter-spacing: 2px; border-bottom: 1px dashed #ff9a9e; padding-bottom: 10px; margin-bottom: 15px;}
.ticket-route { display: flex; justify-content: space-between; align-items: center; font-size: 1.5rem; color: #d6416a; font-weight: bold; margin-bottom: 15px;}
.ticket-details { font-size: 1.2rem; color: #555; }
.highlight-date { font-family: 'Dancing Script', cursive; font-size: 2.2rem; color: #d6416a; display: block; text-align: center; margin-top: 15px; text-shadow: 1px 1px 2px rgba(214,65,106,0.1);}

/* Reveal button */
div.stButton { display: flex; justify-content: center; }
div.stButton > button {
    background: linear-gradient(45deg, #ff6f91, #ff9a9e); color: white; border: none; border-radius: 30px;
    padding: 12px 30px; font-size: 1.1rem; font-weight: 600; box-shadow: 0 4px 12px rgba(255, 111, 145, 0.4); transition: all 0.3s ease;
}
div.stButton > button:hover { transform: scale(1.05); box-shadow: 0 6px 18px rgba(255, 111, 145, 0.6); color: white;}
</style>
""", unsafe_allow_html=True)

# Floating hearts
hearts_html = '<div class="hearts">'
heart_emojis = ["💖", "💕", "💗", "✨", "💝", "✈️"]
for i in range(25):
    left = random.randint(0, 100)
    duration = random.randint(8, 20)
    delay = random.randint(0, 12)
    size = random.uniform(1.0, 2.5)
    emoji = random.choice(heart_emojis)
    hearts_html += f'<span class="heart" style="left:{left}%; font-size:{size}rem; animation-duration:{duration}s; animation-delay:{delay}s;">{emoji}</span>'
hearts_html += '</div>'
st.markdown(hearts_html, unsafe_allow_html=True)

# 3. Initialize Session States 
if "surprise_stage" not in st.session_state:
    st.session_state.surprise_stage = 0
if "reason" not in st.session_state:
    st.session_state.reason = "தூரங்கள் நம்மைப் பிரித்தாலும், என் காதல் உன்னைச் சுற்றியே வாழ்கிறது."

st.balloons()

# 4. Header
st.markdown('<div class="glow-title">Happy Birthday, Laddu! 🎂</div>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">A little corner of the internet, made just for you.</p>', unsafe_allow_html=True)
st.divider()

# 5. The Wedding Countdown
st.header("The Timer ⏳")
wedding_date = datetime(2027, 12, 5)
today = datetime.now()
wedding_days_left = (wedding_date - today).days

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if wedding_days_left > 0:
        st.metric(label="Days until 'I Do' 💍", value=f"{wedding_days_left}")

st.divider()

# 6. The Interactive Unfolding Surprise 
st.header("A Secret For You 💌")

if st.session_state.surprise_stage == 0:
    st.markdown("<p style='text-align:center; color:#b5556b;'>I've been hiding something from you. It's locked safely away.</p>", unsafe_allow_html=True)
    if st.button("Tap to unlock the envelope ✉️"):
        st.session_state.surprise_stage = 1
        st.rerun()

elif st.session_state.surprise_stage == 1:
    st.markdown("<p style='text-align:center; color:#b5556b;'>Are you sure you're ready for this?</p>", unsafe_allow_html=True)
    if st.button("Yes, I'm ready ✨"):
        st.session_state.surprise_stage = 2
        st.rerun()

elif st.session_state.surprise_stage == 2:
    st.markdown("<p style='text-align:center; color:#b5556b;'>Bypassing firewalls and verifying passenger identity...</p>", unsafe_allow_html=True)
    with st.spinner("Authenticating Dr. N.A. Fathima Jasra, PT..."):
        time.sleep(5)
    if st.button("Identity Confirmed. Open Ticket ✈️"):
        st.session_state.surprise_stage = 3
        st.rerun()

elif st.session_state.surprise_stage == 3:
    arrival_date = datetime(2026, 10, 3, 4, 20)  
    td_arrival = arrival_date - today
    arr_days = td_arrival.days
    arr_hours = td_arrival.seconds // 3600
    
    vid_path = "images/anime_message.mp4"
    if os.path.exists(vid_path):
        st.video(vid_path)

    st.markdown(f"""
    <div class="boarding-pass">
        <div class="ticket-header">✨ CONFIRMED PASSENGER: YOUR MACHAN</div>
        <div class="ticket-route">
            <span>SIN 🇸🇬</span>
            <span>➔ ✈️ ➔</span>
            <span>TRZ 🇮🇳</span>
        </div>
        <div class="ticket-details">
            <p><strong>Passenger:</strong> Mohamed Tharik</p>
            <p><strong>Status:</strong> Coming to see his fiancé</p>
            <p style="color:#d6416a; font-weight:bold;">Time remaining: {arr_days} Days, {arr_hours} Hours</p>
        </div>
        <span class="highlight-date">Landing: October 3rd @ 4:20 AM</span>
        <p style="text-align:center; margin-top:10px; font-style:italic; color:#b5556b;">The countdown is officially on. See you soon, Laddu.</p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("Hide Ticket 🤫"):
        st.session_state.surprise_stage = 0
        st.rerun()

st.divider()

# 7. Digital Promises
st.header("Digital Promises 🔐")
st.markdown("<p style='text-align:center; color:#b5556b; margin-top:-10px;'>Tap the secure packets to decrypt them.</p>", unsafe_allow_html=True)

with st.expander("Promise 01: The Distance"):
    st.write("I promise that no matter how many miles are between SIN and TRZ right now, I will always make it feel like I'm right next to you.")
with st.expander("Promise 02: The Daily Updates"):
    st.write("I promise to keep listening to every single detail of your day, especially the parts where you rant about the little things.")
with st.expander("Promise 03: Your Favorite Patient"):
    st.write("I promise to be your willing test subject for new physiotherapy techniques, let you fix my sore muscles after my Anytime Fitness sessions, and make sure you rest just as much as you help others heal.")

st.divider()

# 8. Reasons I Love You (Tamil Kavithai)
st.header("என் கவிதைக்கு கவிதைகள் 💌")
reasons = [
    "தூரங்கள் நம்மைப் பிரித்தாலும், என் காதல் உன்னைச் சுற்றியே வாழ்கிறது.",
    "உன் குறுநகை போதும், என் ஆயிரம் வலிகளை மறக்க.",
    "நீ என் வாழ்வில் வந்த பிறகு தான், என் ஒவ்வொரு நாளும் பண்டிகையானது.",
    "என் அலைபேசி திரையில் உன் முகம் காணும் நொடிகள் தான் என் நாளின் அழகிய கவிதைகள்.",
    "உன் அன்பான வார்த்தைகளில் தான் என் ஒட்டுமொத்த உலகமும் அடங்கியுள்ளது.",
    "என் தனிமையின் இனிமை நீ, என் தேடலின் முகவரி நீ.",
    "கண்கள் மூடினாலும் உன் முகம், நெஞ்சம் திறந்தாலும் உன் நிஜம்."
]

if st.button("💗 Tap for another line"):
    st.session_state.reason = random.choice(reasons)
    st.toast("I mean every word! 🥰", icon="💌")

st.markdown(
    f"<div style='background: rgba(255, 255, 255, 0.5); padding: 20px; border-radius: 15px; margin-top: 15px; box-shadow: 0 4px 10px rgba(0,0,0,0.05);'>"
    f"<p style='text-align:center; font-size:1.4rem; color:#b5556b; font-style:italic; margin: 0;'>“{st.session_state.reason}”</p>"
    f"</div>",
    unsafe_allow_html=True
)

st.divider()

# 9. The Gallery
st.header("The Birthday Girl 📸")
st.markdown("<p style='text-align: center; color: #b5556b;'>Hover over the photos to see them come to life.</p>", unsafe_allow_html=True)

img_dir = "images"
if os.path.exists(img_dir):
    valid_extensions = [".jpg", ".jpeg", ".png", ".webp"]
    image_files = [f for f in os.listdir(img_dir) if any(f.lower().endswith(ext) for ext in valid_extensions)]
    if image_files:
        cols = st.columns(2)
        for index, img_file in enumerate(image_files):
            with cols[index % 2]:
                st.image(os.path.join(img_dir, img_file), use_container_width=True)

st.divider()

st.markdown("<h3 style='text-align: center; color: #d6416a;'>I love you more than words fit on a screen. Have the best birthday, Laddu! ❤️</h3>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#c98a9a; font-size:1rem; font-style: italic;'>made with love (and a bit of Python) — see you October 3rd 💫</p>", unsafe_allow_html=True)
