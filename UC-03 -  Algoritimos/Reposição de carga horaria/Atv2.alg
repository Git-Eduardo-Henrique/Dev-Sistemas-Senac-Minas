algoritmo "escola"
// Autor : Eduardo Henrique
// Data : 29/03/2022
// Seção de Declarações 
// =================================================================================================================
// Em uma escola temos uma classe com 10 alunos de varias idades utilize o algoritmo Bubble
// Sort nesta atividade.
// Obs: o algortimo realizará a leitura da idade dos 10 alunos, discriminando nome e idade utilizando o Bubble Sort.
// =================================================================================================================
var
idade: vetor[0..9] de inteiro
nome: vetor[0..9] de caractere
n: inteiro
inicio
// Seção de Comandos 
n <- 0
para n de 1 ate 10 faca
escreva("escreva o nome do ", n, "° aluno: ")
leia(nome[n - 1])
escreva("escreva a idade", n, "° aluno: ")
leia(idade[n - 1])
limpatela
fimpara

para n de 1 ate 10 faca
escreval("o(a) ", nome[n - 1], " tem", idade[n - 1], " anos")
fimpara
fimalgoritmo
