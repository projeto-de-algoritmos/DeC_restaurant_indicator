import tkinter as tk
from tkinter import messagebox


def count_inversions(user_array, pre_established_arrays):
    result = ""
    min_inversions = float('inf')
    min_index = -1

    for i, pre_established_array in enumerate(pre_established_arrays):
        inversions = 0
        for j in range(len(user_array)):
            for k in range(j + 1, len(user_array)):
                if user_array[j] > user_array[k]:
                    inversions += 1

        result += f"Vetor {i + 1}: Número de inversões = {inversions}\n"

        if inversions < min_inversions:
            min_inversions = inversions
            min_index = i

    result += f"\nVetor com o menor número de inversões: Vetor {min_index + 1}\n"

    messagebox.showinfo("Contagem de Inversões", result)


def on_submit():
    user_input = entry.get()
    user_array = list(map(int, user_input.split(',')))

    count_inversions(user_array, [pre_established_array1, pre_established_array2, pre_established_array3])


# Vetores pré-estabelecidos
pre_established_array1 = [1, 2, 3, 4, 5]
pre_established_array2 = [5, 4, 3, 2, 1]
pre_established_array3 = [2, 4, 1, 3, 5]

# Criação da janela
window = tk.Tk()
window.title("Contagem de Inversões")
window.geometry("300x300")

# Rótulo e campo de entrada
label = tk.Label(window, text="Insira o vetor (separado por vírgulas):")
label.pack()
entry = tk.Entry(window)
entry.pack()

# Botão de submissão
submit_button = tk.Button(window, text="Contar Inversões", command=on_submit)
submit_button.pack()

# Execução da janela
window.mainloop()