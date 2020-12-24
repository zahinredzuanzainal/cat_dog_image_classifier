import streamlit as st

# Text
st.title("Streamlit Tutorial")

#Header/Subheader

st.header("My first header")

# Text
st.text("Welcome to my DS Experiment")

# Markdown
st.markdown("### Here is it!")

#Error / Colorful Indicators
#success
st.success("Successful")
#information
st.info("Information")
#warning
st.warning("Warning")
#error
st.error("Error")
#exception
st.exception("NameError('name three not defined')")

#Get Help Info About Python
st.help(range)

# Writing Text Super Function
st.write("Text with write")

st.write(range(10))

#Images

from PIL import Image
img = Image.open("covid_1.jpg")
st.image(img, width=150, caption="Simple X-Ray")

#Videos
vid_file = open('video.mp4', 'rb').read()
st.video(vid_file)

#Audio
audio_file = open("audio.mp3", "rb").read()
st.audio(audio_file, format='audio/mp3')

#Widgets
#Checkbox

if st.checkbox("Show/Hide"):
    st.text("Show or Hiding Widget")

# Radiobutton

status = st.radio("What is your status", ("Active", "Inactive"))

if status == "Active":
    st.success("You are Active")

else:
    st.error("You are inactive")


# Select Box

occupation = st.selectbox("Occupation", ("Programmer", "Doctor", "Engineer"))
st.write("You selected this occupation", occupation)

# Multiselect
location = st.multiselect("Where do you work?", ("London", "USA", "Japan", "Russia"))
st.write("You selected", len(location), "locations")

# Slider

level = st.slider("What is your level",1,100)

#Buttons
st.button("Simple Button")

if st.button("About"):
    st.text("Streamlit is Cool")

# Text Input

first_name = st.text_input("Enter Your First Name", "Type Here ...")

if st.button("Submit"):
    result = first_name.title()
    st.success(result)

#Text Area
message = st.text_area("Enter Your Message", "Type Here ...")

if st.button("Submit Message"):
    result = message.title()
    st.success(result)

#Date Input
import datetime

today = st.date_input("Today is", datetime.datetime.now())

#Time
the_time = st.time_input("The time is", datetime.time())

#Display JSON

st.text("Display JSON")
st.json({'name':"Jason", 'gender':"Male"})

# Display Raw Code 1

st.text("Display Raw Code 1")
st.code("import numpy as np")

# Display Raw Code 2

with st.echo():
    import pandas as pd
    df = pd.DataFrame()

# Progress Bar
import time
my_bar = st.progress(0)
for p in range(10):
    my_bar.progress(p+1)

# Spinner
with st.spinner("Waiting..."):
    time.sleep(5)
st.success("Finished!")

#Balloon

st.balloons()

#Sidebar
st.sidebar.header("About")
st.sidebar.text("This is Streamlit Tutorial")

#Functions
@st.cache
def run_fx():
    return range(100)

st.write(run_fx())

#Plot
st.pyplot()

#Dataframes
st.dataframe(df)

# Tables
st.table(df)








