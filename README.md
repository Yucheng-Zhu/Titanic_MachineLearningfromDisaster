## About This Repository
*Titanic - Machine Learning from Disaster* is a [*GettingStarted Prediction Competition* on Kaggle](https://www.kaggle.com/competitions/titanic/). This repository shows that a simple DNN with dropout can work very well on this problem, when the data is carefully feature engineered. It ranked at around top 3% in the Leaderboard.

## Feature Engineering
With more victims than survivors on Titanic, the data is slightly imbalanced. 

### Data Visualization
The correlations between numerical features can easily be plotted. 

#### Numerical Features
while sex and embarked location are not numberical features, they can be visualized with a sorted tokenization. It is clear that being female had the greatest impact on survivorship on Titanic, followed by sitting in the 1st class, and then paying a higher fare, embarked location, number of parents and children, age, and finally the number of siblings and spouses.

#### Non-Numerical Features
Categorical and non-numerical features were also considered. Notably, people embarked from C were the most likely to survive, follwed by Q, which only led to a slightly higher chance of survival than S. Since life boats were unequally allocated to different carbins, ticket number and carbin number give valueable insight into where the victims were, and this repository considers missing values as a separate category. People's surname were also categorized, since many victims and survivors travelled with their family.

### Bucketing
During experiment, I found that bucketing on numerical features reduces prediction accuracy, probably due to the fact that bucketing removes information that can be used by the model.


## Models
It is clear that DNN beats logistic regression in this problem. 3 layers with 512 units per layer work best experimentally. A dropout rate of 0.4 helps to deal with overfitting. 200 epochs are enough, and more epochs only lead to overfitting in this simple problem. 

## Todo
* Given that the dataset is small, it may be possible to improve the accuracy of the DNN model with k-fold cross validation.
* Comparing the result with that of a tree based gradient boost model, such as XGBoost
* Bagging and boosting with more models
