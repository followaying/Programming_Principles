class GoCard():
    def __init__(self):
        balance = float(input("Creating account. Input initial balance: "))
        self.__balance = balance
        self.__table_data = [ 
                      ['event', 'amount($)', 'balance($)'],
                      ['initial blance',' ', '{:.2f}'.format(round(self.__balance,2))],]
    def return_balance(self):
        return self.__balance 
    def top(self,value):
        self.__balance += value
        self.__table_data.append(['Top up', '{:.2f}'.format(round(value)),'{:.2f}'.format(round(self.__balance,2))])    
    def ride(self, value):
        self.__balance -= value
        self.__table_data.append(['Ride',  '{:.2f}'.format(round(value)),'{:.2f}'.format(round(self.__balance,2))])
       
    def run_code(self):
        while True:
            line = str(input())
            if line == 'q':
                return
            key, value = None, None
            try: 
                key, value = line.split(' ')
                value = float(value)
            except: key = line
            if key == 'b':
                print("Balance =", '{:.2f}'.format(round(self.return_balance(),2)))
            elif key == 'r':
                if value == None: print("Bad command")
                else: self.ride(value)
            elif key == 't':
                if value == None: print("Bad command")
                else: self.top(value)
            else: print("Bad command")
        
        
Gocard = GoCard()
Gocard.run_code()