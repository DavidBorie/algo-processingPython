ballX = 0
ballY = 0
ballSpeedX = 5
ballSpeedY = 2
ballRadius = 5

racketWidth = 50
racketX = 0
racketY = 0

#ici on défint la fonction setup qui sera exécuté comme point d'entré dans mon code
def setup():
    #on appel la fonction print pour écrire
    global ballX, ballY, ballSpeedX, ballSpeedY, racketX, racketY, racketWidth
    #on appel la fonction print pour écrire dans la console
    print("Hello World")
    #On défini la taille de la fenêtre
    size(500, 500)
    #vider la page
    clear()
    #on change le frameRate de l'application
    frameRate(60)
    ballX = width/2
    ballY = width/2
    
    racketX = mouseX - (racketWidth/2)
    racketY = height -20
    
    
    
def draw():
    clear()
    drawRacket()
    drawBall()


    
def drawRacket():
    global racketX, racketY, racketWidth
    
    fill(255)
    #draw a rectangle in coords
    # x : mouseX minus half of width
    # y : height of the window minus 20
    # width : 50
    # height : 10
    racketX = mouseX - (racketWidth/2)
    rect(racketX, racketY, racketWidth, 10)
    
def drawBall():
    global ballX, ballY, ballSpeedX, ballSpeedY, ballRadius
    #draw circle
    
    #ballX = ballX + ballSpeedX
    #ballY = ballY + ballSpeedY
    ballX += ballSpeedX
    ballY += ballSpeedY
    
    #haut et bad
    if(ballY-ballRadius < 0):
        ballSpeedY *= -1
        ballY = ballRadius
    elif(ballY+ballRadius > height):
        ballSpeedY *= -1
        ballY = height-ballRadius
        
    #droite et gauche
    if(ballX+ballRadius > width):
        ballSpeedX *= -1
        ballX = width-ballRadius
    elif(ballX-ballRadius < 0):
        ballSpeedX *= -1
        ballX = ballRadius
    
    #racket_bas
    if(racketY + 10 >= ballY+ballRadius >= racketY)and(racketX <= ballX+ballRadius <= racketX + racketWidth):
        ballSpeedY *= -1
    
    
    #draw circle
    circle(ballX, ballY, 2*ballRadius);    
        
        
        
