from collections import defaultdict

class AutomatFinit:
    def __init__(self, filename, param_lst):
        if not param_lst and filename is not None:
            self.filename = filename
            self.AutomatFinit = self.read_AutomatFinit()
            self.AutomatFinit_Q = self.AutomatFinit[0]
            self.AutomatFinit_E = self.AutomatFinit[1]
            self.AutomatFinit_d = self.transitions(self.AutomatFinit[4])
            self.AutomatFinit_q0 = self.AutomatFinit[2]
            self.AutomatFinit_F = self.AutomatFinit[3]
        elif filename is None and param_lst:
            self.AutomatFinit_Q = param_lst[0]
            self.AutomatFinit_E = param_lst[1]
            self.AutomatFinit_d = param_lst[2]
            self.AutomatFinit_q0 = param_lst[3]
            self.AutomatFinit_F = param_lst[4]

    def get_AutomatFinit_Q(self):
        return self.AutomatFinit_Q

    def get_AutomatFinit_E(self):
        return self.AutomatFinit_E

    def get_AutomatFinit_d(self):
        return self.AutomatFinit_d

    def get_AutomatFinit_q0(self):
        return self.AutomatFinit_q0

    def get_AutomatFinit_F(self):
        return self.AutomatFinit_F

    def get_filename(self):
        return self.filename

    def read_AutomatFinit(self):
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

        current_state = self.get_AutomatFinit_q0()[0]
        for i in sequence:
            if (current_state, i) not in self.AutomatFinit_d.keys():
                return False
            current_state = self.AutomatFinit_d[(current_state, i)][0]
        if current_state not in self.AutomatFinit_F:
            return False
        return True

    def next_state_from_state_symbol(self):
        f = open(self.filename)
        lines = f.readlines()

        nextstates = []

        while True:
            state = str(input("\nGiv dă state: "))
            if state not in self.get_AutomatFinit_Q():
                print("\nInvalid state\n")
            else:
                break

        while True:
            symb = str(input("\nGiv dă symbol: "))
            if symb not in self.get_AutomatFinit_E():
                print("\nInvalid symbol\n")
            else:
                break

        for line in lines:
            parsed = line.split(',')
            if parsed[0] == state and parsed[1] == symb:
                nextstates.append(parsed[2][:-1])

        return nextstates




    def afiseaza(self):
        print("Q___________________")
        print(self.get_AutomatFinit_Q())
        print("E___________________")
        print(self.get_AutomatFinit_E())
        print("q0___________________")
        print(self.get_AutomatFinit_q0())
        print("F___________________")
        print(self.get_AutomatFinit_F())

        print("d-----------------")
        for r in self.get_AutomatFinit_d():
            print(r[0]+','+r[1]+','+r[2])
