# Import necessary libraries
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
import json
import os

DEVELOPMENT = False

if not os.path.isfile("chosen.json"):
	with open("chosen.json", "w") as f:
		f.write("[0, 25]")

data_list = json.load(open("chosen.json"))

y = np.array(data_list)
x = np.arange(len(data_list)).reshape(-1, 1)  # Reshape to make it a 2D array

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.1, random_state=42)

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(x_train, y_train)

y_pred = model.predict(x)

mse = mean_squared_error(y, y_pred)
print(f"Mean Squared Error: {mse}")

if DEVELOPMENT:
	plt.scatter(x, y.flatten(), color="black", label="Actual")
	plt.scatter(x, y_pred, color="red", label="Predicted")
	plt.xlabel("Sequence")
	plt.ylabel("Value")
	plt.legend()
	plt.show()

val = int(input("Enter a new value (0-25): "))
data_list.append(val)
new_input = np.array([[val]])

prediction = model.predict(new_input)

print(f"Prediction for {new_input[0, 0]}: {prediction[0]}")

with open("chosen.json", "w") as file:
	json.dump(data_list, file)