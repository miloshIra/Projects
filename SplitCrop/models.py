
users_database = {}  # Dictionary that replaces a database, I am to lazy and dumb to make a DB"


class User(object):

    def __init__(self, username, password):  # This class needs to have an id too.
        self.username = username
        self.password = password

    def register(self):
        """Registers a user"""
        if self.username not in users_database:
            users_database.update({self.username: self.password})
        else:
            print("Username Already exists, try another one")

    def login(self):
        if self.username in users_database.keys() and self.password in users_database.values():
            return True  # Goes to user window
        elif self.username in users_database.keys() and self.password not in users_database.values():
            print("Wrong password try again!")   # gui.info_label.config(text="Wrong password try again!")
        else:
            print("No such credentials, register.")  # gui.info_label.config(text="No such credentials, please register"

    def get_by_username(self):
        """Some thing admins might need."""
        pass

    def get_by_id(self):
        """Some thing admins might need, also I need to add id attribute to the class."""
        pass

    def login_valid(self):
        """Check if you are already logged it"""
        pass

    def check_subscription(self):
        """Check is there is a subscription for the user """
        pass

    def make_subscription(self):
        """This is the payment method if it is even done like this .. if not I am dumb shoot me"""
        pass


Milosh = User("Milosh", "Ira")
Sanda = User("Sandra", "Krofna")

Sanda.register()
print(Milosh.username)

Milosh.register()
print(users_database)

Milosh.login()
