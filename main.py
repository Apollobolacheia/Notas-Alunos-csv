from turtle import clear
import pandas as pd
import csv
import os

os.system("cls")

from pandas import *
import numpy as np
import json
import sys
import platform

import tkinter as tk
from tkinter import *

"""
from asyncio.windows_events import NULL

import string
from tkinter.messagebox import CANCEL
from turtle import clear, exitonclick
import pandas as pd
import csv
import os
#from csv import reader
os.system("cls")

from pandas import *
import numpy as np
import json
import sys
import platform
#import pynput 
import tkinter as tk
from tkinter import *
import msvcrt
##import keyboard

import sqlite3
"""
nomes = []
notas_1 = []
notas_2 = []
faltas = []
medias = []
situacaos = []
tips = []

from pynput.keyboard import Key, Listener 

print(" "*15,"Diretório : - ",os.path.abspath(os.getcwd()))
try:
     with open("./alunos.csv", "r") as recentData:
        recentDataframe = csv.reader(recentData)
        for i, linha in enumerate(recentDataframe):
            for il, _ in enumerate(linha):
                if i > 0:
                    if il == 0:
                        pass
                    elif il == 1:
                        nomes.append(linha[il])                        
                    elif il == 2:
                        notas_1.append(linha[il])
                    elif il == 3:
                        notas_2.append(linha[il])
                    elif il == 4:
                        faltas.append(linha[il])
                    elif il == 5:
                        medias.append(linha[il]) 
                    elif il == 6:
                        situacaos.append(linha[il])       
except:
    print(" "*15,"Criando nova Tabela")
    
    with open("./alunos.csv", "w") as recentData:
       pass

def cadastrar():
    print(" "*15,"Diretório : - ",os.path.abspath(os.getcwd()))
    t = 0
    while t == 0 :
      nome = input("            Digite o Nome do Aluno ........: ")
      nome = nome.upper()
      if nome == '':
        return
      else:  
       if nome not in nomes:
        nomes.append(nome)
        print(" "*9,'Nome Adicionado com Sucesso ..')
        t = 1
       else:
        print(" "*9,'Nome Duplicado ..! - Não vou Adicionar ') 
        pass 
    #-------------
    f = 0
    nota1 = input("            Digite a 1a.Nota do Aluno .....: ") 
    if nota1 != "":    
      nota1 = float(nota1)  
    else:
      nota1 = 0   
      nota1 = float(nota1)     
    nota2 =   input("            Digite a 2a.Nota do Aluno .....: ")
    if nota2 != "":   
      nota2 = float(nota2)
    else:
      nota2 = 0  
      nota2 = float(nota2)   
    falta =   input("            Digite o Nr. de Faltas do Aluno: ")
    if falta != "":    
      falta = float(falta)
    else:
      falta = 0 
      falta = float(falta)
    notas_1.append(nota1)
    notas_2.append(nota2)
    faltas.append(falta)
    
    nt = [nota1, nota2]
    nt = sum(nt)/2
    media = nt
    if falta >= 5:
      situacao = "REPROVADO"
    if media < 7:  
      situacao = "REPROVADO"
    if (falta) < 5 and (media) >= 7:
      situacao = "APROVADO" 
    print("")  
    print(" "*9,"Média - ", media, " - Faltas - ",falta, "- ",situacao) 
    print("")
    medias.append(media)
    situacaos.append(situacao)

def consultar(): 
    print(" "*15,"Diretório : - ",os.path.abspath(os.getcwd()))
    print("")   
    results = pd.read_csv('./alunos.csv') 
    print("                Essa tabela possui ", len(results)," registro(s)") 
    print("")
    
    data = {"Nome":nomes, "Notas 1U":notas_1, "Notas 2U":notas_2, "Faltas":faltas, "Media":medias, "Situacao":situacaos}
    df = pd.DataFrame(data) 
    
    #df = pd.read_csv("csv_import.csv",skiprows=1) #==> use to skip first row (header if required)
    df = pd.read_csv("alunos.csv") #===> Include the headers
    correct_df = df.copy()
    correct_df.rename(columns={'Nome': 'Nome do Aluno', 'Notas 1U': '1a. Nota','Notas 2U': '2a. Notas','Faltas': 'Faltas','Media': 'Média','Situacao': 'Situacão'}, inplace=True)
    print(correct_df)
    #Exporting to CSV file
    correct_df.to_csv(r'csv_export', index=False,header=True)
      
def limpatela():   
    print(" "*15,"Diretório : - ",os.path.abspath(os.getcwd()))
    if os.name == "nt": 
      os.system("cls")
    else: 
      os.system("clear")
def remover():
    print(" "*15,"Diretório : - ",os.path.abspath(os.getcwd()))
    indice = input("                Digite o Nr. da Linha para Deletar : ")
    if indice == "":
       return
    else:
       indice = int(indice)  
    nomes.pop(indice)
    notas_1.pop(indice)
    notas_2.pop(indice)
    faltas.pop(indice)
    medias.pop(indice)
    situacaos.pop(indice)
    data = {"Nome":nomes, "Notas 1U":notas_1, "Notas 2U":notas_2, "Faltas":faltas, "Media":medias, "Situacao":situacaos}        
    df = pd.DataFrame(data)
    print(" "*8,df)
def editar():
    print(" "*15,"Diretório : - ",os.path.abspath(os.getcwd()))
    p = 0
    while p == 0:
        colunas = ["Nome", "Faltas", "Notas 1U", "Notas 2U", "Media", "Situacao"]
        print("")
        u = ("Nota Digite : - < Nr. > da Coluna - < 0 > p/Nome - < 1 > p/1a. Nota - ")
        v = ("Nota Digite : - < 2 > p/2a. Nota - < f/F > p/Faltas ")
        print(" "*15,u)
        print(" "*15,v)
        print("")
        l = input("                Digite o Nr. da Coluna para fazer a Alteração : ")
        if l == "":
          return
        else:
          l = int(l)  
        c = input("                Digite <0> p/Nome <1> p/1a.Nota <2> p/2a.Nota <f> p/Faltas: ")
       
        if c == '0':
          c = "Nome" 
        if c == '1':
          c = "Notas 1U"   
        if c == '2':
          c = "Notas 2U"  
        if c == "f" or c == "F":
          c = "Faltas"      
        
        if i > l and c in colunas:  #.lower()
            print(c)
            if c == "Nome": #.lower()
              print("")    
              print(" "*15, "Média - ", data["Media"][l], " - Faltas - ", data["Faltas"][l], " - ",data["Situacao"][l])            
              newVal = input("                Digite o novo Nome : ")
              data["Nome"][l] = newVal.upper()
              print(" "*15,newVal.upper())             
              p = 1
            elif c == "Faltas":  #.lower()
                print("") 
                print(" "*15, "Média - ", data["Media"][l], " - Faltas - ", data["Faltas"][l], " - ",data["Situacao"][l])  
                newVal = float(input("                Digite o novo Nr. de Faltas : "))
                data["Faltas"][l] = newVal
                falta = newVal  
                nt1 = float(data["Notas 1U"][l])
                nt2 = float(data["Notas 2U"][l])
                if falta >= 5:
                  print(" "*15, "Média - ", data["Media"][l], " - Faltas - ", data["Faltas"][l], " - REPROVADO")   
                  data["Situacao"][l] = "REPROVADO" 
                elif  falta < 5 and float(data["Media"][l]) >= 7:
                  print(" "*15, "Média - ", data["Media"][l], " - Faltas - ", data["Faltas"][l], " - APROVADO")   
                  data["Situacao"][l] = "APROVADO"                 
                p = 1
                df = pd.DataFrame(data)
                df.to_csv("./alunos.csv")
            elif c == "Notas 1U":  #.lower()
                print("") 
                print(" "*15, "Média - ", data["Media"][l], " - Faltas - ", data["Faltas"][l], " - ",data["Situacao"][l])  
                newVal = float(input("                Digite o novo Nr. da 1a. Nota : "))                
                data["Notas 1U"][l] = newVal
                falta = float(data["Faltas"][l]) #newVal
                nt1 = float(data["Notas 1U"][l])
                nt2 = float(data["Notas 2U"][l])
                
                nt = [nt1, nt2] 
                nt = sum(nt)/2
                # print(" "*15,"Média : - ",nt)
                media = nt
                data["Media"][l] = media
                if falta >= 5:
                  print(" "*15, "Média - ", data["Media"][l], " - Faltas - ", data["Faltas"][l]," - REPROVADO")   
                  data["Situacao"][l] = "REPROVADO"
                else:  
                  if media < 7:  
                    print(" "*15,"Média - ", data["Media"][l], " - Faltas - ", data["Faltas"][l]," - REPROVADO")  
                    data["Situacao"][l] = "REPROVADO"
                  elif media >= 7 and falta <= 5:   
                    print(" "*15,"Média - ", data["Media"][l], " - Faltas - ", data["Faltas"][l], " - APROVADO")  
                    data["Situacao"][l] = "APROVADO" 
                
                p = 1
                df = pd.DataFrame(data)
                df.to_csv("./alunos.csv")
            elif c == "Notas 2U":  #.lower()
                print("") 
                print(" "*15, "Média - ", data["Media"][l], " - Faltas - ", data["Faltas"][l], " - ",data["Situacao"][l])  
                newVal = float(input("                Digite o novo Nr. da 2a. Nota : "))
                data["Notas 2U"][l] = newVal
                falta = float(data["Faltas"][l]) #newVal
                nt1 = float(data["Notas 1U"][l])
                nt2 = float(data["Notas 2U"][l])
                print(" "*15,'Aluno : ',data["Nome"][l])
               
                nt = [nt1, nt2] 
                nt = sum(nt)/2
                media = nt
                data["Media"][l] = media
                if falta >= 5:
                  print(" "*15,"Média - ", data["Media"][l], " - Faltas - ", data["Faltas"][l], " - REPROVADO")   
                  data["Situacao"][l] = "REPROVADO"
                else:  
                  if media < 7:  
                    print(" "*15,"Média - ", data["Media"][l], "REPROVADO")  
                    data["Situacao"][l] = "REPROVADO"
                  elif media >= 7 and falta <= 5:   
                    print(" "*15,"Média - ", data["Media"][l]," - Faltas - ", data["Faltas"][l], " - APROVADO")  
                    data["Situacao"][l] = "APROVADO" 
                p = 1
                df = pd.DataFrame(data)
                df.to_csv("./alunos.csv")
        else:
            print(" "*15,"Tente novamente")
option = 0
 
data = {"Nome":nomes, "Notas 1U":notas_1, "Notas 2U":notas_2, "Faltas":faltas, "Media":medias, "Situacao":situacaos}#df = pd.DataFrame(data)

while option != '6':
  print(" ")
  print(" "*15,"SISTEMA DE MANUTENÇÃO DE ALUNOS")
  print(" ")
  print(" "*15,"Digite uma das Opções - : < 1 - 2 - 3 - 4 > e Tecle < Enter >")
  print(" "*15,"Digite a Opição < 5 > p/Limpar a Tela e < 6 > p/Sair ")

  option = (input("""  
            [1] - Cadastrar Alunos
            [2] - Consultar Alunos
            [3] - Editar Alunos
            [4] - Remove Registro
            [5] - Limpa Tela 
            [6] - Sai do Programa
 
            """ "Digite uma Opção - : "))   
            
  print("")  

  if option == '1':    
    data = {"Nome":nomes, "Notas 1U":notas_1, "Notas 2U":notas_2, "Faltas":faltas, "Media":medias, "Situacao":situacaos}
    df = pd.DataFrame(data)
    cadastrar()
    data = {"Nome":nomes, "Notas 1U":notas_1, "Notas 2U":notas_2, "Faltas":faltas, "Media":medias, "Situacao":situacaos}
    df = pd.DataFrame(data)
    df.to_csv("./alunos.csv")        
  
  elif option == '2':
    lista = list()
    if os.name == "nt": 
      os.system("cls")
    else:
      os.system("clear") 
    consultar()
    # df = pd.DataFrame(data)
    data = {"Nome":nomes, "Notas 1U":notas_1, "Notas 2U":notas_2, "Faltas":faltas, "Media":medias, "Situacao":situacaos}         
    df = pd.DataFrame(data)
    """
    print('-' * 30) 
    print(f'{"Nr.":<4}{"Nome":<4}{"1a.Nota.":<4}{"2a.Nota":<4}{"Faltas":<4}{"Média":<4}{"Situação":<4}')
    print('-' * 30)
    """

  elif option == '3':   
    editar()       
    data = {"Nome":nomes, "Notas 1U":notas_1, "Notas 2U":notas_2, "Faltas":faltas, "Media":medias, "Situacao":situacaos}
    df = pd.DataFrame(data)
    df.to_csv("./alunos.csv") 
  elif option == '4':
    remover() 
    data = {"Nome":nomes, "Notas 1U":notas_1, "Notas 2U":notas_2, "Faltas":faltas, "Media":medias, "Situacao":situacaos}
    df = pd.DataFrame(data)
    df.to_csv("./alunos.csv")   
  elif option == '5': 
    limpatela()  
  elif option == '': 
    # print("Vou Voltar as Opções ..!")
    limpatela()
    pass  
else:
  pass  
data = {"Nome":nomes, "Notas 1U":notas_1, "Notas 2U":notas_2, "Faltas":faltas, "Media":medias, "Situacao":situacaos}
df = pd.DataFrame(data)
#df.to_csv("./alunos.csv")
if os.name == "nt": 
  os.system("cls")
else: 
  os.system("clear")