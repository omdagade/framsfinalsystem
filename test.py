import tkinter as tk

def on_radio_button_change():
    selected_value.set("Selected Option: " + str(selected_radio.get()))

root = tk.Tk()
root.title("Tkinter Radio Buttons Example")

# Variable to store the selected radio button value
selected_radio = tk.IntVar()

# Create and place radio buttons
radio_button1 = tk.Radiobutton(root, text="Option 1", variable=selected_radio, value=1, command=on_radio_button_change)
radio_button1.pack(pady=5)

radio_button2 = tk.Radiobutton(root, text="Option 2", variable=selected_radio, value=2, command=on_radio_button_change)
radio_button2.pack(pady=5)

radio_button3 = tk.Radiobutton(root, text="Option 3", variable=selected_radio, value=3, command=on_radio_button_change)
radio_button3.pack(pady=5)

# Label to display the selected radio button value
selected_value = tk.StringVar()
selected_label = tk.Label(root, textvariable=selected_value)
selected_label.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
