import os
import pyautogui
from colorama import init, Fore, Style
import time
import keyboard
import socket

init(autoreset=True)

color_toggle = False

last_print_time = time.time()

for i in range(10):
    print(Style.BRIGHT + Fore.WHITE + f"Loading... {i*10}%")
    time.sleep(0.1)

    if i == 9:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(Fore.WHITE + "Loaded\n")
        print(Fore.WHITE + "Press Enter to print coordinates or 'h' for help.")


while True:
    if keyboard.is_pressed('enter'):
            x, y = pyautogui.position()
            if color_toggle:
                color = Fore.WHITE
            elif x < 500 and y < 500:
                color = Fore.GREEN
            elif x < 1000 and y < 1000:
                color = Fore.YELLOW
            else:
                color = Fore.RED
            print(color + f"({x}, {y})")

    elif keyboard.is_pressed('l'):
        current_time = time.time()
        if current_time - last_print_time >= 3:
            print(Fore.WHITE + "This feature is currently broken. Are you sure you want to continue? (Y/N)")
            while True:
                if keyboard.is_pressed('y'):
                    x, y = pyautogui.position()
                    with open(f"coords_log_{time.time()}.txt", "a") as f:
                        f.write(f"{time.ctime()}: ({x}, {y})\n")
                    print(Fore.WHITE + "Coordinates logged.")
                    last_print_time = current_time
                    break
                elif keyboard.is_pressed('n'):
                    print(Fore.WHITE + "Operation cancelled.")
                    last_print_time = current_time
                    break


    elif keyboard.is_pressed('h'):
        current_time = time.time()
        if current_time - last_print_time >= 3:
            print("Hello there! Look like u need some help, there u go whit some key that can help ya <3")
            print(Fore.WHITE + "|     H = Help     |      Q = quit       | Enter = Print Coords|")
            print(Fore.WHITE + "|     L = Logs     |      N = idk        | W = U are a racist  |")
            last_print_time = current_time

    elif keyboard.is_pressed('n'):
        current_time = time.time()
        if current_time - last_print_time >= 3:
            os.system("start https://www.youtube.com/watch?v=dQw4w9WgXcQ")
            print(Fore.WHITE + "okay imma rick roll ur ass...")
            last_print_time = current_time

    elif keyboard.is_pressed('w'):
        current_time = time.time()
        if current_time - last_print_time >= 3:
            color_toggle = not color_toggle
            if color_toggle:
                print(Fore.WHITE + f"because u a racist here is ur IP address: {socket.gethostbyname(socket.gethostname())}")
            else:
                print("Printing coordinates in color again hope u got ur lesson :(")
            last_print_time = current_time
            
            
    elif keyboard.is_pressed('q'):
        print(Fore.WHITE + "Exiting...")
        break


    time.sleep(0.1)
