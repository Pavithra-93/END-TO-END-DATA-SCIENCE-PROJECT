# END-TO-END-DATA-SCIENCE-PROJECT

*COMPANY*: CODTECH IT SOLUTIONS

*NAME*: PAVITHRA K

*INTERN ID*: CT04DF2827

*DOMAIN*: DATA SCIENCE

*DURATION*: 4 WEEKS

*MENTOR*: NEELA SANTHOSH

## DESCRIPTION:

In this project, I developed a complete end-to-end data science workflow designed to transform raw data into actionable predictions through automated preprocessing, model training, evaluation, and deployment. This project demonstrates a professional approach to machine learning pipelines, combining Python libraries such as Pandas, scikit-learn, and Flask within the PyCharm development environment.

The project began with the data collection and extraction phase, where a CSV file containing structured tabular data was loaded using Pandas. The data included both numeric and categorical variables as well as a target column representing the outcome to be predicted. Loading the data into a DataFrame provided a convenient structure for exploring data types, detecting missing values, and preparing for transformations.

The next step was data preprocessing, which plays a critical role in determining the success of a machine learning model. The dataset was split into features and the target variable. Numeric features were handled with a pipeline consisting of two key transformations: imputing missing values with the mean of each column, and scaling features to have zero mean and unit variance using scikit-learn’s StandardScaler. Categorical features were processed through imputation of missing values using the most frequent category, followed by one-hot encoding via OneHotEncoder. This encoding transformed each categorical value into a set of binary columns, ensuring models could interpret the inputs correctly without assuming any implicit order.

These transformations were combined in a ColumnTransformer and encapsulated in a scikit-learn Pipeline, enabling consistent preprocessing during both training and inference. This design is essential for reproducibility and ensures that all steps can be saved, reloaded, and applied consistently to any new data.

After preprocessing, the transformed dataset was saved as a CSV file, ready for modeling. A classification model was then built using scikit-learn’s LogisticRegression to predict the target variable. The model was trained on the cleaned dataset and evaluated using metrics such as accuracy to assess its predictive performance. Hyperparameters could be fine-tuned to optimize results further.

To demonstrate real-world applicability, the project also included a model deployment component. The trained model and preprocessing scaler were serialized and saved to disk using joblib. A lightweight REST API was implemented using Flask. The API script loaded the saved model and scaler, defined a route that accepts JSON input, applied the same preprocessing steps to incoming data, and returned model predictions as a JSON response. This setup made it possible to serve predictions over HTTP, providing an accessible interface for other applications or users.

All development took place in PyCharm, where project folders, Python virtual environments, and dependencies were managed in an organized structure. The environment ensured clean separation between different tasks, such as preprocessing pipelines, model training scripts, and deployment code. This approach reflects professional standards for data science workflows, combining clarity, modular design, and reproducibility.

This end-to-end data science project demonstrates the full cycle of transforming raw data into meaningful insights and deployable services, showcasing how Python libraries can work together seamlessly to deliver robust machine learning solutions.

### OUTPUT:

![Image](https://github.com/user-attachments/assets/b62b26f4-7def-4e08-911d-a2304de9f131)
