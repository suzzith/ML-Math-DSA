import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt


#sample data 
# x->hours studied y->marks obtained

x = np.array([[1], [2], [3], [4], [5]])
y = np.array([30, 40, 50, 65, 80])


#train the model

model = LinearRegression()
model.fit(x,y)

#predict marks 

pred = model.predict([[6]])
print("predicted marks for 6 hours:",pred[0])

#visualizing

plt.scatter(x, y, color='blue', label='Actual')
plt.plot(x, model.predict(x), color='red', label='Predicted Line')
plt.xlabel('Hours Studied')
plt.ylabel('Marks')
plt.title('Simple Linear Regression')
plt.legend()
plt.show()


