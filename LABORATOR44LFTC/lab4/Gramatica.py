from collections import defaultdict

from lab3.AutomatFinit import AutomatFinit


class gramatica:

    def create_GR(self, filename, param_lst):
        if not param_lst and filename is not None:
            self.__terminale = []
            self.__neterminale = []
            self.__reguli = []
            self.__start = None

            with open(filename) as reader:
                neterminals = reader.readline().strip().split(',')

                for neterminal in neterminals:
                    self.__neterminale.append(neterminal)

                terminals = reader.readline().strip().split(',')
                for terminal in terminals:
                    self.__terminale.append(terminal)

                starting = reader.readline().strip()
                self.__start = starting

                no_rules = int(reader.readline().strip())
                for i in range(no_rules):
                    rule = reader.readline().strip()
                    rule_tokens = rule.strip().split('->')
                    self.__reguli.append([rule_tokens[0], rule_tokens[1]])

        elif filename is None and param_lst:
            self.__terminale = param_lst[0]
            self.__neterminale = param_lst[1]
            self.__reguli = param_lst[2]
            self.__start = param_lst[3]
            #print(self.__terminale)
            #print(self.__neterminale)
            #print(self.__reguli)
            #print(self.__start)



    def reguli_pentru_terminal(self, terminal):
        returning_rules = []
        for rule in self.__reguli:
            if terminal in rule[0]:
                returning_rules.append(rule)
        return returning_rules

    def get_neterminale(self):
        return self.__neterminale

    def get_terminale(self):
        return self.__terminale

    def get_reguli(self):
        return self.__reguli

    def get_start(self):
        return self.__start


    def regularitate(self):
        contineeps = False
        ok = True

        for rule in self.__reguli:
            if self.__start in rule[0]:
                if "e" in rule[1]:
                    contineeps = True

        for rule in self.__reguli:
            nrterminale = 0
            nrneterminale = 0
            for i in rule[1]:
                if contineeps == True:
                     if self.__start not in rule[0] and self.__start in rule[1]:
                          ok = False
                if i in self.__terminale:
                    nrterminale += 1
                elif i in self.__neterminale:
                    nrneterminale += 1
                else:
                    if self.__start in rule[0]:
                        if "e" == i:
                            continue
                        else:
                            ok = False
                    else:
                        ok = False
            if (nrterminale == 1 and (nrneterminale == 1 or nrneterminale == 0)) or (nrneterminale == 0 and nrneterminale == 0):
                continue
            else:
                ok = False

        if ok == False:
             print("Gramatica nu este regulara")
             return False
        else:
             print("Gramatica este regulara")
             return True



    def afiseaza(self):
        print("Neterminalele______")
        print(self.__neterminale)
        print("Terminalele______")
        print(self.__terminale)
        print("Simbol de start______")
        print(self.__start)
        print("Productii______")
        for r in self.__reguli:
            print(r[0]+"->"+r[1])



