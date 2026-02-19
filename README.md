# ✈️ Flight Fare Predictor

A Machine Learning web application that predicts flight ticket prices based on user inputs like airline, source, destination, date, time, and number of stops.

🔗 **Live Web App:** https://flight-fare-predictor-kunalx30.streamlit.app/

---

## 🚀 Project Overview

This project uses a **Random Forest Regressor** model to estimate flight ticket prices. The model was trained on a real dataset and deployed using **Streamlit**, allowing users to interact with it in real time without coding knowledge.

---

## 🧠 Machine Learning Details

- **Model Used:** Random Forest Regressor
- **Prediction Type:** Regression
- **Key Features:**
  - Airline
  - Source & Destination
  - Journey Date & Time
  - Total Stops
- **Model File:** `models/rd_random.pkl`

The model development process and notes are available in the uploaded notebook.

---

## 🛠 Tech Stack

- Python 3.10
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Pickle
- Git & GitHub
- Streamlit (Cloud Deployment)

---

## 📁 Repository Structure

```

flight-fare-predictor/
│
├── app.py
├── requirements.txt
├── runtime.txt
├── models/
│ └── rd_random.pkl
├── src/
│ ├── config.py
│ └── preprocess.py
└── README.md

```


---

## ⚙️ Installation & Local Setup

1. **Clone the repository:**

```bash
git clone https://github.com/Kunalx30/flight-fare-predictor.git
cd flight-fare-predictor
```

2. **Create and activate a virtual environment:**
   
```bash
python -m venv venv
venv\Scripts\activate
```


3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Run the Streamlit app:**
```bash
streamlit run app.py
```

## 🌐 Deployment

This application is deployed on **Streamlit Cloud**.

🔗 Live App:
https://flight-fare-predictor-kunalx30.streamlit.app/

The deployment automatically installs dependencies from `requirements.txt`
and runs the app using:

streamlit run app.py

## 🚀 Future Enhancements
   - Add real-time airline pricing API
   - More model improvements (e.g., Gradient Boosting)
   - Better UI / UX with custom components
   - Add interactive visualizations


## 👨‍💻 Author
**Kunal Chandelkar**  
Aspiring Data Analyst | ML Enthusiast  
B.Tech Computer Science & Engineering (2025)
