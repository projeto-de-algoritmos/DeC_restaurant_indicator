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

        result_window = tk.Toplevel(window)
        result_window.title("Resultado")

        if inversions <= 2:
            messagebox.showinfo("Recomendação", "Você tem uma ótima escolha!")
        elif inversions <= 5:
            messagebox.showinfo("Recomendação", "Você tem uma boa escolha!")
        else:
            messagebox.showinfo("Recomendação", "Você pode considerar outras opções.")
    except ValueError:
        messagebox.showerror("Erro", "Insira números inteiros separados por espaço.")

# Criar a janela principal
window = tk.Tk()
window.title("Contagem de Inversões")

# Criar a tabela fixa
table_label = tk.Label(window, text="Tabela de Avaliações")
table_label.pack()

table = ttk.Treeview(window, columns=("Numbers"))
table.heading("#0", text="ID")
table.heading("Numbers", text="Número")
table.pack()

# Adicionar itens à tabela
table.insert("", "end", text="1", values=(4,))
table.insert("", "end", text="2", values=(2,))
table.insert("", "end", text="3", values=(1,))
table.insert("", "end", text="4", values=(3,))
table.insert("", "end", text="5", values=(5,))

# Criar o campo de entrada
input_label = tk.Label(window, text="Insira um vetor de números inteiros separados por espaço:")
input_label.pack()

input_entry = tk.Entry(window)
input_entry.pack()

# Botão para processar o vetor
process_button = tk.Button(window, text="Processar", command=process_input)
process_button.pack()

# Executar a janela principal
window.mainloop()
