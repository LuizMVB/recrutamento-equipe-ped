def ColocarTorres(total_n):
    try:
        #criando uma lista com os dois primeiros elementos da sequência de fibonacci
        fibonacci_list = [0, 1]

        #caso o total de torres seja maior que 1, a posição será diferente de zero
        #uma vez que as duas primeiras torres devem estar na posição zero (0)
        if total_n > 1:

            #utilizei o loop 'for' ao invés de recursão por conta da maior eficiencia
            #veja: https://stackoverflow.com/questions/18172257/efficient-calculation-of-fibonacci-series
            for _ in range(2, total_n):
                fibonacci_list.append(fibonacci_list[-1] + fibonacci_list[-2])

            return " ".join([str(i) for i in fibonacci_list]) 
            #opção de retorno alternativa: "".join(list(map(lambda x: str(x), fibonacci_list)))
            
        elif total_n >= 0:
            return 0
        else:
            return "Negative Value"
    except:
        return "An error occurred"