import euler as e
import rungeKatta4 as rk
import numpy as np
import matplotlib.pyplot as plt
# Conditions initiales et paramètres
N0 = 0  # Population initiale de sardines
P0 = 1  # Population initiale de requins
t = 10  # Temps total
n = 10  # Nombre de pas de temps
h = t / n  # Pas de temps


def functionProie(x, y):
    return x-y


def functionPredateur(x, y):
    return x+y
SardineEulerTest=[]
RequinEulerTest=[]
SardineRK4Test=[]
RequinRK4Test=[]
while n<=100:
    sardinesEuler, requinsEuler = e.euler(functionProie,functionPredateur,N0, P0, t, n, h)
    sardinesRequinsRK4 = rk.rungeKatta4IterationSysteme(functionProie,functionPredateur,N0,P0,h,t,n)
    sardinesRK4=[]
    requinsRK4=[]
    for i in sardinesRequinsRK4:
        sardinesRK4.append(i[0])
        requinsRK4.append(i[1])
    t_values = np.linspace(0, t, n + 1)
    plt.plot(t_values, sardinesEuler)
    plt.plot(t_values, requinsEuler)

    plt.plot(t_values, sardinesRK4)
    plt.plot(t_values, requinsRK4)
    n+=10


plt.xlabel('Temps (t)')
plt.ylabel('Population')
plt.legend()
plt.title("Résolution par la méthode d'Euler")
plt.grid()
plt.show()