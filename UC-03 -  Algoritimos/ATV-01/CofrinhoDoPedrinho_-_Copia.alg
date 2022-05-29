algoritmo "cofrinho do pedrinho"
// Função : calcular moedas
// Autor : eduardo henrique
// Data : 30/11/2021
// Seção de Declarações 
var
moedas: vetor[0..2, 0..6] de real
inicio
// Seção de Comandos 
moedas[0,0] <- 0.01
moedas[0,1] <- 0.05
moedas[0,2] <- 0.10
moedas[0,3] <- 0.25
moedas[0,4] <- 0.50
moedas[0,5] <- 1
escreval("=======================================")
escreval("======== Cofrinho do Pedrinho =========")
escreval("=======================================")
escreva("moedas de 1 centavo: ")
leia(moedas[1,0])
escreval("=======================================")
escreva("moedas de 5 centavos: ")
leia(moedas[1,1])
escreval("=======================================")
escreva("moedas de 10 centavos: ")
leia(moedas[1,2])
escreval("=======================================")
escreva("moedas de 25 centavos: ")
leia(moedas[1,3])
escreval("=======================================")
escreva("moedas de 50 centavos: ")
leia(moedas[1,4])
escreval("=======================================")
escreva("moedas de 1 real: ")
leia(moedas[1,5])
escreval("=======================================")
limpatela
  moedas[2,0] <- moedas[0,0] * moedas[1,0]
  moedas[2,1] <- moedas[0,1] * moedas[1,1]
  moedas[2,2] <- moedas[0,2] * moedas[1,2]
  moedas[2,3] <- moedas[0,3] * moedas[1,3]
  moedas[2,4] <- moedas[0,4] * moedas[1,4]
  moedas[2,5] <- moedas[0,5] * moedas[1,5]
  moedas[2,6] <- moedas[2,0] + moedas[2,1] + moedas[2,2] + moedas[2,3] + moedas[2,4] + moedas[2,5]
  escreval("=======================================")
  escreval("======== Cofrinho do Pedrinho =========")
  escreval("=======================================")
  se moedas[2,0] = 0 entao
      escreval("Não há moedas de 1 centavo")
  senao
      escreval("Total de moedas de 1 centavo: R$", moedas[2,0])
  fimse
  escreval("=======================================")
  se moedas[2,1] = 0 entao
      escreval("Não há moedas de 5 centavos")
  senao
      escreval("Total de moedas de 5 centavos: R$", moedas[2,1])
  fimse
  escreval("=======================================")
  se moedas[2,2] = 0 entao
      escreval("Não há moedas de 10 centavos")
  senao
      escreval("Total de moedas de 10 centavos: R$", moedas[2,2])
  fimse
  escreval("=======================================")
  se moedas[2,3] = 0 entao
      escreval("Não há moedas de 25 centavos")
  senao
      escreval("Total de moedas de 25 centavos: R$", moedas[2,3])
  fimse
  escreval("=======================================")
  se moedas[2,4] = 0 entao
      escreval("Não há moedas de 50 centavos")
  senao
      escreval("Total de moedas de 50 centavos: R$", moedas[2,4])
  fimse
  escreval("=======================================")
  se moedas[2,5] = 0 entao
      escreval("Não há moedas de 1 real")
  senao
      escreval("Total de moedas de 1 real: R$", moedas[2,5])
  fimse
  escreval("=======================================")
  escreval("Total: R$", moedas[2,6])
  escreval("=======================================")








fimalgoritmo
