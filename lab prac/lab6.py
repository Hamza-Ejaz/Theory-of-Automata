no_of_states = int(input("How many number of states: "))

TT = []
for i in range(no_of_states):
    TT.append([])

for i in range(len(TT)):
    no_of_transitions = int(input(f'How many number Of Transistion at S{i}: '))
    for j in range(no_of_transitions):
        print(f'State S{i}: Transistion {j+1}: ')
        transistion = input('Transistion weight: ')
        state = int(input('State number: '))
        TT[i].append([transistion,state])
        
for i in TT:
    print(i) 