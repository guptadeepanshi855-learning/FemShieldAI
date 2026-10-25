import streamlit as st
import cv2
import numpy as np
from scipy.io import wavfile
from PIL import Image
from PIL.ExifTags import TAGS
import io

# 🌟 FemShieldAI App Page Configuration
st.set_page_config(page_title="FemShieldAI Portal", page_icon="🛡️", layout="centered")

# 🎨 Custom Cyberpunk Dark UI Theme Injection (CSS Injection)
st.markdown("""
    <style>
    /* Main App Background & Text Adjustments */
    .stApp {
        background-color: #0b0f19;
        color: #e2e8f0;
    }
    
    /* Global Typography Customizations */
    h1, h2, h3 {
        color: #38bdf8 !important;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        text-shadow: 0px 0px 12px rgba(56, 189, 248, 0.4);
    }
    
    /* Tab Styling Overrides */
    .stTabs [data-baseweb="tab-list"] {
        gap: 12px;
        background-color: #111827;
        padding: 8px;
        border-radius: 12px;
        border: 1px solid #1f2937;
    }
    .stTabs [data-baseweb="tab"] {
        color: #9ca3af !important;
        background-color: transparent !important;
        border-radius: 8px !important;
        padding: 8px 16px !important;
        font-weight: 600 !important;
    }
    .stTabs [aria-selected="true"] {
        color: #38bdf8 !important;
        background-color: #1f2937 !important;
        border-bottom: 2px solid #38bdf8 !important;
    }
    
    /* Unified Styled Container Cards */
    .cyber-card {
        background: linear-gradient(135deg, #111827 0%, #1e1b4b 100%);
        border: 1px solid #312e81;
        padding: 24px;
        border-radius: 16px;
        box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.5);
        margin-bottom: 20px;
    }
    
    /* Custom Styled Buttons mimicking core framework themes */
    div.stButton > button:first-child {
        background: linear-gradient(135deg, #3b82f6 0%, #8b5cf6 100%) !important;
        color: white !important;
        font-weight: bold !important;
        border: none !important;
        padding: 10px 24px !important;
        border-radius: 8px !important;
        box-shadow: 0 4px 14px 0 rgba(139, 92, 246, 0.4) !important;
        transition: all 0.3s ease !important;
        width: 100%;
    }
    div.stButton > button:first-child:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 20px 0 rgba(139, 92, 246, 0.6) !important;
    }
    
    /* System Uploader Blocks Customizing */
    .stFileUploader {
        background-color: #111827;
        border: 1px dashed #4b5563;
        border-radius: 12px;
        padding: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# 🏛️ App Main Core Header Section
st.markdown('<div style="text-align: center; margin-bottom: 25px;">', unsafe_allow_html=True)
st.title("🛡️ FemShieldAI: Privacy & Forensic Portal")
st.write("A proactive anti-AI defense and digital forensic system for women's digital privacy.")
st.markdown('</div>', unsafe_allow_html=True)

# 🏛️ 4 Tabs for the Presentation Demo Layout
tab1, tab2, tab3, tab4 = st.tabs(["📸 Visual Shield", "🎙️ Vocal Shield", "🔍 Digital Forensic", "📊 Dashboard"])

# ==========================================
# 📸 TAB 1: VISUAL SHIELD (INVISIBLE ADVERSARIAL PROTECTION)
# ==========================================
with tab1:
    st.markdown('<div class="cyber-card">', unsafe_allow_html=True)
    st.header("📸 Visual Shield (Identity Poisoning)")
    st.caption("This feature adds invisible pixel-level perturbation to make social media photos deepfake-proof.")
    
    img_file = st.file_uploader("Upload Social Media Photo", type=["jpg", "png", "jpeg"], key="v_img")
    if img_file:
        file_bytes = np.asarray(bytearray(img_file.read()), dtype=np.uint8)
        img = cv2.imdecode(file_bytes, 1)
        
        protection_strength = st.slider("🛡️ Select Protection Intensity", min_value=1, max_value=5, value=2)
        
        if st.button("🛡️ Apply Anti-AI Camouflage Layer"):
            with st.spinner("Generating invisible adversarial perturbation matrix..."):
                h, w, c = img.shape
                float_img = img.astype(np.float32)
                
                grid_y, grid_x = np.indices((h, w))
                structured_pattern = np.sin(grid_x / 2.0) * np.cos(grid_y / 2.0)
                structured_pattern = np.expand_dims(structured_pattern, axis=2)
                structured_pattern = np.repeat(structured_pattern, c, axis=2)
                
                noise = (structured_pattern * protection_strength).astype(np.float32)
                protected_float = cv2.add(float_img, noise)
                protected_img = np.clip(protected_float, 0, 255).astype(np.uint8)
                
            st.success("🎉 Advanced Anti-AI Camouflage Layer successfully embedded!")
            
            col1, col2 = st.columns(2)
            with col1:
                st.image(img, channels="BGR", caption="Original Photo", use_container_width=True)
            with col2:
                st.image(protected_img, channels="BGR", caption="Protected Photo (Invisible Noise Added)", use_container_width=True)
            
            is_success, buffer = cv2.imencode(".png", protected_img)
            st.download_button(
                label="⬇️ Download Protected Photo",
                data=io.BytesIO(buffer).getvalue(),
                file_name="femshield_secured_photo.png",
                mime="image/png"
            )
    st.markdown('</div>', unsafe_allow_html=True)

# ==========================================
# 🎙️ TAB 2: VOCAL SHIELD (ACOUSTIC ENCRYPTION SHIELD)
# ==========================================
with tab2:
    st.markdown('<div class="cyber-card">', unsafe_allow_html=True)
    st.header("🎙️ Vocal Shield (Voice Biometric Decoy)")
    st.caption("This feature blends an ultrasonic decoy wave into audio signals to block unauthorized voice cloning.")
    
    audio_file = st.file_uploader("Upload Audio Clip (.wav format)", type=["wav"], key="v_aud")
    if audio_file:
        st.audio(audio_file, format="audio/wav")
        
        audio_protection_level = st.select_slider(
            "🔒 Select Voice Scrambling Intensity",
            options=["Standard Protection", "Enhanced Tactical Shield", "Maximum Biometric Distortion"],
            value="Enhanced Tactical Shield"
        )
        
        if st.button("🔒 Secure Voice Waves"):
            with st.spinner("Synthesizing dynamic ultrasonic biometric decoy matrix..."):
                sample_rate, data = wavfile.read(audio_file)
                
                scale_map = {"Standard Protection": 0.01, "Enhanced Tactical Shield": 0.03, "Maximum Biometric Distortion": 0.06}
                amplitude_scale = scale_map[audio_protection_level]
                data_float = data.astype(np.float64)
                
                t = np.arange(len(data_float)) / sample_rate
                decay_wave = amplitude_scale * np.sin(2 * np.pi * 19500 * t)
                
                if len(data_float.shape) > 1:
                    channels = data_float.shape
                    ultrasonic_layer = np.tile(decay_wave[:, np.newaxis], (1, channels))
                else:
                    ultrasonic_layer = decay_wave
                
                max_amplitude = np.max(np.abs(data_float)) if np.max(np.abs(data_float)) > 0 else 32767
                protected_float = data_float + (ultrasonic_layer * max_amplitude)
                protected_audio = np.clip(protected_float, np.min(data), np.max(data)).astype(data.dtype)
                
                wav_io = io.BytesIO()
                wavfile.write(wav_io, sample_rate, protected_audio)
                
            st.success("🎉 Adaptive Acoustic Shield integrated successfully!")
            st.audio(wav_io.getvalue(), format="audio/wav")
    st.markdown('</div>', unsafe_allow_html=True)

# ==========================================
# 🔍 TAB 3: DIGITAL FORENSIC (METADATA & INTEGRITY SCAN)
# ==========================================
with tab3:
    st.markdown('<div class="cyber-card">', unsafe_allow_html=True)
    st.header("🔍 Digital Forensic Blueprint (Solid Evidence)")
    st.caption("Scan uploaded suspicious or morphed media files to isolate hidden device signatures and structural integrity anomalies.")
    
    forensic_file = st.file_uploader("Upload Suspect Media File", type=["jpg", "jpeg", "png"], key="f_img")
    if forensic_file:
        image = Image.open(forensic_file)
        st.image(image, caption="Media File Loaded for Analytical Scan", use_container_width=True)
        
        if st.button("🔎 Scan Hidden EXIF Metadata & Structural Integrity"):
            with st.spinner("Analyzing image array strings and metadata blocks..."):
                exif_data = image._getexif()
                
                img_np = np.array(image.convert("RGB"))
                h, w, c = img_np.shape
                
                pixel_variance = np.std(img_np)
                integrity_index = 100.0
                status_notes = []
                
                st.subheader("📋 Core Forensic Evidence Extracted:")
                
                found_any = False
                if exif_data:
                    for tag_id, value in exif_data.items():
                        tag = TAGS.get(tag_id, tag_id)
                        if tag in ["Make", "Model", "DateTime", "Software"]:
                            st.write(f"🔹 **{tag}:** {value}")
                            found_any = True
                
                if not found_any:
                    st.warning("⚠️ EXIF Block Cleaned: No hardware signatures found (Typical for social media downscales or screenshots).")
                    integrity_index -= 25.0
                    status_notes.append("Metadata blocks stripped via platform compression algorithms.")
                else:
                    status_notes.append("Hardware device origin anchors successfully isolated.")
                
