from sklearn import linear_model
from sklearn.preprocessing import PolynomialFeatures
import numpy as np

f, n = map(int, input().split())
factors_array = []
house_prices = []
for _ in range(n):
    *factors, house_price = map(float, input().split())
    factors_array.append(factors)
    house_prices.append(house_price)

input_factors_array = []
for _ in range(int(input())):
    factors = list(map(float, input().split()))
    input_factors_array.append(factors)
    
poly_feat = PolynomialFeatures(degree=3)
linear_reg = linear_model.LinearRegression()
linear_reg.fit(poly_feat.fit_transform(np.array(factors_array)), np.array(house_prices))

results = linear_reg.predict(poly_feat.fit_transform(np.array(input_factors_array)))
for result in results:
    print(result)