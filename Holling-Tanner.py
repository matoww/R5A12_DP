import euler as e
import runge-katta-4 as rk
import numpy as np
import matplotlib.pyplot as plt


def functionProie(x,y):
    r=0 #taux de croissance des proies
    K=1000 #capacité maximale des proies
    m=10 #nombre maximale de proie consommable par un prédateur en une unité de temps
    A=m/2
    return x*r(1-x/K)-(m*x*y)/(x+A)
 
def functionPredateur(x,y):
    s=0 #taux de croissance des prédateurs
    h=0 #qualité de la nourriture des proies pour les prédateurs
    return s*y-(h*s*(y**2))/x
    
# Conditions initiales et paramètres
N0 = 30  # Population initiale de sardines
P0 = 10  # Population initiale de requins
t = 100  # Temps total
n = 1000 # Nombre de pas de temps
h = t / n  # Pas de temps

sardinesEuler, requinsEuler = e.euler(sardine_avec_peche,requin,N0, P0, t, n, h)
sardinesRK4, requinsRK4 = rk.rungeKatta4IterationSysteme(functionProie,functionPredateur,N0,P0,h,t)


t_values = np.linspace(0, t, n+1)
plt.plot(t_values, sardines, label='Sardines (N)')
plt.plot(t_values, requins, label='Requins (P)')
plt.xlabel('Temps (t)')
plt.ylabel('Population')
plt.legend()
plt.title("Résolution par la méthode d'Euler")
plt.grid()
plt.show()