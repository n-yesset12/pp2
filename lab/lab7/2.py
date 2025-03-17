import pygame
import os

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((500, 300))
pygame.display.set_caption("Music Player")

MUSIC_FOLDER = "C:\proger\pp2\lab\lab7\music"

songs = [f for f in os.listdir(MUSIC_FOLDER) if f.endswith(".mp3")]
if not songs:
    print("No MP3 files found in the folder")
    exit()

current_song_index = 0

def play_song(index):
    pygame.mixer.music.load(os.path.join(MUSIC_FOLDER, songs[index]))
    pygame.mixer.music.play()
    pygame.display.set_caption(f"Playing: {songs[index]}")

play_song(current_song_index)

running = True
paused = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                    paused = True
                elif paused:
                    pygame.mixer.music.unpause()
                    paused = False
                else:
                    play_song(current_song_index)

            elif event.key == pygame.K_ESCAPE:
                pygame.mixer.music.stop()

            elif event.key == pygame.K_RIGHT:
                current_song_index = (current_song_index + 1) % len(songs)
                play_song(current_song_index)

            elif event.key == pygame.K_LEFT:
                current_song_index = (current_song_index - 1) % len(songs)
                play_song(current_song_index)

pygame.quit()
