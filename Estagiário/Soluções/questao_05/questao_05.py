def Digitos(a, b):
    try:
        #criando uma lista em que os índices representam os dígitos e os
        #valores as quantidades em que eles se repetem
        digits = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        #realizando uma iteração do valor da entrada 'a' ao valor da entrada 'b'
        for i in range(a, b+1):

            #convertendo o valor atual em str para percorrer cada casa decimal na próxima iteração
            actual = str(i)
            for j in range(len(actual)):
                
                #para cada caso (de 0 à 9), é acrescido +1 ao valor da posição 
                #referente ao dígito
                if actual[j] == '0':
                    digits[0] += 1

                elif actual[j] == '1':
                    digits[1] += 1

                elif actual[j] == '2':
                    digits[2] += 1

                elif actual[j] == '3':
                    digits[3] += 1

                elif actual[j] == '4':
                    digits[4] += 1

                elif actual[j] == '5':
                    digits[5] += 1

                elif actual[j] == '6':
                    digits[6] += 1

                elif actual[j] == '7':
                    digits[7] += 1

                elif actual[j] == '8':
                    digits[8] += 1

                elif actual[j] == '9':
                    digits[9] += 1

        #transformando a lista criada em uma string separada por ' ' e retornando o resultado
        return " ".join([str(i) for i in digits])
    except:
        return "An error ocurred"