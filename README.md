<img src="https://cdn2.iconfinder.com/data/icons/real-estate-60/300/12-512.png" align="left" width="58">

# Kaggle House Pricing (Competition)

---

My submission is in the top 25% of the leaderboard... however, many of the top scores above mine are a product of cheating/memorization as they have a RMSE of almost a true 0 due to the fact that their is not limit to the amount of submissions per user.

The contents of the notebook are:

### EDA
* DataFrame shape/statistics
* Analysis of null values
* Checking correlations between features (correlation heatmap and pairplot).
* Observing errros/obvious outliers

### Feature Engineering

* Imputing LotFrontage based on the neighborhood
* Imputing mean or zero values based on column EDA (numerical data)
* Label Binarizing/Encoding (catergorical data)

### Outliers

* Train model using ElasticNet
* Removing data that is more than 6 std's from ENet mean

### Model Optimization

* GridSeach multiple values for multiple hyperparameters
* CrossFold validation on each search
