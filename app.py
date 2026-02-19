import os
import pickle
import streamlit as st
from src.config import (
    AIRLINES,
    DESTINATIONS,
    SOURCES,
    TOTAL_STOPS_OPTIONS,
    TOTAL_STOPS_MAP,
    AIRLINE_TO_CODE,
    DEST_TO_CODE,
)
from src.preprocess import build_feature_row


APP_TITLE = "Flight Fare Predictor"


@st.cache_resource
def load_model(model_path: str):
    with open(model_path, "rb") as f:
        return pickle.load(f)


def hero_section():
    st.markdown("""
        <div style="
            background: linear-gradient(135deg,#2b6cb0,#1e3a8a);
            padding:60px 20px;
            border-radius:15px;
            text-align:center;
            color:white;">
            <h4>✈ ML-Powered Prediction</h4>
            <h1 style="margin-bottom:10px;">Flight Fare Predictor</h1>
            <p>Enter your trip details and get an instant fare estimate</p>
        </div>
        <br>
    """, unsafe_allow_html=True)


def result_card(pred):
    st.markdown(f"""
        <div style="
            background: linear-gradient(135deg,#2b6cb0,#1e3a8a);
            padding:30px;
            border-radius:15px;
            text-align:center;
            color:white;
            margin-top:20px;">
            <p style="opacity:0.7;">Predicted Fare</p>
            <h1 style="font-size:45px;">₹{pred:,.0f}</h1>
            <p style="opacity:0.5;">Based on Random Forest model estimation</p>
        </div>
    """, unsafe_allow_html=True)


def main():
    st.set_page_config(page_title=APP_TITLE, layout="centered")
    hero_section()

    model_path = os.path.join("models", "rd_random.pkl")
    model = load_model(model_path)

    st.markdown("## 📍 Route Details")

    col1, col2, col3 = st.columns(3)
    with col1:
        airline = st.selectbox("Airline", AIRLINES)
    with col2:
        source = st.selectbox("Source", SOURCES)
    with col3:
        destination = st.selectbox("Destination", DESTINATIONS)

    col4, col5, col6 = st.columns(3)
    with col4:
        total_stops_label = st.selectbox("Total Stops", TOTAL_STOPS_OPTIONS)
    with col5:
        date_day = st.slider("Journey Day", 1, 31, 15)
    with col6:
        date_month = st.slider("Journey Month", 1, 12, 6)

    st.markdown("---")
    st.markdown("## ⏰ Time & Duration")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown("**Departure**")
        dep_hour = st.slider("Hour", 0, 23, 10)
        dep_min = st.slider("Minutes", 0, 59, 30)

    with c2:
        st.markdown("**Arrival**")
        arr_hour = st.slider("Hour ", 0, 23, 12)
        arr_min = st.slider("Minutes ", 0, 59, 0)

    with c3:
        st.markdown("**Duration**")
        duration_hours = st.slider("Hours", 0, 24, 2)
        duration_minutes = st.slider("Minutes  ", 0, 59, 30)

    # Summary Bar
    st.markdown(f"""
        <div style="
            background:#f1f5f9;
            padding:12px;
            border-radius:10px;
            font-size:14px;
            margin-top:10px;">
            <b>{airline}</b> • {source} → {destination} • {total_stops_label} • 
            {dep_hour:02}:{dep_min:02} → {arr_hour:02}:{arr_min:02} • 
            {duration_hours}h {duration_minutes}m
        </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    airline_code = AIRLINE_TO_CODE.get(airline, 0)
    destination_code = DEST_TO_CODE.get(destination, 0)
    total_stops = TOTAL_STOPS_MAP[total_stops_label]
    
      # Custom Button Styling
    st.markdown("""
        <style>
        div.stButton > button {
            background-color: #f59e0b;
            color: white;
            font-size: 18px;
            font-weight: 600;
            padding: 12px 20px;
            border-radius: 10px;
            border: none;
        }
        div.stButton > button:hover {
            background-color: #d97706;
            color: white;
        }
        </style>
    """, unsafe_allow_html=True)

    if st.button("📊 Predict Fare", use_container_width=True):
        X = build_feature_row(
            model=model,
            airline_code=airline_code,
            destination_code=destination_code,
            total_stops=total_stops,
            date_day=int(date_day),
            date_month=int(date_month),
            dep_hour=int(dep_hour),
            dep_min=int(dep_min),
            arr_hour=int(arr_hour),
            arr_min=int(arr_min),
            duration_hours=int(duration_hours),
            duration_minutes=int(duration_minutes),
            source=source,
        )

        pred = model.predict(X)[0]
        result_card(pred)

    # Footer
    st.markdown("""
        <div style="text-align:center; margin-top:40px; font-size:14px; opacity:0.7;">
            Built with ❤️ by <b>Kunal</b><br>
            <span style="font-size:13px;">Powered by Random Forest Regressor</span>
        </div>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
