import sqlite3
import tkinter as tk
from tkinter import messagebox

# Inicializa o banco de dados e cria a tabela 'produtos' se nao existir
def init_db():
    conn = sqlite3.connect('produtos.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY,
            nome TEXT NOT NULL,
            descricao TEXT,
            preco REAL NOT NULL,
            disponibilidade BOOLEAN NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# funcao para adicionar ou editar um produto
def add_or_edit_produto(product_id=None):
    def save_produto():
        nome = entry_nome.get()
        descricao = entry_descricao.get()
        preco = entry_preco.get()
        disponibilidade = var_disponibilidade.get()

        if not nome or not preco:
            messagebox.showwarning("Aviso", "Nome e preco sao campos obrigatorios.")
            return

        try:
            preco = float(preco)
        except ValueError:
            messagebox.showwarning("Aviso", "Preco deve ser um numero valido.")
            return
        
        disponibilidade = "Sim" if disponibilidade == 1 else "Não"

        conn = sqlite3.connect('produtos.db')
        cursor = conn.cursor()

        if product_id:
            cursor.execute('''
                UPDATE produtos
                SET nome = ?, descricao = ?, preco = ?, disponibilidade = ?
                WHERE id = ?
            ''', (nome, descricao, preco, disponibilidade, product_id))
        else:
            cursor.execute('''
                INSERT INTO produtos (nome, descricao, preco, disponibilidade)
                VALUES (?, ?, ?, ?)
            ''', (nome, descricao, preco, disponibilidade))

        conn.commit()
        conn.close()
        messagebox.showinfo("Salvo!", "Produto salvo com sucesso!")
        show_produtos()
        form.destroy()

    form = tk.Toplevel(root)
    form.title("Adicionar Produto" if not product_id else "Editar Produto")

    tk.Label(form, text="Nome do Produto").grid(row=0, column=0)
    entry_nome = tk.Entry(form)
    entry_nome.grid(row=0, column=1)

    tk.Label(form, text="Descricao").grid(row=1, column=0)
    entry_descricao = tk.Entry(form)
    entry_descricao.grid(row=1, column=1)

    tk.Label(form, text="Preco").grid(row=2, column=0)
    entry_preco = tk.Entry(form)
    entry_preco.grid(row=2, column=1)

    tk.Label(form, text="Disponível para venda").grid(row=3, column=0)
    var_disponibilidade = tk.IntVar()
    tk.Radiobutton(form, text="Sim", variable=var_disponibilidade, value=1).grid(row=3, column=1)
    tk.Radiobutton(form, text="Não", variable=var_disponibilidade, value=0).grid(row=3, column=2)

    if product_id:
        conn = sqlite3.connect('produtos.db')
        cursor = conn.cursor()
        cursor.execute('SELECT nome, descricao, preco, disponibilidade FROM produtos WHERE id = ?', (product_id,))
        produto = cursor.fetchone()
        conn.close()

        if produto:
            entry_nome.insert(0, produto[0])
            entry_descricao.insert(0, produto[1])
            entry_preco.insert(0, produto[2])
            var_disponibilidade.set(produto[3])

    tk.Button(form, text="Salvar", command=save_produto).grid(row=4, column=0, columnspan=2)

# funcao para mostrar os produtos cadastrados
def show_produtos():
    for widget in list_frame.winfo_children():
        widget.destroy()

    conn = sqlite3.connect('produtos.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id, nome, preco FROM produtos ORDER BY preco ASC')
    produtos = cursor.fetchall()
    conn.close()

    for index, (product_id, nome, preco) in enumerate(produtos):
        tk.Label(list_frame, text=nome).grid(row=index, column=0)
        tk.Label(list_frame, text=f"R${preco:.2f}").grid(row=index, column=1)
        tk.Button(list_frame, text="Editar", command=lambda pid=product_id: add_or_edit_produto(pid)).grid(row=index, column=2)
        tk.Button(list_frame, text="Excluir", command=lambda pid=product_id: delete_produto(pid)).grid(row=index, column=3)

# funcao para excluir um produto
def delete_produto(product_id):
    conn = sqlite3.connect('produtos.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM produtos WHERE id = ?', (product_id,))
    conn.commit()
    conn.close()
    messagebox.showinfo("Sucesso", "Produto excluido com sucesso!")
    show_produtos()

# Configuracaoo da interface grafica principal
root = tk.Tk()
root.title("Gerenciamento de Produtos")
root.geometry("500x300")

# Inicializa o banco de dados
init_db()

# Frame de botoes
btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Adicionar Produto", command=lambda: add_or_edit_produto()).grid(row=0, column=0, padx=5)

# Frame da lista de produtos
list_frame = tk.Frame(root)
list_frame.pack(pady=10)
show_produtos()

# Inicia o loop principal da interface grafica
root.mainloop()
