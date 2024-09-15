import random
import numpy as np
import matplotlib.pyplot as plt

probabilities = [0.01, 0.85, 0.07, 0.07]
random_variables = [1, 2, 3, 4]
cumulative_probabilities = np.cumsum(probabilities)


def inversion_method(p):
	for i, cumulative_prob in enumerate(cumulative_probabilities):
		if p < cumulative_prob:
			return random_variables[i]
	return random_variables[-1]


A1 = np.array([[0, 0],
			   [0, 0.16]])

A2 = np.array([[0.85, 0.04],
			   [-0.04, 0.85]])
A3 = np.array([[0.2, -0.26],
			   [0.23, 0.22]])
A4 = np.array([[-0.15, 0.28],
			   [0.26, 0.24]])

b1 = np.array([0, 0])
b2 = np.array([0, 1.6])
b3 = np.array([0, 1.6])
b4 = np.array([0, 0.44])

A_list = [A1, A2, A3, A4]
b_list = [b1, b2, b3, b4]

X_n = np.array([0.0, 0.0])

points = [X_n]

n_points = 10000

for _ in range(n_points):
	x = random.random()
	e_n = inversion_method(x)

	A = A_list[e_n - 1]
	b = b_list[e_n - 1]
	X_n = A @ X_n + b
	points.append(X_n)




# Graficar
x_coords = [point[0] for point in points]
y_coords = [point[1] for point in points]

# zoom_x_min = 0.0
# zoom_x_max = 2.0
# zoom_y_min = 8.0
# zoom_y_max = 10.0

plt.figure(figsize=(8, 8))
plt.plot(x_coords, y_coords, 'o', markersize=1, color='blue')
plt.title('Gráfico de los puntos generados')
plt.xlabel('X')
plt.ylabel('Y')
plt.gca().set_aspect('equal', adjustable='box')
# plt.xlim(zoom_x_min, zoom_x_max)
# plt.ylim(zoom_y_min, zoom_y_max)
plt.show()
