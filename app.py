import streamlit as st
import streamlit.components.v1 as components
import base64
import json
import os

# Konfigurasi Halaman
st.set_page_config(page_title="LANY - Soft Sync", page_icon="🎵")

def get_audio_base64(file_path):
    """Mengonversi file audio ke base64 agar bisa diputar di HTML"""
    with open(file_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

def main():
    st.markdown("<h1 style='text-align: center; color: #FFB6C1;'>For Arasha <3</h1>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; color: #FFB6C1;'>🎵 LANY - Soft</h1>", unsafe_allow_html=True)
    
    AUDIO_FILE = "soft.mp3"
    
    if not os.path.exists(AUDIO_FILE):
        st.error(f"File '{AUDIO_FILE}' tidak ditemukan. Pastikan file berada di folder yang sama dengan skrip ini.")
        return

    # Konversi audio ke Base64
    audio_base64 = get_audio_base64(AUDIO_FILE)

    # Data Lirik
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

    lyrics_json = json.dumps(lyrics_data)

    # HTML + JS + CSS
    sync_html = f"""
    <div style="display: flex; flex-direction: column; align-items: center; justify-content: center; 
                background: #1e1e2e; border-radius: 20px; padding: 30px; box-shadow: 0 10px 30px rgba(0,0,0,0.5);">
        
        <div id="lyric-box" style="
            height: 120px;
            display: flex;
            align-items: center;
            justify-content: center;
            margin-bottom: 20px;
        ">
            <div id="lyric-text" style="
                font-family: 'Segoe UI', sans-serif;
                font-size: 26px;
                font-weight: bold;
                text-align: center;
                line-height: 1.4;
                transition: all 0.4s ease;
                color: #FFFFFF;
                opacity: 0.8;
            ">Tekan Play untuk Memulai</div>
        </div>
        
        <audio id="audioPlayer" controls style="width: 100%; filter: invert(20%) sepia(95%) saturate(3000%) hue-rotate(300deg);">
            <source src="data:audio/mp3;base64,{audio_base64}" type="audio/mpeg">
        </audio>
    </div>

    <script>
        const lyrics = {lyrics_json};
        const audio = document.getElementById('audioPlayer');
        const lyricText = document.getElementById('lyric-text');

        audio.ontimeupdate = function() {{
            const currentTime = audio.currentTime;
            let activeLine = lyrics[0].text;
            let activeColor = lyrics[0].color;

            for (let i = 0; i < lyrics.length; i++) {{
                if (currentTime >= lyrics[i].time) {{
                    activeLine = lyrics[i].text;
                    activeColor = lyrics[i].color;
                }}
            }}
            
            if (lyricText.innerHTML !== activeLine) {{
                lyricText.style.transform = "translateY(-10px)";
                lyricText.style.opacity = "0";
                
                setTimeout(() => {{
                    lyricText.innerHTML = activeLine;
                    lyricText.style.color = activeColor;
                    lyricText.style.transform = "translateY(0)";
                    lyricText.style.opacity = "1";
                }}, 200);
            }}
        }};
    </script>
    """

    components.html(sync_html, height=450)

if __name__ == "__main__":
    main()

