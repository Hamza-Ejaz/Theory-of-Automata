class FA:
    def __init__(self,no_of_states,domain,intial_state,final_state,TT):
        self.no_of_states = no_of_states
        self.domain = domain
        self.intial_state = intial_state
        self.final_state = final_state
        self.TT = TT

    def transition(self,state,ch):
        for i in range( len(self.domain) ):
            if ch == self.domain[i]:
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
    
#Even a ,Odd b = TT [[1,3],[0,2],[3,1],[2,0]]   finalstate=[3] intial = 0
#domain ['a','b']
RE = FA(4,['a','b'],0,[3],[[1,3],[0,2],[3,1],[2,0]])

# RE = FA(4,['a','b'],0,[3],[[1,0],[1,2],[1,3],[1,0]])

for i in range(5):
    test = input("Enter test case: ")
    print(RE.validate(test))