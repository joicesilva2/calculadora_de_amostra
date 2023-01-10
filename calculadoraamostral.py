###########
habitantes = int(input('teclar os habitantes:'))
borda_de_erro = int( input('tecla_margem_de_erro'))
borda_de_erro =borda_de_erro/ 100 # modificar de percentual
padrao_primario = 1 / borda_de_erro ** 2
padrao = ( habitantes *padrao_primario)/( habitantes + padrao_primario)
print('A amostra ideal para o número de habitantes inserido é de:',int(padrao))

