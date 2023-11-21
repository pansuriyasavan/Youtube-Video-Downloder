#Scraping GitHub Profile using Python

# import requests
# from bs4 import BeautifulSoup as bs

# github_profile = "https://github.com/pansuriyasavan"
# try:
#     req = requests.get(github_profile)
#     print("\n\n\n\n\n\nreq\n",req)
#     scraper = bs(req.content, "html.parser")
#     print("\n\n\n\n\n\scraper\n",scraper)
#     profile_picture = scraper.find("pansuriyasavan")
#     print(profile_picture)
# except Exception as e:
#     print("\n\n\ne \n",e)


#QR Code using Python       //////////////////////////////////////////////////////////////

# import pyqrcode
# import png
# link = "https://www.instagram.com/the.clever.programmer/"
# qr_code = pyqrcode.create(link)
# qr_code.png("instagram.png", scale=5)


# from pyzbar.pyzbar import decode
# from PIL import Image
# decocdeQR = decode(Image.open('instagram.png'))
# print(decocdeQR[0].data.decode('ascii'))

#Find Duplicate Values using Python        ////////////////////////////////////////////////////

# def find_duplicates(x):
#     length = len(x)
#     duplicates = []
#     for i in range(length):
#         n = i + 1
#         for a in range(n, length):
#             if x[i] == x[a] and x[i] not in duplicates:
#                 duplicates.append(x[i])
#     return duplicates
# names = ["Aman", "Akanksha", "Divyansha", "Devyansh", 
#          "Aman", "Diksha", "Akanksha",]
# print(find_duplicates(names))

#  Send Instagram Messages using Python              ///////////////////////////////////////////////////////

# from instabot import Bot
# bot = Bot()
# try:
#     bot.login(username="savan_ptl_24", password="Sawan@2389")
#     bot.send_message("Hi Brother", ["patelbhai6991"])
# except Exception as e:
#     print(e)


#Animated Scatter Plot using Python /////////////////////////////////////////////

# import plotly.express as px
# data = px.data.gapminder()
# # print(data.head())

# px.scatter(data, x="gdpPercap", y="lifeExp", animation_frame="year", animation_group="country",
#            size="pop", color="country", hover_name="country",
#            log_x=True, size_max=55, range_x=[100,100000], range_y=[25,90])


#Phone Number Details using Python     //////////////////////////////////////////////////

# import phonenumbers as ph
# from phonenumbers import carrier
# from phonenumbers import geocoder
# from phonenumbers import timezone

# number = "+919099071075"
# number = ph.parse(number)
# print(timezone.time_zones_for_number(number))
# print(carrier.name_for_number(number, "en"))
# print(geocoder.description_for_number(number, "en"))


#Data Visualisation on Map using Python /////////////////////////////////////////////

# import numpy as np
# import pandas as pd
# import folium as fo
# data = pd.read_csv("https://raw.githubusercontent.com/amankharwal/Website-data/master/Volcano.csv")
# print("\n\n\n\n\ndata",data)
# print(data.head())

# lat = list(data["Latitude"])
# lon = list(data["Longitude"])
# name = list(data["Name"])

# volcano = fo.FeatureGroup(name="Volcano")
# for a, b, c in zip(lat, lon, name):
#   volcano.add_child(fo.Marker(location=[a, b], popup=c, icon=fo.Icon(color='blue')))
# print("volcano",fo.Map().add_child(volcano))
  
# fo.Map().add_child(volcano)


#Choropleth Map using Python   //////////////////////////////////////////

# import plotly.graph_objects as go
# import pandas as pd
# data = pd.read_csv("usa.csv")
# print(data["code"])

# figure = go.Figure(data=go.Choropleth(locations=data["code"],
#                                       z = data["total exports"].astype(float),
#                                       locationmode="USA-states",
#                                       colorscale="Reds",
#                                       colorbar_title="Millions USD"))
# figure.update_layout(title_text="US Agriculture Exports", geo_scope='usa')
# figure.show()



#Build a Robot with Python    /////////////////////////////////////////////

# import turtle as t
# def rectangle(horizontal, vertical, color):
#     t.pendown()
#     t.pensize(1)
#     t.color(color)
#     t.begin_fill()
#     for counter in range(1, 3):
#         t.forward(horizontal)
#         t.right(90)
#         t.forward(vertical)
#         t.right(90)
#     t.end_fill()
#     t.penup()

# t.penup()
# t.speed('slow')
# t.bgcolor('Dodger blue')
# # feet
# t.goto(-100, -150)
# rectangle(50, 20, 'blue')
# t.goto(-30, -150)
# rectangle(50, 20, 'blue')
# # legs
# t.goto(-25, -50)
# rectangle(15, 100, 'grey')
# t.goto(-55, -50)
# rectangle(-15, 100, 'grey')
# # body
# t.goto(-90, 100)
# rectangle(100, 150, 'red')
# # arms
# t.goto(-150, 70)
# rectangle(60, 15, 'grey')
# t.goto(-150, 110)
# rectangle(15, 40, 'grey')
# t.goto(10, 70)
# rectangle(60, 15, 'grey')
# t.goto(55, 110)
# rectangle(15, 40, 'grey')
# # neck
# t.goto(-50, 120)
# rectangle(15, 20, 'grey')
# # head
# t.goto(-85, 170)
# rectangle(80, 50, 'red')
# # eyes
# t.goto(-60, 160)
# rectangle(30, 10, 'white')
# t.goto(-55, 155)
# rectangle(5, 5, 'black')
# t.goto(-40, 155)
# rectangle(5, 5, 'black')



#Tic Tac Toe GUI with Python    /////////////////////////////////////////////////



# from tkinter import *
# import numpy as np

# size_of_board = 600
# symbol_size = (size_of_board / 3 - size_of_board / 8) / 2
# symbol_thickness = 50
# symbol_X_color = '#EE4035'
# symbol_O_color = '#0492CF'
# Green_color = '#7BC043'


# class Tic_Tac_Toe():
#     # ------------------------------------------------------------------
#     # Initialization Functions:
#     # ------------------------------------------------------------------
#     def __init__(self):
#         self.window = Tk()
#         self.window.title('Tic-Tac-Toe')
#         self.canvas = Canvas(self.window, width=size_of_board, height=size_of_board)
#         self.canvas.pack()
#         # Input from user in form of clicks
#         self.window.bind('<Button-1>', self.click)

#         self.initialize_board()
#         self.player_X_turns = True
#         self.board_status = np.zeros(shape=(3, 3))

#         self.player_X_starts = True
#         self.reset_board = False
#         self.gameover = False
#         self.tie = False
#         self.X_wins = False
#         self.O_wins = False

#         self.X_score = 0
#         self.O_score = 0
#         self.tie_score = 0

#     def mainloop(self):
#         self.window.mainloop()

#     def initialize_board(self):
#         for i in range(2):
#             self.canvas.create_line((i + 1) * size_of_board / 3, 0, (i + 1) * size_of_board / 3, size_of_board)

#         for i in range(2):
#             self.canvas.create_line(0, (i + 1) * size_of_board / 3, size_of_board, (i + 1) * size_of_board / 3)

#     def play_again(self):
#         self.initialize_board()
#         self.player_X_starts = not self.player_X_starts
#         self.player_X_turns = self.player_X_starts
#         self.board_status = np.zeros(shape=(3, 3))

#     # ------------------------------------------------------------------
#     # Drawing Functions:
#     # The modules required to draw required game based object on canvas
#     # ------------------------------------------------------------------

#     def draw_O(self, logical_position):
#         logical_position = np.array(logical_position)
#         # logical_position = grid value on the board
#         # grid_position = actual pixel values of the center of the grid
#         grid_position = self.convert_logical_to_grid_position(logical_position)
#         self.canvas.create_oval(grid_position[0] - symbol_size, grid_position[1] - symbol_size,
#                                 grid_position[0] + symbol_size, grid_position[1] + symbol_size, width=symbol_thickness,
#                                 outline=symbol_O_color)

#     def draw_X(self, logical_position):
#         grid_position = self.convert_logical_to_grid_position(logical_position)
#         self.canvas.create_line(grid_position[0] - symbol_size, grid_position[1] - symbol_size,
#                                 grid_position[0] + symbol_size, grid_position[1] + symbol_size, width=symbol_thickness,
#                                 fill=symbol_X_color)
#         self.canvas.create_line(grid_position[0] - symbol_size, grid_position[1] + symbol_size,
#                                 grid_position[0] + symbol_size, grid_position[1] - symbol_size, width=symbol_thickness,
#                                 fill=symbol_X_color)

#     def display_gameover(self):

#         if self.X_wins:
#             self.X_score += 1
#             text = 'Winner: Player 1 (X)'
#             color = symbol_X_color
#         elif self.O_wins:
#             self.O_score += 1
#             text = 'Winner: Player 2 (O)'
#             color = symbol_O_color
#         else:
#             self.tie_score += 1
#             text = 'Its a tie'
#             color = 'gray'

#         self.canvas.delete("all")
#         self.canvas.create_text(size_of_board / 2, size_of_board / 3, font="cmr 60 bold", fill=color, text=text)

#         score_text = 'Scores \n'
#         self.canvas.create_text(size_of_board / 2, 5 * size_of_board / 8, font="cmr 40 bold", fill=Green_color,
#                                 text=score_text)

#         score_text = 'Player 1 (X) : ' + str(self.X_score) + '\n'
#         score_text += 'Player 2 (O): ' + str(self.O_score) + '\n'
#         score_text += 'Tie                    : ' + str(self.tie_score)
#         self.canvas.create_text(size_of_board / 2, 3 * size_of_board / 4, font="cmr 30 bold", fill=Green_color,
#                                 text=score_text)
#         self.reset_board = True

#         score_text = 'Click to play again \n'
#         self.canvas.create_text(size_of_board / 2, 15 * size_of_board / 16, font="cmr 20 bold", fill="gray",
#                                 text=score_text)

#     # ------------------------------------------------------------------
#     # Logical Functions:
#     # The modules required to carry out game logic
#     # ------------------------------------------------------------------

#     def convert_logical_to_grid_position(self, logical_position):
#         logical_position = np.array(logical_position, dtype=int)
#         return (size_of_board / 3) * logical_position + size_of_board / 6

#     def convert_grid_to_logical_position(self, grid_position):
#         grid_position = np.array(grid_position)
#         return np.array(grid_position // (size_of_board / 3), dtype=int)

#     def is_grid_occupied(self, logical_position):
#         if self.board_status[logical_position[0]][logical_position[1]] == 0:
#             return False
#         else:
#             return True

#     def is_winner(self, player):

#         player = -1 if player == 'X' else 1

#         # Three in a row
#         for i in range(3):
#             if self.board_status[i][0] == self.board_status[i][1] == self.board_status[i][2] == player:
#                 return True
#             if self.board_status[0][i] == self.board_status[1][i] == self.board_status[2][i] == player:
#                 return True

#         # Diagonals
#         if self.board_status[0][0] == self.board_status[1][1] == self.board_status[2][2] == player:
#             return True

#         if self.board_status[0][2] == self.board_status[1][1] == self.board_status[2][0] == player:
#             return True

#         return False

#     def is_tie(self):

#         r, c = np.where(self.board_status == 0)
#         tie = False
#         if len(r) == 0:
#             tie = True

#         return tie

#     def is_gameover(self):
#         # Either someone wins or all grid occupied
#         self.X_wins = self.is_winner('X')
#         if not self.X_wins:
#             self.O_wins = self.is_winner('O')

#         if not self.O_wins:
#             self.tie = self.is_tie()

#         gameover = self.X_wins or self.O_wins or self.tie

#         if self.X_wins:
#             print('X wins')
#         if self.O_wins:
#             print('O wins')
#         if self.tie:
#             print('Its a tie')

#         return gameover





#     def click(self, event):
#         grid_position = [event.x, event.y]
#         logical_position = self.convert_grid_to_logical_position(grid_position)

#         if not self.reset_board:
#             if self.player_X_turns:
#                 if not self.is_grid_occupied(logical_position):
#                     self.draw_X(logical_position)
#                     self.board_status[logical_position[0]][logical_position[1]] = -1
#                     self.player_X_turns = not self.player_X_turns
#             else:
#                 if not self.is_grid_occupied(logical_position):
#                     self.draw_O(logical_position)
#                     self.board_status[logical_position[0]][logical_position[1]] = 1
#                     self.player_X_turns = not self.player_X_turns

#             # Check if game is concluded
#             if self.is_gameover():
#                 self.display_gameover()
#                 # print('Done')
#         else:  # Play Again
#             self.canvas.delete("all")
#             self.play_again()
#             self.reset_board = False


# game_instance = Tic_Tac_Toe()
# game_instance.mainloop()


#Three-Dimensional points and lines    ?////////////////////////////////////

# import numpy as np
# import matplotlib.colors as col
# from mpl_toolkits.mplot3d import Axes3D
# import matplotlib.pyplot as plt
# #Data for a three dimensional line
# z = np.linspace(0, 15, 1000)
# x = np.sin(z)
# y = np.cos(z)
# ax.plot3D(x, y, z, 'grey')
# #Data for three dimensional scattered points
# z = 15 * np.random.random(100)
# x = np.sin(z) + 0.1 * np.random.randn(100)
# y = np.cos(z) + 0.1 * np.random.randn(100)
# ax.scatter3D(x, y, z, c=z, cmap='Greens')
# plt.show()

# def f(x, y):
#     return np.sin(np.sqrt(x ** 2 + y ** 2))
# x = np.linspace(-6, 6, 30)
# y = np.linspace(-6, 6, 30)
# x, y = np.meshgrid(x, y)
# z = f(x, y)
# fig = plt.figure()
# ax = plt.axes(projection='3d')
# ax.contour3D(x,y,z,50, cmap='binary')
# ax.set_xlabel('x')
# ax.set_ylabel('y')
# ax.set_zlabel('z')
# plt.show()

# fig = plt.figure()
# ax = plt.axes(projection='3d')
# ax.plot_wireframe(x,y,z, color='black')
# ax.set_title('wireframe')
# plt.show()

# ax = plt.axes(projection='3d')
# ax.plot_surface(x, y, z, rstride=1,
#                 cstride=1, cmap='viridis',
#                 edgecolor='none')
# ax.set_title('surface')
# plt.show()


#Python Tetris Code   //////////////////////////////////////


# import pygame
# import random

# #Shapes of the blocks
# shapes = [
#         [[1, 5, 9, 13], [4, 5, 6, 7]],
#         [[4, 5, 9, 10], [2, 6, 5, 9]],
#         [[6, 7, 9, 10], [1, 5, 6, 10]],
#         [[2, 1, 5, 9], [0, 4, 5, 6], [1, 5, 9, 8], [4, 5, 6, 10]],
#         [[1, 2, 6, 10], [5, 6, 7, 9], [2, 6, 10, 11], [3, 5, 6, 7]],
#         [[1, 4, 5, 6], [1, 4, 5, 9], [4, 5, 6, 9], [1, 5, 6, 9]],
#         [[1, 2, 5, 6]],
#     ]

# #Colors of the blocks
# shapeColors = [(0, 255, 0), (255, 0, 0), (0, 255, 255), (255, 255, 0), (255, 165, 0), (0, 0, 255), (128, 0, 128)]
# # GLOBALS VARS
# width = 700
# height = 600
# gameWidth = 100  # meaning 300 // 10 = 30 width per block
# gameHeight = 400  # meaning 600 // 20 = 20 height per blo ck
# blockSize = 20
    
# topLeft_x = (width - gameWidth) // 2
# topLeft_y = height - gameHeight - 50

# class Block:
#     x = 0
#     y = 0
#     n = 0
#     def __init__(self, x, y,n):
#         self.x = x
#         self.y = y
#         self.type = n
#         self.color = n
#         self.rotation = 0
#     def image(self):
#         return shapes[self.type][self.rotation]

#     def rotate(self):
#         self.rotation = (self.rotation + 1) % len(shapes[self.type])


# class Tetris:
#     level = 2
#     score = 0
#     state = "start"
#     field = []
#     height = 0
#     width = 0
#     zoom = 20
#     x = 100
#     y = 60
#     block = None
#     nextBlock=None
    
#     #Sets the properties of the board
#     def __init__(self, height, width):
#         self.height = height
#         self.width = width
#         for i in range(height):
#             new_line = []
#             for j in range(width):
#                 new_line.append(0)
#             self.field.append(new_line)

#     #Creates a new block
#     def new_block(self):
#         self.block = Block(3, 0,random.randint(0, len(shapes) - 1))
                            
#     def next_block(self):
#         self.nextBlock=Block(3,0,random.randint(0, len(shapes) - 1))
#     #Checks if the blocks touch the top of the board
#     def intersects(self):
#         intersection = False
#         for i in range(4):
#             for j in range(4):
#                 if i * 4 + j in self.block.image():
#                     if i + self.block.y > self.height - 1 or \
#                             j + self.block.x > self.width - 1 or \
#                             j + self.block.x < 0 or \
#                             self.field[i + self.block.y][j + self.block.x] > 0:
#                         intersection = True
#         return intersection

#     #Checks if a row is formed and destroys that line
#     def break_lines(self):
#         lines = 0
#         for i in range(1, self.height):
#             zeros = 0
#             for j in range(self.width):
#                 if self.field[i][j] == 0:
#                     zeros += 1
#             if zeros == 0:
#                 lines += 1
#                 for i1 in range(i, 1, -1):
#                     for j in range(self.width):
#                         self.field[i1][j] = self.field[i1 - 1][j]
#         self.score += lines ** 2

#     def draw_next_block(self,screen):
    
#         font = pygame.font.SysFont("Calibri", 30)
#         label = font.render("Next Shape", 1, (128,128,128))

#         sx = topLeft_x + gameWidth + 50
#         sy = topLeft_y + gameHeight/2 - 100
#         format = self.nextBlock.image()
#         for i in range(4):
#                 for j in range(4):
#                     p = i * 4 + j
#                     if p in self.nextBlock.image():
#                         pygame.draw.rect(screen, shapeColors[self.nextBlock.color],(sx + j*30, sy + i*30, 30, 30), 0)
    
#     #Moves the block to the bottom
#     def moveBottom(self):
#         while not self.intersects():
#             self.block.y += 1
#         self.block.y -= 1
#         self.freeze()

#     #Moves the block down by a unit
#     def moveDown(self):
#         self.block.y += 1
#         if self.intersects():
#             self.block.y -= 1
#             self.freeze()

#     # This function runs once the block reaches the bottom. 
#     def freeze(self):
#         for i in range(4):
#             for j in range(4):
#                 if i * 4 + j in self.block.image():
#                     self.field[i + self.block.y][j + self.block.x] = self.block.color
#         self.break_lines() #Checking if any row is formed
#         self.block=self.nextBlock
#         self.next_block() #Creating a new block
#         if self.intersects(): #If blocks touch the top of the board, then ending the game by setting status as gameover
#             self.state = "gameover"
#     #This function moves the block horizontally
#     def moveHoriz(self, dx):
#         old_x = self.block.x
#         self.block.x += dx
#         if self.intersects():
#             self.block.x = old_x

#     #This function rotates the block 
#     def rotate(self):
#         old_rotation = self.block.rotation
#         self.block.rotate()
#         if self.intersects():
#             self.block.rotation = old_rotation

#     def go_down(self):
#         pressing_down = True

# pygame.font.init()

# def startGame():
#     done = False
#     clock = pygame.time.Clock()
#     fps = 25
#     game = Tetris(20, 10)
#     counter = 0

#     pressing_down = False
    
#     while not done:
#         #Create a new block if there is no moving block
#         if game.block is None:
#             game.new_block()
#         if game.nextBlock is None:
#             game.next_block()
#         counter += 1 #Keeping track if the time 
#         if counter > 100000:
#             counter = 0

#         #Moving the block continuously with time or when down key is pressed
#         if counter % (fps // game.level // 2) == 0 or pressing_down:
#             if game.state == "start":
#                 game.go_down()
#         #Checking which key is pressed and running corresponding function
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 done = True
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_UP:
#                     game.rotate()
#                 if event.key == pygame.K_DOWN:
#                     game.moveDown()
#                 if event.key == pygame.K_LEFT:
#                     game.moveHoriz(-1)
#                 if event.key == pygame.K_RIGHT:
#                     game.moveHoriz(1)
#                 if event.key == pygame.K_SPACE:
#                     game.moveBottom()
#                 if event.key == pygame.K_ESCAPE:
#                     game.__init__(20, 10)

#         screen.fill('#FFFFFF')

#         #Updating the game board regularly
#         for i in range(game.height):
#             for j in range(game.width):
#                 pygame.draw.rect(screen, '#B2BEB5', [game.x + game.zoom * j, game.y + game.zoom * i, game.zoom, game.zoom], 1)
#                 if game.field[i][j] > 0:
#                     pygame.draw.rect(screen, shapeColors[game.field[i][j]],
#                                         [game.x + game.zoom * j + 1, game.y + game.zoom * i + 1, game.zoom - 2, game.zoom - 1])

#         #Updating the board with the moving block
#         if game.block is not None:
#             for i in range(4):
#                 for j in range(4):
#                     p = i * 4 + j
#                     if p in game.block.image():
#                         pygame.draw.rect(screen, shapeColors[game.block.color],
#                                             [game.x + game.zoom * (j + game.block.x) + 1,
#                                             game.y + game.zoom * (i + game.block.y) + 1,
#                                             game.zoom - 2, game.zoom - 2])

#         #Showing the score
#         font = pygame.font.SysFont('Calibri', 40, True, False)
#         font1 = pygame.font.SysFont('Calibri', 25, True, False)
#         text = font.render("Score: " + str(game.score), True, '#000000')
#         text_game_over = font.render("Game Over", True, '#000000')
#         text_game_over1 = font.render("Press ESC", True, '#000000')

#         #Ending the game if state is gameover
#         screen.blit(text, [300, 0])
#         if game.state == "gameover":
#             screen.blit(text_game_over, [300, 200])
#             screen.blit(text_game_over1, [300, 265])
        
#         game.draw_next_block(screen)

#         pygame.display.flip()
#         clock.tick(fps)


# screen = pygame.display.set_mode((width, height))
# pygame.display.set_caption("Tetris by DataFlair")
# run = True
# while run:
#     screen.fill((16, 57, 34 ))
#     font = pygame.font.SysFont("Calibri", 70, bold=True)
#     label = font.render("Press any key to begin!", True, '#FFFFFF')

#     screen.blit(label, (10, 300 ))
#     pygame.display.update()
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             run = False
#         if event.type == pygame.KEYDOWN:
#             startGame()
# pygame.quit()




#Pinball Game using Python   //////////////////////////////////////////////


# Importing the turtle and random library
# import turtle
# from random import randint

# # Creating the screen with name and size
# screen = turtle.Screen()
# screen.title("DataFlair Pinball game")
# screen.setup(width=1000 , height=600)


# # Creating the paddle
# paddle = turtle.Turtle()
# #Setting its speed as zero, it moves only when key is pressed
# paddle.speed(0) 
# #Setting shape, color, and size
# paddle.shape("square")
# paddle.color("blue")
# paddle.shapesize(stretch_wid=2, stretch_len=6) 
# paddle.penup()
# #The paddle is left-centered initially 
# paddle.goto(-400,-250)


# # Creating the ball of circle shape
# ball = turtle.Turtle()
# #Setting the speed of ball to 0, it moves based on the dx and dy values
# ball.speed(0)
# #Setting shape, color, and size
# ball.shape("circle")
# ball.color("red")
# ball.penup()
# #Ball starts from the random position from the top of the screen
# x=randint(-400,400)
# ball.goto(x, 260)
# #Setting dx and dy that decide the speed of the ball
# ball.dx = 2
# ball.dy = -2


# score=0

# # Displaying the score
# scoreBoard = turtle.Turtle()
# scoreBoard.speed(0)
# scoreBoard.penup()
# #Hiding the turtle to show text
# scoreBoard.hideturtle()
# #Locating the score board on top of the screen
# scoreBoard.goto(0, 260)
# #Showing the score
# scoreBoard.write("Score : 0 ", align="center", font=("Courier", 20, "bold"))

# # Functions to move the paddle left and right
# def movePadRight():
#     x = paddle.xcor() #Getting the current x-coordinated of the paddle
#     x += 15 
#     paddle.setx(x) #Updating the x-coordinated of the paddle

# # Function to move the left paddle down
# def movePadLeft():
#     x = paddle.xcor() #Getting the current x-coordinated of the paddle
#     x -= 15 
#     paddle.setx(x) #Updating the x-coordinated of the paddle

# #Mapping the functions to the keyboard buttons
# screen.listen()
# screen.onkeypress(movePadRight, "Right")
# screen.onkeypress(movePadLeft, "Left")



# while True:
#     #Updating the screen everytime with the new changes
#     screen.update()
    
#     ball.setx(ball.xcor()+ball.dx)
#     ball.sety(ball.ycor()+ball.dy)

#     # Checking if ball hits the left, right, and top walls of the screen  
#     if ball.xcor() > 480:
#         ball.setx(480)
#         ball.dx *= -1 #Bouncing the ball 
 
#     if ball.xcor() < -480:
#         ball.setx(-480)
#         ball.dx *= -1#Bouncing the ball 
    
#     if ball.ycor() >280:
#         ball.setx(280)
#         ball.dy *= -1#Bouncing the ball 
    
#     #Checking if the ball hits bottom and ending the game
#     if ball.ycor() < -260:
#         scoreBoard.clear()
#         scoreBoard1 = turtle.Turtle()
#         scoreBoard1.speed(0)
#         scoreBoard1.penup()
#         #Hiding the turtle to show text
#         scoreBoard1.hideturtle()
#         #Locating the score board on top of the screen
#         scoreBoard1.goto(0, 0)
#         scoreBoard1.color('black')
#         #Showing the score
#         scoreBoard1.write("Score : {} ".format(score),    align="center", font=("Courier", 30, "bold"))
#         break
    
#     #Checking if paddle hits the ball, updating score, increasing speed and bouncing the ball
#     if (paddle.ycor() + 30 > ball.ycor() > paddle.ycor() - 30 and 
#        paddle.xcor() + 50 > ball.xcor() > paddle.xcor() - 50 ):

#         #Increasing score of left player and updating score board
#         score += 1 
#         scoreBoard.clear()
#         scoreBoard.write("Score: {}".format(score), align="center", font=("Courier", 20, "bold"))
        
#         #Increasing speed of the ball with the limit 7
#         if(ball.dy>0 and ball.dy<5): #If dy is positive increasing dy
#             ball.dy+=0.5
#         elif(ball.dy<0 and ball.dy>-5): #else if dy is negative decreasing dy
#             ball.dy-=0.5
            
#         if(ball.dx>0 and ball.dx<5):#If dx is positive increasing dx
#             ball.dx+=0.5
#         elif(ball.dx<0 and ball.dx>-5): #else if dx is negative decreasing dx
#             ball.dx-=0.5
        
#         #Changing the direction of ball towards the right player
#         ball.dy *=-1 
# while (True):
#     screen.update()








# def triangle(n):
#     return recursive_triangle(n, n)

# def recursive_triangle(x, n):
#     # First we must verify that both input values are integers.
#     if type(x) != int or type(n) != int:
#         return 'error'
#     # If x is bigger than n, we will still only print the full triangle, so we can set them equal.
#     if x > n:
#         x = n
#     # If either value is zero, the output should be an empty string because there are no lines or triangle to print.
#     if x == 0 or n == 0:
#         return ''
#     # Let's set some variable names to help us out.
#     star_print = n
#     line_number = x
#     # I'll create an empty string that we can concatenate values to.
#     line_print = ''

# # The difference value will determine how many shapes are needed to fill the line before the stars are printed.
#     difference = star_print - line_number
#     # If difference is not zero, we will print that value of spaces before the stars. The star print will be the
#     # remainder, also known as line number.
#     if difference != 0:
#         line_print += ' '*difference
#         line_print += '*'*line_number
#     # If difference is zero, then we can just fill the line with stars.
#     else:
#         line_print += '*'*star_print
#     # If the line number is greater than one, we can return our string and use the recursive call to run the function
#     # again with the line number as one value less.
#     if line_number > 1:
#         return line_print+'\n'+str(recursive_triangle(line_number-1, star_print))
#     # If the line number is exactly one, then we don't need to use the recursive call.
#     elif line_number == 1:
#         return line_print
# num = int(input("Please Enter num. of rows : "))
# print(triangle(num))


# '''
# Dice Roll Generator
# -------------------------------------------------------------
# '''


# import random
# import os


# def num_die():
#   while True:
#       try:
#           num_dice = input('Number of dice: ')
#           valid_responses = ['1', 'one', 'two', '2']
#           if num_dice not in valid_responses:
#               raise ValueError('1 or 2 only')
#           else:
#               return num_dice
#       except ValueError as err:
#           print(err)


# def roll_dice():
#    min_val = 1
#    max_val = 6
#    roll_again = 'y'

#    while roll_again.lower() == 'yes' or roll_again.lower() == 'y':
#        os.system('cls' if os.name == 'nt' else 'clear')
#        amount = num_die()

#        if amount == '2' or amount == 'two':
#            print('Rolling the dice...')
#            dice_1 = random.randint(min_val, max_val)
#            dice_2 = random.randint(min_val, max_val)

#            print('The values are:')
#            print('Dice One: ', dice_1)
#            print('Dice Two: ', dice_2)
#            print('Total: ', dice_1 + dice_2)

#            roll_again = input('Roll Again? ')
#        else:
#            print('Rolling the die...')
#            dice_1 = random.randint(min_val, max_val)
#            print(f'The value is: {dice_1}')

#            roll_again = input('Roll Again? ')


# if __name__ == '__main__':
#    roll_dice()



# '''
# Birthday Email Sender
# -------------------------------------------------------------
# pip install pandas openpyxl
# excel file cols:
# Name, Email, Birthday (MM/DD/YYYY), Last Sent (YYYY)
# '''


# import pandas as pd
# from datetime import datetime
# import smtplib
# from email.message import EmailMessage


# def send_email(recipient, subject, msg):
#    GMAIL_ID = 'your_email_here'
#    GMAIL_PWD = 'your_password_here'

#    email = EmailMessage()
#    email['Subject'] = subject
#    email['From'] = GMAIL_ID
#    email['To'] = recipient
#    email.set_content(msg)

#    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as gmail_obj:
#        gmail_obj.ehlo()
#        gmail_obj.login(GMAIL_ID, GMAIL_PWD)
#        gmail_obj.send_message(email)
#    print('Email sent to ' + str(recipient) + ' with Subject: \''
#          + str(subject) + '\' and Message: \'' + str(msg) + '\'')


# def send_bday_emails(bday_file):
#    bdays_df = pd.read_excel(bday_file)
#    today = datetime.now().strftime('%m-%d')
#    year_now = datetime.now().strftime('%Y')
#    sent_index = []

#    for idx, item in bdays_df.iterrows():
#        bday = item['Birthday'].to_pydatetime().strftime('%m-%d')
#        if (today == bday) and year_now not in str(item['Last Sent']):
#            msg = 'Happy Birthday ' + str(item['Name'] + '!!')
#            send_email(item['Email'], 'Happy Birthday', msg)
#            sent_index.append(idx)

#    for idx in sent_index:
#        bdays_df.loc[bdays_df.index[idx], 'Last Sent'] = str(year_now)

#    bdays_df.to_excel(bday_file, index=False)


# if __name__ == '__main__':
#    send_bday_emails(bday_file='your_bdays_list.xlsx')




# import time
# import random
# import argparse
# import collections

# # Get commandline arguments
# parser = argparse.ArgumentParser(description = 'Attempt to guess a word you are thinking of.')
# parser.add_argument('--debug', dest='debug', action='store_true')
# parser.set_defaults(debug = False)
# args = parser.parse_args()

# # Adhoc variables
# words		= open('dictionary.txt').read().lower().splitlines()
# print("\n\n\n",len(words))
# alphabet	= list('abcdefghijklmnopqrstuvwxyz')
# example		= random.choice(words)	# Choose a random word as an example
# success		= None					# False for failed, string for success, None for no guesses
# wrong		= []					# Store characters that are NOT in the users word
# correct		= {}					# Store characters that are in the word and how many times they occur
# guesses		= 0						# Keep track of how many questions are asked

# # Get the minimum and maximum word lengths
# minimum = len( min(words, key = len) )
# maximum = len( max(words, key = len) )

# #
# # Check if user input is boolean
# #
# # @param	string	question	Question that will be printed to the user
# # @return	boolean
# #
# def check(question):
# 	response = input('%s [Yes/no] ' % question)
# 	return response.lower() in ['y', 'yes', '1', 'true']

# #
# # Check if user input is an integer
# #
# # @param	string			question	Question that will be printed to the user
# # @return	integer|boolean				False if not an integer
# #
# def integer(question):
# 	try:
# 		return int( input('%s ' % question) )
# 	except ValueError:
# 		print('Please enter a valid number.')
# 		return False

# #
# # Debug helper, only prints string if debug argument is passed
# #
# # @param	mixed	to_print
# # @return	void
# #
# def debug(to_print):
# 	if args.debug:
# 		print(to_print)

# #
# # Spoof loading interface
# #
# # @param 	int		length	The number of times to repeat symbol
# # @param	float	timeout	Timeout between each print
# # @param	string	symbol	Symbol to print to screen
# # @return	void
# #
# def loading(length = 3, timeout = 0.1, symbol = '.'):
# 	if not args.debug:
# 		string = ''
# 		for i in range(0, length):
# 			string += symbol
# 			time.sleep(timeout)
# 			print(string)

# #
# # Filter words that have characters matching correct guesses
# # and characters that do not match wrong guesses
# #
# # @return	list	A filtered list of global variable `words`
# #
# def filter_words():

# 	filtered = []

# 	for index, word in enumerate(words):
# 		check_correct = True
# 		check_wrong = False

# 		for char, count in correct.items():
# 			if word.count(char) is not count:
# 				check_correct = False

# 		for char in wrong:
# 			if char in word:
# 				check_wrong = True

# 		delete = True if not check_correct or check_wrong else False

# 		debug('[%s] correct=%s wrong=%s delete=%s' % (word, check_correct, check_wrong, delete))

# 		if not delete:
# 			filtered.append(word)

# 	return filtered

# #
# # Order alphabet by most frequent character in `words` list
# #
# # @return	void
# #
# def order_alphabet():
# 	global alphabet

# 	combined	= ''.join(words)
# 	common_2d	= collections.Counter(combined).most_common()
# 	common_list	= [char[0] for char in common_2d]

# 	ordered = []

# 	for char in common_list:
# 		if char in alphabet:
# 			ordered.append(char)

# 	for char in alphabet:
# 		if char not in ordered:
# 			ordered.append(char)

# 	alphabet = ordered


# #
# # Filter alphabet of characters that don't appear in the words list
# #
# # @return	void
# #
# def filter_alphabet():
# 	global alphabet
# 	global wrong

# 	for char in alphabet:
# 		in_word = False
# 		for word in words:
# 			if char in word:
# 				in_word = True

# 		debug('[%s] %s used' % (char, 'is' if in_word else 'is not'))

# 		if not in_word:
# 			alphabet.remove(char)
# 			if char not in wrong:
# 				wrong.append(char)

# 	order_alphabet()

# #
# # Ask the user for their word length and confirm, repeat if wrong
# #
# # @param	boolean		confirm		Run confirmation check if True
# # @return	integer
# #
# def ask_for_length(confirm = True):
# 	word_length = False

# 	# Loop untile word_lenght is valid
# 	while word_length is False or word_length > maximum or word_length < minimum:

# 		# If length is invalid, print helper text
# 		if word_length is not False:
# 			print('Your word should have a length between %d and %d' % (minimum, maximum))

# 		# Store users input
# 		word_length = integer('Enter your word length here:')


# 	# Confirm the users input
# 	if confirm:
# 		confirmed = False
# 		while not confirmed:
# 			confirmed = check('You entered "%d", is that correct?' % word_length)
# 			if not confirmed:
# 				word_length = ask_for_length(False)

# 	return word_length

# # Print debug helpers
# debug('--- Playing in debug mode ---')

# #
# # Start game with a nice introducition
# #
# print('''
# I will be attempting to guess a word you are thinking of!
# All you have todo is think of a word with a length between %d and %d

# For example: %s (length: %d)
# ''' % (minimum, maximum, example, len(example)))

# # Get users word length
# word_length = ask_for_length()

# #
# # Lets get guessing
# #
# print('Great! Lets get started.')
# loading()

# # Filter words by length matching users input (`word_length`)
# words = [word for word in words if len(word) is word_length]

# # Order alphabet by most occuring character in list of words
# order_alphabet()

# # Cycle through `alphabet` until we can guess the word
# while success is None:

# 	# Count how many characters we have to work with
# 	total_chars = 0
# 	for char, count in correct.items():
# 		total_chars += count

# 	# If we have used all available characters, add remaing alphabet to wrong list
# 	if total_chars is word_length:
# 		wrong.extend(alphabet)
# 		alphabet = []

# 	# Check if we have any letters left in the alphabet
# 	if alphabet:

# 		# Incriment guess counter
# 		guesses += 1

# 		# Get next character to check
# 		next_char = alphabet[0]

# 		# Ask if this character occurs in their word
# 		count = integer('How many times does "%s" occur in your word? ' % next_char)

# 		# If user input is invalid, loop round and try again
# 		if count is False:
# 			continue

# 		# Ask the user if this character is in their word
# 		if count > 0:
# 			correct[next_char] = count
# 		else:
# 			wrong.append(next_char)

# 		# Now remove from alphabet
# 		alphabet.remove(next_char)

# 	# Update words list now we know what characters are/not in the word
# 	words = filter_words()

# 	# Update alphabet to reflect words list
# 	filter_alphabet()

# 	# Print loading UI
# 	loading()

# 	# Print stats
# 	debug('-' * 60)
# 	debug('Words(%d): %s' % (len(words), words))
# 	debug('Alphabet(%d): %s' % (len(alphabet), alphabet))
# 	debug('Correct(%d): %s' % (len(correct), correct))
# 	debug('Wrong(%d): %s' % (len(wrong), wrong))
# 	debug('-' * 60)

# 	# Check if we are ready to make a guess
# 	if len(words) == 1 or not alphabet:

# 		if words:
# 			success = check('Is your word "%s"?' % words[0])
# 			if success:
# 				print('Woohoo! I had to ask you %d question(s) before I got the correct answer.' % guesses)
# 			else:
# 				print('Oh no! You have outsmarted me!')
# 		else:
# 			success = False
# 			print('I ran out of words, you win!')




####################Rock Paper Scissors Game     ###############################

#RPS GUI 
#By Praveen Kathirvasan 9C
# from tkinter import *
# import random
# import tkinter
# user = int
# computer = int
# win = 0
# lose = 0
# def rps(win, lose, user):
#     computer = random.randrange(1,4)
#     if user == computer:
#         var.set("It's a draw. \n No Points")  
#     elif user == 1 and computer == 3:
#         var.set("You chose Rock, I chose Scissors. \nYou win")
#         wins.set(wins.get() + 1)
            
#     elif user == 1 and computer == 2:
#         var.set("You chose Rock, I chose Paper. \nYou lose")
#         lose += 1
#         wins.set(wins.get() - 1)    
#     elif user == 2 and computer == 1:
#         var.set("You chose Paper, I chose Rock. \nYou win")
#         wins.set(wins.get() + 1)
#         wins.set(wins.get() - 1)    
#     elif user == 2 and computer == 3:
#         var.set("You chose Paper, I chose Scissors. \nYou lose")
#         lose += 1
#         wins.set(wins.get() - 1)   
#     elif user == 3 and computer == 1:
#         var.set("You chose Scissors, I chose Rock. \nYou lose")
#         lose += 1
#         wins.set(wins.get() - 1)    
#     elif user == 3 and computer == 2:
#         var.set("You chose Scissors, I chose Paper. \nYou win")
#         wins.set(wins.get() + 1)
        
#     elif user == 4 and computer == 3:
#         var.set("You chose Spock, I chose Scissors. \nYou win")
#         wins.set(wins.get() + 1)
        
#     elif user == 4 and computer == 1:
#         var.set("You chose Spock, I chose Rock. \nYou win")
#         wins.set(wins.get() + 1)
        
#     elif user == 4 and computer == 5:
#         var.set("You chose Spock, I chose Lizard. \nYou lose")
#         lose +=1
#         wins.set(wins.get() - 1)
#     elif user == 4 and computer == 2:
#         var.set("You chose Spock, I chose Paper. \nYou lose")
#         lose +=1
#         wins.set(wins.get() - 1)
#     elif user == 5 and computer == 1:
#         var.set("You chose Lizard, I chose Rock. \nYou lose")
#         lose +=1
#         wins.set(wins.get() - 1)
#     elif user == 5 and computer == 2:
#         var.set("You chose Lizard, I chose Paper. \nYou win")
#         wins.set(wins.get() + 1)
        
#     elif user == 5 and computer == 3:
#         var.set("You chose Lizard, I chose Scissors. \nYou lose")
#         lose +=1
#         wins.set(wins.get() - 1)
#     elif user == 5 and computer == 4:
#         var.set("You chose Lizard, I chose Spock. \nYou win")
#         wins.set(wins.get() + 1)
        
#     elif user == 1 and computer == 4:
#         var.set("You chose Rock, I chose Spock. \nYou lose")
#         lose +=1
#         wins.set(wins.get() - 1)
#     elif user == 2 and computer == 4:
#         var.set("You chose Paper, I chose Spock. \nYou win")
#         wins.set(wins.get() + 1)
        
#     elif user == 3 and computer == 4:
#         var.set("You chose Scissors, I chose Spock. \nYou lose")
#         lose +=1
#         wins.set(wins.get() - 1)
#     elif user == 5 and computer == 4:
#         var.set("You chose Lizard, I chose Spock. \nYou win")
#         wins.set(wins.get() + 1)
        
#     elif user == 1 and computer == 5:
#         var.set("You chose Rock, I chose Lizard. \nYou win")
#         wins.set(wins.get() + 1)
        
#     elif user == 2 and computer == 5:
#         var.set("You chose Paper, I chose Lizard. \nYou lose")
#         lose +=1
#         wins.set(wins.get() - 1)
#     elif user == 3 and computer == 5:
#         var.set("You chose Scissors, I chose Lizard. \nYou win")
#         wins.set(wins.get() + 1)
        
#     elif user == 4 and computer == 5:
#         var.set("You chose Spock, I chose Lizard. \nYou lose")
#         lose +=1
#         wins.set(wins.get() - 1)  
#     else:
#         var.set("Thanks for playing. \nYou have " + str(win) + " wins and " + str(lose) + " losses.")


    
# top = tkinter.Tk()
# top.wm_title("RPS Python GUI")
# top.minsize(width=1000, height=500)
# top.maxsize(width=1000, height=500)
# B1 = tkinter.Button(top, text ="Rock", command = lambda: rps(win, lose, 1))
# B1.grid(row=0, column=1)
# B2 = tkinter.Button(top, text ="Paper", command = lambda: rps(win, lose, 2))
# B2.grid(row=0, column=2)
# B3 = tkinter.Button(top, text ="Scissors", command = lambda: rps(win, lose, 3))
# B3.grid(row=0, column=3)
# space = tkinter.Label(top, text="")
# space.grid(row=1)
# var = StringVar()
# var.set('Welcome!')
# l = Label(top, textvariable = var)
# l.grid(row=2, column=2)
# wins = IntVar()
# wins.set(win)
# w = Label(top, textvariable = wins)
# w.grid(row=4, column=2)
# labeled = Label(top, text = "Score:")
# labeled.grid(row=3, column=2)
# copy = Label(top, text= "RPS GUI on Tkinter on Python. By Savan")
# copy.grid(row=5, column=2)
# top.mainloop()



###########   Currency Converter   ########################


# Import required modules
# from tkinter import *
# from tkinter import ttk
# from tkinter import messagebox
# import tkinter as tk
# import requests
# import datetime as dt

# # Converting stuff
# class CurrencyConverter:

#     def __init__(self, url):
#         self.url = 'https://api.exchangerate.host/latest'
#         self.response = requests.get(url)
#         self.data = self.response.json()
#         self.rates = self.data.get('rates')

#     def convert(self, amount, base_currency, des_currency):
#         if base_currency != 'EUR':
#             amount = amount/self.rates[base_currency]

#         # Limiting the result to 2 decimal places
#         amount = round(amount*self.rates[des_currency], 2)
#         # Add comma every 3 numbers
#         amount = '{:,}'.format(amount)
#         return amount

# # Main window
# class Main(tk.Tk):

#     def __init__(self, converter):
#         tk.Tk.__init__(self)
#         self.title('Currency Converter')
#         self.geometry('400x400')
#         self.config(bg='#3A3B3C')
#         self.CurrencyConverter = converter

#         # Create title label
#         self.title_label = Label(self, text='Currency Converter', bg='#3A3B3C', fg='white', font=('franklin gothic medium', 20), relief='sunken')
#         self.title_label.place(x=200, y=35, anchor='center')

#         # Create date label
#         self.date_label = Label(self, text=f'{dt.datetime.now():%A, %B %d, %Y}', bg='#3A3B3C', fg='white', font=('calibri', 10))
#         self.date_label.place(x=0, y=400, anchor='sw')

#         # Create version label
#         self.version_label = Label(self, text='v1.0', bg='#3A3B3C', fg='white', font=('calibri', 10))
#         self.version_label.place(x=400, y=400, anchor='se')

#         # Create amount label
#         self.amount_label = Label(self, text='Input Amount: ', bg='#3A3B3C', fg='white', font=('franklin gothic book', 15))
#         self.amount_label.place(x=200, y=80, anchor='center')

#         # Create amount entry box
#         self.amount_entry = Entry(self)
#         self.amount_entry.config(width=25)
#         self.amount_entry.place(x=200, y=110, anchor='center')

#         # Create 'from' label
#         self.base_currency_label = Label(self, text='From: ', bg='#3A3B3C', fg='white', font=('franklin gothic book', 15))
#         self.base_currency_label.place(x=200, y=140, anchor='center')

#         # Create 'to' label
#         self.destination_currency_label = Label(self, text='To: ', bg='#3A3B3C', fg='white', font=('franklin gothic book', 15))
#         self.destination_currency_label.place(x=200, y=200, anchor='center')

#         # Create dropdown menus
#         self.currency_variable1 = StringVar(self)
#         self.currency_variable2 = StringVar(self)
#         self.currency_variable1.set('USD')
#         self.currency_variable2.set('IDR')

#         self.currency_combobox1 = ttk.Combobox(self, width=20, textvariable=self.currency_variable1, values=list(self.CurrencyConverter.rates.keys()), state='readonly')
#         self.currency_combobox1.place(x=200, y=170, anchor='center')

#         self.currency_combobox2 = ttk.Combobox(self, width=20, textvariable=self.currency_variable2, values=list(self.CurrencyConverter.rates.keys()), state='readonly')
#         self.currency_combobox2.place(x=200, y=230, anchor='center')

#         # Create 'convert' button
#         self.convert_button = Button(self, text='Convert', bg='#52595D', fg='white', command=self.processed)
#         self.convert_button.place(x=170, y=270, anchor='center')

#         # Create 'clear' button
#         self.clear_button = Button(self, text='Clear', bg='red', fg='white', command=self.clear)
#         self.clear_button.place(x=230, y=270, anchor='center')

#         # Create converted result field
#         self.final_result = Label(self, text='', bg='#52595D', fg='white', font=('calibri', 12), relief='sunken', width=40)
#         self.final_result.place(x=200, y=310, anchor='center')

#     # Create clear function, to clear the amount field and final result field
#     def clear(self):
#         clear_entry = self.amount_entry.delete(0, END)
#         clear_result = self.final_result.config(text='')
#         return clear_entry, clear_result

#     # Create a function to perform
#     def processed(self):
#         try:
#             given_amount = float(self.amount_entry.get())
#             given_base_currency = self.currency_variable1.get()
#             given_des_currency = self.currency_variable2.get()
#             converted_amount = self.CurrencyConverter.convert(given_amount, given_base_currency, given_des_currency)
#             # Add comma every 3 numbers
#             given_amount = '{:,}'.format(given_amount)

#             self.final_result.config(text=f'{given_amount} {given_base_currency} = {converted_amount} {given_des_currency}')

#         # Create warning message box
#         except ValueError:
#             convert_error = messagebox.showwarning('WARNING!', 'Please Fill the Amount Field (integer only)!')
#             return convert_error


# if __name__ == '__main__':
#     converter = CurrencyConverter('https://api.exchangerate.host/latest')
#     Main(converter)
#     mainloop()


###############     Music Player GUI with Python:   ###############



# import pygame
# import tkinter as tkr
# from tkinter.filedialog import askdirectory
# import os

# music_player = tkr.Tk()
# music_player.title("My Music Player")
# music_player.geometry("450x350")
# directory = askdirectory()
# os.chdir(directory)
# song_list = os.listdir()

# play_list = tkr.Listbox(music_player, font="Helvetica 12 bold", bg='yellow', selectmode=tkr.SINGLE)
# for item in song_list:
#     pos = 0
#     play_list.insert(pos, item)
#     pos += 1
# pygame.init()
# pygame.mixer.init()

# def play():
#     pygame.mixer.music.load(play_list.get(tkr.ACTIVE))
#     var.set(play_list.get(tkr.ACTIVE))
#     pygame.mixer.music.play()
# def stop():
#     pygame.mixer.music.stop()
# def pause():
#     pygame.mixer.music.pause()
# def unpause():
#     pygame.mixer.music.unpause()
# Button1 = tkr.Button(music_player, width=5, height=3, font="Helvetica 12 bold", text="PLAY", command=play, bg="blue", fg="white")
# Button2 = tkr.Button(music_player, width=5, height=3, font="Helvetica 12 bold", text="STOP", command=stop, bg="red", fg="white")
# Button3 = tkr.Button(music_player, width=5, height=3, font="Helvetica 12 bold", text="PAUSE", command=pause, bg="purple", fg="white")
# Button4 = tkr.Button(music_player, width=5, height=3, font="Helvetica 12 bold", text="UNPAUSE", command=unpause, bg="orange", fg="white")

# var = tkr.StringVar() 
# song_title = tkr.Label(music_player, font="Helvetica 12 bold", textvariable=var)

# song_title.pack()
# Button1.pack(fill="x")
# Button2.pack(fill="x")
# Button3.pack(fill="x")
# Button4.pack(fill="x")
# play_list.pack(fill="both", expand="yes")
# music_player.mainloop()


from tkinter import *
from pytube import YouTube

root = Tk()
root.geometry('500x300')
root.resizable(0,0)
root.title("DataFlair-youtube video downloader")


Label(root,text = 'Youtube Video Downloader', font ='arial 20 bold').pack()




##enter link
link = StringVar()

Label(root, text = 'Paste Link Here:', font = 'arial 15 bold').place(x= 160 , y = 60)
link_enter = Entry(root, width = 70,textvariable = link).place(x = 32, y = 90)



#function to download video


def Downloader():
     
    url =YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(root, text = 'DOWNLOADED', font = 'arial 15').place(x= 180 , y = 210)  


Button(root,text = 'DOWNLOAD', font = 'arial 15 bold' ,bg = 'pale violet red', padx = 2, command = Downloader).place(x=180 ,y = 150)



root.mainloop()