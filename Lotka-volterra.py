import euler as e
import numpy as np
import matplotlib.pyplot as plt
import rungeKatta4 as rk


def sardine(N, P):
    a = 0.1  # Taux de croissance des sardines
    b = 0.01 # Taux de prédation des sardines par les requins
    dNdt = a * N - b * N * P  # Changement de la population des sardines
    return dNdt

def sardine_avec_peche(N,P):
    a = 0.1  # Taux de croissance des sardines
    b = 0.01 # Taux de prédation des sardines par les requins
    h = 0.01 # Taux de pêche de sardine par l'homme
    dNdt = a * N - b * N * P - h * P  # Changement de la population des sardines
    return dNdt

def requin(N,P):
    c = 0.5  # Taux de mortalité des requins
    d = 0.01 # Taux de reproduction des requins par sardine capturée
    dPdt = -c * P + d * N * P  # Changement de la population des requins
    return dPdt


# Conditions initiales et paramètres
N0 = 30  # Population initiale de sardines
P0 = 10  # Population initiale de requins
t = 100  # Temps total
n = 1000 # Nombre de pas de temps
h = t / n  # Pas de temps

sardines, requins = e.euler(sardine_avec_peche,requin,N0, P0, t, n, h)
sardinesRequinsRK4 = rk.rungeKatta4IterationSysteme(sardine_avec_peche,requin,N0,P0,h,t,n)
sardinesRK4=[]
requinsRK4=[]
for i in sardinesRequinsRK4:
    sardinesRK4.append(i[0])
    requinsRK4.append(i[1])


t_values = np.linspace(0, t, n+1)
plt.plot(t_values, sardines, label='Sardines (N)')
plt.plot(t_values, requins, label='Requins (P)')
plt.plot(t_values, sardinesRK4, label='Sardines RK4 (N)')
plt.plot(t_values, requinsRK4, label='Requins RK4(P)')
plt.xlabel('Temps (t)')
plt.ylabel('Population')
plt.legend()
plt.title("Résolution par la méthode d'Euler")
plt.grid()
plt.show()

