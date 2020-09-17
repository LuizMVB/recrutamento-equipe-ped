# Processo Seletivo Estagiário Radix - Equipe P&D

## Introdução

Conforme informado durante a sua entrevista, este desafio tem o objetivo de testar de forma geral sua capacidade de solucionar problemas. Neste desafio, as questões são constituídas por desafios de programação contextualizados para o setor elétrico, tal qual os desafios que serão enfrentados por você durante o trabalho. Leia atentamente as regras antes de começar e caso não saiba ou não consiga resolver alguma questão, escreva o máximo possível demonstrando seu raciocínio e dificuldades encontradas. Boa sorte!

## Regras Gerais

 - Procure escolher uma única linguagem para resolver as questões. Com exceção à questão nº 3, dê preferências às seguintes:
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

## Critérios de Avaliação
   - Execução/compilação correta do código;
   - Explicação do raciocínio utilizado;
   - Estrutura, organização e legibilidade do código.
   - Diferenciais:
      - Utilização de orientação à objetos;
      - Criação de testes unitários;
      - Utilização eficiente de recursos específicos de uma determinada linguagem;
      - Criação de uma interface WEB (mesmo que muito simples).

## Envio e Finalização
1. Na pasta da sua solução, inclua um arquivo `lang.info` que contenha somente uma linha com o nome da linguagem utilizada para solucionar o desafio (exceto a questão nº 3) em letras __MAIÚSCULAS__. Caso tenha sido feita em pseudocódigo, escreva somente `PSEUDO`;
2. Envio:
   - Método 1:
      - Crie um merge request no mesmo repositório onde estas instruções foram obtidas.

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

### Questão 3 - Número de Série dos Transformadores (SQL) (2,0 pontos)
Elian, um desenvolvedor especialista em bancos de dados precisa construir uma aplicação que liste os números de série dos transformadores de uma empresa de transmissão de energia. Porém, a organização dos bancos de dados da empresa em questão não é das melhores e além de ficarem em uma tabela separada, os números de série que possuem um formato específico na realidade estão salvos sem nenhum formato. Como Elian está exageradamente atarefado com a construção do backend da solução, pediu à você que selecione os números de série associados a cada transformador e aplique uma máscara nos valores, para que fiquem formatados corretamente. A estrutura das tabelas é a seguinte:

   - Tabela "tb_transformadores":

   | Coluna     | Tipo         | Exemplo|
   | -----------| -------------| -------|
   | id         | numeric (PK) | 171    |
   | nome       | varchar (255)| t1_A   |
   | subestacao | char (3)     | TZO    |

   - Tabela "tb_transformadores_num_serie"

   | Coluna           | Tipo         | Exemplo            |
   | -----------------| -------------| -------------------|
   | id_transformador | numeric (FK) | 171                |
   | num_serie        | char (20)    | 8856223677895521   |

O formato do número de série segue a máscara "00.0000.0000-0000/00".
Escreva uma consulta SQL que atualize os números de série dos transformadores de maneira que sigam o padrão fornecido pela máscara.

#### Dica
 - A coluna `id_transformador` é uma chave estrangeira para a tabela `tb_transformadores`. 

##### Ponto Extra (0,5 ponto):
Enquanto você implementava a primeira solução, a empresa recebeu novos transformadores do fornecedor. Dessa vez, os números de série recebidos do fornecedor estão em formatos variados. Alguns valores já possuem a máscara aplicada, porém outros não. Sua tarefa é escrever uma nova consulta SQL que seja capaz de lidar com os valores já formatados.

### Questão 4 - Fases Palíndromas (3,0 pontos)
Kleyton Verão, um renomado cientista de dados do interior utiliza seu tempo livre para porcurar padrões e sequências em locais inusitados. Ao observar uma base de dados de um projeto do setor de distribuição observou que informações sobre quais fases da rede apresentavam defeito apresentavam um padrão de palíndromo. Uma sequência de caracteres é um palíndromo caso seja idêntica quando lida da esquerda pra direita e da direita pra esquerda. Por exemplo, `ABCBA` é um palíndromo enquanto `ABCNBA` não. Kleyton então pediu que você criasse uma função `Palindromo` que encontre em cada sequência presente na base de dados a maior subsequência que seja um palíndromo. Por exemplo, na sequência `ABCBABN` a maior subsequência que é um palíndromo é `ABCBA` (`BCB` também é um palíndromo, mas não o maior).
As sequências presentes na base são formadas pelas letras A, B, C e N (ex. `ABCABBACNANBC`).

![Gerador e seus enrolamentos](https://s.dicio.com.br/palindromo.png)

#### Dica
 - Sequências de somente um caractere não são consideradas palíndromos;
 - Avalie se as sequências são válidas.

### Questão 5 - Numeração Ineficiente (2,0 pontos)
Flábio Loubão, de forma a entender melhor o processo de um cliente durante a fase de prospecção de novos projetos decidiu que seria uma boa ideia passar um dia no setor a ser contemplado pelo projeto para entender melhor o dia a dia dos funcionários. Após um voo atrasado e uma revista não esperada na segurança do aeroporto, Flábio chegou no cliente e imediatamente percebeu uma forma de melhorar o processo. Na gestão do estoque dos equipamentos de medição da empresa, as caixas dos medidores deveriam ser marcadas com número sequenciais. A marcação é feita utilizando adesivos, com os dígitos. A separação dos adesivos era feita "on-demand", conforme os equipamentos eram colocados nas caixas, de maneira ineficiente. Os funcionários sabiam no início do dia o número da primeira e última caixa a serem numeradas. Dessa maneira, Flábio pediu que você criasse uma função `Digitos(a, b)` que receba o número da primeira e última caixa (inteiros positivos) e informe aos funcionários quantos adesivos de cada dígito serão necessários para um dia. Por exemplo, se as caixas do dia forem númeradas de `1` a `10`, a função deveria retornar `1 2 1 1 1 1 1 1 1`, ou seja, um dígito zero, dois dígitos um, um dígito dois e assim por diante.

#### Dica
 - Teste sua função com números grandes e pequenos.







