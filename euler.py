import numpy as np
import matplotlib.pyplot as plt

def euleur(F, G, x0, y0, t, n, h):
    t_values = np.linspace(0, t, n+1)
    Xk = np.zeros(n+1)
    Yk = np.zeros(n+1)

    Xk[0] = x0
    Yk[0] = y0

    for k in range(n):
        Xk[k + 1] = Xk[k] + h * F(Xk[k], Yk[k])
        Yk[k + 1] = Yk[k] + h * G(Xk[k], Yk[k])

    for k in range(n+1):
        print("t = ", t_values[k], " N = ", Xk[k], " P = ", Yk[k])
    
    plt.plot(t_values, Xk, label='Sardines (N)')
    plt.plot(t_values, Yk, label='Requins (P)')
    plt.xlabel('Temps (t)')
    plt.ylabel('Population')
    plt.legend()
    plt.title("Résolution par la méthode d'Euler")
    plt.grid()
    plt.show()