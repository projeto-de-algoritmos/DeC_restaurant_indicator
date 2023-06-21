import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.font import Font

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
            messagebox.showinfo("Recomendação - Restaurante Mexicano", "De acordo com suas preferências o restaurante indicado a você e o Restaurante Mexicano!! \n\nAlgumas opções:\n\n"
            + "Nome: Si Senor\n link: https://www.sisenor.com.br/\n\n Nome: El Paso Texas\n Site: https://www.elpaso.com.br/\n\n Nome: Hermanito\n Site: https://www.instagram.com/hermanito_asanorte")
        elif inversions <= 3:
            messagebox.showinfo("Recomendação - Restaurante Churrascaria", "De acordo com suas preferências o restaurante indicado a você e o Restaurante Churrascaria!! \n\nAlgumas opções:\n\n"
            + "Nome: Potência do Sul\n Site: https://potenciadosul.com.br/\n\n Nome: Fogo de Chão Brasília\n Site: https://fogodechao.com.br/location/brasilia/\n\n Nome: Sal e Brasa Brasília\n Site: https://salebrasa.com.br/")
        elif inversions <= 5:
            messagebox.showinfo("Recomendação - Restaurante Brasileiro", "De acordo com suas preferências o restaurante indicado a você e o Restaurante Brasileiro!! \n\nAlgumas opções:\n\n"
            + "Nome: Mangai\n Site: https://mangai.com.br/\n\n Nome: Tapera Brasileira Restaurante\n Site: https://restaurantguru.com.br/Tapera-Brasileira-Brasilia\n\n Nome: Fogão Mineiro\n Site: https://www.fogaomineiro.com.br/")
        elif inversions <= 7:
            messagebox.showinfo("Recomendação - Restaurante Italiano", "De acordo com suas preferências o restaurante indicado a você e o Restaurante Italiano!! \n\nAlgumas opções:\n\n"
            + "Nome: Papa Cucina\n Site: https://www.instagram.com/papacucina_/\n\n Nome: Villa Tevere\n Site: https://www.villatevere.com.br/\n\n Nome: A Mano\n Site: https://www.instagram.com/amanorestaurante/" )
        elif inversions <= 8:
            messagebox.showinfo("Recomendação - Restaurante Japones", "De acordo com suas preferências o restaurante indicado a você e o Restaurante Japones!!\n\nAlgumas opções:\n\n"
            +"Nome: Nippon\n Site: https://nipponbrasilia.com.br/\n\n Nome: Restaurante Kojima\n Site: https://www.restaurantekojima.com.br/\n\n Nome: Shoio Sushi Lounge\n Site: https://www.shoiosushi.com/" )
        else:
            messagebox.showinfo("Recomendação - Restaurante Indiano", "De acordo com suas preferências o restaurante indicado a você e o Restaurante Indiano!!\n\nAlgumas opções:\n\n"
            + "Nome: Indian House\n Site: https://www.hubt.com.br/indian-house/\n\n Nome: Namaste Restaurante\n Site: https://www.ifood.com.br/delivery/brasilia-df/namaste-indian-restaurante-asa-norte/\n\n Nome: Indian Lounge\n Site: https://www.facebook.com/indianloungebsb/" )
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

#espaço vazio
container = tk.Frame(window)
container.pack()
space_label = tk.Label(container, text="", height=1)
space_label.pack()

# Criar o campo de entrada
input_label = tk.Label(window, text="Insira a ordem de IDs de acordo com sua preferência do que não\n pode faltar no seu prato (separe por espaço):", padx=30)
font = Font(family="Helvetica", size=11, weight="bold")
input_label.configure(font=font)
input_label.pack()


input_entry = tk.Entry(window)
input_entry.pack()

#espaço vazio
container = tk.Frame(window)
container.pack()
space_label = tk.Label(container, text="", height=1)
space_label.pack()


# Botão para processar o vetor
process_button = tk.Button(window, text="Indicar Restaurante", command=process_input, bg="green", fg="white", pady=6, padx=10)
process_button.pack()

# Executar a janela principal
window.mainloop()