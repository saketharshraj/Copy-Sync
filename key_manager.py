import info
from configparser import ConfigParser, NoOptionError, NoSectionError
from github import Github, Auth, BadCredentialsException

class KeyManager:
    def __init__(self):
        self.config = ConfigParser()
        self.CONFIG_FILE = 'configs.ini'
        self.config.read(self.CONFIG_FILE)
        self.CLOUD_TOKEN_SECTION = 'CLOUD TOKENS'
        self.GITHUB_TOKEN_OPTION = 'github_auth_token'

    def get_github_key(self):
        github_auth_token = ''
        try:
            github_auth_token = self.config.get(self.CLOUD_TOKEN_SECTION, self.GITHUB_TOKEN_OPTION)
        except (NoSectionError, NoOptionError) as e:
            print(e)

        if github_auth_token == '':
            self.handle_github_token_input()
        else:
            print('Found your github auth token !!')
            if (self.check_github_auth_token(github_auth_token)):
                return github_auth_token
            return None
        
    def check_github_auth_token(self, token):
        print("Validating Your Token")
        try:
            auth = Auth.Token(token)
            g = Github(auth=auth)
            repo = g.get_user().get_repo('clipboard')
            print("Token Looks Sexy")
            return True
        except BadCredentialsException:
            print('Your github auth token is invalid')
            print('Please enter a valid token')
            self.handle_github_token_input()
            print('Run the program again to use the new token')
        except e:
            print('[ERROR IN KEY MANAGER]', e)
            return False
    def handle_github_token_input(self):
        print('You need to enter github auth token')
        res = input('Do you need instructions to get the token (y/n) : ')
        if res.lower() == 'y' or res.lower() == 'yes':
            info.github_auth_token_instructions()
        self.new_key_input('Enter your github auth token : ', self.GITHUB_TOKEN_OPTION)

    def new_key_input(self, message, key_name):
        key = input(message)
        if not self.config.has_section(self.CLOUD_TOKEN_SECTION):
            self.config.add_section(self.CLOUD_TOKEN_SECTION)
        self.config.set(self.CLOUD_TOKEN_SECTION, key_name, key)
        with open(self.CONFIG_FILE, 'w') as config_file:
            self.config.write(config_file)
