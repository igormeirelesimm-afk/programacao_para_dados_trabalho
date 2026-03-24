
"""
Teste para se fazer com os arquivos:
Esta classe analisa uma lista de jogos tentando responder três perguntas!
1) Qual o percetual de jogos gratuítos e pagos na plataforma?
2) Qual o ano com maior número de novos jogos?
3) Qual o primeiro e o último ano de lançamento dos jogos?
>>> teste=processador_de_arquivos()
>>> teste.analisar('steam_games_teste.csv',20)
>>> teste.total
20
>>> teste.percentual()
O percentual de jogos pagos são: 0.00%
O percentual de jogos gratuítos são: 100.00%
>>> teste.AnoComMaisLanc()
O(s) ano(s) com mais jogos foi/foram: [2021] com 7 jogos!
>>> teste.intervalo()
O primeiro ano a lançar um jogo foi: 2017 e o último foi 2022!
"""

import csv

class processador_de_arquivos:
  def __init__(self):
    self.cont=0
    self.free=0
    self.paid=0
    self.menor_ano=2050
    self.maior_ano=0
    self.conta_jogos={}
    self.maior_quantidade=0

  def analisar(self,nome_arquivo,quant_linhas=5000):
    self.ano_mais_jogos=[]

    #Caso não seja indicado um valor, a código utilizar o valor de 5000 pois foi o máximo de linhas que o colab rodou enquanto estava gerando o código!
     #O arquivo original era muito grande. Toda vez que ía rodar o programa para testar o código o colab fica muito tempo processando. Por isso foi criado um limitador.
     #Caso queira rodar todas as linhas basta aumentar quantidade de linhas para quanto você deseja ler.

    with open(nome_arquivo,mode='r',encoding='utf-8',newline='') as dados:

      arquivo=csv.reader(dados)

      next(arquivo)

      for line in arquivo:
        if self.cont>quant_linhas:
          break
        try:
          if line[7]=='0' or line[7]=='0.0':
            self.free+=1
          else:
            self.paid+=1
          data=line[2]
          ano=data.split()
          ano=int(ano[-1])
          if self.menor_ano>ano:
            self.menor_ano=ano
          if self.maior_ano<ano:
            self.maior_ano=ano
          self.conta_jogos[ano]=self.conta_jogos.get(ano,0)+1
          self.cont+=1
        except(IndexError,ValueError):
          continue

      for ano, quantidade in self.conta_jogos.items():
        if quantidade>self.maior_quantidade:
          self.maior_quantidade=quantidade
          self.ano_mais_jogos=[ano]
        elif quantidade==self.maior_quantidade:
          self.ano_mais_jogos.append(ano)


    self.total=self.free+self.paid
    if self.total==0:
      return print("ERRO: O arquivo não possui linhas válidas para análise!")

  def AnoComMaisLanc(self):
    print(f"O(s) ano(s) com mais jogos foi/foram: {self.ano_mais_jogos} com {self.maior_quantidade} jogos!")


  def percentual(self):
    print(f"O percentual de jogos pagos são: {((self.paid/self.total)*100):.2f}%")
    print(f"O percentual de jogos gratuítos são: {((self.free/self.total)*100):.2f}%")

  def intervalo(self):
    print(f'O primeiro ano a lançar um jogo foi: {self.menor_ano} e o último foi {self.maior_ano}!')

  def resultados(self):
    print('='*200)
    for ano in sorted(self.conta_jogos):
        quantidade=self.conta_jogos[ano]
        print(f'A quantidade de jogos do ano {ano} é {quantidade}!')

    if self.total>0:
      print(f"O total de jogos são: {self.total}, sendo {self.free/self.total*100:.2f}% gratuítos e {self.paid/self.total*100:.2f}% pagos!")
      print(f'O primeiro ano a lançar um jogo foi: {self.menor_ano} e o último foi {self.maior_ano}!')
    else:
      print('O arquivo estava vazio!')

if __name__=='__main__':
  import doctest
  doctest.testmod(verbose=True)
