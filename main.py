import numpy as np
import matplotlib.pyplot as plt
import euler as e 

# Paramètres du modèle Malthus
population_initiale = 100
ressources_initiales = 150  
taux_croissance_population = 0.05  
taux_croissance_ressources = 10  
nombre_de_periodes = 50
h = 1  # Pas de temps (1 période)
t = 1000  # Temps total de simulation

# Ajout pour le modèle de Verhulst
capacité_porteuse = 200  # Capacité porteuse maximale de la population

# Fonction pour la dérivée de la population, pour le modèle de Malthus (croissance exponentielle)
def dPdt_Malthus(P, R):
    return taux_croissance_population * P  # Croissance exponentielle de la population

# Fonction pour la dérivée de la population, pour le modèle de Verhulst (croissance logistique)
def dPdt_Verhulst(P, R):
    return taux_croissance_population * P * (1 - P / capacité_porteuse)

# Fonction pour la dérivée des ressources (croissance linéaire)
def dRdt(P, R):
    return taux_croissance_ressources  # Croissance linéaire des ressources (constante)

# Appel de la fonction d'Euler pour le modèle de Malthus
populations_Malthus, ressources_Malthus = e.euler(dPdt_Malthus, dRdt, population_initiale, ressources_initiales, t, nombre_de_periodes, h)

# Appel de la fonction d'Euler pour le modèle de Verhulst
populations_Verhulst, ressources_Verhulst = e.euler(dPdt_Verhulst, dRdt, population_initiale, ressources_initiales, t, nombre_de_periodes, h)

# Tracer les résultats
t_values = np.linspace(0, t, nombre_de_periodes + 1)  # Recalcul des valeurs de temps
plt.plot(t_values, populations_Malthus, label="Population Malthus")
plt.plot(t_values, ressources_Malthus, label="Ressources")
plt.plot(t_values, populations_Verhulst, label="Population Verhulst")
plt.axhline(0, color="black", linewidth=0.5, linestyle="--")
plt.title("Simulation des modèles de Malthus et Verhulst avec dérivées")
plt.xlabel("Périodes")
plt.ylabel("Valeurs")
plt.legend()
plt.grid()
plt.show()
