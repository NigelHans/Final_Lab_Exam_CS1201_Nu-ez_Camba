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
                elif username in self.user_database:
                    print('Username Already Exist')
                    
                password = input("Enter a Password or leave blank to Exit")
                if len(password) < 8:
                    print("Password must be 8 characters")
                else:
                    print("Account Successfully Registered")
            except ValueError as e:
                print(e)
    def login(self):
            pass
             