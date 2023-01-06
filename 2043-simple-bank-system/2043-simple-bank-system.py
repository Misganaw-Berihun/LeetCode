class Bank:

    def __init__(self, balance: List[int]):
        self.num_accounts = len(balance)
        self.balance = balance.copy()

    def isValidAccount(self, account_num):
        valid = True
        
        if account_num < 1 or account_num > self.num_accounts:
            valid = False
        
        return valid
    
    def hasEnoughMoney(self, account, money):
        enough = True
        
        if self.balance[account - 1] < money:
            enough = False
            
        return enough
    
    def transfer(self, account1: int, account2: int, money: int) -> bool:
        valid = True
        
        if not self.isValidAccount(account1):
            valid = False
            
        elif not self.isValidAccount(account2):
            valid = False
            
        elif not self.hasEnoughMoney(account1, money):
            valid = False
        
        else:
            self.balance[account1 - 1] -= money
            self.balance[account2 - 1] += money
            
        return valid

    def deposit(self, account: int, money: int) -> bool:
        successful = True
        
        if not self.isValidAccount(account):
            successful = False
            
        else:
            self.balance[account - 1] += money
        
        return successful
        

    def withdraw(self, account: int, money: int) -> bool:
        successful = True
        
        if not self.isValidAccount(account):
            successful = False
            
        elif not self.hasEnoughMoney(account, money):
            successful = False
            
        else:
            self.balance[account - 1] -= money
            
        return successful


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)