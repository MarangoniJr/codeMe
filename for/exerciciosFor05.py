for numero in range(3, 31):
    e_Primo = True

    for num_teste in range(2, numero):
        if (numero % num_teste == 0):
            e_Primo = False
            break

    if(e_Primo):
        print('O número %i é primo!' %(numero))
    else:
        print('O número %i não é primo!' %(numero))