
class DNS():
    def __init__(self):
        self.__map = {}
        self.__blacklist = {}
    def add_DNS(self, name, IPA):
        if name in self.__map:  
            print ("The name already have IPA")
        else: self.__map[name] = IPA
    def add_blacklist(self,IPA):
        lst = {i for i in self.__map if self.__map[i]==IPA}
        for i in lst:
            self.__blacklist[i] = IPA
    def return_IPA(self, name):
        if name in self.__blacklist: return None
        try: return self.__map[name]
        except: return "None"
    def run_code(self):
        while True:
            line = str(input())
            if line == 'q': return
            key, name, IPA,value = None, None, None, None
            try: key, name, IPA = line.split(' ')
            except: key, value = line.split(' ')
            if key =='u':
                if IPA == None: print("Bad command")
                else: self.add_DNS(name,IPA)
            elif key =='b':
                IPA = value
                self.add_blacklist(IPA)
            elif key == 'l':
                name = value
                print(self.return_IPA(name))
    
DNS = DNS()
DNS.run_code()