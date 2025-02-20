import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression                                                       
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score


async def supervised_learning_alg(user_query,operation, sub_operation,Area):
    if operation == 'linear_regression':
        if sub_operation == 'single_linear':
            linear_regression = await single_lin_reg(user_query,Area)
    return linear_regression 


"""Single Linear Regression is a statistical method that establishes a relationship between one dependent variable and one independent variable.
It models the relationship using an equation of the form:

[ y = \beta_0 + \beta_1 x + \epsilon \]
y = Mx+c

where:
- \( y \) is the dependent variable,
- \( x \) is the independent variable,
- \( \beta_0 \) or c is the intercept (the value of \( y \) when \( x = 0 \)),
- \( \beta_1 \) or M is the slope (the change in \( y \) for a one-unit increase in \( x \)),
- \( \epsilon \) is the error term, representing random noise.

### Key Components:
1. **Slope (\( \beta_1 \))**: Measures how much \( y \) changes with a unit change in \( x \).
2. **Intercept (\( \beta_0 \))**: The value of \( y \) when \( x = 0 \), though it may not always be meaningful depending on the context.
3. **Error Term (\( \epsilon \))**: Represents random variations that cannot be explained by the model.

### Assumptions:
- Linearity: The relationship between \( x \) and \( y \) is linear.
- Homoscedasticity: The variance of \( y \) is constant across all levels of \( x \).
- Independence: Observations are independent of each other.
- Normality: Errors are normally distributed.

### Steps to Perform Single Linear Regression:
1. **Collect Data**: Gather pairs of observations for the dependent and independent variables.
2. **Plot Data**: Visualize the relationship between \( x \) and \( y \). If a linear relationship is observed, proceed with regression.
2. **Plot Data**: Visualize the relationship between \( x \) and \( y \). If a linear relationship is observed, proceed with regression.
3. **Estimate Parameters**: Calculate the intercept (\( \beta_0 \)) and slope (\( \beta_1 \)) that minimize the sum of squared errors.
4. **Evaluate Model**: Check goodness of fit using metrics like \( R^2 \), p-values for coefficients, and residual plots.
5. **Make Predictions**: Use the regression equation to predict \( y \) for new values of \( x \).   
6. **Interpret Results**: Understand the relationship between the variables and the predictive power of the model.  """

async def single_lin_reg(user_query,Area):
        df = pd.read_csv(r'sl1.csv')
        print(df.head())
        print(df.shape)
        print(df.describe())  
        features = df.drop(columns = 'Price')  
        target = df['Price'] 

        # Create training and testing datasets
        x_train, x_test, y_train, y_test = train_test_split(features,target, train_size = 0.7, random_state = 10) 
       
        # Model building 
        lin_model = LinearRegression()

        # Fit the model or train the model
        lin_model.fit(x_train, y_train) 
        # model evaluation
        ypred = lin_model.predict(x_train)
        print("ypred",ypred)

        # R2 score or finding accuracy
        r2 = r2_score(y_train, ypred)
        print("Accuracy",r2)

        # Model parameters
        b1 = lin_model.coef_
        print("b1",b1)
        b0 = lin_model.intercept_
        print("b0",b0)
        # y = b0 + b1x

        print("Model training complete")
       ## new data prediction
        new_data = pd.DataFrame([[Area]], columns=['Area'])
        price_y = lin_model.predict(new_data)  
        print("Predicted Price for the given Area is:",type(price_y[0]),price_y[0]) 

        return price_y[0]

