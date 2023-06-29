import time


def github_auth_token_instructions():
    print("Don't have github access auth token ?\nDon't worry, I will guide you !\nFollow the below steps . . .")
    time.sleep(1)
    print(r'[STEP 1] Browse this URL : https://github.com/settings/tokens/new')
    time.sleep(0.5)
    print('(Make sure you are logged in with the browser you are browsing this url)')
    time.sleep(0.5)
    print('(It may ask you to enter your github password, enter and continue)\n')
    time.sleep(0.5)
    res = input("Hit enter for next step or 'q' to exit instruction mode")
    if res == 'q' or res == 'Q':
        return
    print('[STEP 2] Enter the name of the token as per your choice\n')
    if res == 'q' or res == 'Q':
        return
    print('[STEP 3] In scope tick all the boxes under repo heading\n')
    if res == 'q' or res == 'Q':
        return
    print('[STEP 4] Save it and you will have you github auth token')




