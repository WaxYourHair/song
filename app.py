import streamlit as st
import time
import os

# Konfigurasi Halaman
st.set_page_config(page_title="LANY - Soft Lyrics", page_icon="🎵")

# Styling Custom CSS untuk tampilan estetik
st.markdown("""
    <style>
    .lyric-text {
        font-family: 'Serif';
        font-size: 24px;
        text-align: center;
        font-weight: bold;
        transition: all 0.5s ease-in-out;
    }
    .stAudio {
        margin-top: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

def main():
    st.title("🎵 LANY - Soft")
    
    # Path Audio (Pastikan soft.mp3 ada di folder yang sama)
    AUDIO_FILE = "soft.mp3"
    
    if not os.path.exists(AUDIO_FILE):
        st.error(f"File '{AUDIO_FILE}' tidak ditemukan. Pastikan file ada di direktori yang sama.")
        return

    # Tampilkan Audio Player
    audio_file = open(AUDIO_FILE, 'rb')
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format='audio/mp3')

    st.info("Klik tombol 'Start Lyrics' tepat saat lagu dimulai untuk sinkronisasi.")

    # Data Lirik
    lyrics = [
        [0.0, "But I'm the only one that gets to", "#FFFFFF"],
        [6.0, "Take you upstairs", "#FFB6C1"],
        [8.50, "Closer to heaven", "#FFB6C1"],
        [10.50, "Tell you how beautiful you are", "#FFB6C1"],
        [15.50, "Lips like a prayer", "#00FFFF"],
        [18.50, "Undone in your presence", "#00FFFF"],
        [22.00, "Worship your body in the dark", "#FFFFFF"],
        [25.50, "You're so soft", "#FFB6C1"],
        [27.50, "Nothing about you ever hurts me", "#FFB6C1"],
        [31.50, "You're so soft", "#FFB6C1"],
        [33.00, "I'm a lover at your mercy", "#FFB6C1"],
        [47.15, "You're so soft", "#FFB6C1"],
        [49.15, "Nothing about you ever hurts me", "#FFB6C1"],
        [52.00, "You're so soft", "#FFB6C1"],
        [54.00, "I'm a lover at your mercy :)", "#FFB6C1"],
    ]

    if st.button("🚀 Start Lyrics"):
        placeholder = st.empty()
        start_time = time.time()
        
        for i, (target_time, text, color) in enumerate(lyrics):
            # Hitung waktu tunggu
            current_elapsed = time.time() - start_time
            wait_time = target_time - current_elapsed
            
            if wait_time > 0:
                time.sleep(wait_time)
            
            # Simulasi efek mengetik (Typewriter)
            full_display = ""
            for char in text:
                full_display += char
                placeholder.markdown(
                    f'<p class="lyric-text" style="color: {color};">{full_display}</p>', 
                    unsafe_allow_html=True
                )
                # Kecepatan ketik (sesuaikan jika ingin lebih cepat/lambat)
                time.sleep(0.05) 
            
            # Memberikan jeda singkat antar baris lirik
            time.sleep(0.5)

if __name__ == "__main__":
    main()
