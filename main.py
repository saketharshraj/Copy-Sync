import time
import pyautogui
from github import Github, Auth, GithubException
import key_manager


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


app_version = '0.1'
km = key_manager.KeyManager()
github_auth_token = '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' #km.get_github_key()
auth = Auth.Token(github_auth_token)
g = Github(auth=auth)
repo = g.get_user().get_repo('clipboard')
print("Running")
try:
    clipboard = repo.get_contents("code.txt")
    content = clipboard.decoded_content.decode()
    with open('clipboard.txt', 'w') as f:
        f.write(content)


except GithubException:
    repo.create_file(path="code.txt", message="New_User", content=str('This file is automatically created by copy '
                                                                      'sync.\nYou can edit this file and start copy '
                                                                      'paste'))
    print('File Created')

copy_paste()
