
users_database = {"Milosh": "Ira", "asd": "asd"}  # Dictionary that replaces a database, I am to lazy and dumb to make a DB"


class User(object):
    """Defines what the user and and what it can do"""
    def __init__(self, username, password):  # This class needs to have an id too.
        self.username = username
        self.password = password

    def register(self):
        """Registers a user"""
        if self.username not in users_database:
            users_database.update({self.username: self.password})
            return "User registered please log in"
        else:
            return "Username Already exists,\n try another one."

    def login(self):
        """Logs in the user """
        if self.username in users_database and self.password in users_database[self.username] == self.password:
            return True
        elif self.username in users_database and self.password != users_database[self.username]:
            return "Wrong password try again!"   # gui.info_label.config(text="Wrong password try again!")
        else:
            return "No such credentials, register."  # gui.info_label.config(text="No such credentials, please register"

    def get_by_username(self):
        """Some thing admins might need."""
        pass

    def get_by_id(self):
        """Some thing admins might need, also I need to add id attribute to the class."""
        pass

    def logged(self):
        """Check if you are already logged it"""
        pass

    def check_subscription(self):
        """Check is there is a subscription for the user """
        pass

    def make_subscription(self):
        """This is the payment method if it is even done like this .. if not I am dumb shoot me"""
        pass

