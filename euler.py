import numpy as np
import matplotlib.pyplot as plt
x0 = 1          # Condition initiale pour x(0)
y0 = 2          # Condition initiale pour y(0)
T = 2           # Intervalle de temps [0, T]
n = 100         # Nombre de pas
h = T / n       # Taille du pas

def F(x,y):
    return x + y

def G(x,y):
    return x + y

t_values = np.linspace(0, T, n+1)
Xk = np.zeros(n+1)
Yk = np.zeros(n+1)

Xk[0] = x0
Yk[0] = y0

for k in range(n) :
    Xk[k +1] = Xk[k] + h * F(Xk[k], Yk[k])
    Yk[k +1] = Yk[k] + h * G(Xk[k], Yk[k])
    
for k in range(n+1):
    print(f"t = {t_values[k]:.2f}, Xk = {Xk[k]:.5f}, Yk = {Yk[k]:.5f}")

plt.plot(t_values, Xk, label='x(t)')
plt.plot(t_values, Yk, label='y(t)')
plt.xlabel('Temps t')
plt.ylabel('Valeurs')
plt.legend()
plt.title("Résolution par la méthode d'Euler")
plt.grid()
plt.show()
