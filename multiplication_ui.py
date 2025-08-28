import tkinter as tk

def show_table():
    try:
        num = int(entry_num.get())         
        limit = int(entry_limit.get())     
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, f"ตารางสูตรคูณแม่ {num}\n")
        result_text.insert(tk.END, "-"*25 + "\n")
        for i in range(1, limit + 1):
            result_text.insert(tk.END, f"{num} x {i} = {num*i}\n")
    except ValueError:
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, "กรุณากรอกตัวเลขที่ถูกต้อง!")


root = tk.Tk()
root.title("ตารางสูตรคูณอัตโนมัติ")
root.geometry("350x450")


label_num = tk.Label(root, text="กรอกแม่สูตรคูณ:", font=("Tahoma", 12))
label_num.pack(pady=5)
entry_num = tk.Entry(root, font=("Tahoma", 12))
entry_num.pack()


label_limit = tk.Label(root, text="ต้องการคูณถึงเลข:", font=("Tahoma", 12))
label_limit.pack(pady=5)
entry_limit = tk.Entry(root, font=("Tahoma", 12))
entry_limit.insert(0, "12")  
entry_limit.pack()


button = tk.Button(root, text="แสดงตารางสูตรคูณ", command=show_table, font=("Tahoma", 12))
button.pack(pady=10)


result_text = tk.Text(root, height=15, width=35, font=("Consolas", 11))
result_text.pack(pady=10)

root.mainloop()
