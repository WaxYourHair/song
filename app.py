import streamlit as st
import time

# Konfigurasi Halaman
st.set_page_config(page_title="LANY - Soft Lyrics", page_icon="🎵")

# Definisi Warna HEX (Menggantikan ANSI)
PINK = "#FFB6C1"
CYAN = "#00FFFF"
WHITE = "#FFFFFF"

# Styling CSS
st.markdown(f"""
    <style>
    .lyric-box {{
        font-size: 32px;
        text-align: center;
        margin-top: 100px;
        font-family: 'Serif';
        transition: all 0.5s ease;
    }}
    .stButton>button {{
        width: 100%;
        border-radius: 20px;
    }}
    </style>
""", unsafe_allow_html=True)

def lany_soft_lyrics():
    st.title("🎵 LANY - Soft")
    
    # Audio Player
    try:
        audio_file = open("Soft - LANY.mp3", "rb")
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format="audio/mp3")
    except FileNotFoundError:
        st.error("File 'Soft - LANY.mp3' tidak ditemukan. Pastikan file ada di folder yang sama.")
        return

    st.info("Petunjuk: Klik 'Play' pada pemutar musik di atas, lalu SEGERA klik tombol 'Mulai Lirik' di bawah.")
    
    if st.button("Mulai Lirik Sinkron"):
        # Format: [Menit, Detik, Lirik, Warna]
        lyrics = [
            [0, 14.39, "I've never been so high", PINK],
            [0, 19.75, "From sitting here just looking at you", PINK],
            [0, 25.13, "I'm swimming in your eyes", CYAN],
            [0, 30.47, "I'd let you drown me if you want to", CYAN],
            [0, 34.78, "You're the only light", WHITE],
            [0, 38.82, "Left in the room", WHITE],
            [0, 41.13, "How is it that I", WHITE],
            [0, 44.10, "Get to be the one that gets to?", WHITE],
            [0, 49.46, "Take you upstairs", PINK],
            [0, 52.17, "Closer to heaven", PINK],
            [0, 54.84, "Tell you how beautiful you are", PINK],
            [1, 0.14, "Lips like a prayer", CYAN],
            [1, 2.56, "Undone in your presence", CYAN],
            [1, 5.46, "Worship your body in the dark", WHITE],
            [1, 9.94, "You're so soft", PINK],
            [1, 11.88, "Nothing about you ever hurts me", PINK],
            [1, 15.13, "You're so soft", PINK],
            [1, 17.12, "I'm a lover at your mercy", PINK],
            [1, 26.45, "The way you say my name", PINK],
            [1, 31.76, "The way you're taking off my t-shirt", PINK],
            [1, 37.10, "I want you every day", CYAN],
            [1, 42.48, "The way I wouldn't change a thing", CYAN],
            [1, 46.18, "About my baby girl", CYAN],
            [1, 50.75, "How is it true", WHITE],
            [1, 53.35, "That there's a whole world", WHITE],
            [1, 55.88, "But I'm the only one that gets to", WHITE],
            [2, 1.40, "Take you upstairs", PINK],
            [2, 4.12, "Closer to heaven", PINK],
            [2, 6.73, "Tell you how beautiful you are", PINK],
            [2, 12.09, "Lips like a prayer", CYAN],
            [2, 14.62, "Undone in your presence", CYAN],
            [2, 17.47, "Worship your body in the dark", WHITE],
            [2, 21.88, "You're so soft", PINK],
            [2, 23.79, "Nothing about you ever hurts me", PINK],
            [2, 27.13, "You're so soft", PINK],
            [2, 29.11, "I'm a lover at your mercy", PINK],
            [2, 43.15, "You're so soft", PINK],
            [2, 45.15, "Nothing about you ever hurts me", PINK],
            [2, 48.55, "You're so soft", PINK],
            [2, 50.58, "I'm a lover at your mercy", PINK],
        ]

        placeholder = st.empty()
        start_time = time.time()

        for i in range(len(lyrics)):
            m, s, line, color = lyrics[i]
            target_time = m * 60 + s
            
            # Sinkronisasi waktu
            while time.time() - start_time < target_time:
                time.sleep(0.01)

            # Hitung durasi mengetik agar pas dengan baris berikutnya
            if i < len(lyrics) - 1:
                next_m, next_s, _, _ = lyrics[i+1]
                duration = (next_m * 60 + next_s) - target_time
            else:
                duration = 3.0
            
            char_speed = min(0.06, duration / len(line))

            # Efek Mengetik
            full_text = ""
            for char in line:
                full_text += char
                placeholder.markdown(
                    f"<div class='lyric-box' style='color:{color};'>{full_text}</div>", 
                    unsafe_allow_html=True
                )
                time.sleep(char_speed)

        st.balloons()
        st.success("Selesai! ✨")

if __name__ == "__main__":
    lany_soft_lyrics()