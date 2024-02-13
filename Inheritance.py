class Mpesa:
    def __init__(self, account_balance, phone_number):
        self.account_balance = account_balance
        self.phone_number = phone_number
    def send_money(self,amount,recipient):
        if self.account_balance >= amount:
            self.account_balance -= amount
            print({f"{amount} KES Sent to {recipient} successful"})
        else:
            print("Insufficient balance")

class Personal_Mpesa(Mpesa):
    def __init__(self, account_balance, phone_number, id_number):
        super().__init__(account_balance, phone_number)
        self.id_number = id_number
    def buyairtime(self,amount):
        if self.account_balance >= amount:
            self.account_balance -= amount
            print(f"{amount} KES airtime bought successfully")
        else:
            print("Insufficient Balance")

class Business_Mpesa(Mpesa):
    def __init__(self, account_balance, phone_number, business_name):
        super().__init__(account_balance, phone_number)
        self.business_name = business_name
    def receive_money(self,amount):
        self.account_balance += amount
        print(f"{amount} KES received successfully")

personal = Personal_Mpesa(500,7346464600,22888450)
personal.send_money(400,7384982170)
personal.buyairtime(25)

business = Business_Mpesa(25000, 1234567891, 911)
business.receive_money(15700)






