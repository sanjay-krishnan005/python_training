import streamlit as st
import random
import time
st.title("hospital sensor live monitoring")
st.write("simulating live sensor in the hospital : heart rate, temperature, oxygen")
def sensor_data():
    while True:
        yield{
            "heart_rate" : random.randint(60, 100),
            "blood pressure" : round(random.uniform(110, 130), 1),
            "oxygen_saturation" : random.randint(95,100)
        }
        time.sleep(2)
heart_rate_bar = st.progress(0)
bp_bar = st.progress(0)
oxygen_bar = st.progress(0)

heart_rate = st.empty()
bp_rate  = st.empty()
oxygen_sat = st.empty()

for reading in sensor_data():
    hr = reading["heart_rate"]
    bp = reading["blood pressure"]
    oxy = reading["oxygen_saturation"]

    heart_rate_bar.progress(min(hr, 100))
    bp_bar.progress(min(int(bp-97)/100*3, 100))
    oxygen_bar.progress(oxy)
  
    heart_rate.text(f"Heart Rate : {hr} bpm")
    bp_rate.text(f"blood pressure : {bp} °F")   
    oxygen_sat.text(f"Oxygen Saturation : {oxy} %")