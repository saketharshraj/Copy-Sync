from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
import configparser


class KeyManager:
    def __init__(self):
        self.config = configparser.ConfigParser()
        master_key = self.config.get('Encryption Keys', 'master_key')
        if master_key == '':
            key = Fernet.generate_key()


    @staticmethod
    def get_password():
        while True:
            password = input('Enter password to unlock your tokens : ')
            confirm_password = input('Enter it again')
            if not password == confirm_password:
                print("Password didn't match. Try again !!")
            else:
                return password

    def get_github_key(self):
        self.config.read('configs.ini')
        github_auth_token = self.config.get('Cloud Tokens', 'github_auth_token')
        if github_auth_token == '':
            self.handle_github_token_input()
        else:
            print('Found your github auth token !!')
            pass_key = input('Enter your decryption key : ')


    def handle_github_token_input(self):

    def new_key_input(self, message, key_name):


km = KeyManager()
km.get_github_key()
