class ApolloLogin:
    message: str

    def __init__(self, message: str = 'Default message'):
        self.message = message

    def display_login_page(self):
        print(f'Message from login page {self.message!r}')
