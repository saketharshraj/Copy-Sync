import time
import os
import platform
import pyautogui
from github import Github, Auth, GithubException
import key_manager
import keyboard

# Auto-detect OS
IS_MAC = platform.system() == "Darwin"

def copy_paste(e):
    time.sleep(3)
    try:
        with open('clipboard.txt', 'r') as r:
            lines = r.readlines()
            for line in lines:
                
                if IS_MAC:
                    # Native AppleScript completely bypasses PyAutoGUI's Mac modifier bug. 
                    # No emojis, no dictation popups, no stuck command keys.
                    # 1. Press Cmd + Shift + Left (Selects the IDE's auto-indent)
                    os.system("osascript -e 'tell application \"System Events\" to key code 123 using {command down, shift down}'")
                    # 2. Press Backspace (Deletes it)
                    os.system("osascript -e 'tell application \"System Events\" to key code 51'")
                else:
                    # Windows/Linux approach
                    pyautogui.press('home')
                    pyautogui.keyDown('shift')
                    pyautogui.press('end')
                    pyautogui.keyUp('shift')
                    pyautogui.press('backspace')
                
                # Adding interval=0.02 slows typing just enough to prevent Mac from turning double-spaces into periods (.)
                pyautogui.write(line, interval=0.001)
                
    except pyautogui.FailSafeException:
        print("[CURRENT TYPING IS TERMINATED DUE TO SAFETY TRIGGER]")
    except FileNotFoundError:
        # create the file with some content in the directory
        s = 'This file is automatically created by copy sync.\nCopy the content on your github repo clipboard with file name code.txt'
        with open('clipboard.txt', 'w') as f:
            f.write(s)
        pyautogui.write(s)
            

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
    except Exception as ex:
        print('[ERROR IN SYNC CONTENT]', ex)
        


def terminate_program(e):
    global running
    running = False
    print("Program is terminating...")



app_version = 'v1.1.0'
km = key_manager.KeyManager()
github_auth_token = km.get_github_key()
if not github_auth_token:
    print('Run the program again . . .')
    exit()

auth = Auth.Token(github_auth_token)
g = Github(auth=auth)
repo = g.get_user().get_repo('clipboard')
print("Running")



# Assign functions to hotkeys
keyboard.on_press_key('f9', copy_paste)
keyboard.on_press_key('f8', sync_content)

keyboard.on_press_key('f12', terminate_program)

running = True

# Main loop
while running:
    time.sleep(0.1)

print("Program has terminated.")