import time
import pyautogui
from github import Github, Auth, GithubException
import key_manager
import asyncio
from pynput import keyboard


def copy_paste():
    time.sleep(3)
    with open('clipboard.txt', 'r') as r:
        lines = r.readlines()
        print(lines)
        for line in lines:
            s = line
            pyautogui.hotkey('ctrl', 'backspace')
            pyautogui.write(s)
            pyautogui.write(' ')


def sync_content():
    try:
        github_auth_token = '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' #km.get_github_key()
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


async def on_key_press(key):
    if key == keyboard.Key.f9:
        copy_paste()
    if key == keyboard.Key.f8:
        sync_content()


app_version = '0.1'
# km = key_manager.KeyManager()
# github_auth_token = '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' #km.get_github_key()
# auth = Auth.Token(github_auth_token)
# g = Github(auth=auth)
# repo = g.get_user().get_repo('clipboard')
print("Running")


async def listen_for_keyboard_events():
    # Create a keyboard listener
    listener = keyboard.Listener(on_press=on_key_press)
    
    # Start the listener asynchronously
    listener.start()

    # Wait for the listener to finish (e.g., until Ctrl+C is pressed)
    await listener.join()

loop = asyncio.get_event_loop()
loop.run_until_complete(listen_for_keyboard_events())


