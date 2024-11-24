from gerenciar_urna import *
import pickle
from common import *
import tkinter as tk
from tkinter import messagebox

#==================================================================================================#
# Preparos iniciais da Urna
global urna
global titulo_eleitor
global eleitor

FILE_ELEITORES = 'eleitores.pkl'
FILE_CANDIDATOS = 'candidatos.pkl'

eleitores = {} #dicionário a chave será o titulo
candidatos = {}
try:
    print("Carregando arquivo de eleitores ...")

    with open(FILE_ELEITORES, 'rb') as arquivo:
            eleitores = pickle.load(arquivo)

    print("Carregando arquivo de candidatos...")
    with open(FILE_CANDIDATOS, "rb") as arquivo:
        candidatos = pickle.load(arquivo)

except FileNotFoundError as fnfe:
    print(fnfe)
    print("Arquivo nao encontrado, nenhum eleitor carregado!")
urna = Urna("madu", "1", "1", candidatos.values(), eleitores.values())
#==================================================================================================#

# Função para alternar entre telas
def mudar_tela(nova_tela):
    for widget in urna_eletronica.winfo_children():
        widget.destroy()  # Remove todos os widgets da tela atual
        #widgets igual a qualquer componente da interface 
    nova_tela()

# Tela inicial
def tela_inicial():
    def confirmar_principal():
        mudar_tela(tela_titulo)

# Estrutura principal #nswe igual a bussola
   #contem o visor no lado esquerdo
    frame_esquerdo = tk.Frame(urna_eletronica, bg="white", width=400, height=400)
    frame_esquerdo.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
#contem o teclado no lado direito
    frame_direito = tk.Frame(urna_eletronica, bg="white", width=300, height=400)
    frame_direito.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

 # Texto inicial
    texto_inicial = tk.Label(
        frame_esquerdo,
        text="Para inserir título de eleitor, aperte em Confirmar.",
        bg="white",
        font=("Arial", 12),
        wraplength=380,
        justify="center"
    )
    texto_inicial.pack(pady=20)

# Teclado numérico
    criar_teclado_no_frame(frame_direito, None, confirmar_principal)

# Função para alternar entre telas
def mudar_tela(nova_tela):
    for widget in urna_eletronica.winfo_children():
        widget.destroy()
    nova_tela()
    

#==================================================================================================#

#==================================================================================================#

# Tela para inserir título de eleitor
def tela_titulo():
    def confirmar_titulo():
        titulo = visor.get()
        if len(titulo) == 12:
            titulo_eleitor = int(titulo)
            eleitor = urna.get_eleitor(titulo_eleitor)
            if not eleitor:
                raise Exception("Eleitor não é desta Urna")
            
            eleitor = eleitores[titulo_eleitor]
            mudar_tela(lambda: tela_informacoes(eleitor))

        else:
            messagebox.showwarning("Erro", "O título deve conter 12 dígitos!")

 # Estrutura principal
 #visor
    frame_esquerdo = tk.Frame(urna_eletronica, bg="white", width=400, height=400)
    frame_esquerdo.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
#teclado
    frame_direito = tk.Frame(urna_eletronica, bg="white", width=300, height=400)
    frame_direito.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

# Texto e visor
    texto = tk.Label(frame_esquerdo, text="Digite o Título de Eleitor:", bg="white", font=("Arial", 12))
    texto.pack(pady=10)

    visor = tk.Entry(frame_esquerdo, font=("Arial", 16), justify="center")
    visor.pack(pady=10)

 # Teclado numérico
    criar_teclado_no_frame(frame_direito, visor, confirmar_titulo)

# Tela para exibir informações do eleitor
def tela_informacoes(eleitor):
    def confirmar_informacoes():
        mudar_tela(lambda: tela_voto(eleitor))
    
 # Estrutura principal
 #visor
    frame_esquerdo = tk.Frame(urna_eletronica, bg="white", width=400, height=400)
    frame_esquerdo.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
#teclado
    frame_direito = tk.Frame(urna_eletronica, bg="white", width=300, height=400)
    frame_direito.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

 # Informações do eleitor
    texto = tk.Label(frame_esquerdo, text="Informações do Eleitor:", bg="white", font=("Arial", 12))
    texto.pack(pady=10)

    info = tk.Label(frame_esquerdo, text=f"{eleitor}", bg="white", font=("Arial", 12))
    info.pack(pady=10)

 # Teclado numérico
    criar_teclado_no_frame(frame_direito, None, confirmar_informacoes)

# tela para votação
def tela_voto(eleitor):
    def confirmar_voto():
        voto = int(visor.get())
        urna.registrar_voto(eleitor, voto)

        mudar_tela(tela_confirmacao)

  #  estrutura principal
  #visor
    frame_esquerdo = tk.Frame(urna_eletronica, bg="white", width=400, height=400)
    frame_esquerdo.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
#teclado
    frame_direito = tk.Frame(urna_eletronica, bg="white", width=300, height=400)
    frame_direito.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

 # Texto e visor
    texto = tk.Label(frame_esquerdo, text="Vote:", bg="white", font=("Arial", 12))
    texto.pack(pady=10)

    visor = tk.Entry(frame_esquerdo, font=("Arial", 16), justify="center")
    visor.pack(pady=10)

 # teclado numérico
    criar_teclado_no_frame(frame_direito, visor, confirmar_voto)

# ela de confirmação
def tela_confirmacao():
    def finalizar_votacao():
        mudar_tela(tela_inicial)

 # Estrutura principal
 #visor
    frame_esquerdo = tk.Frame(urna_eletronica, bg="white", width=400, height=400)
    frame_esquerdo.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
#teclado
    frame_direito = tk.Frame(urna_eletronica, bg="white", width=300, height=400)
    frame_direito.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

# Texto
    texto = tk.Label(frame_esquerdo, text=f"Voto Confirmado!\nObrigado por votar!\n{urna}", bg="white", font=("Arial", 12))
    texto.pack(pady=20)

# teclado numérico
    criar_teclado_no_frame(frame_direito, None, finalizar_votacao)

# funcao do teclado numérico
def criar_teclado_no_frame(frame, visor, confirmar):
    def adicionar_numero(numero):
        if visor and len(visor.get()) < 12:
            visor.insert(tk.END, numero)

    def corrigir():
        if visor:
            visor.delete(0, tk.END)

    def branco():
        if visor:
            visor.delete(0, tk.END)
            visor.insert(0, "Voto em Branco")
# o primeiro numero é a numero do teclado
# o segundo numero é a linha
# o terceiro numero é a coluna
    botoes = [
        ('1', 1, 0), ('2', 1, 1), ('3', 1, 2),
        ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
        ('7', 3, 0), ('8', 3, 1), ('9', 3, 2),
        ('0', 4, 1)
    ]

    for (text, row, col) in botoes:
        tk.Button(frame, text=text, font=("Arial", 12), width=5, height=2,
                  command=lambda t=text: adicionar_numero(t)).grid(row=row, column=col, padx=5, pady=5)

    tk.Button(frame, text="Corrigir", font=("Arial", 12), bg="red", fg="white", width=7, height=2,
              command=corrigir).grid(row=5, column=0, pady=5)
    tk.Button(frame, text="Branco", font=("Arial", 12), bg="white", width=7, height=2,
              command=branco).grid(row=5, column=1, pady=5)
    tk.Button(frame, text="Confirmar", font=("Arial", 12), bg="green", fg="white", width=7, height=2,
              command=confirmar).grid(row=5, column=2, pady=5)

# config da janela principal
urna_eletronica = tk.Tk()
urna_eletronica.title("Urna Eletrônica")
urna_eletronica.geometry("700x400")
urna_eletronica.config(bg="white")

# inicia com a tela inicial novamente
tela_inicial()

urna_eletronica.mainloop()
