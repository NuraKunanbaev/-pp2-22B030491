import pygame
import os

pygame.init()

# Define some constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BG_COLOR = (255, 255, 255)
FONT_SIZE = 35
FONT_COLOR = (0, 0, 0)

MUSIC_FILES = []
way='C:/Users/admin/Desktop/fx/-pp2-22B030491/TSIS7/music/'
FILES = os.listdir('C:/Users/admin/Desktop/fx/-pp2-22B030491/TSIS7/music/')
print(FILES)
for song in FILES :
    if song.endswith(".mp3"):
        MUSIC_FILES.append(way+song)
print(MUSIC_FILES)


# Initialize the display window and font
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
font = pygame.font.Font(None, FONT_SIZE)

current_music = 0
# Initialize the music player
pygame.mixer.music.load(MUSIC_FILES[current_music])

# Define some helper functions
def play_music():
    pygame.mixer.music.play()

def stop_music():
    pygame.mixer.music.stop()

def next_music():
    global current_music
    current_music = int(current_music + 1) % len(MUSIC_FILES)
    pygame.mixer.music.stop()
    pygame.mixer.music.load(MUSIC_FILES[current_music])
    pygame.mixer.music.play()

def prev_music():
    global current_music
    current_music = (current_music - 1) % len(MUSIC_FILES)
    pygame.mixer.music.stop()
    pygame.mixer.music.load(MUSIC_FILES[current_music])
    pygame.mixer.music.play()

# Start playing the first music file

    play_music()
# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if pygame.mixer.music.get_busy():
                    stop_music()
                else:
                    play_music()
            elif event.key == pygame.K_a:
                next_music()
            elif event.key == pygame.K_d:
                prev_music()

    # Draw the text on the screen
    text = font.render("Press SPACE to play/pause, LEFT/RIGHT to change music", True, FONT_COLOR)
    text_rect = text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2))
    screen.fill(BG_COLOR)
    screen.blit(text, text_rect)
    pygame.display.update()