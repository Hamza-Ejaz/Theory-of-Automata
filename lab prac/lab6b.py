import re
class NFA:
    def __init__(self,nStates,domain,intial_state,final_state,TT):
        self.intial_state = intial_state
        self.final_state = final_state
        self.nStates = nStates
        self.domain = domain
        self.TT = TT
        self.check = False

    def validate(self,word):
        current = self.intial_state
        index = 0
        result = self.transition(current,word,index)
        self.check = False
        return  result,word
                
    def transition(self,current,word,index=0):
        if len(word) <= index:
            if current in self.final_state:
                self.check = True
            return
        for connection in self.TT[current]:
            if re.compile(connection[0]).search(word[index]):
                #current = connection[1]
                self.transition(connection[1],word,index+1)
                if self.check == True:
                    return True
        return False    


A = NFA(5,['a','b'],0,[2,4],[   [['a', 0], ['a', 1], ['b', 0], ['b', 3]],
                                [['a', 2]],
                                [['a', 2]],
                                [['b', 4]],
                                [['b', 4]]])

#ends with double letter
print(A.validate("baabb"))
print(A.validate("a"))                                
print(A.validate("aa"))
print(A.validate("aaabbb"))
print(A.validate("bb"))
print(A.validate("babb"))
print(A.validate("aab"))

D = NFA(5,['[A-Za-z]','[0-9]','[_]'],0,[2],  [  [['[A-Za-z]', 1], ['[_]', 1], ['[A-Za-z]', 2]],
                                                [['[A-Za-z]', 1], ['[0-9]', 1], ['[A-Za-z]', 2], ['[0-9]', 2], ['[_]', 1]],
                                                [['[A-Za-z]', 2], ['[0-9]', 2]]])
print(D.validate("13a"))
print(D.validate("a1"))
print(D.validate("a1_"))
print(D.validate("_41"))
print(D.validate("a1_5_s"))
