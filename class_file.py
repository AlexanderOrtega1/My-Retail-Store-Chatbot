
class AccountCreation:
  def __init__(self, email, password):
    self.email = email
    self.password = password

  def create_account(self):
    return {'email': self.email, 'password': self.password}
