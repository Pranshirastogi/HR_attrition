import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px 
import pickle 
st.title('HR-EMPLOYEE-ATTRITION')
st.markdown('''**HR-EMPLOYEE-ATTRITION** is a web app to predict the attrition of an employee in an organization.
            This app shows the prediction of attrition of an employee based on the data provided by the user.
            And also understanding the employees behaviour and their performance in the organization.
            Also things affecting the attrition of an employee in the organization.
            ''')
df=pd.read_csv('HR-Employee-Attrition.csv')
df=df.drop(['EmployeeCount','EmployeeNumber','Over18','StandardHours'],axis=1)
st.subheader('Data Information:')
if st.sidebar.checkbox('Show Data'):
    st.subheader('Raw Data')
    st.write(df)
if st.sidebar.checkbox('Show Shape'):
    st.subheader('Data Shape:')
    st.write(df.shape)
if st.sidebar.checkbox('Show Columns'):
    st.subheader('Columns Names:')
    st.write(df.columns)  
if st.sidebar.checkbox('Attribute Information'):
    st.subheader('Attrition Count:')
    st.write(df['Attrition'].value_counts())
    st.subheader('Attrition Percentage:')
    st.write(df['Attrition'].value_counts()/df.shape[0]*100)
if st.sidebar.subheader('Visualization Selector:'):
    if st.sidebar.checkbox('Types of Job Roles'):
        fig1 = px.pie(df, names='JobRole', title='Job Role') 
        st.plotly_chart(fig1)
        st.subheader('Data Analysis:')
        st.write('**Sales Executive** has the highest number of employees in the organization.Followed by **Research Scientist** and **Laboratory Technician**.')
    if st.sidebar.checkbox('Business Travel'):
        fig2 = px.bar(df,x='JobRole', y='BusinessTravel',facet_col='BusinessTravel',color='JobRole', title='Business Travel by Job Role',height=600,width=800)
        st.plotly_chart(fig2)
        st.subheader('Data Analysis:')
        st.write('**Sales Executives** travels the most rarely in the organization.And by the visualisation of data we can see employees prefer traveling rarely or frequently. ')
    if st.sidebar.checkbox('Monthly Income by Gender division'):
        fig3 = px.violin(df, x='JobRole', y='MonthlyIncome', color='JobRole',facet_col='Gender', title='Monthly Income by Job Role')
        st.plotly_chart(fig3)
        st.subheader('Data Analysis:')
        st.write('There is slight difference between montly incomes of males and females in the organization irrespective of their job roles. ')
    if st.sidebar.checkbox('Monthly Income by Age'):
        fig4 = px.scatter(df, x='MonthlyIncome', y='Age', color='JobRole', title='Monthly Income by Age')
        st.plotly_chart(fig4)
        st.subheader('Data Analysis:')
        st.write('Employees with age between 30 to 40 have the highest monthly income in the organization.')
    if st.sidebar.checkbox('Job Satisfaction by Job Role'):
        fig5 = px.histogram(df, x='JobRole', y='JobSatisfaction',facet_col='Attrition', color='JobRole', title='Job Satisfaction by Job Role')
        st.plotly_chart(fig5)
        st.subheader('Data Analysis:')
        st.write('Employees with job role **Sales Executive** and **Research Scientist** have the highest job satisfaction in the organization.')
    if st.sidebar.checkbox('Marital Status'):
        fig6 = px.bar(df,x='Age',y='MaritalStatus',facet_col='Gender',color='Attrition',title='Marital Status by Age')
        st.plotly_chart(fig6)
        st.subheader('Data Analysis:')
        st.write('Employees with age between 30 to 40 are married and have the highest attrition rate in the organization.')
    if st.sidebar.checkbox('Job Satisfaction by Age'):
        fig7 = px.histogram(df,x='Age',y='JobSatisfaction',color='Gender',title='Job Satisfaction by Age')
        st.plotly_chart(fig7)
        st.subheader('Data Analysis:')
        st.write('Employees with age between 30 to 40 have the highest job satisfaction in the organization.')
    if st.sidebar.checkbox('Years worked at company'):
        fig8 = px.scatter(df,x='Age',y='YearsAtCompany',facet_col='Attrition',title='Years at Company by Age')
        st.plotly_chart(fig8)
        st.subheader('Data Analysis:')
        st.write('Employees with no attrition have worked for more than 10 years in the organization than the employees with attrition.')
    if st.sidebar.checkbox('Years worked in current role'):
        fig9 = px.bar(df,x='JobRole',y='YearsInCurrentRole',facet_col='Attrition',title='Years in Current Role by Age')
        st.plotly_chart(fig9)
        st.subheader('Data Analysis:')
        st.write('Employees with no attrition have worked for more than 10 years in the organization than the employees with attrition in the current roles.')
    if st.sidebar.checkbox('Years worked with current manager'):
        fig10 = px.box(df,x='JobRole',y='YearsWithCurrManager',facet_col='Attrition',color='JobRole',title='Years with Current Manager by Age')
        st.plotly_chart(fig10)
        st.subheader('Data Analysis:')
        st.write('**Research Directors**have worked for more than 10 years with current manager than the employees with attrition than the employees of other roles.')
    if st.sidebar.checkbox('Percent salary hike'):
        fig11 = px.histogram(df,x='MonthlyIncome',y='PercentSalaryHike',facet_col='Gender',color='JobRole',title='Percent Salary Hike by Monthly Income') 
        st.plotly_chart(fig11)
        st.subheader('Data Analysis:')
        st.write('Employees with monthly income between 5000 to 10000 have the highest percent salary hike in the organization.**Human resource** employees have the greatest percent salary hike in the organization.')
    if st.sidebar.checkbox('Performance rating'):
        fig12 = px.bar(df,x='JobRole',y='PerformanceRating',facet_col='Attrition',color='JobRole',title='Performance Rating by Job Role')
        st.plotly_chart(fig12)
        st.subheader('Data Analysis:')
        st.write('Employees with no attrition have the highest performance rating in the organization.And **Sales Executive** has the highest performance rating in the organization.')
    if st.sidebar.checkbox('Work life balance'):
        fig13 = px.funnel(df,x='JobRole',y='WorkLifeBalance',color='JobRole',title='Work Life Balance by Job Role')
        st.plotly_chart(fig13)
        st.subheader('Data Analysis:')
        st.write('Employees with job role **Sales Executive** have the highest work life balance in the organization.')
    if st.sidebar.checkbox('Show tree map'):
        fig14 = px.treemap(df,path=['JobRole','OverTime','JobSatisfaction'],values='MonthlyIncome',title='Job Satisfaction by Job Role and Overtime')
        st.plotly_chart(fig14)
        st.subheader('Data Analysis:')
        st.write('Employees with job role **Sales Executive** have the highest job satisfaction and highest pay with over time in the organization.')
        fig15 = px.treemap(df,path=['EducationField','Department','JobRole'],values='MonthlyRate',title='Montly rate by educational field and department')
        st.plotly_chart(fig15)
        st.subheader('Data Analysis:')
        st.write('Employees with job role **Sales Executive** have the highest montly rate in the organization after calculating their education field depatment and job role.')

# Load the trained model
model_path = 'bal_model.pkl'  # Replace with your actual model file
with open(model_path, 'rb') as file:
    model = pickle.load(file)

# Function to encode categorical inputs
def encode_inputs(data):
    # Replace categorical string values with numerical codes
    data['BusinessTravel'] = {'Non-Travel': 0, 'Travel_Rarely': 2, 'Travel_Frequently': 1}[data['BusinessTravel']]
    data['Department'] = {'Sales': 2, 'Research & Development': 1, 'Human Resources': 0}[data['Department']]
    data['EducationField'] = {
        'Life Sciences': 1, 'Medical': 3, 'Marketing': 2, 
        'Technical Degree': 5, 'Other': 4, 'Human Resources': 0
    }[data['EducationField']]
    data['JobRole'] = {
        'Sales Executive': 7, 'Research Scientist': 6, 'Laboratory Technician': 2,
        'Manufacturing Director': 4, 'Healthcare Representative': 0, 'Manager': 3,
        'Sales Representative': 8, 'Research Director': 5, 'Human Resources': 1
    }[data['JobRole']]
    data['MaritalStatus'] = {'Married': 1, 'Single': 2, 'Divorced': 0}[data['MaritalStatus']]
    return data

# Function to collect user input
def user_input_features():
    age = st.sidebar.slider('Age', 18, 60, 30)
    business_travel = st.sidebar.selectbox('BusinessTravel', ['Non-Travel', 'Travel_Rarely', 'Travel_Frequently'])
    daily_rate = st.sidebar.slider('DailyRate', 100, 1500, 500)
    department = st.sidebar.selectbox('Department', ['Sales', 'Research & Development', 'Human Resources'])
    distance_from_home = st.sidebar.slider('DistanceFromHome', 1, 30, 10)
    education = st.sidebar.selectbox('Education', (1, 2, 3, 4, 5))
    education_field = st.sidebar.selectbox('EducationField', [
        'Life Sciences', 'Medical', 'Marketing', 
        'Technical Degree', 'Other', 'Human Resources'
    ])
    employee_number = st.sidebar.slider('EmployeeNumber', 1, 2068, 1000)
    environment_satisfaction = st.sidebar.slider('EnvironmentSatisfaction', 1, 4, 3)
    hourly_rate = st.sidebar.slider('HourlyRate', 50, 100, 70)
    job_involvement = st.sidebar.slider('JobInvolvement', 1, 4, 3)
    job_level = st.sidebar.slider('JobLevel', 1, 5, 3)
    job_role = st.sidebar.selectbox('JobRole', [
        'Sales Executive', 'Research Scientist', 'Laboratory Technician', 
        'Manufacturing Director', 'Healthcare Representative', 'Manager', 
        'Sales Representative', 'Research Director', 'Human Resources'
    ])
    job_satisfaction = st.sidebar.slider('JobSatisfaction', 1, 4, 3)
    marital_status = st.sidebar.selectbox('MaritalStatus', ['Married', 'Single', 'Divorced'])
    monthly_income = st.sidebar.slider('MonthlyIncome', 1000, 20000, 5000)
    monthly_rate = st.sidebar.slider('MonthlyRate', 2000, 25000, 5000)
    num_companies_worked = st.sidebar.slider('NumCompaniesWorked', 0, 10, 5)
    percent_salary_hike = st.sidebar.slider('PercentSalaryHike', 10, 25, 15)
    performance_rating = st.sidebar.slider('PerformanceRating', 1, 4, 3)
    relationship_satisfaction = st.sidebar.slider('RelationshipSatisfaction', 1, 4, 3)
    stock_option_level = st.sidebar.slider('StockOptionLevel', 0, 3, 1)
    total_working_years = st.sidebar.slider('TotalWorkingYears', 0, 40, 10)
    training_times_last_year = st.sidebar.slider('TrainingTimesLastYear', 0, 10, 3)
    work_life_balance = st.sidebar.slider('WorkLifeBalance', 1, 4, 3)
    years_at_company = st.sidebar.slider('YearsAtCompany', 0, 40, 5)
    years_in_current_role = st.sidebar.slider('YearsInCurrentRole', 0, 20, 2)
    years_since_last_promotion = st.sidebar.slider('YearsSinceLastPromotion', 0, 15, 1)
    years_with_curr_manager = st.sidebar.slider('YearsWithCurrManager', 0, 15, 2)
    over_time = st.sidebar.slider('OverTime_Yes', 0, 1)
    gender = st.sidebar.slider('Gender_Male', 0, 1)

    # Store inputs in a dictionary
    data = {
        'Age': age,
        'BusinessTravel': business_travel,
        'DailyRate': daily_rate,
        'Department': department,
        'DistanceFromHome': distance_from_home,
        'Education': education,
        'EducationField': education_field,
        'EmployeeNumber': employee_number,
        'EnvironmentSatisfaction': environment_satisfaction,
        'HourlyRate': hourly_rate,
        'JobInvolvement': job_involvement,
        'JobLevel': job_level,
        'JobRole': job_role,
        'JobSatisfaction': job_satisfaction,
        'MaritalStatus': marital_status,
        'MonthlyIncome': monthly_income,
        'MonthlyRate': monthly_rate,
        'NumCompaniesWorked': num_companies_worked,
        'PercentSalaryHike': percent_salary_hike,
        'PerformanceRating': performance_rating,
        'RelationshipSatisfaction': relationship_satisfaction,
        'StockOptionLevel': stock_option_level,
        'TotalWorkingYears': total_working_years,
        'TrainingTimesLastYear': training_times_last_year,
        'WorkLifeBalance': work_life_balance,
        'YearsAtCompany': years_at_company,
        'YearsInCurrentRole': years_in_current_role,
        'YearsSinceLastPromotion': years_since_last_promotion,
        'YearsWithCurrManager': years_with_curr_manager,
        'OverTime_Yes': over_time,
        'Gender_Male': gender
    }
    
    # Encode categorical features
    data = encode_inputs(data)
    return pd.DataFrame(data, index=[0])

# Streamlit app
st.title("Employee Attrition Prediction App")

st.markdown("""
### How to Use:
1. Adjust the sliders in the sidebar to input employee features.
2. See the prediction and probabilities in the main view.
3. This app uses Logistic Regression to predict employee attrition.
""")

# Get user input
user_data = user_input_features()

st.subheader("User Input Features")
st.write(user_data)

# Predict using the loaded model
user_data_array = user_data.values  
prediction = model.predict(user_data_array)
prediction_proba = model.predict_proba(user_data_array)

# Display results
attrition = "Yes" if prediction[0] == 1 else "No"
st.subheader("Prediction")
st.write(f"Predicted Attrition: **{attrition}**")

st.subheader("Prediction Probability")
st.write(f"Attrition: {prediction_proba[0][1]:.2f}")
st.write(f"No Attrition: {prediction_proba[0][0]:.2f}")
