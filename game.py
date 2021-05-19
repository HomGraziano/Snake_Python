import pygame as game
import random

game.init()

#Parametros de la ventana
altura = 600
ancho = 800
dis = game.display.set_mode((ancho, altura))
game.display.set_caption("A comerla")

#Colores usados en el programa
blue = (0, 0, 255)
red = (255, 0, 0)
rcol = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
white = (255 ,255, 255)
black = (0, 0, 0)
gray = (50, 50, 50)

#Estado del juego
game_over = False

#Parametros de la serpiente
snake_block = 10
snake_speed = 10

#Coordenadas para el juego
x1 = 300
y1 = 300
x1_change = 0
y1_change = 0
clock = game.time.Clock()

font_style = game.font.SysFont("bahnschrift", 25)
score_font = game.font.SysFont("comicsansms", 35)

#Esto contiene el puntaje actual
def puntaje(score):
    value = score_font.render("Cuadraditos comidos: " + str(score), True, blue)
    dis.blit(value, [0, 0])

#def alto_puntaje(highscore):
#    value = score_font.render("Record de cuadraditos: " + str(puntaje_alto), True, blue)
#    dis.blit(value, [0, 60])

#Esto contiene el largo de la serpiente   
def our_snake(snake_block, snake_list):
    for x in snake_list:
        game.draw.rect(dis, white, [x[0], x[1], snake_block, snake_block])

#Esto define la funcion para imprimir un mensaje en la pantalla
def message(msg, coord, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, coord)

#La funcion para la comida
def gameLoop():
    game_over = False
    game_close = False

    x1 = ancho / 2
    y1 = altura / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    largo_snake = 1
    punt = 0

    comidax = round(random.randrange(0, ancho - snake_block) / 10.0) * 10.0
    comiday = round(random.randrange(0, altura - snake_block) / 10.0) * 10.0
    
    #Esto repite el programa todo el tiempo hasta que game_over sea verdadero.
    while not game_over:

        while game_close == True:
            dis.fill(white)
            message("La cagaste capo! Apreta Q-Salir o C-Jugar otra vez", [120, 300], red)
            message(f'Puntaje: {punt}', [120, 350], red)
            #Almaceno el puntaje alto

            game.display.update()
            
            for event in game.event.get():
                if event.type == game.KEYDOWN:
                    if event.key == ord("q"):
                        game_over = True
                        game_close = False
                    elif event.key == ord("c"):
                        gameLoop()
        
        #Esto define las teclas a utilizar para jugar.
        for event in game.event.get():
            if event.type == game.QUIT:
                game_over = True
            if event.type == game.KEYDOWN:
                if event.key == ord("a"):
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == ord("d"):
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == ord("w"):
                    x1_change = 0
                    y1_change = -snake_block
                elif event.key == ord("s"):
                    x1_change = 0
                    y1_change = snake_block

        #Esto define los limites del mundo jugable
        if x1 >= (ancho - 10) or x1 < 10 or y1 >= (altura - 10) or y1 < 120:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(white)
        game.draw.rect(dis, black, [0, 120, 800, 480])
        game.draw.rect(dis, gray, [0, 110, 800, 10])
        game.draw.rect(dis, gray, [0, 110, 10, 480])
        game.draw.rect(dis, gray, [0, 590, 800, 10])
        game.draw.rect(dis, gray, [790, 110, 10, 480])

        #Estas condiciones logran que SIEMPRE el rectangulo comida este dentro de los limites del terreno jugable
        if comiday <= 120:
            comiday = comiday + 120
        elif comiday == 600:
            comiday = comiday - 10
        elif comidax == 800:
            comidax = comidax - 10
        elif comidax == 0:
            comidax = comidax + 10
        else:
            pass
        game.draw.rect(dis, blue, [comidax, comiday, snake_block, snake_block])
        
        #Esto define de que manera la serpiente va a crecer
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > largo_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        punt = (largo_snake - 1)
        our_snake(snake_block, snake_List)
        puntaje(punt)
        game.display.update()

        if x1 == comidax and y1 == comiday:
            comidax = round(random.randrange(0, ancho - snake_block) / 10.0) * 10.0
            comiday = round(random.randrange(0, altura - snake_block) / 10.0) * 10.0
            largo_snake += 1
        
        clock.tick(snake_speed)
    game.quit()
    quit()

gameLoop()