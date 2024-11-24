from gerenciar_urna import *
import pickle
from common import *
import tkinter as tk
from tkinter import messagebox

#==================================================================================================#
# Inicialização da Urna
global eleitor
global titulo_eleitor
global urna


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
    # Visor
    frame_esquerdo = tk.Frame(urna_eletronica, bg="white", width=400, height=400)
    frame_esquerdo.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

    # Teclado
    frame_vazio = tk.Frame(urna_eletronica, bg="white", width=50, height=400)  # espaçamento 1
    frame_vazio.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

    frame_vazio_2 = tk.Frame(urna_eletronica, bg="white", width=30, height=400)  # largura reduzida
    frame_vazio_2.grid(row=0, column=2, padx=8, pady=10, sticky="nsew")

    frame_vazio_3 = tk.Frame(urna_eletronica, bg="white", width=1, height=300)  # espaçamento 3
    frame_vazio_3.grid(row=0, column=2, padx=0, pady=10, sticky="nsew")

    frame_direito = tk.Frame(urna_eletronica, bg="white", width=250, height=400)  # aumentada a largura
    frame_direito.grid(row=0, column=4, padx=15, pady=10, sticky="nsew")

    # Texto explicativo
    texto = tk.Label(frame_esquerdo, text="Digite o Título de Eleitor:", bg="white", font=("Arial", 14, "bold"))
    texto.grid(row=0, column=0, padx=5, pady=10, sticky="w")

    # Caixa de texto para o visor (com fundo cinza e abaixo da mensagem)
    visor = tk.Entry(frame_esquerdo, font=("Arial", 16), justify="center", bg="#f4f4f4", width=20)
    visor.grid(row=1, column=0, padx=5, pady=10, sticky="w")

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
    frame_vazio = tk.Frame(urna_eletronica, bg="white", width=50, height=400)  #  espaçamento 1
    frame_vazio.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

    frame_vazio_2 = tk.Frame(urna_eletronica, bg="white", width=50, height=400)  #  espaçamento 2
    frame_vazio_2.grid(row=0, column=2, padx=10, pady=10, sticky="nsew")

    frame_vazio_3 = tk.Frame(urna_eletronica, bg="white", width=25, height=300)  # espaçamento 3
    frame_vazio_3.grid(row=0, column=2, padx=20, pady=10, sticky="nsew")

    frame_direito = tk.Frame(urna_eletronica, bg="white", width=300, height=400)
    frame_direito.grid(row=0, column=4, padx=10, pady=10, sticky="nsew")

    # Informações do eleitor
    texto = tk.Label(frame_esquerdo, text="Informações do Eleitor:", bg="white", font=("Arial", 16, "bold"),
                     fg="#4A90E2")
    texto.pack(pady=15)
    # Caixa para as informações do eleitor
    info_frame = tk.Frame(frame_esquerdo, bg="#f4f4f4", bd=2, relief="solid", padx=12, pady=12, width=350)
    info_frame.pack(pady=5, fill="x")

    info = tk.Label(info_frame, text=f"{eleitor}", bg="#f4f4f4", font=("Arial", 14), fg="#333333")
    info.pack()

    # Teclado numérico
    criar_teclado_no_frame(frame_direito, None, confirmar_informacoes)

# tela para votação
def tela_voto(eleitor):
    def confirmar_voto():
        voto = visor.get().strip()

        print(f"Voto recebido: '{voto}'")

        if voto == "Voto em Branco":
            urna.registrar_voto(eleitor, "BRANCO")
        elif voto == "":
            urna.registrar_voto(eleitor, "NULO")
        elif voto.isdigit():
            voto = int(voto)
            if any(candidato.numero == voto for candidato in urna.candidatos):
                urna.registrar_voto(eleitor, voto)
            else:
                urna.registrar_voto(eleitor, "NULO")
        else:
            urna.registrar_voto(eleitor, "NULO")

        mudar_tela(tela_confirmacao)



    frame_esquerdo = tk.Frame(urna_eletronica, bg="white", width=400, height=400)
    frame_esquerdo.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

    frame_vazio = tk.Frame(urna_eletronica, bg="white", width=50, height=400)
    frame_vazio.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

    frame_vazio_2 = tk.Frame(urna_eletronica, bg="white", width=50, height=400)
    frame_vazio_2.grid(row=0, column=2, padx=10, pady=10, sticky="nsew")

    frame_vazio_3 = tk.Frame(urna_eletronica, bg="white", width=25, height=300)
    frame_vazio_3.grid(row=0, column=2, padx=20, pady=10, sticky="nsew")

    frame_direito = tk.Frame(urna_eletronica, bg="white", width=300, height=400)
    frame_direito.grid(row=0, column=4, padx=10, pady=10, sticky="nsew")

    texto = tk.Label(frame_esquerdo, text="Vote:", bg="white", font=("Arial", 14))
    texto.pack(pady=10)

    visor = tk.Entry(frame_esquerdo, font=("Arial", 16), justify="center", bg="#f4f4f4", width=20)
    visor.pack(pady=10)

    criar_teclado_no_frame(frame_direito, visor, confirmar_voto)


def tela_confirmacao_voto(numero_candidato):
    mudar_tela(tela_confirmacao)

    # estrutura
    frame_principal = tk.Frame(urna_eletronica, bg="white", width=700, height=400)
    frame_principal.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")


    texto_pergunta = tk.Label(
        frame_principal,
        text=f"Você deseja confirmar o voto no número {numero_candidato}?",
        bg="white",
        font=("Arial", 16, "bold"),
        fg="#007BFF"
    )
    texto_pergunta.pack(pady=50)





# tela de confirmação
def tela_confirmacao():
    def finalizar_votacao():
        mudar_tela(tela_inicial)

    frame_esquerdo = tk.Frame(urna_eletronica, bg="white", width=400, height=400)
    frame_esquerdo.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

    frame_vazio = tk.Frame(urna_eletronica, bg="white", width=50, height=400)
    frame_vazio.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

    frame_vazio_2 = tk.Frame(urna_eletronica, bg="white", width=50, height=400)
    frame_vazio_2.grid(row=0, column=2, padx=10, pady=10, sticky="nsew")

    frame_vazio_3 = tk.Frame(urna_eletronica, bg="white", width=25, height=300)
    frame_vazio_3.grid(row=0, column=2, padx=20, pady=10, sticky="nsew")

    frame_direito = tk.Frame(urna_eletronica, bg="white", width=300, height=400)
    frame_direito.grid(row=0, column=4, padx=10, pady=10, sticky="nsew")

    msg_confirmacao = tk.Label(
        frame_esquerdo,
        text="Voto Confirmado!",
        bg="white",
        font=("Arial", 14, "bold"),
        fg="#007BFF"
    )
    msg_confirmacao.pack(pady=(10, 0))

    msg_obrigado = tk.Label(
        frame_esquerdo,
        text="Obrigado por votar!",
        bg="white",
        font=("Arial", 12),
        fg="#007BFF"
    )
    msg_obrigado.pack(pady=(0, 10))

    info_frame = tk.Frame(frame_esquerdo, bg="#f4f4f4", bd=2, relief="solid", padx=10, pady=10)
    info_frame.pack(pady=10, fill="x")

    texto_info = tk.Label(
        info_frame,
        text=f"{urna}",
        bg="#f4f4f4",
        font=("Arial", 12),
        fg="#333333"
    )
    texto_info.pack()

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
