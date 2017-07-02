import math

PRICES = {
    'premium'        : 200,
    'premium_monthly': 100,
    'rename'         : 50
}

class Customer():
    """A class representing a customer account in an online game"""

    def __init__(self, name, funbux=0, is_premium=False):
        """Initializes a Customer"""
        self.name = name
        self.funbux = funbux
        self.premium = is_premium
        self.purchase_history = []

    def buy_funbux(self, real_money):
        """Converts real money paid into funbux"""
        funbux_amount = math.ceil(real_money * 10)
        self.funbux = self.funbux + funbux_amount
        return "You spent " + str(real_money) + " monies to get " + str(funbux_amount) + " funbux!"

    def rename(self, new_name):
        """If the customer has enough funbux to rename, they can"""
        if self.funbux <= PRICES['rename']:
            return "You do not have enough funbux to purchase this."
        else:
            self.funbux = self.funbux - PRICES['rename']
            self.name = new_name
            history_entry = {'service': 'rename', 'cost': PRICES['rename']}
            self.purchase_history.append(history_entry)
            return "You have successfully changed your name to: " + new_name

    def get_premium(self):
        """The customer is signed up for premium. They pay in funbux now and once every months"""
        if self.premium == False and self.funbux >= PRICES['premium']:
            self.premium = True
            self.funbux = self.funbux - PRICES['premium']
            history_entry = {'service': 'premium', 'cost': PRICES['premium']}
            return "Account is now premium."
        elif self.premium == True:
            return "You already have a premium account."
        else:
            return "You do not have enough funbux to purchase premium."

    def end_of_month(self):
        """Pays for premium if the customer has it active"""
        if self.premium and self.funbux >= PRICES['premium_monthly']:
            self.funbux = self.funbux - PRICES['premium_monthly']
            return "Paid for another month of premium."
        elif self.premium and self.funbux < PRICES['premium_monthly']:
            self.premium = False
            return "Premium has been disabled as you cannot pay for this month of service."
