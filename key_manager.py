import info
from configparser import ConfigParser, NoOptionError, NoSectionError


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
            github_auth_token = self.config.get(self.CLOUD_TOKEN_SECTION, self.CLOUD_TOKEN_SECTION)
        except (NoSectionError, NoOptionError):
            pass

        if github_auth_token == '':
            self.handle_github_token_input()
        else:
            print('Found your github auth token !!')
            return github_auth_token

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
