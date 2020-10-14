#ici on défint la fonction setup qui sera exécuté comme point d'entré dans mon code
def setup():
        #on appel la fonction print pour écrire dans la console
    print("Hello World")
    #On défini la taille de la fenêtre
    size(400, 400)
    clear()
    #on change le frameRate de l'application
    frameRate(60)

def draw():
    clear()
    fill(500, 255,5)
    #dessine un rectangle avec les paramètres suivant x, y, largeur du rectangle, hauteur du rectangle
    #rect(mouseX -100 mouseY -40, 200, 80)
    rect(width/2 + cos(millis() * 0.001) * 100, height/2 + cos(millis() * 0.003) * 100, 80, 80)
    #dessine une ellipse avec les paramètres suivant x, y, largeur de l'élipse, hauteur de l'ellipse
    #on récupère les coordonnées de la souris avec mouseX et mouseY
    #ellipse(mouseX, mouseY, 80, 80)
    ellipse(width/2 + cos(millis() * 0.001) * 100, height/2 + cos(millis() * 0.003) * 100, 100, 150)
