import pygame

# Initialize Pygame
pygame.init()

# Set up the display window
screen_width = 600
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("My Game")

# Define colors (R, G, B)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0 ,0)

# Create a player rectangle object at position (x,y) with size width x height 
player_size = 50
player_x_pos = screen_width //2 - player_size //2 # center horizontally on screen 
player_y_pos= screen_height *3/4 - player_size//2 # place near bottom of screen 
player_rect=pygame.Rect(player_x_pos , player_y_pos , player_size , player_size )

#button
button_position = (200, 200)  # 按钮位置
button_size = (100, 50)  # 按钮大小
button_color = (255, 0, 0)  # 按钮颜色（红色）
button_text = "Click Me"  # 按钮文本

button = pygame.Rect(button_position[0], button_position[1], button_size[0], button_size[1])

# Load font and render text surface object  
font_obj=pygame.font.SysFont('arial',25,True,False)   # create font object       
text_surface_obj1=font_obj.render('Welcome to My Game!', True,BLACK)    # create text surface obj 

# Define game loop variables 
clock=pygame.time.Clock()
running=True 



while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # If user clicked close button in title bar  
            running=False 
            
        elif event.type==pygame.KEYDOWN: # If user pressed down any key  
            if event.key==pygame.K_LEFT:   # Move to left when 'LEFT' arrow is pressed   
                player_rect.move_ip(-10*5/6 ,0)    
                
            elif event.key==pygame.K_RIGHT:   # Move to right when 'RIGHT' arrow is pressed         
                player_rect.move_ip(10*5/6 ,0)     
                
    clock.tick(60)     # Limit frame rate to maximum of sixty frames per second 
    
    ## Draw the game world ##
    
    # Fill background color      
    screen.fill(WHITE)  
    
	# Draw text on the screen
    screen.blit(text_surface_obj1,(screen_width /2 - text_surface_obj1.get_width() / 2, 50))
	
    # Draw player rectangle
    pygame.draw.rect(screen, RED, player_rect)
    pygame.draw.rect(screen, button_color, button)
    font = pygame.font.Font(None, 36)
    text = font.render(button_text, True, (255, 255, 255))
    text_rect = text.get_rect(center=button.center)
    screen.blit(text, text_rect)

    # Update the display 
    pygame.display.flip()
            
pygame.quit()