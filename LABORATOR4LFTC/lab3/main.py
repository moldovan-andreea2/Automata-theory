from lab3.FiniteAutomate import FiniteAutomate


fin_Auto = FiniteAutomate("Ident.in", [])
while True:
    try:
        option = input("\n\n1 All states "
                       "\n2 Alphabet "
                       "\n3 Starting state "
                       "\n4 Final states "
                       "\n5 Transitions "
                       "\n6 Check seq "
                       "\n7 Next state through state and symbol "
                       "\n8 Convert to GR "
                       "\nx Outta\n\n")
        if option == '1':
            print(fin_Auto.get_FiniteAutomate_Q())
        elif option == '2':
            print(fin_Auto.get_FiniteAutomate_E())
        elif option == '3':
            print(fin_Auto.get_FiniteAutomate_q0())
        elif option == '4':
            print(fin_Auto.get_FiniteAutomate_F())
        elif option == '5':
            print(fin_Auto.get_FiniteAutomate_d())
        elif option == '6':
            seq = input("Sequence: ")
            if fin_Auto.check_sequence(seq):
                print("HEHE!")
            else:
                print("NOT HEHE!")
        elif option == '7':
            print(fin_Auto.next_state_from_state_symbol())
        elif option == '8':
            gramatica = fin_Auto.AF_to_GR()
            gramatica.afiseaza()
        elif option == 'x':
            break
        else:
            print("WRONG!")
    except Exception as e:
        print(e)
