import numpy as np
from matplotlib import pyplot as plt

data = np.array([[3.34, 14],
		[6.55, 24],
		[9.08, 11],
		[5.12, 20],
		[8.24, 20]
				 ])

plt.scatter(data[:, 0], data[:, 1])
plt.title("Positive Review / Score")
plt.xlabel("Score (n)")
plt.ylabel("Positive Review (n)")
plt.axis([0, 10, 0, 30])
plt.show()


def qr_householder(A):
	m, n = A.shape
	Q = np.eye(m)  # Orthogonal transform so far
	R = A.copy()  # Transformed matrix so far

	for j in range(n):
		# Find H = I - beta*u*u' to put zeros below R[j,j]
		x = R[j:, j]
		normx = np.linalg.norm(x)
		rho = -np.sign(x[0])
		u1 = x[0] - rho * normx
		u = x / u1
		u[0] = 1
		beta = -rho * u1 / normx

		R[j:, :] = R[j:, :] - beta * np.outer(u, u).dot(R[j:, :])
		Q[:, j:] = Q[:, j:] - beta * Q[:, j:].dot(np.outer(u, u))

	return Q, R

m, n = data.shape
A = np.array([data[:,0], np.ones(m)]).T
b = data[:, 1]

Q, R = qr_householder(A)
b_hat = Q.T.dot(b)

R_upper = R[:n, :]
b_upper = b_hat[:n]

print(R_upper, b_upper)

x = np.linalg.solve(R_upper, b_upper)
slope, intercept = x