class Atm(object):
    def __init__(self,atmCard,PinNumber):
        self.atmCard = atmCard
        self.PinNumber = PinNumber
        
    def CashWithdrawl(self):
        print("atm machine making sound to give money")
    
    def BalanceEnquiry(self):
        print("after crediting money show balane")
    
         


sathvik = Atm("RuPay","2893")
print(sathvik.BalanceEnquiry())