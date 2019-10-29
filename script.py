''' Libraries imported '''
import json
''' Powerset Functions '''
def power_set(nfa):
    powerset=[[]]
    for i in nfa:
        for sub in powerset:
            powerset=powerset+[list(sub)+[i]]
    return powerset

''' Reading file '''
with open('input.json', 'r') as inpjson:
    nfa = json.loads(inpjson.read())

''' Setting up DFA '''
dfa={}
numstates=1
for i in range(nfa["states"]):
    numstates=numstates*2
dfa['states']=numstates
dfa['letters']=nfa['letters']
dfa['t_func']=[]
set1=[]
states = nfa['states']
for i in range(nfa['states']):
    set1.append(i)

''' Making powerset '''
set2=power_set(set1)

''' Converting NFA relation to DFA function'''
for inp in nfa['letters']:
    for states in set2:
        temp=[]
        for state in states:
            for func in nfa['t_func']:
                if state==func[0] and inp==func[1]:
                    for i in func[2]:
                        temp.append(i)
        dfa['t_func'].append([states,inp,temp])

''' setting DFA start and final states '''
dfa['start']=nfa['start']
dfa['final']=[]
for states in set2:
    for state in states:
        if state in nfa['final'] and states not in dfa['final']:
            dfa['final'].append(states)

''' Writing to output.json'''
with open('output.json', 'w') as outjson:
    outjson.write(json.dumps(dfa,indent=4))
