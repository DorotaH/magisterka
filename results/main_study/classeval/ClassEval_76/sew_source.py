class SignInSystem:
    def __init__(self):
        self.users = dict()

    def add_user(self, username):
        if not username in self.users:
            self.users[username] = False
            return True
        else:
            return False

    def sign_in(self, username):
        if not username not in self.users:
            self.users[username] = True
            return True
        else:
            return False

    def check_sign_in(self, username):
        if not username not in self.users:
            if self.users[username]:
                return True
            else:
                return False
        else:
            return False

    def all_signed_in(self):
        if not all(self.users.values()):
            return False
        else:
            return True

    def all_not_signed_in(self):
        not_signed_in_users = []
        for username, signed_in in self.users.items():
            if not signed_in:
                not_signed_in_users.append(username)
        return not_signed_in_users