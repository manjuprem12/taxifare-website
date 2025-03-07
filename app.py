import streamlit as st
import datetime
import requests

'''
# TaxiFareModel front
'''

st.markdown('''
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
''')

'''
## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

1. Let's ask for:
- date and time
- pickup longitude
- pickup latitude
- dropoff longitude
- dropoff latitude
- passenger count
'''

'''
## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Off course... The `requests` package 💡
'''

url = 'https://taxifare.lewagon.ai/predict'

if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

'''

2. Let's build a dictionary containing the parameters for our API...

3. Let's call our API using the `requests` package...

4. Let's retrieve the prediction from the **JSON** returned by the API...

## Finally, we can display the prediction to the user
'''

col1, col2 = st.columns(2)

with col1:
    selected_date = st.date_input("Date", value=datetime.date.today())
    selected_time = st.time_input("Time", value=datetime.time(12, 00))  # Default time: 12:00
    selected_datetime = datetime.datetime.combine(selected_date, selected_time)


    pickup_longitude = st.number_input("Pickup longitude")
    pickup_latitude = st.number_input("Pickup latitude")


    pass_count = st.number_input("Passenger count")



number = st.slider("Pick a number", 0, 100)

if number:
   st.write("number: ", number)



with col2:
    long = st.number_input("Dropoff longitude")
    lat = st.number_input("Dropoff latitude")
    st.date_input("Pick a date")
    uploaded_file =  st.file_uploader("upload a file")


    if uploaded_file:
        st.write("Filename: ", uploaded_file.name)


params = {
    "pickup_datetime": selected_datetime.strftime("%Y-%m-%d %H:%M:%S"),
    "pickup_longitude": pickup_longitude,
    "pickup_latitude": pickup_latitude,
    "dropoff_longitude": long,
    "dropoff_latitude": lat,
    "passenger_count": int(pass_count)

}

left, middle, right = st.columns(3)
# if left.button("Plain button", use_container_width=True):
#     left.markdown("You clicked the plain button.")
if middle.button("SUBMMIT", icon="😃", use_container_width=True, type="secondary"):
    middle.markdown("You clicked the emoji button.")
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)
        prediction = response.json().get("fare")
        st.markdown(f"<h1 style='font-size: 48px;'>Predicted Taxi Fare: ${prediction:.2f}</h1>", unsafe_allow_html=True)

    except requests.exceptions.RequestException as e:
        st.error(f"Error calling the API: {e}")
    except (ValueError, KeyError) as e:
        st.error(f"Error parsing API response: {e}")

# if right.button("Material button", icon=":material/mood:", use_container_width=True, type="tertiary"):
#     right.markdown("You clicked the Material button.")




# response = requests.get(url, params=params)
