# RPG Game!
import pygame
import sys
import random
import time

check_errors = pygame.init()

if check_errors[1] > 0:
    print("(!) Had {0} initializing errors, exiting...".format(check_errors[1]))
    sys.exit(-1)
else:
    print("(+) PyGame successfully initialized!")

# Play Surface
screen_widht = 720
screen_height = 460
screen = pygame.display.set_mode((screen_widht, screen_height))  # display size on a tuple
pygame.display.set_caption("RPG time!")

# Colours
color_black = pygame.Color(0, 0, 0)  # pygame.Color(r, g, b)
color_blue = pygame.Color(0, 0, 255)
color_green = pygame.Color(0, 255, 0)
color_red = pygame.Color(255, 0, 0)
color_white = pygame.Color(255, 255, 255)
color_brown = pygame.Color(164, 42, 42)

# Frames per second controller
fps_controller = pygame.time.Clock()

# More variables
framerate = 15
block_size = 20
score = 0
msg_display = False
msg_time = time.time()
msg_duration = 2
key_pressed = ""
heart_image = pygame.image.load("images/heart01.png").convert()
heart_image = pygame.transform.scale(heart_image, (int(block_size), int(block_size)))

def show_text(text="Nice try", color=color_blue, position=(int(screen_widht/2), 20)):
    text_font = pygame.font.SysFont("monaco", 72)  # pygame.font.SysFont(name, size)
    text_surface = text_font.render(text, True, color)  # gameover_font.render(text, antialias, color) - The surface where the font will be rendered
    text_rectangule = text_surface.get_rect()  # represents the rectangle of the surface
    text_rectangule.midtop = position  # (x=horizontal, y=vertical) coordinates
    screen.blit(text_surface, text_rectangule)  # puts the surface on the play surface


def quit_game():
    screen.fill(color_white)
    show_text(text="Bye", position=(int(screen_widht/2), int(screen_height/2)))
    pygame.display.flip()  # flips the frame to make the text appear
    time.sleep(1)
    pygame.quit()  # pygame exit
    sys.exit(0)  # console exit


# Game over function
def game_over():
    pygame.mixer.music.set_endevent(pygame.USEREVENT)
    pygame.mixer.music.load("sounds/gameover_laugh.mp3")
    pygame.mixer.music.play()
    show_lifes(0)
    show_text(text="Game Over", color=color_red)
    pygame.display.flip()  # flips the frame to make the text appear
    time.sleep(3)
    quit_game()


def show_lifes(lifes=5):
    text_font = pygame.font.SysFont("monaco", 24)
    lifes_surface = text_font.render("Lifes: ", True, color_black)
    lifes_rectangle = lifes_surface.get_rect()
    lifes_rectangle.midtop = (block_size*2, block_size * 3)
    screen.blit(lifes_surface, lifes_rectangle)  # puts the surface on the play surface
    screen.blit(heart_image, (block_size * 2, block_size * 4), )
    screen.blit(heart_image, (block_size * 3, block_size * 4), )


def show_class(class_name="warrior"):
    text_font = pygame.font.SysFont("monaco", 24)
    score_surface = text_font.render("Class: " + str(class_name), True, color_black)
    score_rectangle = score_surface.get_rect()
    score_rectangle.midtop = (block_size * 2, block_size * 2)
    screen.blit(score_surface, score_rectangle)  # puts the surface on the play surface


show_text(text="Deploying enemies...", color=color_white)
pygame.display.flip()  # flips the frame to make the text appear
pygame.mixer.music.load("sounds/open_laugh.mp3")
pygame.mixer.music.play()
time.sleep(1)


# Main logic of the game
while True:
    try:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Checks if user requested to quit
                quit_game()
            elif event.type == pygame.KEYDOWN:  # Checks if the user hit a key
                if event.key == pygame.K_UP or event.key == ord('w'):  # Check if key hitted was the up arrow key or the w button
                    key_pressed = 'UP'
                if event.key == pygame.K_DOWN or event.key == ord('s'):
                    key_pressed = 'DOWN'
                if event.key == pygame.K_LEFT or event.key == ord('a'):
                    key_pressed = 'LEFT'
                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    key_pressed = 'RIGHT'
                if event.key == pygame.K_ESCAPE:
                    pygame.event.post(pygame.event.Event(pygame.QUIT))

        screen.fill(color_white)
        # Drawings should be bellow this line, otherwise they will not appear

        show_lifes()
        show_class()
        pygame.display.flip() # update the frame
        fps_controller.tick(framerate) # controls the framerate
    except Exception as e:
        print(e)
        show_text(text="Error!")
        quit_game()
