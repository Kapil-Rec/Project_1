import pygame
import random

pygame.init()

#color
white=(255, 255, 255)
red=(255,0,0)
pink1=(255, 127, 127)
black=(0,0,0)
pink=(255, 134, 100)

# display
screen_height=600
screen_width=900




gameWindow=pygame.display.set_mode((screen_width,screen_height))
 #title
pygame.display.set_caption("Snake_Game")
pygame.display.update()

#variable


clock = pygame.time.Clock()

font = pygame.font.SysFont(None,40)

def text_screen(text,color,x,y):
      screen_text=font.render(text,True,color)
      gameWindow.blit(screen_text,[x,y])

def plot_snake(gameWindow,color,snk_list,snake_size):
      for x,y in snk_list:
            pygame.draw.rect(gameWindow,color,[x,y,snake_size,snake_size])
      


      
#loop
def gameloop():
      exit_game=False
      game_over=False
      snake_x=45
      snake_y=55
      snake_size=10

      velocity_x=0
      velocity_y=0

      food_x=random.randint(20,screen_width/2)
      food_y=random.randint(20,screen_height/2)

      init_velocity=3
      score=0
      fps=50

      snk_list=[]
      snk_length= 1

      while not exit_game:

            if game_over :
                  gameWindow.fill(white)
                  text_screen("Game Over! Press Enter To Continue",black,150,250)
                  text_screen("Score:"+str(score * 5),red, 160, 223)
                  for event in pygame.event.get():

                        if event.type == pygame.QUIT:
                              exit_game = True
                        if event.type == pygame.KEYDOWN:
                              if event.key == pygame.K_RETURN:
                                    gameloop()
                        
                  
            else:      
                  
                  for event in pygame.event.get():

                        if event.type == pygame.QUIT:
                              exit_game = True
                        if event.type == pygame.KEYDOWN:
                              if event.key == pygame.K_RIGHT:
                              
                                    velocity_x=init_velocity
                                    velocity_y=0

                              if event.key == pygame.K_LEFT:
                                    velocity_x=-init_velocity
                                    velocity_y=0

                              if event.key == pygame.K_UP:
                                    velocity_y=-init_velocity
                                    velocity_x=0

                              if event.key == pygame.K_DOWN:
                                    velocity_y=init_velocity
                                    velocity_x=0

                              
                  snake_x=snake_x + velocity_x
                  snake_y=snake_y + velocity_y

                  if abs(snake_x - food_x)<6 and abs(snake_y - food_y)<6:
                        score+=1
                        #print("score:",score)
                        
                        food_x=random.randint(20,screen_width/2)
                        food_y=random.randint(20,screen_height/2)

                        snk_length+=5
                  
                  gameWindow.fill(black)
                  # function score display
                  text_screen("Score:"+str(score * 5),pink1, 2, 3)
                  # ..
                  head=[]
                  head.append(snake_x)
                  head.append(snake_y)
                  snk_list.append(head)

                  if len(snk_list)>snk_length:
                        del snk_list[0]

                  if head in snk_list[:-1]:
                        game_over = True
                        

                  if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height :
                        game_over = True
                        print("game over")

                              
                        
                  plot_snake(gameWindow,pink,snk_list,snake_size)
                  
                  
                  pygame.draw.rect(gameWindow, red, [food_x,food_y, snake_size, snake_size])
                  pygame.draw.rect(gameWindow, white, [snake_x,snake_y, snake_size, snake_size])
            pygame.display.update()

            clock.tick(fps)

      pygame.quit()
      quit()

gameloop()



