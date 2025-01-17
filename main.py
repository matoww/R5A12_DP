import numpy as np
import matplotlib.pyplot as plt
import euler as e
import rungeKatta4 as rk4

# Paramètres du modèle Malthus
population_initiale = 100
ressources_initiales = 150
taux_croissance_population = 0.05
taux_croissance_ressources = 10
nombre_de_periodes = 100
h = 1  # Pas de temps (1 période)
t = 100  # Temps total de simulation

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
populations_ressources_Malthus_RK4 = rk4.rungeKatta4IterationSysteme(dPdt_Malthus, dRdt, population_initiale, ressources_initiales, h, t, nombre_de_periodes)
populations_Malthus_RK4 = [i[0] for i in populations_ressources_Malthus_RK4]

# Appel de la fonction d'Euler pour le modèle de Verhulst
populations_Verhulst, ressources_Verhulst = e.euler(dPdt_Verhulst, dRdt, population_initiale, ressources_initiales, t, nombre_de_periodes, h)
populations_ressources_Verhulst_RK4 = rk4.rungeKatta4IterationSysteme(dPdt_Verhulst, dRdt, population_initiale, ressources_initiales, h, t, nombre_de_periodes)
populations_Verhulst_RK4 = [i[0] for i in populations_ressources_Verhulst_RK4]
ressources_Verhulst_RK4 = [i[1] for i in populations_ressources_Verhulst_RK4]

# Solution analytique pour Malthus
t_values = np.linspace(0, t, nombre_de_periodes + 1)  # Recalcul des valeurs de temps
populations_Malthus_analytique = population_initiale * np.exp(taux_croissance_population * t_values)

# Solution analytique pour Verhulst
populations_Verhulst_analytique = capacité_porteuse * population_initiale / (population_initiale + (capacité_porteuse - population_initiale) * np.exp(-taux_croissance_population * t_values))

# Augmenter la taille du graphique
plt.figure(figsize=(12, 8))  # Taille du graphique (12x8 pouces)

# Tracer les courbes
plt.plot(t_values, populations_Malthus, label="Population Malthus (Euler)")
plt.plot(t_values, ressources_Malthus, label="Ressources Malthus")
plt.plot(t_values, populations_Malthus_RK4, label="Population Malthus (RK4)")
plt.plot(t_values, populations_Verhulst, label="Population Verhulst (Euler)")
plt.plot(t_values, populations_Verhulst_RK4, label="Population Verhulst (RK4)")
plt.plot(t_values, populations_Malthus_analytique, label="Population Malthus (Analytique)", linestyle='--')
plt.plot(t_values, populations_Verhulst_analytique, label="Population Verhulst (Analytique)", linestyle='--')

plt.axhline(0, color="black", linewidth=0.5, linestyle="--")
plt.title("Simulation des modèles de Malthus et de Verhulst avec dérivées")
plt.xlabel("Périodes")
plt.ylabel("Valeurs")
plt.legend()
plt.grid()
plt.show()


