import tkinter as tk

def binary_to_text(binary_str):
    text = ""
    binary_chunks = [binary_str[i:i+8] for i in range(0, len(binary_str), 8)]
    for chunk in binary_chunks:
        decimal_value = int(chunk, 2)
        text += chr(decimal_value)
    return text

def text_to_binary(text):
    binary_str = ""
    for char in text:
        decimal_value = ord(char)
        binary_str += format(decimal_value, '08b')
    return binary_str

def convert(event=None):
    input_data = input_entry.get().replace(" ", "")  #Remove spaces from input
    output_data = ""

    if all(char in '01' for char in input_data):
        try:
            output_data = binary_to_text(input_data)
        except ValueError:
            output_data = "Invalid binary input. Please enter a valid binary string."

    #Check if the input contains any character other than 0s and 1s
    elif any(char not in '01' for char in input_data):
        output_data = text_to_binary(input_data)

    #If neither binary nor text input, show an error message
    else:
        output_data = "Invalid input. Please enter either binary or text."

    output_entry.delete(0, tk.END)
    output_entry.insert(0, output_data)

def copy_to_clipboard():
    output_data = output_entry.get()
    root.clipboard_clear()
    root.clipboard_append(output_data)

root = tk.Tk()
root.title("Binary and Text Converter")

input_label = tk.Label(root, text="Input:")
input_label.grid(row=0, column=0, padx=5, pady=5)

input_entry = tk.Entry(root, width=40)
input_entry.grid(row=0, column=1, columnspan=2, padx=5, pady=5)

output_label = tk.Label(root, text="Output:")
output_label.grid(row=1, column=0, padx=5, pady=5)

output_entry = tk.Entry(root, width=40)
output_entry.grid(row=1, column=1, columnspan=2, padx=5, pady=5)

convert_button = tk.Button(root, text="Convert", command=convert)
convert_button.grid(row=2, column=0, padx=5, pady=5)

copy_button = tk.Button(root, text="Copy", command=copy_to_clipboard)
copy_button.grid(row=2, column=1, padx=5, pady=5)

clear_button = tk.Button(root, text="Clear", command=lambda: (input_entry.delete(0, tk.END), output_entry.delete(0, tk.END)))
clear_button.grid(row=2, column=2, padx=5, pady=5)

root.bind('<Return>', convert)

root.mainloop()

