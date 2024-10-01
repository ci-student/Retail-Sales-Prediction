# Retail Sales Prediction Project

## Dataset Content and Explanation

This project uses a retail dataset sourced from Kaggle, containing historical sales data for 45 stores. The dataset consists of three main tables:

- **Stores**: Provides anonymized information about each store, including store type and size.
- **Features**: Contains store, department, and regional data like temperature, fuel prices, markdowns, CPI, unemployment, and whether the week includes a major holiday.
- **Sales**: Historical weekly sales data from 2010-02-05 to 2012-11-01, including store number, department number, weekly sales, and holiday flags.

## Business Requirements

1. **Predict Department Sales**: The main goal is to predict department-wide sales for each store in the following year.
2. **Analyze Markdown Effects**: Evaluate the impact of markdowns on sales, particularly during holiday weeks.
3. **Provide Strategic Recommendations**: Offer actionable insights to maximize business impact, especially around key holidays such as the Super Bowl, Labor Day, Thanksgiving, and Christmas.

## Hypothesis and Validation

### Hypothesis 1:
Markdown events before holidays have a significant positive effect on sales.
- **Validation**: Use time series analysis and hypothesis testing (e.g., t-tests) to compare sales during markdown periods vs. non-markdown periods.

### Hypothesis 2:
Sales increase in stores with larger size or specific store types.
- **Validation**: Build machine learning models incorporating store size and type as features to assess their impact on sales predictions.

## Mapping Business Requirements to Visualizations and ML Tasks

- **Business Requirement 1**: Predicting department-wise sales maps to building predictive models (time series forecasting, regression models).
- **Business Requirement 2**: Visualizations showing markdown effect on sales during holiday periods, comparing markdown vs. non-markdown sales.
- **ML Tasks**: Train models (e.g., Random Forest, Gradient Boosting) to predict sales and understand feature importance related to markdowns, CPI, and holiday effects.

## Machine Learning Business Case

- **Objective**: Develop a model that predicts future sales, enabling the company to optimize inventory and promotional strategies.
- **Approach**: Leverage historical data on markdowns, store features, and past sales to train machine learning models (e.g., Regression, Random Forest) for accurate sales prediction. Feature engineering will focus on creating holiday indicators, lag variables for sales, and markdown imputation.

## Dashboard Design

The project will deploy an interactive Tableau Public dashboard showcasing:
- Sales trends across stores and departments.
- Markdown effects on holiday and non-holiday sales.
- Sales predictions for future periods, highlighting high-sales weeks for inventory planning.

## Unfixed Bugs

No known bugs at this time. Continuous testing and model validation will ensure robust performance.

## Deployment

The machine learning model and Tableau dashboard will be deployed using:
- **Tableau Public** for visualizing trends and markdown effects.
- **Jupyter Notebooks** for data handling and analysis.
- GitHub will host the project and include detailed documentation.

## Main Data Analysis and Machine Learning Libraries

- **Data Manipulation**: `Pandas`, `NumPy`
- **Data Visualization**: `Seaborn`, `Matplotlib`, `Plotly`, `Tableau Public`
- **Machine Learning**: `Scikit-learn`, `Random Forest`, `Statsmodels`
- **Deployment**: `Flask`, `Heroku` or similar cloud service

## Credits

This project is based on the retail dataset provided by Manjeet Singh on Kaggle.

## Acknowledgements (optional)

A special thanks to the Kaggle community for data-sharing and providing an environment for developing data analysis and machine learning projects.
