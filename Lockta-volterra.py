
import euler as e



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
n = 500 # Nombre de pas de temps
h = t / n  # Pas de temps

e.euleur(sardine_avec_peche,requin,N0, P0, t, n, h)


