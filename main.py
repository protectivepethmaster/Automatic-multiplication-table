import random
import tkinter as tk
from tkinter import ttk, messagebox

# ค่าคงที่
MAX_BASE = 100
MAX_END = 100



def generate_table_lines(number, start_i, end_i):
    header = f"--- ตารางสูตรคูณสำหรับแม่ {number} (1 ถึง {end_i}) ---"
    lines = [header]
    for i in range(start_i, end_i + 1):
        lines.append(f"{number:>3} x {i:>3} = {number * i:>5}")
    lines.append("-" * 34)
    return lines


class MultiplicationGUI:
    def __init__(self, root):
        self.root = root
        root.title("โปรแกรมตารางสูตรคูณ (GUI แบบง่าย)")
        root.geometry("760x520")

        # กรอบซ้ายสำหรับการตั้งค่าและปุ่ม
        left = ttk.Frame(root, padding=(10, 10))
        left.pack(side=tk.LEFT, fill=tk.Y)

        # กรอบขวาสำหรับแสดงผล
        right = ttk.Frame(root, padding=(10, 10))
        right.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # --- Widgets ด้านซ้าย ---
        ttk.Label(left, text="ตั้งค่า (กรอกตัวเลขเป็นจำนวนเต็ม)", font=(None, 11, 'bold')).pack(pady=(0, 8))

        # แม่ (single)
        ttk.Label(left, text="แม่ (สำหรับแสดงตาราง):").pack(anchor=tk.W)
        self.entry_base = ttk.Entry(left, width=12)
        self.entry_base.insert(0, "7")
        self.entry_base.pack(pady=(0, 6))

        # ตัวคูณสิ้นสุด
        ttk.Label(left, text="ตัวคูณสิ้นสุด:").pack(anchor=tk.W)
        self.entry_end = ttk.Entry(left, width=12)
        self.entry_end.insert(0,"12")
        self.entry_end.pack(pady=(0, 8))

        # ช่วงแม่
        ttk.Label(left, text="ช่วงแม่ (เริ่ม - สิ้นสุด):").pack(anchor=tk.W)
        range_frame = ttk.Frame(left)
        range_frame.pack(pady=(0, 6))
        self.entry_range_start = ttk.Entry(range_frame, width=6)
        self.entry_range_start.insert(0, "2")
        self.entry_range_start.pack(side=tk.LEFT)
        ttk.Label(range_frame, text=" - ").pack(side=tk.LEFT)
        self.entry_range_end = ttk.Entry(range_frame, width=6)
        self.entry_range_end.insert(0, "5")
        self.entry_range_end.pack(side=tk.LEFT)

        # จำนวนข้อสำหรับ quiz
        ttk.Label(left, text="จำนวนข้อ (quiz):").pack(anchor=tk.W)
        self.entry_quiz_count = ttk.Entry(left, width=12)
        self.entry_quiz_count.insert(0, "5")
        self.entry_quiz_count.pack(pady=(0, 8))

        # ปุ่มการทำงาน
        ttk.Button(left, text="แสดงตาราง (แม่เดียว)", command=self.show_table).pack(fill=tk.X, pady=4)
        ttk.Button(left, text="แสดงช่วงแม่", command=self.show_range).pack(fill=tk.X, pady=4)
        ttk.Button(left, text="โหมดแบบทดสอบ (Quiz)", command=self.quiz_mode).pack(fill=tk.X, pady=4)
        ttk.Button(left, text="ล้างหน้าต่างผลลัพธ์", command=self.clear_output).pack(fill=tk.X, pady=4)
        ttk.Button(left, text="ช่วยเหลือ / Help", command=self.show_help).pack(fill=tk.X, pady=4)
        ttk.Button(left, text="ออก", command=root.quit).pack(fill=tk.X, pady=12)

        # --- Widgets ด้านขวา (ผลลัพธ์) ---
        ttk.Label(right, text="ผลลัพธ์:", font=(None, 11, 'bold')).pack(anchor=tk.W)
        self.output = tk.Text(right, wrap=tk.NONE, font=("Consolas", 11))
        self.output.pack(fill=tk.BOTH, expand=True)

        # ให้มี scrollbars
        ysb = ttk.Scrollbar(self.output, orient=tk.VERTICAL, command=self.output.yview)
        xsb = ttk.Scrollbar(self.output, orient=tk.HORIZONTAL, command=self.output.xview)
        self.output.configure(yscrollcommand=ysb.set, xscrollcommand=xsb.set)
        ysb.pack(side=tk.RIGHT, fill=tk.Y)
        xsb.pack(side=tk.BOTTOM, fill=tk.X)

    # ---- ฟังก์ชันช่วยเหลือและแสดงผล ----
    def append_output(self, lines):
        if isinstance(lines, str):
            self.output.insert(tk.END, lines + "\n")
        else:
            for line in lines:
                self.output.insert(tk.END, line + "\n")
        # เลื่อนลงล่างสุด
        self.output.see(tk.END)

    def clear_output(self):
        self.output.delete("1.0", tk.END)

    def show_help(self):
        help_text = (
            "คำสั่งและคำอธิบาย:\n"
            "- ใส่ค่าในช่องแล้วกดปุ่มที่ต้องการ\n"
            "- แสดงตาราง: แสดงตารางแม่เดียว\n"
            "- แสดงช่วงแม่: แสดงตารางของแม่ตั้งแต่ 'ช่วงเริ่ม' ถึง 'ช่วงสิ้นสุด'\n"
            "- โหมดแบบทดสอบ: จะถามโจทย์ตามช่วงที่กำหนด (ตอบใน dialog)\n"
            "หมายเหตุ: กรุณากรอกจำนวนเต็มในช่วงที่กำหนด (1-100)\n"
        )
        messagebox.showinfo("ช่วยเหลือ", help_text)

    # ---- ตรวจสอบค่าเข้า (เบื้องต้น) ----
    def _get_int_from_entry(self, entry_widget, name, min_val=1, max_val=100):
        raw = entry_widget.get().strip()
        if raw == "":
            raise ValueError(f"กรุณากรอกช่อง {name}")
        try:
            val = int(raw)
        except ValueError:
            raise ValueError(f"{name} ต้องเป็นจำนวนเต็ม")
        if val < min_val or val > max_val:
            raise ValueError(f"{name} ต้องอยู่ระหว่าง {min_val} ถึง {max_val}")
        return val

    # ---- ปุ่ม: แสดงตาราง (แม่เดียว) ----
    def show_table(self):
        try:
            base = self._get_int_from_entry(self.entry_base, "แม่", 1, MAX_BASE)
            end = self._get_int_from_entry(self.entry_end, "ตัวคูณสิ้นสุด", 1, MAX_END)
        except ValueError as e:
            messagebox.showwarning("ค่าไม่ถูกต้อง", str(e))
            return
        lines = generate_table_lines(base, 1, end)
        self.append_output(lines)

    # ---- ปุ่ม: แสดงช่วงแม่ ----
    def show_range(self):
        try:
            start_b = self._get_int_from_entry(self.entry_range_start, "ช่วงเริ่ม", 1, MAX_BASE)
            end_b = self._get_int_from_entry(self.entry_range_end, "ช่วงสิ้นสุด", 1, MAX_BASE)
            end = self._get_int_from_entry(self.entry_end, "ตัวคูณสิ้นสุด", 1, MAX_END)
        except ValueError as e:
            messagebox.showwarning("ค่าไม่ถูกต้อง", str(e))
            return
        if start_b > end_b:
            start_b, end_b = end_b, start_b

        for b in range(start_b, end_b + 1):
            lines = generate_table_lines(b, 1, end)
            self.append_output(lines)
            self.append_output("")

    # ---- ปุ่ม: โหมดแบบทดสอบ ----
    def quiz_mode(self):
        try:
            base_min = self._get_int_from_entry(self.entry_range_start, "แม่ต่ำสุด", 1, MAX_BASE)
            base_max = self._get_int_from_entry(self.entry_range_end, "แม่สูงสุด", 1, MAX_BASE)
            if base_min > base_max:
                base_min, base_max = base_max, base_min
            end_max = self._get_int_from_entry(self.entry_end, "ตัวคูณสูงสุด", 1, MAX_END)
            total_q = self._get_int_from_entry(self.entry_quiz_count, "จำนวนข้อ", 1, 200)
        except ValueError as e:
            messagebox.showwarning("ค่าไม่ถูกต้อง", str(e))
            return

        score = 0
        asked = 0
        lines = ["--- ผลการทำแบบทดสอบ ---"]

        for i in range(total_q):
            a = random.randint(base_min, base_max)
            b = random.randint(1, end_max)
            # ใช้ simple dialog (askstring) เพื่อให้ผู้ใช้ตอบ
            ans = tk.simpledialog.askstring("คำตอบ", f"{a} x {b} = (พิมพ์ 'ออก' เพื่อยกเลิก)")
            if ans is None or ans.lower() in {"ออก", "quit", "exit"}:
                messagebox.showinfo("ออก", "ยกเลิกแบบทดสอบ")
                break
            try:
                ans_int = int(ans)
                correct = a * b
                is_right = (ans_int == correct)
                score += int(is_right)
                result_str = "ถูก" if is_right else f"ผิด (คำตอบที่ถูก: {correct})"
                messagebox.showinfo("ผลคำตอบ", result_str)
                lines.append(f"{a:>3} x {b:>3} = {ans_int:>5}  -> {result_str}")
                asked += 1
            except ValueError:
                messagebox.showwarning("ไม่รับคำตอบ", "กรุณาป้อนจำนวนเต็มเท่านั้น (คำถามนี้จะถูกข้าม)")
                lines.append(f"{a:>3} x {b:>3} = (ไม่รับคำตอบ)")

        if asked > 0:
            percent = (score / asked) * 100
            summary = f"สรุปคะแนน: {score}/{asked} ({percent:.1f}%)"
            lines.append(summary)

        # แสดงผลสรุปในพื้นที่ขวา
        self.append_output(lines)


if __name__ == '__main__':
    root = tk.Tk()
    import tkinter.simpledialog
    app = MultiplicationGUI(root)
    root.mainloop()
