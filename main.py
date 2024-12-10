import matplotlib.pyplot as plt

population_initiale = 100  
ressources_initiales = 150  
taux_croissance_population = 0.05  
taux_croissance_ressources = 10  
nombre_de_periodes = 50  

populations = [population_initiale]
ressources = [ressources_initiales]

for periode in range(1, nombre_de_periodes + 1):
    
    nouvelle_population = populations[-1] * (1 + taux_croissance_population)
    nouvelles_ressources = ressources[-1] + taux_croissance_ressources

    populations.append(nouvelle_population)
    ressources.append(nouvelles_ressources)

plt.plot(range(nombre_de_periodes + 1), populations, label="Population")
plt.plot(range(nombre_de_periodes + 1), ressources, label="Ressources")
plt.axhline(0, color="black", linewidth=0.5, linestyle="--")
plt.title("Simulation du modèle de Malthus")
plt.xlabel("Périodes")
plt.ylabel("Valeurs")
plt.legend()
plt.grid()
plt.show()



if(__name__=="__main__"):
    print("fonction principale")
