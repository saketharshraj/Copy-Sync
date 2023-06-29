import time
import pyautogui
from github import Github, Auth, GithubException
import key


def get_cloud_platform():
    print('Choose cloud platform for your clipboard :')
    print('1. GitHub ')
    choice = input('Your Choice : ')
    if choice == '1':
        auth_token = input('Your github auth token : ')
        return 'GitHub', auth_token


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
# cloud_data, token = get_cloud_platform()


auth = Auth.Token(key.KEY)
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
