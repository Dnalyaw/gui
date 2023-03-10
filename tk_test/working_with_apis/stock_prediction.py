import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pandas_datareader as web
import datetime as dt

from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, LSTM

#load Data
company = 'TSLA'
start = dt.datetime(2012, 1, 1)
end = dt.datetime(2020, 1, 1)

data = web.DataReader(company, 'yahoo', start, end)#lookup facebook stock from yahoo finance api from start to end

#prepare data
scaler = MinMaxScaler(feature_range=(0,1))#puts values together so they fit in as values between zero and one
scaled_data = scaler.fit_transform(data['Close'].values.reshape(-1, 1))#predicting the close price; reshape for format

prediction_days = 60#how many days we want to look in the past to look into the future

x_train = []
y_train = []#training data

for x in range(prediction_days, len(scaled_data)):#starting from the 60th index to the last index
    x_train.append(scaled_data[x-prediction_days:x, 0])#adding the scaled data to x_train; 60 days
    y_train.append(scaled_data[x, 0])  #61st day

x_train, y_train = np.array(x_train), np.array(y_train)#converting to numpy arrays
x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))#reshape to work with the neural network

#build the model
model = Sequential()
model.add(LSTM(units=50, return_sequences=True, input_shape=(x_train.shape[1], 1)))    #layers
model.add(Dropout(0.2))
model.add(LSTM(units=50, return_sequences=True))    #layers
model.add(Dropout(0.2))
model.add(LSTM(units=50))    #layers
model.add(Dropout(0.2))
model.add(Dense(units=1))#prediction of the next price adj closing value

model.compile(optimizer='adam', loss='mean_squared_error')
model.fit(x_train, y_train, epochs=25, batch_size=32)






'''TESTING THE MODEL ACCURACY ON EXISTING DATA'''

#Load Test Data
test_start = dt.datetime(2020, 1, 1)
test_end = dt.datetime.now()

test_data = web.DataReader(company, 'yahoo', test_start, test_end)
actual_prices = test_data['Adj Close'].values

total_dataset = pd.concat((data['Close'], test_data['Close']), axis=0)

model_inputs = total_dataset[len(total_dataset)-len(test_data)-prediction_days:].values#what model will see as an input
model_inputs = model_inputs.reshape(-1, 1)
model_inputs = scaler.transform(model_inputs)

#make predictions on test data

x_test = []

for x in range(prediction_days, len(model_inputs)):
    x_test.append(model_inputs[x - prediction_days:x, 0])  # adding the scaled data to x_train; 60 days

x_test = np.array(x_test)
x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))

predicted_prices = model.predict(x_test)#prediction time
predicted_prices = scaler.inverse_transform(predicted_prices)#since the predicted prices are going to be scaled, we need to reverse scale them

#plot the test predictions
plt.plot(actual_prices, color="black", label=f'Actual {company} price')
plt.plot(predicted_prices, color="green", label=f'Predicted {company} price')
plt.title(f"{company} Share Price")
plt.xlabel('Time')
plt.ylabel(f'{company} Share Price')
plt.legend()
plt.show()

#predict tommorow

real_data = [model_inputs[len(model_inputs) + 1 - prediction_days:len(model_inputs+1), 0]]
real_data = np.array(real_data)
real_data = np.reshape(real_data, (real_data.shape[0], real_data.shape[1], 1))
print(real_data)

print(scaler.inverse_transform(real_data[-1]))
prediction = model.predict(real_data)
prediction = scaler.inverse_transform(prediction)
print(f"Prediction: {prediction}")

