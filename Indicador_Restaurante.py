import tkinter as tk
from tkinter import ttk, messagebox

def merge_sort(arr):
    if len(arr) <= 1:
        return arr, 0

    mid = len(arr) // 2
    left, inv_left = merge_sort(arr[:mid])
    right, inv_right = merge_sort(arr[mid:])
    merged, inv_merge = merge(left, right)

    return merged, inv_left + inv_right + inv_merge

def merge(left, right):
    merged = []
    inv_count = 0
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            inv_count += len(left) - i
            j += 1

    while i < len(left):
        merged.append(left[i])
        i += 1

    while j < len(right):
        merged.append(right[j])
        j += 1

    return merged, inv_count

def process_input():
    user_input = input_entry.get()
    try:
        numbers = list(map(int, user_input.split()))
        sorted_numbers, inversions = merge_sort(numbers)


        if inversions <= 1:
            messagebox.showinfo("Recomendação - Restaurante Mexicano", "De acordo com suas preferencias o restaurante indicado a você e o Restaurante Mexicano!! \n\nAlgumas opções:\n\n"
            + "nome: Si Senor\n link: https://www.sisenor.com.br/\n\n nome: El Paso Texas\n link: https://www.elpaso.com.br/\n\n nome: Hermanito\n link: https://www.instagram.com/hermanito_asanorte")
        elif inversions <= 3:
            messagebox.showinfo("Recomendação - Restaurante Churrascaria", "De acordo com suas preferencias o restaurante indicado a você e o Restaurante Churrascaria!! \n\nAlgumas opções:\n\n"
            + "nome: Potência do Sul\n link: https://potenciadosul.com.br/\n\n nome: Fogo de Chão Brasília\n link: https://fogodechao.com.br/location/brasilia/\n\n nome: Sal e Brasa Brasília\n link: https://salebrasa.com.br/")
        elif inversions <= 5:
            messagebox.showinfo("Recomendação - Restaurante Brasileiro", "De acordo com suas preferencias o restaurante indicado a você e o Restaurante Brasileiro!! \n\nAlgumas opções:\n\n"
            + "nome: Mangai\n link: https://mangai.com.br/\n\n nome: Tapera Brasileira Restaurante\n link: https://restaurantguru.com.br/Tapera-Brasileira-Brasilia\n\n nome: Fogão Mineiro\n link: https://www.fogaomineiro.com.br/")
        elif inversions <= 7:
            messagebox.showinfo("Recomendação - Restaurante Italiano", "De acordo com suas preferencias o restaurante indicado a você e o Restaurante Italiano!! \n\nAlgumas opções:\n\n"
            + "nome: Papa Cucina\n link: https://www.instagram.com/papacucina_/\n\n nome: Villa Tevere\n link: https://www.villatevere.com.br/\n\n nome: A Mano\n link: https://www.instagram.com/amanorestaurante/" )
        elif inversions <= 8:
            messagebox.showinfo("Recomendação - Restaurante Japones", "De acordo com suas preferencias o restaurante indicado a você e o Restaurante Japones!!\n\nAlgumas opções:\n\n"
            +"nome: Nippon\n link: https://nipponbrasilia.com.br/\n\n nome: Restaurante Kojima\n link: https://www.restaurantekojima.com.br/\n\n nome: Shoio Sushi Lounge\n link: https://www.shoiosushi.com/" )
        else:
            messagebox.showinfo("Recomendação - Restaurante Indiano", "De acordo com suas preferencias o restaurante indicado a você e o Restaurante Indiano!!\n\nAlgumas opções:\n\n"
            + "nome: Indian House\n link: https://www.hubt.com.br/indian-house/\n\n nome: Namaste Restaurante\n link: https://www.ifood.com.br/delivery/brasilia-df/namaste-indian-restaurante-asa-norte/\n\n nome: Indian Lounge\n link: https://www.facebook.com/indianloungebsb/" )
    except ValueError:
        messagebox.showerror("Erro", "Insira números inteiros separados por espaço.")

# Criar a janela principal
window = tk.Tk()
window.title("Indicador de restaurante")

# Criar a tabela fixa
table_label = tk.Label(window, text="Tabela de Identificação")
table_label.pack()

table = ttk.Treeview(window, columns=("Numbers"), height=7) 
table.heading("#0", text="     ID ")
table.heading("Numbers", text="    Ingrediente ")

# Centralizar os valores
table.column("#0", anchor="center")
table.column("Numbers", anchor="center")

table.pack()

# Adicionar itens à tabela
table.insert("", "end", text="", values=("",))
table.insert("", "end", text="1", values=("Pimenta",))
table.insert("", "end", text="2", values=("Legumes",))
table.insert("", "end", text="3", values=("Carne",))
table.insert("", "end", text="4", values=("Massas",))
table.insert("", "end", text="5", values=("Arroz",))

# Criar o campo de entrada
input_label = tk.Label(window, text="Insira a ordem de IDs de acordo com sua \npreferência do que não pode faltar no seu prato: (separe por espaço)")
input_label.pack()

input_entry = tk.Entry(window)
input_entry.pack()

# Botão para processar o vetor
process_button = tk.Button(window, text="Processar", command=process_input)
process_button.pack()

# Executar a janela principal
window.mainloop()
