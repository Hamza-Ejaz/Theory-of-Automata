class FA:
    def __init__(self, nStates, domain, initial_state, final_state, TT):
        self.nStates = nStates
        self.domain = domain
        self.initial_state = initial_state
        self.final_state = final_state
        self.TT = TT

    def transition(self, state, ch):
        for i in range(len(self.domain)):
            if ch == self.domain[i]:
                return self.TT[state][i]
        return -1

A = FA(2, ['a', 'b'], 0, [1], [[1, 0], [1, 0]])
B = FA(3, ['a', 'b'], 0, [1], [[2, 1], [1, 1], [2, 2]])

def DFA_OR(DFA1, DFA2):
    if DFA1.domain != DFA2.domain:
        print("Incorrect DFA")
        return None
    Equation = [[0,0]]
    final_state = []
    if (Equation[0][0] in DFA1.final_state) or (Equation[0][1] in DFA2.final_state):
        final_state.append(0)
    i = 0
    new_TT = []
    while len(Equation) > i:
        current_state = Equation[i]
        connection = []
        for domain in DFA1.domain:
            flag = False
            s1 = DFA1.transition(current_state[0], domain)
            s2 = DFA2.transition(current_state[1], domain)

            for j in range(len(Equation)):
                if [s1, s2] == Equation[j]:
                    flag = True
                    index=j
                    break
            if not flag:
                Equation.append([s1, s2])
                index = len(Equation) - 1
                if (s1 in DFA1.final_state) or (s2 in DFA2.final_state):
                    final_state.append(index)
            connection.append(index)
        new_TT.append(connection);
        i += 1

    noState = len(Equation)
    initial_st = 0
    domain = DFA1.domain
    return FA(noState, domain, initial_st, final_state, new_TT)

# Driver Code
DFA_OR_TT = DFA_OR(A, B)
print("Transition Table: ", DFA_OR_TT.TT)
print("Final States: ", DFA_OR_TT.final_state)

