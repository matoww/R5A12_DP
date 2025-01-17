#equation
def fonctionX(x,y):
    """
    x : première variable du système d'équation
    y : deuxième variable du système d'équation
    retourne le résultat de la première fonction du système d'équation
    """
    return x+y

def fonctionY(x,y):
    """
    x : première variable du système d'équation
    y : deuxième variable du système d'équation
    retourne le résultat de la deuxième fonction du système d'équation
    """
    return x*2

#Résolution

def rungeKatta4IterationNormal(equationX,x,y,h,nbIteration):
    """
    equationX : fonction représentant x dans le système
    x : x initial
    y : y initial
    h : pas de discretion
    nbIteration : nombre de sous ensemble voulu
    retourne le résultat du système d'équation où seul X est dépendant de l'autre variable
    """
    results=[(x,y)]
    for i in range(nbIteration):
        y=rungeKatta4(equationX,x,y,h)
        x+=h
        results.append((x,y))
    return results

def rungeKatta4(equation,x,y,h):
    """
    equation : fonction représentant le terme dont on veut calculer le prochain terme
    x : terme non dépendant de l'autre
    y : terme dont on veut calculer la prochaine valeur
    h : pas de discrétion
    calcul du prochain terme de l'équation différentielle
    """
    k1=equation(x,y)
    k2=equation(x+0.5*h,y+0.5*h*k1)
    k3=equation(x+0.5*h,y+0.5*h*k2)
    k4=equation(x+h,y+h*k3)
    return y+(h/6)*(k1+2*k2+2*k3+k4)


def rungeKatta4IterationSysteme(equationX,equationY,x,y,h,n):
    """
    equationX : fonction représentant x dans le système
    equationY : fonction représentant y dans le système
    x : x initial
    y : y initial
    h : pas de discretion
    n : nombre de sous ensemble voulu
    retourne le résultat du système d'équation où X et Y sont dépendants l'un de l'autre
    """
    results=[(x,y)]
    for i in range(n):
        x,y=rungeKatta4Systeme(equationX,equationY,x,y,h)
        results.append((x,y))
    return results    

def rungeKatta4Systeme(equationX,equationY,x,y,h):
    """
    equationX : fonction représentant x dans le système
    equationY : fonction représentant y dans le système
    x : x au ènième terme
    y : y au ènième terme
    h : pas de discrétion
    calcul du prochain terme de l'équation différentielle dans le cas d'un système possédant deux variables dépendantes de l'autre
    """
    
    k1X=equationX(x,y)
    k1Y=equationY(x,y)

    k2X=equationX(x+0.5*h*k1X,y+0.5*h*k1Y)
    k2Y=equationY(x+0.5*h*k1X,y+0.5*h*k1Y)

    k3X=equationX(x+0.5*h*k2X,y+0.5*h*k2Y)
    k3Y=equationY(x+0.5*h*k2X,y+0.5*h*k2Y)

    k4X=equationX(x+h*k3X,y+h*k3Y)
    k4Y=equationY(x+h*k3X,y+h*k3Y)

    return x+(1/6)*h*(k1X+2*k2X+2*k3X+k4X), y+(1/6)*h*(k1Y+2*k2Y+2*k3Y+k4Y)
