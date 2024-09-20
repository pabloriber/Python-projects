import tkinter as tk
from tkinter import messagebox

Dinheiro = 1500
itens_comprados = []  # Lista para armazenar os itens que o usuário comprou

# Função para atualizar o saldo exibido na janela
def atualizar_saldo():
    label_saldo.config(text=f'Saldo: ${Dinheiro}')

# Função para trabalhar e ganhar $1500
def trabalhar():
    global Dinheiro
    Dinheiro += 1500
    atualizar_saldo()
    messagebox.showinfo("Trabalho", "Você trabalhou e ganhou $1500!")

# Função para processar a compra
def comprar_produto(nome, preco):
    global Dinheiro
    if Dinheiro >= preco:
        Dinheiro -= preco
        itens_comprados.append(nome)  # Adiciona o item comprado à lista
        atualizar_saldo()
        messagebox.showinfo("Compra", f"Você comprou {nome} por ${preco}!")
    else:
        resposta = messagebox.askquestion("Saldo insuficiente", f"Você não tem dinheiro suficiente para comprar {nome}. Deseja se prostituir?")
        if resposta == 'yes':
            itens_comprados.append(nome)  # Adiciona o item mesmo assim
            messagebox.showinfo("Compra", f"Você adquiriu {nome}!")
        else:
            messagebox.showinfo("Compra cancelada", "Compra cancelada.")

# Função para exibir as opções de compra
def mostrar_produtos():
    janela_produtos = tk.Toplevel()
    janela_produtos.title("Produtos")
    
    produtos = [
        ('PC Gamer', 5000),
        ('Geladeira', 2000),
        ('AirPods', 1000),
        ('Guitarra Gibson', 6000),
        ('Guitarra Fender', 3000),
        ('Guitarra Memphis', 800),
        ('Microondas', 500),
        ('Ukulele', 300),
        ('TV 50 polegadas', 2500),
        ('TV 70 polegadas', 4000),
        ('Amplificador Marshall', 3500),
        ('Amplificador Fender', 3000),
        ('Amplificador Meteoro', 500)
    ]
    
    for produto, preco in produtos:
        botao = tk.Button(janela_produtos, text=f"{produto} (${preco})", command=lambda p=produto, c=preco: comprar_produto(p, c))
        botao.pack(fill='x', padx=10, pady=5)

# Função para exibir os itens que o usuário comprou
def mostrar_itens():
    janela_itens = tk.Toplevel()
    janela_itens.title("Itens comprados")
    
    if itens_comprados:
        for item in itens_comprados:
            label_item = tk.Label(janela_itens, text=item)
            label_item.pack(pady=5)
    else:
        label_vazio = tk.Label(janela_itens, text="Você não comprou nada ainda.")
        label_vazio.pack(pady=5)

# Configuração da janela principal
janela = tk.Tk()
janela.title("Loja Virtual")
janela.geometry("300x250")

# Rótulo para exibir o saldo
label_saldo = tk.Label(janela, text=f'Saldo: ${Dinheiro}', font=("Arial", 14))
label_saldo.pack(pady=10)

# Botão para abrir o menu de produtos
botao_comprar = tk.Button(janela, text="Comprar Produtos", command=mostrar_produtos)
botao_comprar.pack(pady=10)

# Botão para trabalhar e ganhar dinheiro
botao_trabalhar = tk.Button(janela, text="Trabalhar e ganhar $1500", command=trabalhar)
botao_trabalhar.pack(pady=10)

# Botão para exibir os itens comprados
botao_itens = tk.Button(janela, text="Ver itens comprados", command=mostrar_itens)
botao_itens.pack(pady=10)

# Botão para sair
botao_sair = tk.Button(janela, text="Sair", command=janela.quit)
botao_sair.pack(pady=10)

# Iniciar a interface gráfica
janela.mainloop()
