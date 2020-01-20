import pygame
import pygame.freetype
import random
import time
#Importa o pygame e a biblioteca freetype.

res = (1280, 720)
#Define a resolução do ecrã.  

screen = pygame.display.set_mode(res)
#criação de variável para o ecrã.
    
pygame.display.set_caption("Shuffle! a project made by André Figueira")  
image = pygame.image.load("shuffle.png")
#Escreve na barra no topo do ficheiro e cria uma variável para a imagem de título.

yellow = (255, 200, 0)
bright_yellow = (255, 255, 0)
dark_blue = (0, 0, 20)
bright_green = (0, 255, 0)
pink = (255, 20 ,147)
bright_blue = (0, 0, 255)
bright_red = (255, 0, 0)
cyan = (0, 255, 255)
grey = (169, 169, 169)
#Criação de variáveis para diferentes cores usadas.

gamerunning = False
buttons = True
gamemode = 0
rows = None
cols = None
game_cards = []
turned = []
score = 0
pick = 1
pick1 = None
pick2 = None
verify = False
missed = 0
#Dá valores às variáveis para serem usadas nas funções.


def main():
    global game_cards, turned, pick, pick1, pick2, verify, score
#Função main do jogo.    
    
    pygame.init()
    gamefont = pygame.freetype.Font("NotoSans-Regular.ttf", 24)
    #Inicialização do pygame e definição da fonte usada.
    
    def button(msg, x, y, w, h, ic, ac,tw, th, action=None):
    #Função para a criação dos botões e as suas respetivas ações.
        global gamemode, gamerunning, buttons, rows, cols
        #Definição das variáveis como global para poderem ser alteradas dentro da função
        if buttons == True:
            if x+w > mouse[0] > x and y+h > mouse[1] > y:
                
                pygame.draw.rect(screen, ac, (x,y, w, h), 2)
                gamefont.render_to(screen, (tw, th), msg, ac)
                
                if click[0] == 1 and action != None:
                    
                    if action == "4 X 3":
                        rows = 3
                        cols = 4
                        random_cards()
                        gamerunning = True
                        gamemode = 1
                    
                    elif action == "4 X 4":
                        rows = 4
                        cols = 4
                        random_cards()
                        gamerunning = True
                        gamemode = 2
                    
                    elif action == "5 X 4":
                        rows = 4
                        cols = 5
                        random_cards()
                        gamerunning = True
                        gamemode = 3

                    elif action == "6 X 5":
                        rows = 5
                        cols = 6
                        random_cards()
                        gamerunning = True
                        gamemode = 4

                    elif action == "6 X 6":
                        rows = 6
                        cols = 6
                        random_cards()
                        gamerunning = True
                        gamemode = 5
                    
                    elif action == "EXIT":
                        pygame.quit()
                        
                        exit()

            else:
                pygame.draw.rect(screen, ic, (x,y, w, h), 2)
                gamefont.render_to(screen, (tw, th), msg, ic)

    def random_cards():
        global rows, cols, game_cards, turned

        game_cards = []

        card_list = [card1, card1a, card2, card2a, card3, card3a, card4, card4a, card5, card5a, card6, card6a, card7, card7a, card8, card8a, card9, card9a, card10, card10a, card11, card11a, card12, card12a, card13, card13a, card14, card14a, card15, card15a, card16, card16a, card17, card17a, card18, card18a]
        
        aux_cards = []

        for x in range(rows * cols):
            aux_cards.append(card_list.pop())
        random.shuffle(aux_cards)
        for x in range(rows):
            aux_list = []
            turned.append([])
            for y in range(cols):
                aux_list.append(aux_cards.pop())
                turned[x].append(0)
            game_cards.append(aux_list)

    def verify_cards():
        global pick1, pick2, verify, score

        if game_cards[pick1[0]][pick1[1]] == game_cards[pick2[0]][pick2[1]]:            
            game_cards[pick1[0]][pick1[1]] = None
            game_cards[pick2[0]][pick2[1]] = None
            score += 100
        else:
            diff()

        if score < 0:
            score = 0
        verify = False
        pygame.display.flip()
        time.sleep(.5)
    
    def diff():
        global turned, pick1, pick2, score, missed, verify
        turned[pick1[0]][pick1[1]] = 0
        turned[pick2[0]][pick2[1]] = 0
        score -= missed * 20
        missed += 1
    
    while (True):
        
        global gamerunning
        global buttons
        global gamemode
        pygame.event.get()
        
        for event in pygame.event.get():           
            if (event.type == pygame.QUIT):
               exit()
        
        k = pygame.key.get_pressed()

        if (k[pygame.K_ESCAPE]):
            
            exit()

        screen.fill((0, 0, 20))
       
        screen.blit(image, (240,0))
        
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        button("4 X 3", 565, 300, 140, 36, yellow, bright_yellow,608, 310, "4 X 3")
        button("4 X 4", 565, 350, 140, 36, yellow, bright_yellow,608, 360, "4 X 4" )
        button("5 X 4", 565, 400, 140, 36, yellow, bright_yellow,608, 410, "5 X 4")
        button("6 X 5", 565, 450, 140, 36, yellow, bright_yellow,608, 460, "6 X 5")
        button("6 X 6", 565, 500, 140, 36, yellow, bright_yellow,608, 510, "6 X 6")
        button("EXIT", 565, 600, 140, 36, yellow, bright_yellow,610, 610, "EXIT")

        class Square():
            def __init__(self, color, shape_color):
                self.color = color
                self.shape_color = shape_color

            def draw(self, win,x , y, width, height):
                self.x = x
                self.y = y
                self.width = width
                self.height = height
                self.shape_width = int(self.width/2)
                self.shape_height = int(self.width/2)
                self.shape_x = self.x + int(self.shape_width/2)
                self.shape_y = self.y + int(self.height/2 - int(self.shape_height/2))
                pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 0)
                pygame.draw.rect(win, self.shape_color, (self.shape_x, self.shape_y, self.shape_width, self.shape_height))
                
        
        class Circle():
            def __init__(self, color, shape_color):
                self.color = color
                self.shape_color = shape_color

            def draw(self, win,x , y, width, height):
                self.x = x
                self.y = y
                self.width = width
                self.height = height            
                self.shape_x = self.x + int(self.width/2)
                self.shape_y = self.y + int(self.height/2)
                pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 0)                
                pygame.draw.circle(win, self.shape_color, (self.shape_x, self.shape_y), int(self.width/4))
                
        
        class Triangle():
            def __init__(self, color, shape_color):
                self.color = color
                self.shape_color = shape_color

            def draw(self, win,x , y, width, height):
                self.x = x
                self.y = y
                self.width = width
                self.height = height
                pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 0)                            
                pygame.draw.polygon(win , self.shape_color , [(self.x + int(self.width/2), (self.y + int(self.height/2)) - int(self.height/4))  , (self.x + int(self.width/4), self.y + int(self.height/2) + int(self.width/4)) , (self.x + self.width - int(self.width/4), self.y + int(self.height/2) + int(self.width/4))])
                


        card1 = Square(dark_blue, yellow)
        card1a = Square(dark_blue, yellow)
        card2 = Square(dark_blue, cyan)
        card2a = Square(dark_blue, cyan)
        card3 = Square(dark_blue, pink)
        card3a = Square(dark_blue, pink)
        card4 = Square(dark_blue, bright_green)
        card4a = Square(dark_blue, bright_green)
        card5 = Square(dark_blue, bright_red)
        card5a = Square(dark_blue, bright_red)
        card6 = Square(dark_blue, bright_blue)
        card6a = Square(dark_blue, bright_blue)
        card7 = Circle(dark_blue, yellow)
        card7a = Circle(dark_blue, yellow)
        card8 = Circle(dark_blue, cyan)
        card8a = Circle(dark_blue, cyan)
        card9 = Circle(dark_blue, pink)
        card9a = Circle(dark_blue, pink)
        card10 = Circle(dark_blue, bright_green)
        card10a = Circle(dark_blue, bright_green)
        card11 = Circle(dark_blue, bright_red)
        card11a = Circle(dark_blue, bright_red)
        card12 = Circle(dark_blue, bright_blue)
        card12a = Circle(dark_blue, bright_blue)
        card13 = Triangle(dark_blue, yellow)
        card13a = Triangle(dark_blue, yellow)
        card14 = Triangle(dark_blue, cyan)
        card14a = Triangle(dark_blue, cyan)
        card15 = Triangle(dark_blue, pink)
        card15a = Triangle(dark_blue, pink)
        card16 = Triangle(dark_blue, bright_green)
        card16a = Triangle(dark_blue, bright_green)
        card17 = Triangle(dark_blue, bright_red)
        card17a = Triangle(dark_blue, bright_red)
        card18 = Triangle(dark_blue, bright_blue)
        card18a = Triangle(dark_blue, bright_blue)

        card_list = [card1, card1a, card2, card2a, card3, card3a, card4, card4a, card5, card5a, card6, card6a, card7, card7a, card8, card8a, card9, card9a, card10, card10a, card11, card11a, card12, card12a, card13, card13a, card14, card14a, card15, card15a, card16, card16a, card17, card17a, card18, card18a]

        while gamerunning:
            for event in pygame.event.get():           
                if (event.type == pygame.QUIT):
                    exit()
                elif (event.type == pygame.MOUSEBUTTONDOWN):
                    pos = pygame.mouse.get_pos()
                    for i in range(rows):
                        for j in range(cols):
                            if game_cards[i][j] != None:
                                if game_cards[i][j].x < pos[0] < game_cards[i][j].x + game_cards[i][j].width:
                                    if game_cards[i][j].y < pos[1] < game_cards[i][j].y + game_cards[i][j].height:
                                        turned[i][j] = 1
                                        if pick == 1:
                                            pick1 = (i, j)
                                            pick = 2
                                        elif pick == 2:
                                            pick2 = (i, j)
                                            pick = 1
                                            verify = True
            
            buttons = False
            
            #k = pygame.key.get_pressed()

            if gamemode == 1:
                screen.fill(dark_blue)

                for x in range(rows):
                    for y in range(cols):
                        if game_cards[x][y] != None:
                            game_cards[x][y].draw(screen, 345 + (150 * y), 50 + (210 * x), 140, 200)
                            if not turned[x][y]:
                                pygame.draw.rect(screen, bright_green, (345 + (150 * y), 50 + (210 * x), 140, 200), 0)

                          
                
                
                #pygame.display.update()
            
            if gamemode == 2:
                screen.fill(dark_blue)

                for x in range(rows):
                    for y in range(cols):
                        if game_cards[x][y] != None:
                            game_cards[x][y].draw(screen, 415 + (115 * y), 45 + (160 * x), 105, 150)
                            if not turned[x][y]:
                                pygame.draw.rect(screen, bright_green, (415 + (115 * y), 45 + (160 * x), 105, 150), 0)                   
                        

            

                #pygame.display.update() 

            if gamemode == 3:
                screen.fill(dark_blue)
                
                for x in range(rows):
                    for y in range(cols):
                        if game_cards[x][y] != None:
                            game_cards[x][y].draw(screen, 358 + (115 * y), 45 + (160 * x), 105, 150)
                            if not turned[x][y]:
                                pygame.draw.rect(screen, bright_green, (358 + (115 * y), 45 + (160 * x), 105, 150), 0)
                        

                
            
                #pygame.display.update()

            if gamemode == 4:
                screen.fill(dark_blue)
                
                for x in range(rows):
                    for y in range(cols):
                        if game_cards[x][y] != None:
                            game_cards[x][y].draw(screen, 405 + (80 * y) , 90 + (110 * x), 70, 100)
                            if not turned[x][y]:
                                pygame.draw.rect(screen, bright_green, (405 + (80 * y) , 90 + (110 * x), 70, 100), 0)
                    
                
            
                #pygame.display.update()

            if gamemode == 5:
                screen.fill(dark_blue)
                
                for x in range(rows):
                    for y in range(cols):
                        if game_cards[x][y] != None:
                            game_cards[x][y].draw(screen, 405 + (80 * y) , 35 + (110 * x), 70, 100)
                            if not turned[x][y]:
                                pygame.draw.rect(screen, bright_green, (405 + (80 * y) , 35 + (110 * x), 70, 100), 0)

                #pygame.display.update()

            
            if (k[pygame.K_q]):
                gamerunning = False
                buttons = True
                

            
            if verify:
                verify_cards()

    
            pygame.display.flip()
        pygame.display.flip()       


main()