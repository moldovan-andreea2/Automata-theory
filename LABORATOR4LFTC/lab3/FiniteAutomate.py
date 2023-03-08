from collections import defaultdict
#import Gramatica


class FiniteAutomate:
    def __init__(self, filename, param_lst):
        if not param_lst and filename is not None:
            self.filename = filename
            self.FiniteAutomate = self.read_FiniteAutomate()
            self.FiniteAutomate_Q = self.FiniteAutomate[0]  # all states = neterminale = ABC
            self.FiniteAutomate_E = self.FiniteAutomate[1]  # alphabet = terminale = abc
            self.FiniteAutomate_d = self.transitions(self.FiniteAutomate[4])    # tranzitii = reguli
            self.FiniteAutomate_q0 = self.FiniteAutomate[2]     # starting state = starting nonterminal
            self.FiniteAutomate_F = self.FiniteAutomate[3]  # final state = final nonterminal
        elif filename is None and param_lst:
            self.FiniteAutomate_Q = param_lst[0]
            self.FiniteAutomate_E = param_lst[1]
            self.FiniteAutomate_d = param_lst[2]
            self.FiniteAutomate_q0 = param_lst[3]
            self.FiniteAutomate_F = param_lst[4]

    def get_FiniteAutomate_Q(self):
        return self.FiniteAutomate_Q

    def get_FiniteAutomate_E(self):
        return self.FiniteAutomate_E

    def get_FiniteAutomate_d(self):
        return self.FiniteAutomate_d

    def get_FiniteAutomate_q0(self):
        return self.FiniteAutomate_q0

    def get_FiniteAutomate_F(self):
        return self.FiniteAutomate_F

    def get_filename(self):
        return self.filename

    def read_FiniteAutomate(self):
        fin_Auto = []
        with open(self.filename) as f:
            line = f.readline()
            fin_Auto.append(line[0:-1].split(" "))
            line = f.readline()
            fin_Auto.append(line[0:-1].split(" "))
            line = f.readline()
            fin_Auto.append(line[0:-1].split(" "))
            line = f.readline()
            fin_Auto.append(line[0:-1].split(" "))
            d = []
            line = f.readline()
            while line:
                transition = line[0:-1]

                d.append(transition.split(","))
                line = f.readline()
            fin_Auto.append(d)

        return fin_Auto

    def transitions(self, transitions):
        rep = {}
        for t in transitions:
            s = (t[0], t[1])
            if s not in rep.keys():
                rep[s] = []
            rep[s].append(t[2])
        return rep

    def check_sequence(self, sequence):

        current_state = self.get_FiniteAutomate_q0()[0]
        for i in sequence:
            if (current_state, i) not in self.FiniteAutomate_d.keys():
                return False
            current_state = self.FiniteAutomate_d[(current_state, i)][0]
        if current_state not in self.FiniteAutomate_F:
            return False
        return True

    def next_state_from_state_symbol(self):
        f = open(self.filename)
        lines = f.readlines()

        nextstates = []

        while True:
            state = str(input("\nGiv dă state: "))
            if state not in self.get_FiniteAutomate_Q():
                print("\nInvalid state\n")
            else:
                break

        while True:
            symb = str(input("\nGiv dă symbol: "))
            if symb not in self.get_FiniteAutomate_E():
                print("\nInvalid symbol\n")
            else:
                break

        for line in lines:
            parsed = line.split(',')
            if parsed[0] == state and parsed[1] == symb:
                nextstates.append(parsed[2][:-1])

        return nextstates

    def AF_to_GR(self):
        l = []
        for el in self.FiniteAutomate[4]:
            l.append([el[0], str(el[1])+str(el[2])])

        terminale = self.FiniteAutomate_E
        neterminale = self.FiniteAutomate_Q
        start = self.FiniteAutomate_q0

        # gr = gramatica()
        # gr.create_GR(None, [terminale, neterminale, l, start])
        #
        # return gr


    def afiseaza(self):
        for r in self.get_FiniteAutomate_d():
            print(r[0]+','+r[1]+','+r[2])
