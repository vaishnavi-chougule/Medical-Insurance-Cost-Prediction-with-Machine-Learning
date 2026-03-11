import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Healthcare - Insurance Analysis", layout="wide")

# -------------------------
# Load Data
# -------------------------
@st.cache_data
def load_data():
    return pd.read_csv("insurance_final_dataset.csv")

df = load_data()

numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns.tolist()
categorical_cols = df.select_dtypes(include=["object"]).columns.tolist()

# ==========================================================
# 🔷 BEAUTIFUL DASHBOARD TITLE
# ==========================================================
st.markdown("""
<h1 style='text-align: center; 
background: linear-gradient(90deg,#1f4e79,#2980b9);
color:white; 
padding:15px;
border-radius:10px;
font-size:40px;'>
🏥 Healthcare - Insurance Analysis 📊
</h1>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ==========================================================
# 🔷 KPI CARDS
# ==========================================================
col1, col2, col3, col4 = st.columns(4)

col1.markdown(f"""
<div style="background: linear-gradient(45deg,#1abc9c,#16a085);
padding:20px;border-radius:12px;text-align:center;color:white;">
<h4>Total Records</h4>
<h2>{df.shape[0]}</h2>
</div>
""", unsafe_allow_html=True)

col2.markdown(f"""
<div style="background: linear-gradient(45deg,#3498db,#2c3e50);
padding:20px;border-radius:12px;text-align:center;color:white;">
<h4>Average Charges</h4>
<h2>₹{df['charges'].mean():,.0f}</h2>
</div>
""", unsafe_allow_html=True)

col3.markdown(f"""
<div style="background: linear-gradient(45deg,#e67e22,#d35400);
padding:20px;border-radius:12px;text-align:center;color:white;">
<h4>Average BMI</h4>
<h2>{df['bmi'].mean():.1f}</h2>
</div>
""", unsafe_allow_html=True)

col4.markdown(f"""
<div style="background: linear-gradient(45deg,#9b59b6,#8e44ad);
padding:20px;border-radius:12px;text-align:center;color:white;">
<h4>Smoker %</h4>
<h2>{round((df['smoker']=='yes').mean()*100,1)}%</h2>
</div>
""", unsafe_allow_html=True)

# Divider
st.markdown("""
<hr style='height:4px;
border:none;
background:linear-gradient(90deg,#1abc9c,#3498db,#9b59b6);
margin-top:25px;
margin-bottom:25px;'>
""", unsafe_allow_html=True)

# ==========================================================
# 🔷 ADVANCED HORIZONTAL BUTTONS (CORRECT ORDER)
# ==========================================================

st.markdown("""
<style>
div.stButton > button {
    width: 100%;
    background: linear-gradient(45deg,#1f4e79,#2980b9);
    color: white;
    border-radius: 10px;
    height: 45px;
    font-weight: 600;
    border: none;
}
div.stButton > button:hover {
    background: linear-gradient(45deg,#154360,#1f618d);
    color: white;
    transform: scale(1.03);
    transition: 0.2s;
}
</style>
""", unsafe_allow_html=True)

btn1, btn2, btn3, btn4, btn5, btn6 = st.columns(6)

if "section" not in st.session_state:
    st.session_state.section = "Dataset Overview"

if btn1.button("📘 Dataset Overview"):
    st.session_state.section = "Dataset Overview"

if btn2.button("📊 Univariate Analysis"):
    st.session_state.section = "Univariate Analysis"

if btn3.button("📈 Bivariate Analysis"):
    st.session_state.section = "Bivariate Analysis"

if btn4.button("🧠 Multivariate Analysis"):
    st.session_state.section = "Multivariate Analysis"

if btn5.button("🔍 Correlation Analysis"):
    st.session_state.section = "Correlation Analysis"

if btn6.button("💼 Business Insights"):
    st.session_state.section = "Business Insights"

st.markdown("<br>", unsafe_allow_html=True)

# ==========================================================
# 🔷 SECTION CONTENT
# ==========================================================

if st.session_state.section == "Dataset Overview":

    st.subheader("📘 Dataset Information")
    st.write("Shape of Dataset:", df.shape)
    st.dataframe(df)

elif st.session_state.section == "Univariate Analysis":

    st.subheader("📊 Univariate Analysis")
    feature = st.selectbox("Select Feature", df.columns)

    fig, ax = plt.subplots(figsize=(8,5))

    if feature in numeric_cols:
        sns.histplot(df[feature], bins=20, kde=True, ax=ax)
    else:
        sns.countplot(data=df, x=feature, ax=ax)

    st.pyplot(fig)

elif st.session_state.section == "Bivariate Analysis":

    st.subheader("📈 Bivariate Analysis (Feature vs Charges)")
    feature = st.selectbox("Select Feature", df.columns)

    fig, ax = plt.subplots(figsize=(8,6))

    if feature in numeric_cols:
        sns.scatterplot(data=df, x=feature, y="charges", ax=ax)
    else:
        sns.boxplot(data=df, x=feature, y="charges", ax=ax)

    st.pyplot(fig)

elif st.session_state.section == "Multivariate Analysis":

    st.subheader("🧠 Multivariate Analysis")

    st.write("### Pairplot of Age, BMI & Charges")
    fig1 = sns.pairplot(df[["age", "bmi", "charges"]])
    st.pyplot(fig1)

    st.write("### Combined Impact (Age + BMI + Smoker → Charges)")
    fig2, ax = plt.subplots(figsize=(8,6))
    sns.scatterplot(data=df, x="age", y="charges",
                    hue="smoker", size="bmi", ax=ax)
    st.pyplot(fig2)

elif st.session_state.section == "Correlation Analysis":

    st.subheader("🔍 Correlation Matrix")
    corr = df[numeric_cols].corr()

    fig, ax = plt.subplots(figsize=(8,6))
    sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax)

    st.pyplot(fig)

else:

    st.subheader("💼 Key Findings")

    st.markdown("""
    - Smokers have significantly higher insurance charges.
    - Age positively impacts medical cost.
    - BMI moderately influences charges.
    - Region impact is minimal.
    """)

    st.subheader("📌 Recommendations")

    st.markdown("""
    - Implement smoker-based premium pricing.
    - Offer BMI wellness discount programs.
    - Apply age-based premium tiers.
    - Promote preventive healthcare initiatives.
    """)
