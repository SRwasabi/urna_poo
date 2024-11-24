from gerenciar_urna import *
import pickle
from common import *
import tkinter as tk
from tkinter import messagebox

#==================================================================================================#
# Inicialização da Urna
global urna
global titulo_eleitor
global eleitor

ARQUIVO_ELEITORES = 'eleitores.pkl'
ARQUIVO_CANDIDATOS = 'candidatos.pkl'

eleitores = {}  # Dicionário onde a chave será o título
candidatos = {}
try:
    print("Carregando lista de eleitores...")

    # Carregar eleitores do arquivo
    with open(ARQUIVO_ELEITORES, 'rb') as arquivo:
        eleitores = pickle.load(arquivo)

    print("Carregando lista de candidatos...")

    # Carregar candidatos do arquivo
    with open(ARQUIVO_CANDIDATOS, 'rb') as arquivo:
        candidatos = pickle.load(arquivo)

except FileNotFoundError as erro:
    print(erro)
    print("Arquivo não encontrado. Nenhum eleitor carregado!")

# Criação da urna com os dados carregados
urna = Urna("madu", "1", "1", candidatos.values(), eleitores.values())
#==================================================================================================#


# Função para alternar entre telas
def mudar_tela(nova_tela):
    # Limpa todos os widgets existentes na janela principal
    for componente in urna_eletronica.winfo_children():
        componente.destroy()

    # Executa a função correspondente à nova tela
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
        font=("Arial", 15, "bold"),  # Adicionado 'bold' para o texto ficar em negrito
        wraplength=380,
        justify="center"
    )
    texto_inicial.pack(pady=22)

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
            try:
                titulo_eleitor = int(titulo)
                eleitor = urna.get_eleitor(titulo_eleitor)
                if not eleitor:
                    # Exceção levantada quando o eleitor não for encontrado
                    raise Exception("Eleitor não é desta Urna")

                eleitor = eleitores[titulo_eleitor]
                mudar_tela(lambda: tela_informacoes(eleitor))

            except Exception as e:
                # Exibe a mensagem de erro no caso de exceção
                messagebox.showwarning("Erro", str(e))
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

    # botao corrigir formatação
    tk.Button(
        frame,
        text="Corrigir",
        font=("Arial", 12, "bold"),
        bg="red",
        fg="white",
        width=8,
        height=2,
        command=corrigir
    ).grid(row=5, column=0, pady=5)

    # botao branco formatação
    tk.Button(
        frame,
        text="Branco",
        font=("Arial", 12, "bold"),
        bg="white",
        fg="black",
        width=8,
        height=2,
        command=branco
    ).grid(row=5, column=1, pady=5)

    # botao confirmar formataçaõ
    tk.Button(
        frame,
        text="Confirmar",
        font=("Arial", 12, "bold"),
        bg="green",
        fg="white",
        width=8,
        height=2,
        command=confirmar
    ).grid(row=5, column=2, pady=5)


# Configuração da janela principal
urna_eletronica = tk.Tk()
urna_eletronica.title("Urna Eletrônica")
urna_eletronica.geometry("700x450")
urna_eletronica.config(bg="white")

# Inicia com a tela inicial
tela_inicial()

# Mantém a execução da interface gráfica

urna_eletronica.mainloop()
