import euler as e
import rungeKatta4 as rk
import numpy as np
import matplotlib.pyplot as plt


def functionProie(x,y):
    r=0.5 #taux de croissance des proies
    K=5000 #capacité maximale des proies
    m=15 #nombre maximale de proie consommable par un prédateur en une unité de temps
    A=m/2
    result=x*r-(x*x*r)/K - (m*x*y)/(x+A)
    return result
 
def functionPredateur(x,y):
    s=-0.1 #taux de croissance des prédateurs
    h=0.1 #qualité de la nourriture des proies pour les prédateurs
    if x==0:
        x=1
    return s*y-(h*s*y*y)/x
    
# Conditions initiales et paramètres
N0 = 30  # Population initiale de sardines
P0 = 300  # Population initiale de requins
t = 100  # Temps total
n = 1000 # Nombre de pas de temps
h = t / n  # Pas de temps

#sardinesEuler, requinsEuler = e.euler(functionProie,functionPredateur,N0, P0, t, n, h)
sardinesRequinsRK4 = rk.rungeKatta4IterationSysteme(functionProie,functionPredateur,N0,P0,h,t,n)
sardinesRK4=[]
requinsRK4=[]
for i in sardinesRequinsRK4:
    sardinesRK4.append(i[0])
    requinsRK4.append(i[1])

t_values = np.linspace(0, t, n+1)
#plt.plot(t_values, sardinesEuler, label='Sardines (N)')
#plt.plot(t_values, requinsEuler, label='Requins (P)')
plt.plot(t_values, sardinesRK4, label='Sardines RK4 (N)')
plt.plot(t_values, requinsRK4, label='Requins RK4(P)')
plt.xlabel('Temps (t)')
plt.ylabel('Population')
plt.legend()
plt.title("Résolution par la méthode d'Euler")
plt.grid()
plt.show()