import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

st.set_page_config(page_title="Employee Attrition Dashboard", layout="wide")
st.title("📊 Employee Attrition Insights Platform")

# Load dataset
df = pd.read_csv("EA.csv")

# Sidebar filters
st.sidebar.header("🔍 Filter Options")
departments = st.sidebar.multiselect("Select Department", df['Department'].unique())
genders = st.sidebar.multiselect("Select Gender", df['Gender'].unique())
education_fields = st.sidebar.multiselect("Select Education Field", df['EducationField'].unique())

# Apply filters
if departments:
    df = df[df['Department'].isin(departments)]
if genders:
    df = df[df['Gender'].isin(genders)]
if education_fields:
    df = df[df['EducationField'].isin(education_fields)]

# Helper to explain visual
def explain(text):
    st.markdown(f"**Insight:** {text}")

# Row 1
explain("Visualizing the overall attrition levels in the organization.")
sns.set_style("whitegrid")
fig1, ax1 = plt.subplots()
sns.countplot(data=df, x="Attrition", palette="Set2", ax=ax1)
st.pyplot(fig1)

explain("Understanding the distribution of employee ages with respect to attrition status.")
fig2 = px.histogram(df, x="Age", color="Attrition", barmode="overlay", nbins=30)
st.plotly_chart(fig2, use_container_width=True)

# Row 2
explain("Comparing attrition across departments to identify hotspots.")
fig3 = px.histogram(df, x="Department", color="Attrition", barmode="group")
st.plotly_chart(fig3, use_container_width=True)

explain("Evaluating gender-based attrition trends.")
fig4 = px.pie(df, names='Gender', hole=0.4, title='Gender Distribution by Attrition')
st.plotly_chart(fig4, use_container_width=True)

# Row 3
explain("Assessing income disparity and its link to attrition.")
fig5 = px.box(df, x="Attrition", y="MonthlyIncome", color="Attrition")
st.plotly_chart(fig5, use_container_width=True)

explain("Drilling down attrition across specific job roles.")
fig6 = px.histogram(df, x="JobRole", color="Attrition", barmode="group")
st.plotly_chart(fig6, use_container_width=True)

# Row 4
explain("Does frequent travel influence attrition?")
fig7 = px.histogram(df, x="BusinessTravel", color="Attrition", barmode="group")
st.plotly_chart(fig7, use_container_width=True)

explain("Is education field a significant factor in employee attrition?")
fig8 = px.histogram(df, x="EducationField", color="Attrition", barmode="group")
st.plotly_chart(fig8, use_container_width=True)

# Row 5
explain("Tenure distribution: are newer employees more at risk?")
fig9 = px.histogram(df, x="YearsAtCompany", color="Attrition", nbins=20)
st.plotly_chart(fig9, use_container_width=True)

explain("Does work-life balance influence attrition?")
fig10 = px.histogram(df, x="WorkLifeBalance", color="Attrition", barmode="group")
st.plotly_chart(fig10, use_container_width=True)

# Row 6
explain("Evaluating job involvement as a driver for employee retention.")
fig11 = px.histogram(df, x="JobInvolvement", color="Attrition", barmode="group")
st.plotly_chart(fig11, use_container_width=True)

explain("Are high performers leaving more?")
fig12 = px.histogram(df, x="PerformanceRating", color="Attrition", barmode="group")
st.plotly_chart(fig12, use_container_width=True)

# Row 7
explain("Heatmap to visualize correlations among key variables.")
fig13, ax13 = plt.subplots(figsize=(10,8))
sns.heatmap(df.corr(numeric_only=True), cmap="coolwarm", annot=False)
st.pyplot(fig13)

explain("Visualize the Age-Income dynamics and its correlation with attrition.")
fig14 = px.scatter(df, x="Age", y="MonthlyIncome", color="Attrition")
st.plotly_chart(fig14, use_container_width=True)

# Row 8
explain("Dynamic, filterable view of entire employee dataset.")
st.dataframe(df)

explain("Examining overtime influence on attrition.")
fig15 = px.pie(df, names='OverTime', color='Attrition', title='Overtime vs Attrition')
st.plotly_chart(fig15, use_container_width=True)

explain("Analyzing whether lack of promotion impacts attrition.")
fig16 = px.histogram(df, x="YearsSinceLastPromotion", color="Attrition")
st.plotly_chart(fig16, use_container_width=True)

# Row 9
explain("Is there a marital status pattern in attrition?")
fig17 = px.histogram(df, x="MaritalStatus", color="Attrition", barmode="group")
st.plotly_chart(fig17, use_container_width=True)

explain("Does higher education level reduce attrition?")
fig18 = px.histogram(df, x="Education", color="Attrition", barmode="group")
st.plotly_chart(fig18, use_container_width=True)

st.markdown("---")
st.success("Dashboard loaded with full insights. Use sidebar filters to explore micro-segments.")
