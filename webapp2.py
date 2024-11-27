# import libraries
import streamlit as st
from PIL import Image
st.write("""
         # Add media file in streamlit web_app
         """)

# Add image file
st.write("""
         ## Image of Snow Leopard
         """)
img = Image.open("leo_image.jpg")
# Create a slider to adjust the image size
image_width = st.slider("Adjust image width", min_value=100, max_value=800, value=400)
st.image(img, caption='Leo', width=image_width)

# Add Video file
st.write("""
         ## Video of Snow Leopard
         """)
vid = open("leo_video.mp4", "rb")
# Add a slider to select the start time in seconds
start_time = st.slider("Select start time (seconds)", min_value=0, max_value=12, value=0)
st.video(vid, start_time=start_time)

# Add Audio file
st.write("""
         ## Sound_Track of Snow Leopard
         """)
aud = open("leo_audio.mp3", "rb")
st.audio(aud)