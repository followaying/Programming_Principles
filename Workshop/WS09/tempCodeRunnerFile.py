class Children:
    def __init__(self):
        self.dict = {}
    def input(self, var):
        val = int(input("Enter a value for {}: ".format(var)))
        self.dict[var] = val
    def print_var(self,var):
        if var not in self.dict: 
            print("{} is undefined.".format(var))
        else: 
            print ( "{} equals {}".format(var,self.dict[var]))
    def get(self, var, val):
        try: 
            dec = int(val)
            self.dict[var] = dec
        except: 
            if not val.isalpha(): print("Syntax error.")
            else: self.dict[var] =  self.dict[val]
    def add(self, var, val):
        try: 
            dec = int(val)
            self.dict[var] += dec
        except: 
            if not val.isalpha(): print("Syntax error.")
            else: self.dict[var] +=  self.dict[val]
    
    def run_code(self):
        file = open('children.txt', 'r')
        print ("Script name: children.txt")
        while True:
            line = file.readline()
            if line == "quit" : 
                break
            elif "print" in line:
                try: 
                    dec = int(line[6:-1])
                    print(dec)
                except: 
                    var = line[6:-1]
                    if not var.isalpha(): print("Syntax error.")
                    else: self.print_var(var)
                    
            elif "input" in line:
                var = line[6:-1]
                if not var.isalpha(): print("Syntax error.")
                else: self.input(var)
                
            elif "gets" in line:
                var = line[:line.index("gets")-1]
                val =line[line.index("gets")+5:-1]
                if not (var.isalpha()): print("Syntax error.")
                else: self.get(var, val)
                
            elif "adds" in line:
                var = line[:line.index("adds")-1]
                val =line[line.index("adds")+5:-1]
                if not (var.isalpha()): print("Syntax error.")
                else: self.add(var, val)
            else: print("Syntax error.")
        file.close()
   
Children = Children()
Children.run_code() 