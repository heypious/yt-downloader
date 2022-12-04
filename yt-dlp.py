from os import system as terminal
from os import getcwd as curdir
link = []

def path(): #happens once at start
    path_ask = input("[I]nput path or [C]urrent Directory?: ").lower
    if path_ask == "i":
        terminal(f"cd {input('Path: ')}")
    elif path_ask == "c":
        terminal(f"cd {curdir()}")

path()
while True:
    ask = input("Link: ")
    if ask != "x":
        link.append(ask)
    elif ask == "x":
        break


type = input("[V]ideo or [A]udio?: ").lower

if type == "v":
    for links in link:
        terminal(f'yt-dlp -f "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[mp4]" {links}')

else:
    for links in link:
        terminal(f'yt-dlp -f "bestaudio[ext=m4a]" {links}')
