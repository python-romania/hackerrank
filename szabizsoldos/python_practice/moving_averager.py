# MA example
from statsmodels.tsa.arima_model import ARMA

# contrived dataset
data = [7865, 12881, 6913, 7271, 9754, 9135, 8850, 10309, 8133, 8637, 6813, 6531, 9545]
# fit model
model = ARMA(data, order=(0, 1))
model_fit = model.fit(disp=False)
# make prediction
yhat = model_fit.predict(len(data), len(data))
print(round(float(yhat), 2))
