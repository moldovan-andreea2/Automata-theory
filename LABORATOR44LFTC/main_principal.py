from collections import defaultdict

from lab3.AutomatFinit import AutomatFinit
from lab4.Gramatica import gramatica


def GR_to_AF(grmatica):
    d = defaultdict(list)
    for rule in grmatica.get_reguli():
        d[rule[0]].append(rule[1])

    rules = []

    neterminale = grmatica.get_neterminale()
    terminale = grmatica.get_terminale()
    start = grmatica.get_start()
    finals = neterminale.copy()
    finals.remove(str(start))

    for T in grmatica.get_terminale():
        for NT1 in grmatica.get_neterminale():
            for NT2 in grmatica.get_neterminale():
                if str(T) + str(NT2) in d[NT1]:
                    rules.append([NT1, str(T), NT2])
                    # print(NT1+","+T+","+NT2)
            if str(T) in d[NT1]:
                rules.append([NT1, str(T), "K"])
                if "K" not in neterminale:
                    neterminale.append("K")
                    # print(NT1+","+T+",K")
    FA = AutomatFinit(None, [neterminale, terminale, rules, start, finals])

    return FA

def AF_to_GR(automat):
    l = []
    for el in automat.AutomatFinit[4]:
        l.append([el[0], str(el[1]) + str(el[2])])

    terminale = automat.AutomatFinit_E
    neterminale = automat.AutomatFinit_Q
    start = automat.AutomatFinit_q0

    gr = gramatica()
    gr.create_GR(None, [terminale, neterminale, l, start])

    return gr


def print_maniu_automat(automat_finit):
    while True:
        try:
            option = input("\n\n1) Multimea starilor "
                           "\n2) Alfabetul "
                           "\n3) Starea Start"
                           "\n4) Starea finala"
                           "\n5) FUNCTIA DE TRANZITIE "
                           "\n6) VERIFICATI ACCEPTAREA UNEI SECVENTE"
                           "\n7) Pentru o stare si un simbol starea sau starile urmatoare (ca lista)"
                           "\n8) AF -> GR "
                           "\nx EXIT\n\n")
            if option == '1':
                print(automat_finit.get_AutomatFinit_Q())
            elif option == '2':
                print(automat_finit.get_AutomatFinit_E())
            elif option == '3':
                print(automat_finit.get_AutomatFinit_q0())
            elif option == '4':
                print(automat_finit.get_AutomatFinit_F())
            elif option == '5':
                print(automat_finit.get_AutomatFinit_d())
            elif option == '6':
                seq = input("Sequence: ")
                if automat_finit.check_sequence(seq):
                    print("MERGE!")
                else:
                    print("NU A MERS!")
            elif option == '7':
                print(automat_finit.next_state_from_state_symbol())
            elif option == '8':
                gr=AF_to_GR(automat_finit)
                gr.afiseaza()
            elif option == 'x':
                return
            else:
                print("GRESIT!")
        except Exception as e:
            print(e)
def print_meniu_gramatica(gramatica):
    inner_menu = "\nAlege de afisat\n"
    inner_menu += "1) Afisare neterminale\n"
    inner_menu += "2) Afisare terminale\n"
    inner_menu += "3) Simbolul de start\n"
    inner_menu += "4) Afisarea productiilor\n"
    inner_menu += "5) Afisarea productiilor pentru un neterminal dat\n"
    inner_menu += "6) regularitate gramatica\n"
    inner_menu += "7) GR->AF\n"
    inner_menu += "Apasati tasta 0 pentru exit"
    while True:
        print(inner_menu)
        task = int(input())
        if task == 1:
            print(gramatica.get_neterminale())
        elif task == 2:
            print(gramatica.get_terminale())
        elif task == 4:
            for rule in gramatica.get_reguli():
                print(rule[0] + " -> " + rule[1])
        elif task == 3:
            print(gramatica.get_start())
        elif task == 5:
            terminal = input("DATI: ")
            rules = gramatica.reguli_pentru_terminal(terminal)
            for rule in rules:
                print(rule[0] + " -> " + rule[1])
        elif task == 6:
            gramatica.regularitate()
        elif task == 7:
            pass
            af=GR_to_AF(gramatica)
            af.afiseaza()
        else:
            return

def main():
    gram = gramatica()
    gram.create_GR("G.txt", [])

    automat_finit = AutomatFinit("AF.txt", [])

    option = int(input("1 pentru automat si 2 pentru gramatica :)"))

    while True:
        if option == 1 :
            print_maniu_automat(automat_finit)
        elif option == 2:
            print_meniu_gramatica(gram)

main()
