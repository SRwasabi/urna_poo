from common import *
from eleicao import Urna
import tkinter as tk
from tkinter import messagebox

# Função para alternar entre telas
def mudar_tela(nova_tela):
    for widget in urna_eletronica.winfo_children():
        widget.destroy()  # Remove todos os widgets da tela atual
    nova_tela()

# Instancia uma urna globalmente (será inicializada na tela inicial)
urna = None

# Tela inicial para configurar a urna
def tela_inicial():
    def configurar_urna():
        global urna
        try:
            secao = int(entry_secao.get())
            zona = int(entry_zona.get())
            nome_mes = entry_mesario_nome.get()
            rg_mes = entry_mesario_rg.get()
            cpf_mes = entry_mesario_cpf.get()

            mesario = Pessoa(nome_mes, rg_mes, cpf_mes)
            urna = Urna(mesario, secao, zona, [], [])  # Configuração inicial
            messagebox.showinfo("Sucesso", "Urna configurada com sucesso!")
            mudar_tela(tela_titulo)
        except ValueError:
            messagebox.showerror("Erro", "Preencha todos os campos corretamente!")

    frame = tk.Frame(urna_eletronica, bg="white")
    frame.pack(expand=True, fill="both")

    tk.Label(frame, text="Configurar Urna", bg="white", font=("Arial", 14)).pack(pady=10)
    
    tk.Label(frame, text="Seção:", bg="white", font=("Arial", 12)).pack()
    entry_secao = tk.Entry(frame, font=("Arial", 12))
    entry_secao.pack(pady=5)

    tk.Label(frame, text="Zona:", bg="white", font=("Arial", 12)).pack()
    entry_zona = tk.Entry(frame, font=("Arial", 12))
    entry_zona.pack(pady=5)

    tk.Label(frame, text="Nome do Mesário:", bg="white", font=("Arial", 12)).pack()
    entry_mesario_nome = tk.Entry(frame, font=("Arial", 12))
    entry_mesario_nome.pack(pady=5)

    tk.Label(frame, text="RG do Mesário:", bg="white", font=("Arial", 12)).pack()
    entry_mesario_rg = tk.Entry(frame, font=("Arial", 12))
    entry_mesario_rg.pack(pady=5)

    tk.Label(frame, text="CPF do Mesário:", bg="white", font=("Arial", 12)).pack()
    entry_mesario_cpf = tk.Entry(frame, font=("Arial", 12))
    entry_mesario_cpf.pack(pady=5)

    tk.Button(frame, text="Confirmar Configuração", bg="green", fg="white", font=("Arial", 12),
              command=configurar_urna).pack(pady=10)

# Tela para inserir título de eleitor
def tela_titulo():
    def confirmar_titulo():
        try:
            titulo = int(visor.get())
            eleitor = urna.get_eleitor(titulo)
            if eleitor:
                messagebox.showinfo("Sucesso", f"Eleitor encontrado: {eleitor}")
                mudar_tela(tela_voto)
            else:
                messagebox.showwarning("Erro", "Eleitor não encontrado nesta urna!")
        except ValueError:
            messagebox.showerror("Erro", "O título deve conter apenas números!")

    frame_esquerdo = tk.Frame(urna_eletronica, bg="white", width=400, height=400)
    frame_esquerdo.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
    frame_direito = tk.Frame(urna_eletronica, bg="white", width=300, height=400)
    frame_direito.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

    tk.Label(frame_esquerdo, text="Digite o Título de Eleitor:", bg="white", font=("Arial", 12)).pack(pady=10)
    visor = tk.Entry(frame_esquerdo, font=("Arial", 16), justify="center")
    visor.pack(pady=10)

    criar_teclado_no_frame(frame_direito, visor, confirmar_titulo)

# Tela de votação
def tela_voto():
    def confirmar_voto():
        try:
            voto = int(visor.get())
            urna.registrar_voto(eleitor, voto)
            messagebox.showinfo("Sucesso", "Voto registrado com sucesso!")
            mudar_tela(tela_confirmacao)
        except ValueError:
            messagebox.showerror("Erro", "Digite um número válido para o voto!")

    frame_esquerdo = tk.Frame(urna_eletronica, bg="white", width=400, height=400)
    frame_esquerdo.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
    frame_direito = tk.Frame(urna_eletronica, bg="white", width=300, height=400)
    frame_direito.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

    tk.Label(frame_esquerdo, text="Digite o número do candidato ou 0 para branco:", bg="white", font=("Arial", 12)).pack(pady=10)
    visor = tk.Entry(frame_esquerdo, font=("Arial", 16), justify="center")
    visor.pack(pady=10)

    criar_teclado_no_frame(frame_direito, visor, confirmar_voto)

# Configuração da janela principal
urna_eletronica = tk.Tk()
urna_eletronica.title("Urna Eletrônica")
urna_eletronica.geometry("700x400")
urna_eletronica.config(bg="white")

# Inicia na tela inicial
tela_inicial()

urna_eletronica.mainloop()
