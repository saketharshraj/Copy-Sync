import time
import pyautogui
from github import Github, Auth, GithubException
import key_manager
import keyboard


def copy_paste(e):
    time.sleep(3)
    try:
        with open('clipboard.txt', 'r') as r:
            lines = r.readlines()
            print(lines)
            for line in lines:
                s = line
                pyautogui.hotkey('ctrl', 'backspace')
                pyautogui.write(s)
                pyautogui.write(' ')
    except e:
        print("[CURRENT TYPING IS TERMINATED PROBABLY DUE TO SAFETY TRIGGER]")


def sync_content(e):
    try:
        github_auth_token = km.get_github_key()
        auth = Auth.Token(github_auth_token)
        g = Github(auth=auth)
        repo = g.get_user().get_repo('clipboard')
        clipboard = repo.get_contents("code.txt")
        content = clipboard.decoded_content.decode()
        with open('clipboard.txt', 'w') as f:
            f.write(content)
        print('File Synced')

    except GithubException:
        repo.create_file(path="code.txt", message="New_User", content=str('This file is automatically created by copy '
                                                                        'sync.\nYou can edit this file and start copy '
                                                                        'paste'))
        print('File Created')
    except e:
        print('[ERROR IN SYNC CONTENT]', e)
        


def terminate_program(e):
    global running
    running = False
    print("Program is terminating...")



app_version = '0.1'
km = key_manager.KeyManager()
github_auth_token = km.get_github_key()
if not github_auth_token:
    print('No github auth token found. Exiting...')
    exit(0)

auth = Auth.Token(github_auth_token)
g = Github(auth=auth)
repo = g.get_user().get_repo('clipboard')
print("Running")



# Assign functions to hotkeys
keyboard.on_press_key('f9', copy_paste)
keyboard.on_press_key('f7', sync_content)

keyboard.on_press_key('f12', terminate_program)

running = True

# Main loop
while running:
    time.sleep(0.1)

print("Program has terminated.")
