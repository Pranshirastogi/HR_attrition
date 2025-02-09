# Dataset
 
  Dataset Name: HR Attrition Analysis
  This dataset was clean, with no missing or duplicate values.

# Libraries Used

The following libraries were used for data manipulation, visualization, and modeling:

- numpy: For numerical computations.
- pandas: For data handling and preprocessing.
- matplotlib: For static data visualizations.
- seaborn: For advanced visualization and trend analysis.
- plotly: For interactive visualizations.
- sklearn: For machine learning modeling and evaluation.
- pickle: For model serialization and deployment.

# EDA Summary

The dataset was already clean with the following characteristics:
- No missing values and no duplicate values were present.

# Key Insights from Data Visualizations:

- Business Travel:
Most employees prefer traveling rarely or frequently, with Sales Executives being the ones who travel the most rarely.

- Monthly Income:
There is a slight difference in monthly income between males and females across various job roles.
Employees aged 30-40 have the highest monthly income in the organization.

- Job Satisfaction:
Employees in the Sales Executive and Research Scientist roles exhibit the highest job satisfaction.
Employees aged 30-40 also display the highest job satisfaction.

- Attrition:
Employees aged 30-40, especially those who are married, exhibit the highest attrition rates.
Employees without attrition have typically worked for more than 10 years, both in the organization and in their current roles.

- Current Manager Relationship:
Research Directors with no attrition have worked with their current manager for more than 10 years, which is longer than other roles.

- Salary Insights:
Employees with a monthly income between 5000-10000 enjoy the highest percent salary hikes.
Human Resources employees receive the highest percentage salary hike.

- Performance Ratings:
Employees with no attrition tend to have the highest performance ratings, with Sales Executives leading this category.

- Work-Life Balance:
Sales Executives have the highest work-life balance, job satisfaction, overtime pay, and monthly rate in the organization.

# ML Model Development

- Objective:

 - The primary goal of the model was to predict employee attrition.
 - The target (dependent) variable is Attrition, and the independent variables include features like Age, BusinessTravel, Department, MonthlyIncome, OverTime, etc.

- Data Preprocessing:

 - Applied Label Encoding and One-Hot Encoding to handle categorical features.
 - Performed Standard Scaling on numerical features to normalize the data.

- Model Selection:

 - Used Logistic Regression for prediction due to its simplicity and interpretability.
 - Trained the model on a balanced dataset after addressing class imbalance.

- Model Evaluation:

 - Achieved approximately 85% accuracy on both the training and test datasets.
 - Used a confusion matrix and a classification report to evaluate performance.
 - The initial model showed low sensitivity, indicating difficulty in correctly predicting attrition cases.

- Optimization:

 - Performed Grid Search Cross-Validation to fine-tune hyperparameters for better performance.
 - Incorporated class weights to handle imbalanced data and improve sensitivity while maintaining accuracy.

- Final Model:

 - The balanced Logistic Regression model performed well, achieving improvements in both sensitivity and accuracy.
 - The final model was saved as a pickle file for deployment.

# Streamlit App

- App Features:

 - Built an interactive Streamlit app (dapp.py) to visualize the data insights and predict employee attrition.
 - The app allows users to input various employee attributes (like Age, JobRole, MonthlyIncome, etc.) and provides a prediction on whether    the employee is likely to leave.

- Visualization Module:

 - Included key data visualizations highlighting trends like monthly income differences, attrition rates, and work-life balance across job roles.

- Prediction Module:

 - Integrated the trained Logistic Regression model using the pickle file.
 - The app predicts attrition based on user inputs and displays the prediction with probabilities.

- Deployment:

 - The Streamlit app enables real-time predictions for employee attrition, providing HR teams with actionable insights.
 - This project effectively combines EDA insights, Machine Learning modeling, and Streamlit deployment to address employee attrition prediction, delivering a user-friendly and insightful solution for decision-making.

# Conclusion

 - This project integrates Exploratory Data Analysis, Machine Learning, and Streamlit Deployment to offer a practical solution for employee attrition prediction. By identifying key patterns and providing real-time predictive capabilities, it empowers organizations to take proactive measures in retaining talent and improving workforce management.