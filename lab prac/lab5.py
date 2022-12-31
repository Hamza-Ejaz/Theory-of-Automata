import re
class FA:
    def __init__(self,no_of_states,domain,intial_state,final_state,TT):
        self.no_of_states = no_of_states
        self.domain = domain
        self.intial_state = intial_state
        self.final_state = final_state
        self.TT = TT

    def transition(self,state,ch):
        for i in range( len(self.domain) ):
            pattern = re.compile(self.domain[i]) #compile each domain per loop
            if pattern.search(ch): #check in which domain character belongs too
                return self.TT[state][i]   
        return -1 #if test character isnot belong to domain(domain)
            
    def validate(self,word):
        current = self.intial_state
        for i in range( len(word) ):
            current = self.transition(current,word[i])
            #if test character not in domain then current false return false output
            if current == -1: 
                return False

        for i in range( len(self.final_state )):
            if current == self.final_state[i]:
                return True
        return False
    
#Identifier = TT [[1,3,2],[1,1,2],[1,1,2],[3,3,3]]
#finalstate=[1] intial = 0
#domain [Aplhabet,Digit,_]
RE = FA(4,['[A-Za-z]','[0-9]','[_]'],0,[1],[[1,3,2],[1,1,2],[1,1,2],[3,3,3]])

for i in range(5):
    test = input("Enter test case: ")
    print(RE.validate(test))
