import numpy as np

def euler(F, G, x0, y0, t, n, h):
    """
    Résout un système d'équations différentielles à l'aide de la méthode d'Euler explicite.
    
    Paramètres :
    F : fonction représentant la dérivée de X par rapport au temps (F(X, Y))
    G : fonction représentant la dérivée de Y par rapport au temps (G(X, Y))
    x0 : valeur initiale de X à t = 0
    y0 : valeur initiale de Y à t = 0
    t : temps final de la simulation
    n : nombre de pas de temps (nombre de périodes)
    h : pas de temps (taille de l'intervalle entre chaque étape)
    
    Retourne :
    Xk : tableau des valeurs de X à chaque étape de temps
    Yk : tableau des valeurs de Y à chaque étape de temps
    """
    # Création d'un tableau contenant les valeurs de temps de 0 à t, avec n+1 points
    t_values = np.linspace(0, t, n+1)
    
    # Initialisation des tableaux Xk et Yk avec des zéros, de taille n+1 
    Xk = np.zeros(n+1)
    Yk = np.zeros(n+1)
    
    # Définition des conditions initiales
    Xk[0] = x0
    Yk[0] = y0

    # Boucle pour calculer les valeurs de Xk et Yk par la méthode d'Euler
    for k in range(n):
        # Calcul de Xk+1 avec la méthode d'Euler a
        Xk[k + 1] = Xk[k] + h * F(Xk[k], Yk[k])
        Yk[k + 1] = Yk[k] + h * G(Xk[k], Yk[k])

    # Affichage des résultats pour chaque instant de temps
    for k in range(n+1):
        # Affichage des valeurs de t, X (population) et Y (ressources)
        print("t = ", t_values[k], " N = ", Xk[k], " P = ", Yk[k])
        
    return Xk, Yk
    
