import webbrowser
import os
import time
import random
import pygame
import threading

# Global variables to manage music playback
current_track_index = 0
music_files = []
paused = False
music_stopped = False

# Define the music folder path here
music_folder = r'C:\Users\three\Nathan\Coding\Python\PythonCodeEnv\MegaProject'

def open_google():
    webbrowser.open('https://www.google.com')

def open_youtube():
    webbrowser.open('https://www.youtube.com')

def initialize_mixer():
    try:
        pygame.mixer.init()
    except pygame.error as e:
        print(f"Error initializing mixer: {e}")
        return False
    return True

def load_music_files():
    global music_files
    supported_formats = ('.mp3', '.wav', '.ogg')
    
    music_files = [f for f in os.listdir(music_folder) if f.endswith(supported_formats)]

    if not music_files:
        print("No music files found in the specified folder.")
        return False

    random.shuffle(music_files)
    return True

def play_music():
    global current_track_index, paused, music_stopped

    if not initialize_mixer():
        return
    if not load_music_files():
        return

    while True:
        if not paused and not music_stopped:
            file_path = os.path.join(music_folder, music_files[current_track_index])
            try:
                pygame.mixer.music.load(file_path)
                pygame.mixer.music.play()
            except pygame.error as e:
                print(f"Error loading or playing the file: {e}")
                return

            while pygame.mixer.music.get_busy() or paused:
                if music_stopped:
                    return
                time.sleep(1)

            if not paused and not music_stopped:
                current_track_index = (current_track_index + 1) % len(music_files)

def play_music_thread():
    global music_stopped
    music_stopped = False
    music_thread = threading.Thread(target=play_music)
    music_thread.start()

def pause_music():
    global paused
    if not paused:
        pygame.mixer.music.pause()
        paused = True
    else:
        print("Music is already paused.")

def resume_music():
    global paused
    if paused:
        pygame.mixer.music.unpause()  # This resumes the song from where it was paused
        paused = False
    else:
        print("Music is already playing.")

def next_music():
    global current_track_index, paused, music_stopped
    if len(music_files) > 1:
        pygame.mixer.music.stop()  # Stop current song
        current_track_index = (current_track_index + 1) % len(music_files)  # Move to next song
        paused = False
        music_stopped = False
        play_music_thread()  # Play the next song
    else:
        print("No more tracks in the playlist.")

def previous_music():
    global current_track_index, paused, music_stopped
    if len(music_files) > 1:
        pygame.mixer.music.stop()  # Stop current song
        # Move to the previous track, but make sure it's in range
        current_track_index = (current_track_index - 1) % len(music_files)
        paused = False
        music_stopped = False
        play_music_thread()  # Play the previous song
    else:
        print("No previous tracks in the playlist.")

def open_whatsapp():
    webbrowser.open('https://web.whatsapp.com')

def main():
    while True:
        print("\nChoose an option:")
        print("1. Open Google")
        print("2. Open YouTube")
        print("3. Play Music")
        print("4. Pause Music")
        print("5. Resume Music")
        print("6. Next Track")
        print("7. Previous Track")
        print("8. Open WhatsApp")
        print("9. Exit")
        
        choice = input("Enter your choice (1-9): ")

        if choice == '1':
            open_google()
        elif choice == '2':
            open_youtube()
        elif choice == '3':
            play_music_thread()
        elif choice == '4':
            pause_music()
        elif choice == '5':
            resume_music()
        elif choice == '6':
            next_music()
        elif choice == '7':
            previous_music()
        elif choice == '8':
            open_whatsapp()
        elif choice == '9':
            print("Exiting...")
            pygame.mixer.music.stop()
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
