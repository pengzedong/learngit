class UserAccount:
    users = []

    def __init__(self, name, password, user_id, email):
        self.name = name
        self.password = password
        self.user_id = user_id
        self.email = email
        self.check_id_unique()

    def check_id_unique(self):
        for user in UserAccount.users:
            if user.user_id == self.user_id:
                raise ValueError("User ID must be unique.")
        UserAccount.users.append(self)
