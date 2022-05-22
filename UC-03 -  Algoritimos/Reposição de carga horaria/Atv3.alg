algoritmo "fibonacci"
// Autor : Eduardo Henrique
// Data : 29/03/2022
// Seção de Declarações 
// =================================================================================
// Pesquisa sobre série de Fibonacci e implementação no algoritmo pedido abaixoSabemos que
// os dois primeiros números da série de Fibonacci são o número 1 e que a partir deles,
// calculamos o número subsequente sempre fazendo a soma dos dois últimos. Faça um
// que imprima os 20 primeiros números da série de Fibonacci.
// Obs: fórmula de formação da série de Fibonaci abaixo utilize no algoritmo
// P=Posição; (n)=Numero; P(1)=P(2)=1; P(n)=P(n-1)+P(n-2)
// ==================================================================================
Var
v: vetor[0..2] de inteiro
limite, cont: inteiro
Inicio
escreva("Digite um limite: ")
leia(limite)
v[0] <- -1
v[1] <- 1
cont <- 0

enquanto cont < limite faca
v[2] <- v[0] + v[1]
v[0] <- v[1]
v[1] <- v[2]
escreva(v[2])
cont <- cont+1
fimenquanto
Fimalgoritmo
