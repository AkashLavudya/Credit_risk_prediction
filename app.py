import streamlit as st
import pandas as pd
import joblib

# ---------------------------
# Page Configuration
# ---------------------------

st.set_page_config(
    page_title="Credit Risk Predictor",
    page_icon="💳",
    layout="wide"
)

# ---------------------------
# Load Model
# ---------------------------

model = joblib.load("model.pkl")
columns = joblib.load("columns.pkl")

# ---------------------------
# Custom CSS
# ---------------------------

st.markdown("""
<style>

.main{
    background:#f6f8fc;
}

.title{
    text-align:center;
    font-size:40px;
    font-weight:bold;
    color:#0A4DA3;
}

.subtitle{
    text-align:center;
    color:gray;
    margin-bottom:30px;
}

.card{
    padding:20px;
    border-radius:15px;
    background:white;
    box-shadow:0px 5px 20px rgba(0,0,0,0.1);
}

.success-card{
    background:#e8f8ee;
    border-left:8px solid #2ecc71;
    padding:20px;
    border-radius:15px;
}

.danger-card{
    background:#fdeaea;
    border-left:8px solid #e74c3c;
    padding:20px;
    border-radius:15px;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------
# Sidebar
# ---------------------------

st.sidebar.title("💳 Credit Risk Predictor")

st.sidebar.markdown("---")

st.sidebar.write("### Model")
st.sidebar.success("Logistic Regression")

st.sidebar.write("### Dataset")
st.sidebar.info("German Credit Dataset")

st.sidebar.write("### Technologies")

st.sidebar.write("""
- Python
- Pandas
- Scikit-Learn
- Streamlit
""")

st.sidebar.markdown("---")

st.sidebar.write("Developed by")
st.sidebar.write("**Akash Lavudya**")

# ---------------------------
# Header
# ---------------------------

st.markdown(
    "<div class='title'>💳 Credit Risk Prediction System</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='subtitle'>AI Powered Loan Risk Assessment</div>",
    unsafe_allow_html=True
)

# ---------------------------
# Form
# ---------------------------

with st.container():

    col1, col2 = st.columns(2)

    with col1:

        age = st.number_input(
            "Age",
            18,
            100,
            30
        )

        sex = st.selectbox(
            "Gender",
            ["Female", "Male"]
        )

        housing = st.selectbox(
            "Housing",
            ["Own", "Rent"]
        )

        income = st.number_input(
            "Annual Income",
            min_value=0,
            value=50000
        )

    with col2:

        loan = st.number_input(
            "Loan Amount",
            min_value=0,
            value=10000
        )

        duration = st.slider(
            "Loan Duration",
            1,
            72,
            24
        )

        saving = st.selectbox(
            "Saving Account",
            [
                "little",
                "moderate",
                "quite rich",
                "rich"
            ]
        )

        checking = st.selectbox(
            "Checking Account",
            [
                "little",
                "moderate",
                "rich"
            ]
        )

    purpose = st.selectbox(
        "Purpose",
        [
            "car",
            "radio/TV",
            "education",
            "business",
            "furniture/equipment",
            "domestic appliances",
            "repairs",
            "vacation/others"
        ]
    )

# ---------------------------
# Predict Button
# ---------------------------

if st.button("🚀 Predict Credit Risk", use_container_width=True):

    data = pd.DataFrame(
        0,
        index=[0],
        columns=columns
    )

    if "Age" in data.columns:
        data["Age"] = age

    if "Credit amount" in data.columns:
        data["Credit amount"] = loan

    if "Duration" in data.columns:
        data["Duration"] = duration

    if "Income" in data.columns:
        data["Income"] = income

    def set_dummy(prefix, value):
        col = f"{prefix}_{value}"
        if col in data.columns:
            data[col] = 1

    set_dummy("Sex", sex.lower())
    set_dummy("Housing", housing.lower())
    set_dummy("Saving accounts", saving)
    set_dummy("Checking account", checking)
    set_dummy("Purpose", purpose)

    prediction = model.predict(data)[0]

    probability = model.predict_proba(data)[0]

    confidence = probability.max() * 100

    st.markdown("---")

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Model",
        "Logistic Regression"
    )

    c2.metric(
        "Confidence",
        f"{confidence:.2f}%"
    )

    c3.metric(
        "Prediction Time",
        "<1 sec"
    )

    st.progress(confidence / 100)

    if prediction == 1:
        st.success("✅ LOW CREDIT RISK")

        st.info("""
            Recommendation
        
            ✔ Loan can be approved.
        """)

    else:
        st.error("🔴 HIGH CREDIT RISK")
    
        st.warning("""
            Recommendation
    
            ⚠ Manual verification required.
        """)
        st.markdown("---")

    st.subheader("Prediction Summary")

    summary = pd.DataFrame(
        {
            "Field": [
                "Age",
                "Income",
                "Loan Amount",
                "Duration",
                "Purpose"
            ],
            "Value": [
                age,
                income,
                loan,
                duration,
                purpose
            ]
        }
    )

    st.dataframe(summary, use_container_width=True)

st.markdown("---")

st.caption(
    "Built with Python • Streamlit • Scikit-Learn • Pandas"
)
