import re
class FA:
    def __init__(self,nStates,domain,initial_state,final_state,TT):
        self.initial_state = initial_state
        self.final_state = final_state
        self.nStates = nStates
        self.domain = domain
        self.TT = TT

    def transition(self,state,ch):
        for i in range( len(self.domain) ):
            pattern = re.compile(self.domain[i])  
            if pattern.search(ch): 
                return self.TT[state][i]
        return -1
            
    def validate(self,word):
        current = self.initial_state
        for i in range( len(word) ):
            current = self.transition(current,word[i])
            if current == -1: 
                return False
        for i in range( len(self.final_state )):
            if current == self.final_state[i]:
                return True
        return False

def DFA_Complement(DFA):
    final = []
    for i in range(len(DFA.TT)):
        if i not in DFA.final_state:
            final.append(i)
    return FA(DFA.nStates, DFA.domain, DFA.initial_state, final, DFA.TT)


def DFA_OR(DFA1,DFA2):
    def transition( DFA, current, char):
        return DFA.TT[current][DFA.domain.index(char)]
    
    if DFA1.domain != DFA2.domain:
        print("Wrong DFA")
        return None

    Equations = [ [DFA1.initial_state, DFA2.initial_state] ]
    final_states = []
    if (DFA1.initial_state in DFA1.final_state) or (DFA2.initial_state in DFA2.final_state):
        final_states.append(0)
    
    i = 0
    new_TT = []
    while i < len(Equations):
        connection = []
        current = Equations[i]
        for char in (DFA1.domain):
            index = 0
            exist = False
            
            state_1 = transition( DFA1, current[0], char)
            state_2 = transition( DFA2, current[1], char)
            equation = [state_1, state_2]

            for j in range(len(Equations)):
                if equation == Equations[j]:
                    index = j
                    exist = True
                    break

            if not exist:
                Equations.append(equation)
                index = len(Equations) - 1
                if (state_1 in DFA1.final_state) or (state_2 in DFA2.final_state):
                    final_states.append(index)

            connection.append(index)
        
        new_TT.append(connection)
            
        i += 1

    no_of_states = len(Equations)
    domain = DFA1.domain
    initial_state = DFA1.initial_state
    return FA(no_of_states, domain, initial_state, final_states, new_TT)



def DFA_Intersection(DFA1, DFA2):
    X = DFA_Complement(DFA1)
    Y = DFA_Complement(DFA2)
    Result = DFA_OR(X,Y)
    return DFA_Complement(Result)


def DFA_Concatenate(DFA1,DFA2):
    def transition( DFA, current, char):
        return DFA.TT[current][DFA.domain.index(char)]

    class eq:
        def __init__(self, x=None, y=[]) -> None:
            self.x = x
            self.y = set(y)
    
    if DFA1.domain != DFA2.domain:
        print("Wrong DFA")
        return None

    state_2 = []
    if DFA1.initial_state in DFA1.final_state:
        state_2.append(DFA2.initial_state)
    Equations = [ eq( DFA1.initial_state, state_2 ) ]
    
    
    i = 0
    new_TT = []
    final_states = []
    while i < len(Equations):
        connection = []
        current = Equations[i]
        for char in (DFA1.domain):
            index = 0
            exist = False
            equation = eq()
            equation.x = transition( DFA1, current.x, char)
            if equation.x in DFA1.final_state:
                equation.y.add(DFA2.initial_state)
            
            for y_states in current.y:
                equation.y.add(transition( DFA2, y_states, char))
            
            for j in range(len(Equations)):
                if equation.x == Equations[j].x and equation.y == Equations[j].y:
                    index = j
                    exist = True
                    break

            if not exist:
                Equations.append(equation)
                index = len(Equations) - 1
                for state in equation.y:
                    if state in DFA2.final_state:
                        final_states.append(index)
                        break

            connection.append(index)
        
        new_TT.append(connection)
            
        i += 1

    no_of_states = len(Equations)
    domain = DFA1.domain
    initial_state = DFA1.initial_state
    return FA(no_of_states, domain, initial_state, final_states, new_TT)



def DFA_Closure(DFA):

    def transition( DFA, current, char):
        return DFA.TT[current][DFA.domain.index(char)]

    Equations = [ set([DFA.initial_state, 'f']) ]
    final_states = []
    if (DFA.initial_state in DFA.final_state):
        final_states.append(0)
    
    i = 0
    new_TT = []
    while i < len(Equations):
        connection = []
        current = Equations[i]
        for char in (DFA.domain):
            index = 0
            exist = False
            equation = set([])
            for x_states in current:
                if x_states != 'f':
                    s = transition( DFA, x_states, char)
                    if s in DFA.final_state:
                        equation.add(DFA.initial_state)
                    equation.add(s)

            for j in range(len(Equations)):
                if equation == Equations[j]:
                    index = j
                    exist = True
                    break

            if not exist:
                Equations.append(equation)
                index = len(Equations) - 1
                for state in equation:
                    if state in DFA.final_state:
                        final_states.append(index)
                        break
                    
            connection.append(index)

        new_TT.append(connection)
        
        i += 1
        
    no_of_states = len(Equations)
    domain = DFA.domain
    initial_state = DFA.initial_state
    return FA(no_of_states, domain, initial_state, final_states, new_TT)