import tkinter as tk
# Import the logic 
from defang_code_p import defang_url

def run_defang():
    url = url_entry.get()
    defanged = defang_url(url)
    result_label.config(text=f"Defanged URL:\n{defanged}")


# GUI setup
root = tk.Tk()
root.title("URL Defanger")
root.geometry("400x200")

tk.Label(root, text="Enter URL:").pack(pady=5)
url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=5)

tk.Button(root, text="Defang", command=run_defang).pack(pady=10)

result_label = tk.Label(root, text="" ,wraplength=380, justify="left")
result_label.pack(pady=10)

root.mainloop()


