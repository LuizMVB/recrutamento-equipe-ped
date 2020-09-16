# Processo Seletivo Estagiário Radix - Equipe P&D

## Introdução

Conforme informado durante a sua entrevista, este desafio tem o objetivo de testar de forma geral sua capacidade de solucionar problemas. Neste desafio, as questões são constituídas por desafios de programação contextualizados para o setor elétrico, tal qual os desafios que serão enfrentados por você durante o trabalho. Leia atentamente as regras antes de começar e caso não saiba ou não consiga resolver alguma questão, escreva o máximo possível demonstrando seu raciocínio e dificuldades encontradas. Boa sorte!

## Regras Gerais

 - Procure escolher uma única linguagem para resolver as questões. Dê preferências às seguintes:
    - Python;
    - C#.NET;
    - Java;
    - Javascript;
    - Pseudocódigo.

 - Em __nenhuma__ hipótese utilize ferramentas pagas (ex. Matlab) para resolver as questões;
 - Escreva seu código de maneira clara e bem estruturada (bem dividido, indentado corretamente, etc);
 - Comente o código onde houver relevância;
 - Sua capacidade de pesquisa acerca de um problema encontrado também será avaliada. Ao utilizar sites de dúvidas (ex. Stackoverflow) não copie o código cegamente. Busque analisar criticamente as soluções antes de implementá-las.
 - Explique o seu raciocínio de maneira escrita. Mesmo que seu código não funcione 100% corretamente, a ideia por trás da lógica é o mais importante.
 - Apesar do trabalho equipe ser importante, procure fazer as questões __sozinho__. Códigos copiados de outros candidatos (atuais ou passados) podem ser facilmente identificados!

### Questão 1 - Linha de Transmissão de Fibonacci (1,5 pontos)

Um engenheiro civil e um engenheiro eletricista ficaram encarregados de um projeto com o objetivo de construir uma linha de transmissão conectando Mordor e Tangamandápio. Os engenheiros recentemente chegaram de uma viagem da Itália, onde além de se decepcionar com a culinária local, ficaram encantados pelos cientistas e matemáticos italianos. Para homenagear [Fibonacci](https://en.wikipedia.org/wiki/Fibonacci), decidiram contra diversas recomendações em espaçar as torres de acordo com a [sequência de mesmo nome](https://pt.wikipedia.org/wiki/Sequ%C3%AAncia_de_Fibonacci). Para isso, pediram à você que fizesse um programa que indique a posição das torres de acordo com o total de torres que devem ser colocadas. 

![Torres de Transmissão](https://imagens.ebc.com.br/4B5E4Np9_7f33aka4jwwKE38cuY=/1170x700/smart/https://agenciabrasil.ebc.com.br/sites/default/files/thumbnails/image/agencia_brasil170912_mca7686.jpg?itok=c5ZDE7sY "Torres de Transmissão")

A única exigência dos engenheiros é que as duas primeiras torres fiquem nas posições zero (0) e um (1) respectivamente.

Desenvolva uma função `ColocarTorres` que receba um número inteiro positivo representando o total de torres a serem colocadas e retorne suas posições, separadas por um caractere em branco.

#### Dica

   - `ColocarTorres(0) => 0`
   - `ColocarTorres(1) => 0`
   - `ColocarTorres(2) => 0 1`

##### Ponto Extra (1,0 pontos):
Para fazer com que a função se torne mais geral e aplicável à mais casos, os engenheiros pediram que você substitua a entrada da função do número de torres para a distância em quilômetros entre duas localidades quaisquer. Considerando que as posições das torres são mostradas também em quilômetros, calcule o número de torres e suas posições.

### Questão 2 - Número de Enrolamentos Perfeito (1,5 pontos)
Um engenheiro eletricista responsável por otimizar a construção de geradores elétricos para utilização em plantas de geração térmica descobriu uma nova metodologia para definir o número de voltas que os condutores dos enrolamentos do gerador devem possuir. Após assistir ao filme [Uma Mente Brilhante](https://en.wikipedia.org/wiki/A_Beautiful_Mind_(film)) em um fim de semana pacato, o engenheiro decidiu que o número de voltas dos enrolamentos deveria ser um __número__ __perfeito__. 

![Gerador e seus enrolamentos](https://www.asiantec.co.id/tinymce_uploaded/product/generator/gen_2.jpg)

Números perfeitos são números inteiros cujos divisores ao serem somados são iguais ao próprio número. Por exemplo, `6` é um número perfeito, já que seus divisores `1`, `2` e `3` ao serem somados resultam em `6`. Sua tarefa é fazer um programa que auxilie o engenheiro na definição de quais números são perfeitos.

Crie uma função `Perfeito` que receba um número inteiro positivo e diga se é ou não perfeito. A saída do programa devera ser:
   - "O número {n} é perfeito." caso positivo;
   - "O número {n} não é perfeito." caso negativo.

##### Ponto Extra (1,0 ponto):
Na semana seguinte, o engenheiro assistiu a série [Dark](https://dark.netflix.io/pt) e agora acredita que tudo está conectado. Por isso, gostaria também de conferir se os divisores de um número perfeito também são perfeitos. Modifique a sua função para que além da definição do número perfeito, diga se seus divisores também são perfeitos. A saída deve ser:
   - "O número {n} é perfeito. Seu(s) divisor(es) {x, y, z} também são perfeitos."







