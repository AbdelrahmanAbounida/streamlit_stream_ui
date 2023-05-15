import time 
import pandas as pd  
import streamlit as st  
import random
import requests
import json

st.set_page_config(
    page_title="Real-Time Data Science Dashboard",
    page_icon="✅",
    layout="wide",
)


st.markdown(
    """
    <style>
    .title {
        text-align: center;
        margin-bottom: 35px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)
# Display the centered title
st.markdown("<h1 class='title'>Real-Time Sensor Data</h1>", unsafe_allow_html=True)


def get_current_sensor_data():
    url = "https://sensor-stream.onrender.com/readings"

    headers = {"content-type": "application/json"}
    response = requests.get(url, headers=headers)
    out = json.loads(response.text)
    return out["x_value"],out["y_value"]

def main():
    # creating a single-element container
    placeholder = st.empty()

    x_values = [0]
    y_values = [0]
    while True:
        with placeholder.container():

            x,y = get_current_sensor_data() # update sensor reading

            print(x,y)

            if x != x_values[-1] or y != y_values[-1]: # check that sensor readings have been changed
                x_values.append(x)
                y_values.append(y)
            
            # start = 10.0
            # end = 20.0
            # x_values.append(random.uniform(1, 55))
            # y_values.append(random.uniform(start, end))

            chart_data = pd.DataFrame({'X-value': x_values, 'Y-vaue': y_values})
            st.line_chart(chart_data)


            time.sleep(1)

if __name__ == "__main__":
    main()