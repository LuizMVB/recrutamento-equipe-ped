def Perfeito(number):
    try:
        #criando objetos int e list para utiliza-los posteriormente
        summation = int()
        dividers = list()

        #cada número, até a entrada (exclusive), que sejam disores
        #do valor de entrada (number), será armazenado em na lista
        #dividers
        for i in range(1,number):
            if number % i == 0:
                summation += i
                dividers.append(i)

        #caso o somatório dos divisores seja igual à entrada, a resposta é positiva (é perfeito)
        if summation == number:
            print("O número {%d} é perfeito. Seu(s) divisor(es)"%(number), end=" {")

            #percorrendo a lista 'dividers' crianda anteriormente para realizar a 
            #saída na tela dos divisores do número definido como perfeito que 
            #também são perfeitos
            for i in range(len(dividers)):
                if i != len(dividers)-1:
                    print(dividers[i], end=", ")
                else:
                    print(dividers[i], end="} ")
            print("também são perfeitos")
    except:
        print("An error ocurred")

    #se o somatório não for igual ao número, saída negativa (não é perfeito)
    else:
        print("O número {%d} não é perfeito"%(number))