def Palindromo(word):
    try:
        #para que não haja problemas com relação a entrada em letras minúsculas
        #ou maiúsculas, a entrada é convertida em UpperCase
        word = word.upper()
        palind = "" #aqui será armazenado o maior palidromo

        #se a entrada tiver uma posição, palidromo não será um palindromo
        if len(word) == 1:
            return palind
        else:
            
            #se a entrada for um palindromo completo, a mesma será o maior
            #palidromo dentro das possibilidades internas
            if word == word[::-1]:
                palind = word
            else:

                #percorrendo a string word e comparando, caracter por caracter,
                #a posição atual com as anteriores (a cada iteração é verificado
                # se existe um palindromo interno até que toda string seja percorrida)
                for i in range(2, len(word)+1):
                    for j in range(i-1):
                        actual_sub = word[j:i]

                        #se a substring atual (uma parte de word - da posição j à posição i)
                        #for igual ao seu inverso e seu tamanho for maior que o tamanho anterior
                        #que estava armazenado na variável 'palind', será atribuída a palind
                        if actual_sub == actual_sub[::-1] and len(actual_sub) > len(palind):
                            palind = actual_sub
            return palind
    except:
        return 'An error ocurred'