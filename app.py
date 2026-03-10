import streamlit as st
import streamlit.components.v1 as components
import json
import os

# Konfigurasi Halaman
st.set_page_config(page_title="LANY - Soft Sync", page_icon="🎵")

def main():
    st.markdown("<h1 style='text-align: center; color: #FFB6C1;'>🎵 LANY - Soft</h1>", unsafe_allow_html=True)
    
    AUDIO_FILE = "soft.mp3"
    
    if not os.path.exists(AUDIO_FILE):
        st.error(f"File '{AUDIO_FILE}' tidak ditemukan di direktori.")
        return

    # Data Lirik (Detik, Teks, Warna)
    lyrics_data = [
        {"time": 0.0, "text": "But I'm the only one that gets to", "color": "#FFFFFF"},
        {"time": 6.0, "text": "Take you upstairs", "color": "#FFB6C1"},
        {"time": 8.50, "text": "Closer to heaven", "color": "#FFB6C1"},
        {"time": 10.50, "text": "Tell you how beautiful you are", "color": "#FFB6C1"},
        {"time": 15.50, "text": "Lips like a prayer", "color": "#00FFFF"},
        {"time": 18.50, "text": "Undone in your presence", "color": "#00FFFF"},
        {"time": 22.00, "text": "Worship your body in the dark", "color": "#FFFFFF"},
        {"time": 25.50, "text": "You're so soft", "color": "#FFB6C1"},
        {"time": 27.50, "text": "Nothing about you ever hurts me", "color": "#FFB6C1"},
        {"time": 31.50, "text": "You're so soft", "color": "#FFB6C1"},
        {"time": 33.00, "text": "I'm a lover at your mercy", "color": "#FFB6C1"},
        {"time": 47.15, "text": "You're so soft", "color": "#FFB6C1"},
        {"time": 49.15, "text": "Nothing about you ever hurts me", "color": "#FFB6C1"},
        {"time": 52.00, "text": "You're so soft", "color": "#FFB6C1"},
        {"time": 54.00, "text": "I'm a lover at your mercy :)", "color": "#FFB6C1"},
    ]

    # Mengonversi data ke JSON agar bisa dibaca JavaScript
    lyrics_json = json.dumps(lyrics_data)

    # Integrasi HTML + JS untuk Audio Player & Sinkronisasi
    sync_html = f"""
    <div style="display: flex; flex-direction: column; align-items: center; justify-content: center; height: 300px; background: #0e1117; border-radius: 15px; padding: 20px;">
        <div id="lyric-container" style="
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            font-size: 28px;
            font-weight: bold;
            text-align: center;
            min-height: 80px;
            margin-bottom: 30px;
            transition: all 0.3s ease;
        ">Putar lagu untuk melihat lirik...</div>
        
        <audio id="myAudio" controls style="width: 100%; max-width: 500px;">
            <source src="app/static/{AUDIO_FILE}" type="audio/mpeg">
            Browser Anda tidak mendukung elemen audio.
        </audio>
    </div>

    <script>
        const lyrics = {lyrics_json};
        const audio = document.getElementById('myAudio');
        const container = document.getElementById('lyric-container');

        audio.ontimeupdate = function() {{
            const currentTime = audio.currentTime;
            let currentLine = "";
            let currentColor = "#FFFFFF";

            for (let i = 0; i < lyrics.length; i++) {{
                if (currentTime >= lyrics[i].time) {{
                    currentLine = lyrics[i].text;
                    currentColor = lyrics[i].color;
                }}
            }}
            
            if (container.innerText !== currentLine) {{
                container.innerText = currentLine;
                container.style.color = currentColor;
                // Animasi sederhana saat teks berubah
                container.style.opacity = 0;
                setTimeout(() => {{ container.style.opacity = 1; }}, 50);
            }}
        }};
    </script>
    """

    # Menampilkan komponen di Streamlit
    # Catatan: Kita perlu trik agar Streamlit bisa membaca file lokal
    # Buat folder bernama 'static' di direktori project jika ingin lebih rapi
    components.html(sync_html, height=400)

    st.markdown("---")
    st.caption("Pastikan file 'soft.mp3' berada di folder yang sama dengan skrip ini.")

if __name__ == "__main__":
    main()
