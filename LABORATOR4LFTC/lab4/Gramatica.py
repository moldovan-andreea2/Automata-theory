from collections import defaultdict


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

    def GR_to_AF(self):
        d = defaultdict(list)
        for rule in self.__reguli:
            d[rule[0]].append(rule[1])

        rules = []

        neterminale = self.__neterminale
        terminale = self.__terminale
        start = self.__start
        finals = neterminale.copy()
        finals.remove(str(start))



        for T in self.__terminale:
            for NT1 in self.__neterminale:
                for NT2 in self.__neterminale:
                    if str(T) + str(NT2) in d[NT1]:
                        rules.append([NT1, str(T), NT2])
                        #print(NT1+","+T+","+NT2)
                if str(T) in d[NT1]:
                    rules.append([NT1, str(T), "K"])
                    neterminale.append("K")
                    #print(NT1+","+T+",K")

        # FA = FiniteAutomate(None, [neterminale, terminale, rules, start, finals])
        #
        # return FA


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


    def print_gramatica(self):
        inner_menu = "\nAlege de afisat\n"
        inner_menu += "Apasati tasta 1 pentru afisarea nonterminalelor\n"
        inner_menu += "Apasati tasta 2 pentru afisarea terminalelor\n"
        inner_menu += "Apasati tasta 3 pentru afisarea simbolului de start\n"
        inner_menu += "Apasati tasta 4 pentru afisarea productiilor\n"
        inner_menu += "Apasati tasta 5 pentru afisarea productiilor pentru un neterminal dat\n"
        inner_menu += "Apasati tasta 6 pentru a verifica regularitatea gramaticii\n"
        inner_menu += "7) Convert to AF\n"
        inner_menu += "Apasati tasta 0 pentru exit"
        while True:
            print(inner_menu)
            task = int(input())
            if task == 1:
                print(self.__neterminale)
            elif task == 2:
                print(self.__terminale)
            elif task == 4:
                for rule in self.__reguli:
                    print(rule[0] + " -> " + rule[1])
            elif task == 3:
                print(self.__start)
            elif task == 5:
                terminal = input("TERMINAL: ")
                rules = self.reguli_pentru_terminal(terminal)
                for rule in rules:
                    print(rule[0] + " -> " + rule[1])
            elif task == 6:
                self.regularitate()
            elif task == 7:
                pass
                # fa = self.GR_to_AF()
                # fa.afiseaza()
            else:
                return
