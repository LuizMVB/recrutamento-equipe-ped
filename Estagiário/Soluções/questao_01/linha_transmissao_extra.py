def ColocarTorres(distance):

    try:
        #caso a distância seja igual a zero (onde pode haver duas torres)
        #o resultado será dois
        if distance > 0:

            #as duas variáveis vão guardar, respectivamente, os valores
            #dos dois ultimos resultados de forma dinâmica (tornando o algoritmo
            # mais eficiente)
            result, aux = 0, 1

            #variável responsável por armazenar o valor anterior de result
            prev_result = 0
            tower_n = 0
            while True:
                result, aux = aux, result+aux

                #as iterações serão realizadas enquanto o resultado do item da
                #sequência de Fibonacci for menor que a distância defiida pelo 
                #usuáio
                if result > distance:

                    #como a última iteração representa o valor posterior ao que 
                    #se deseja obter, se utiliza o resultado anterior para determinar
                    #o numero da sequência de fibonacci correspondente
                    result = prev_result
                    break
                else:
                    prev_result = result
                    
                    #uma torre é adicionada a cada iteração, já que cada iteração significa 
                    #uma posição
                    tower_n += 1

            #agora que se sabe o número de torres, é possível percorrer uma lista para se construir
            #uma string com as posições separadas por ' '
            fibonacci_list = [0, 1]
            for _ in range(2, tower_n):
                fibonacci_list.append(fibonacci_list[-1] + fibonacci_list[-2])
            return tower_n, " ".join([str(i) for i in fibonacci_list])
        elif distance == 0:
            return 2, 0
        else:
            return "Negative Value"
    except:
        return "An error occurred"