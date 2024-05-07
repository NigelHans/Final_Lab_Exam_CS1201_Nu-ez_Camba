class UserManager: 
    user_database = {}
    def load_users():
        pass
    def save_users():
        pass
    def validate_username():
        pass
    def validate_password():
        pass
    def register(self):
        print("Welcome to Register")
        while True:
            try:
                username = input("Enter a Username or leave blank to Exit")
                if not username:
                    return
                
                if username < 4:
                    print('username must be atleast 4 characters')
                    self.register()
                else:
                    password = input("Enter password (atleast 8 characters): ")

                if username in self.user_database:
                    print('Username Already Exist')
                    self.register()
            except ValueError as e:
                print(e)
    def login(self):
            pass
             