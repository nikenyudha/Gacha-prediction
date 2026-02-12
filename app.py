import streamlit as st

# Pengaturan halaman
st.set_page_config(page_title="LADS Gacha Helper", page_icon="✨")

# Header dengan gaya yang menarik
st.title("✨ Love & Deepspace Gacha Strategist")
st.markdown("""
This app helps you decide: ***Is now the right time to pull?*** by calculating your chances based on the pity system and your recent card history.
""")

st.divider()

# --- SIDEBAR INPUT ---
st.sidebar.header("📊 Detail Account")

acc_name = st.sidebar.text_input("Account Name", "My Hunter Account")

# Input Pity yang lebih manusiawi
pity_input = st.sidebar.slider(
    "How many pulls have you done since your last 5-star?", 
    min_value=0, max_value=70, value=0,
    help="Check the in-game 'History` menu and count how many cards you've pulled since your last 5-star."
)

# Input Logika Spook (Revisi: Lebih Mudah Dipahami)
st.sidebar.subheader("Card History")
last_card = st.sidebar.radio(
    "What type of 5-star card did you get last?",
    (
        "LIMITED card (from the banner that was active at the time)", 
        "STANDARD / SPOOK card (card that is always in the permanent banner)"
    ),
    help="If the last 5-star card you got was from a limited banner, it's a LIMITED card. If it was from the permanent banner, it's a STANDARD/SPOOK card."
)

# Konversi input ke logika program
is_guaranteed = True if last_card == "STANDARD / SPOOK card (card that is always in the permanent banner)" else False

# --- LOGIKA ANALISIS ---
st.subheader(f"🔍 Stategic Analytic : {acc_name}")

def analyze_gacha(pity, guaranteed):
    # Fase Hard Pity
    if pity >= 65:
        status = "🔥 RED ZONE (Almost Guaranteed!)"
        color = "error" # Warna merah di Streamlit
        if guaranteed:
            advice = "IMITED CARD IS RIGHT IN FRONT OF YOU! You`re currently under a 100% guarantee. That limited card is definitely yours. Just make sure it`s truly the one you want and need!"
        else:
            advice = "Your chances of getting a 5-star are very high, but be careful! You're currently on a 50/50 status. There`s a chance you might get a standard/spook card"
    
    # Fase Soft Pity
    elif pity >= 50:
        status = "⚡ YELLOW ZONE (Increased Chances)"
        color = "warning"
        if guaranteed:
            advice = "Your chances of getting a 5-star are starting to rise, and you're guaranteed to get the limited card. Keep going!"
        else:
            advice = "Your chances are rising, but remember—you`re still on 50/50, which means there`s still a chance you`ll get a standard card."
            
    # Fase Hemat
    else:
        status = "💎 BLUE ZONE (Still Far)"
        color = "info"
        if guaranteed:
            advice = "Your status is safe (Limited Guarantee), but you`ll still need a lot of diamonds to reach pity."
        else:
            advice = "You`re currently on 50/50, and your pity is still low"
            
    return status, advice, color

status_text, advice_text, color_type = analyze_gacha(pity_input, is_guaranteed)

# --- TAMPILAN HASIL ---
# Menampilkan Status dalam kotak berwarna
if color_type == "error": st.error(status_text)
elif color_type == "warning": st.warning(status_text)
else: st.info(status_text)

st.write(advice_text)

# Visualisasi Progress Bar
st.write(f"**Pity Progress (70):** {pity_input}/70")
st.progress(pity_input / 70)

# Ringkasan Data
st.divider()
col1, col2 = st.columns(2)
with col1:
    st.metric("Probability Status", "100% Guaranteed" if is_guaranteed else "50/50 (Random)")
with col2:
    st.metric("Maximum Pulls Left", 70 - pity_input)

#st.caption("© 2026 Niken Larasati —  gacha game stategist💗")

st.markdown(
    "<hr style='margin-top:50px;'>"
    "<center style='color: gray;'>© 2026 Niken Larasati —  gacha game stategist💗</center>",
    unsafe_allow_html=True
)