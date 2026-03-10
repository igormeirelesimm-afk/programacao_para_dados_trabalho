
#Gerando o módulo#Senti dificuldades em gerar um código que antedesse a toda a demanda o trabalho. Então resolvi ir por partes.
#A primeira parte foi criar um código que abrisse e lê-se o arquivo.
#Então, constatei que o arquivo era muito pesado para ficar executando, por isso criei uma espécie de limitador para isso.
#Logo após, foi atribuiído o comando next para tirar o cabeçalho do trabalho
#Depois foi criado um código para separar os jogos gratuítos dos não gratuítos. Foi então que descobri que o arquivo estava em forma de texto e precisei adptar o código para '0' e '0.0', para ler os textos.
#A minha primeira ideia para contar os jogos por ano foi encontrar o primeiro e o último ano, pois achando o primeiro e o último eu preencheria manualmente o intervalo entre eles.
#Depois disso, usaria if para contar todos os jogos para cada ano, individualmente.
#Depois de ter feito o código para analisar arquivos resolvi transforma-lo em um módulo com classe, o que fico mais difícil do que se eu tivesse criado como classe desde o início.
#Precisei utilizar o Gemini para corrigir o trabalho, e ele me apontou uma incosistência.
#Caso o arquivo não tivesse linhas a variável total seria igual zero, e como ela está no diviso isso geraria um erro! Por isso foi criado um If para ele!


import csv

class processador_de_arquivos:
  def __init__(self):
    self.cont=0
    self.free=0
    self.paid=0
    self.menor_ano=2050
    self.maior_ano=0
    self.conta_jogos={}

  def resultados(self,nome_arquivo,quant_linhas=5000): 
    
    #Caso não seja indicado um valor, a código utilizar o valor de 5000 pois foi o máximo de linhas que o colab rodou enquanto estava gerando o código!
     #O arquivo original era muito grande. Toda vez que ía rodar o programa para testar o código o colab fica muito tempo processando. Por isso foi criado um limitador.
     #Caso queira rodar todas as linhas basta aumentar quantidade de linhas para quanto você deseja ler.

    with open(nome_arquivo,mode='r',encoding='utf-8',newline='') as dados:

      arquivo=csv.reader(dados)

      next(arquivo)

      for line in arquivo:
       if self.cont<quant_linhas:
         if line[7]=='0' or line[7]=='0.0': #O código foi escrito dessa forma porque o comando csv.reader lê o arquivo como texto!
           self.free+=1 
         else:
           self.paid+=1
         data=line[2]
         ano=data.split()
         ano=int(ano[-1]) #Nesse trecho eu não achei outra forma e tive que converter o dado para um valor numérico. Poderia ter feito isso desde o começo!
         if self.menor_ano>ano:
           self.menor_ano=ano
         if self.maior_ano<ano:
           self.maior_ano=ano
           
         self.conta_jogos[ano]=self.conta_jogos.get(ano,0)+1

         #Na linha acima eu pensei em usar uma outra lógica mais manual.
         #Como eu já sabia o primeiro ano e o último ano do arquivo eu ia listar todos os anos e usar uma estratura com if e um contador. Mas resolvi achar esse comando na internet!

         print(line)
         self.cont+=1
    total=self.free+self.paid
     
    print('='*200)
    for ano in sorted(self.conta_jogos):
        quantidade=self.conta_jogos[ano]
        print(f'A quantidade de jogos do ano {ano} é {quantidade}!')
    
    if total>0:
      print(f"O total de jogos são: {total}, sendo {self.free/total*100:.2f}% gratuítos e {self.paid/total*100:.2f}% pagos!")
      print(f'O primeiro ano a lançar um jogo foi: {self.menor_ano} e o último foi {self.maior_ano}!')
    else:
      print('O arquivo estava vazio!')
