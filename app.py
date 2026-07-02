import streamlit as st
import pandas as pd
import joblib

# =====================================
# PAGE CONFIGURATION
# =====================================
st.set_page_config(
    page_title="California Housing Price Predictor",
    page_icon="🏠",
    layout="wide"
)

# =====================================
# LOAD MODEL
# =====================================
model = joblib.load("house_price_model.pkl")

# =====================================
# TITLE SECTION
# =====================================
st.title("🏠 California Housing Price Prediction")

st.markdown("""
### 🏡 Smart California Housing Predictor

Estimate California house prices instantly using a **Machine Learning model**
trained on the **California Housing Dataset**.

✅ 20,640 Housing Records  
✅ Linear Regression Model  
✅ Real-Time Predictions  
✅ Interactive Streamlit Dashboard  
""")

# =====================================
# PROJECT DASHBOARD
# =====================================
c1, c2, c3 = st.columns(3)

c1.metric("📊 Dataset Size", "20,640")
c2.metric("📌 Features Used", "12")
c3.metric("🤖 Algorithm", "Linear Regression")

# =====================================
# SIDEBAR
# =====================================
st.sidebar.header("📖 About Project")

st.sidebar.info("""
**Model:** Linear Regression

**R² Score:** 0.625

**Dataset:** California Housing Dataset

**Developer:** Abhay Dwivedi
""")

# =====================================
# INPUT SECTION
# =====================================
st.markdown("---")
st.header("🏡 Enter House Details")

col1, col2 = st.columns(2)

with col1:

    longitude = st.number_input(
        "Longitude",
        min_value=-124.0,
        max_value=-114.0,
        value=-120.0
    )

    latitude = st.number_input(
        "Latitude",
        min_value=32.0,
        max_value=42.0,
        value=35.0
    )

    housing_median_age = st.slider(
        "Housing Median Age",
        min_value=1,
        max_value=52,
        value=25
    )

    total_rooms = st.number_input(
        "Total Rooms",
        min_value=1,
        value=2000
    )

with col2:

    total_bedrooms = st.number_input(
        "Total Bedrooms",
        min_value=1,
        value=400
    )

    population = st.number_input(
        "Population",
        min_value=1,
        max_value=40000,
        value=1000
    )

    households = st.number_input(
        "Households",
        min_value=1,
        value=350
    )

    median_income = st.slider(
        "Median Income",
        min_value=0.0,
        max_value=15.0,
        value=3.5
    )

# =====================================
# OCEAN PROXIMITY
# =====================================
ocean = st.selectbox(
    "Ocean Proximity",
    [
        "<1H OCEAN",
        "INLAND",
        "ISLAND",
        "NEAR BAY",
        "NEAR OCEAN"
    ]
)

# =====================================
# MANUAL ONE-HOT ENCODING
# =====================================
inland = 1 if ocean == "INLAND" else 0
island = 1 if ocean == "ISLAND" else 0
near_bay = 1 if ocean == "NEAR BAY" else 0
near_ocean = 1 if ocean == "NEAR OCEAN" else 0

# =====================================
# PREDICTION BUTTON
# =====================================
if st.button("🔮 Predict House Price"):

    input_df = pd.DataFrame({
        'longitude': [longitude],
        'latitude': [latitude],
        'housing_median_age': [housing_median_age],
        'total_rooms': [total_rooms],
        'total_bedrooms': [total_bedrooms],
        'population': [population],
        'households': [households],
        'median_income': [median_income],
        'ocean_proximity_INLAND': [inland],
        'ocean_proximity_ISLAND': [island],
        'ocean_proximity_NEAR BAY': [near_bay],
        'ocean_proximity_NEAR OCEAN': [near_ocean]
    })

    # ---------------------------
    # SHOW USER INPUTS
    # ---------------------------
    st.subheader("📋 Prediction Summary")

    st.dataframe(input_df)

    # ---------------------------
    # MODEL PREDICTION
    # ---------------------------
    prediction = model.predict(input_df)

    # ---------------------------
    # DISPLAY RESULT
    # ---------------------------
    st.success(
        f"🏡 Estimated House Price: ${prediction[0]:,.2f}"
    )

    st.info(
        "⚠️ This prediction is generated using a Linear Regression model "
        "and should be used for educational purposes."
    )

# =====================================
# MODEL PERFORMANCE
# =====================================
st.markdown("---")

st.header("📊 Model Performance")

m1, m2, m3 = st.columns(3)

m1.metric("R² Score", "0.625")
m2.metric("MAE", "$50,670")
m3.metric("MSE", "4.91 Billion")

# =====================================
# FEATURE COEFFICIENTS
# =====================================
st.markdown("---")

st.header("📈 Feature Contribution")

feature_names = [
    'longitude',
    'latitude',
    'housing_median_age',
    'total_rooms',
    'total_bedrooms',
    'population',
    'households',
    'median_income',
    'ocean_proximity_INLAND',
    'ocean_proximity_ISLAND',
    'ocean_proximity_NEAR BAY',
    'ocean_proximity_NEAR OCEAN'
]

coef_df = pd.DataFrame({
    "Feature": feature_names,
    "Coefficient": model.coef_
})

st.bar_chart(
    coef_df.set_index("Feature")
)

st.caption(
    "The chart above shows how each feature contributes "
    "to the Linear Regression model."
)

# =====================================
# FOOTER
# =====================================
st.markdown("---")

st.markdown("""
### 👨‍💻 About the Developer

**Abhay Dwivedi**

• Computer Science Student  
• Aspiring Data Scientist & ML Engineer  
• Passionate about building practical AI solutions  

**Technologies Used:**
- Python
- Pandas
- Scikit-Learn
- Streamlit
- Joblib
- GitHub
""")

st.markdown("---")

st.markdown(
    "<center>Made by <b>Abhay Dwivedi</b></center>",
    unsafe_allow_html=True
)