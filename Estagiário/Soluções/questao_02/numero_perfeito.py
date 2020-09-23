def Perfeito(number):
    try:
        summation = int()

        #aramazenando o somatório dos divisores do valor de entrada (number)
        for i in range(1,number):
            if number % i == 0:
                summation += i
        
        #se o somatório for igual ao número, saída afirmativa (é perfeito)
        if summation == number:
            print("O número {%d} é perfeito"%(number))

        #se o somatório não for igual ao número, saída negativa (não é perfeito)
        else:
            print("O número {%d} não é perfeito"%(number))
    except:
        print("An error occurred")