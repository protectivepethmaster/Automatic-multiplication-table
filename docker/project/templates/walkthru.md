# README: โปรแกรมตารางสูตรคูณ (GUI)

**สรุปสั้นๆ:**
โปรเจคนี้เป็นโปรแกรม GUI แบบง่ายด้วย `tkinter` สำหรับแสดงตารางสูตรคูณ แสดงช่วงของแม่ค้าต่าง ๆ และมีโหมดแบบทดสอบ (Quiz) เพื่อฝึกคำนวณ การใช้งานหลักๆ ทำได้ผ่านช่องกรอกค่าและปุ่มในหน้าต่าง

---

# ข้อกำหนด (Requirements)
- Python 3.8+ (หากใช้ Python เวอร์ชันใหม่กว่า 3.8 ก็ใช้ได้)
- โมดูล `tkinter` (โดยปกติจะมาพร้อม Python บน Windows/macOS; บน Linux อาจต้องติดตั้งแพ็กเกจ `python3-tk`)

**คำสั่งรัน:**
```bash
python multiplication_gui.py
```
(สมมติไฟล์โค้ดชื่อ `multiplication_gui.py`)

---

# โครงสร้างไฟล์
- `multiplication_gui.py` — โค้ดโปรแกรมทั้งหมด (GUI + ฟังก์ชันช่วยเหลือ)

---

# ฟีเจอร์หลัก
- แสดงตารางสูตรคูณของ "แม่" เดียว
- แสดงตารางสูตรคูณสำหรับช่วงแม่ (เช่น แม่ 2 ถึง 5)
- โหมดแบบทดสอบ (Quiz) สุ่มโจทย์ให้ตอบและสรุปคะแนน
- ปุ่มล้างผลลัพธ์ และปุ่มช่วยเหลือ (Help)

---

# คำอธิบายโค้ด (complete walk-through)

> ด้านล่างอธิบายเป็นหมวดๆ ตามฟังก์ชันและส่วนประกอบสำคัญของโค้ด

## ค่าคงที่
```python
MAX_BASE = 100
MAX_END = 100
```
- จำกัดค่าสูงสุดสำหรับ "แม่" และตัวคูณ เพื่อป้องกันการป้อนค่ามหาศาลที่อาจทำให้โปรแกรมค้าง

## ฟังก์ชัน `generate_table_lines(number, start_i, end_i)`
- ทำหน้าที่สร้างรายการ `lines` ซึ่งเป็น `list` ของบรรทัดข้อความที่จะแสดงในช่องผลลัพธ์
- รูปแบบบรรทัด: `"{แม่:>3} x {ตัวคูณ:>3} = {ผลลัพธ์:>5}"`
- ส่งกลับเป็น `list` (ทำให้เรียกแทรกหลายบรรทัดได้สะดวกด้วย `append_output`)

ตัวอย่างผลลัพธ์ (ตัวอย่างบรรทัด):
```
--- ตารางสูตรคูณสำหรับแม่ 7 (1 ถึง 12) ---
  7 x   1 =     7
  7 x   2 =    14
...
----------------------------------
```

## คลาส `MultiplicationGUI`
คลาสนี้เตรียม GUI ทั้งหมดและจัดการ event ของปุ่ม

### เมธอด `__init__(self, root)`
- สร้างหน้าต่างหลัก กำหนดขนาด `root.geometry("760x520")`
- แบ่ง layout เป็น 2 คอลัมน์: `left` (ตั้งค่าและปุ่ม) และ `right` (แสดงผล)
- ช่องกรอกข้อมูล (Entry) ที่สำคัญ:
  - `entry_base` — แม่ (ค่าเริ่มต้น 7)
  - `entry_end` — ตัวคูณสิ้นสุด (ค่าเริ่มต้น 12)
  - `entry_range_start`, `entry_range_end` — ช่วงของแม่ (ตัวอย่าง: 2 - 5)
  - `entry_quiz_count` — จำนวนข้อสำหรับโหมด Quiz
- ปุ่มหลัก: แสดงตาราง (แม่เดียว), แสดงช่วงแม่, โหมดแบบทดสอบ (Quiz), ล้างผล, ช่วยเหลือ, ออก
- พื้นที่แสดงผลเป็น `tk.Text` พร้อม scrollbars

> หมายเหตุเชิงเทคนิค: ในโค้ดตัวอย่าง scrollbars ถูกสร้างโดยใช้ parent เป็น `self.output` (คือสร้าง `ttk.Scrollbar(self.output, ...)`) ซึ่งทำงานได้ แต่รูปแบบที่แนะนำปกติคือวาง `Text` และ `Scrollbar` เป็นพี่น้อง (sibling) ภายใน `Frame` แล้วเชื่อมกันด้วย `command` และ `yscrollcommand` — จะยกตัวอย่างวิธีแก้ไขในส่วนปรับปรุง

### เมธอด `append_output(self, lines)`
- ถ้า `lines` เป็น `str` จะต่อบรรทัดเดียว หากเป็น `list` จะวนเพิ่มทีละบรรทัดลงใน `Text`
- ใช้ `self.output.see(tk.END)` เพื่อเลื่อนลงมาด้านล่างสุดอัตโนมัติ

### เมธอด `clear_output(self)`
- ล้างข้อความทั้งหมดใน `Text` ด้วย `self.output.delete("1.0", tk.END)`

### เมธอด `show_help(self)`
- แสดงคำอธิบายการใช้โปรแกรมผ่าน `messagebox.showinfo` (ข้อความช่วยเหลือ)

### เมธอด `_get_int_from_entry(self, entry_widget, name, min_val=1, max_val=100)`
- ดึงค่า `str` จาก `Entry` แล้วพยายามแปลงเป็น `int`
- หากช่องว่าง, ไม่ใช่จำนวนเต็ม, หรือนอกช่วง จะ `raise ValueError` พร้อมข้อความที่เข้าใจง่าย
- เมธอดนี้เป็นจุดศูนย์กลางสำหรับตรวจสอบค่าเข้า (input validation)

### เมธอด `show_table(self)`
- อ่านค่า `base` และ `end` โดยเรียก `_get_int_from_entry`
- หากค่าถูกต้อง จะเรียก `generate_table_lines` แล้ว `append_output`
- หากไม่ถูกต้อง จะแสดง `messagebox.showwarning` และยกเลิกการทำงาน

### เมธอด `show_range(self)`
- อ่านค่า `start_b`, `end_b` (ช่วงแม่) และ `end` (ตัวคูณสิ้นสุด)
- สลับค่าเริ่ม/สิ้นสุดถ้า user ใส่กลับกัน
- วน `for b in range(start_b, end_b + 1)` เรียก `generate_table_lines` และแสดงทีละแม่

### เมธอด `quiz_mode(self)`
- อ่านขอบเขตแม่ (`base_min`, `base_max`) และ `end_max` และจำนวนคำถาม `total_q`
- สุ่มคำถาม `total_q` ข้อ (โดยสุ่มแม่ `a` และตัวคูณ `b`)
- ใช้ `tk.simpledialog.askstring` ขอคำตอบจากผู้ใช้ (ผู้ใช้สามารถพิมพ์คำว่า `ออก` หรือ `quit` เพื่อยกเลิก)
- ตรวจคำตอบว่าเป็นจำนวนเต็มและเทียบกับคำตอบที่ถูกต้อง แล้วเก็บคะแนน
- หลังทำคำถามจบหรือยกเลิก จะแสดงสรุปคะแนนในช่องผลลัพธ์

**ข้อสังเกต:** โค้ดนำเข้า `tkinter.simpledialog` ภายใน `if __name__ == '__main__':` แต่ในเมธอดใช้ `tk.simpledialog.askstring` — การ import นี้เกิดขึ้นก่อนการสร้างแอปใน `__main__` ดังนั้นโปรแกรมทำงานตามปกติ แต่ถ้าต้องการความชัดเจน แนะนำ import `tkinter.simpledialog as simpledialog` ด้านบนของไฟล์ (top-level)

---

# ตัวอย่างการใช้งานจริง (ตัวอย่างอินพุต/เอาต์พุต)

**อินพุตตัวอย่างใน GUI:**
- แม่ = `7`
- ตัวคูณสิ้นสุด = `12`

**เอาต์พุตตัวอย่างใน Text widget:**
```
--- ตารางสูตรคูณสำหรับแม่ 7 (1 ถึง 12) ---
  7 x   1 =     7
  7 x   2 =    14
  7 x   3 =    21
  7 x   4 =    28
  7 x   5 =    35
  7 x   6 =    42
  7 x   7 =    49
  7 x   8 =    56
  7 x   9 =    63
  7 x  10 =    70
  7 x  11 =    77
  7 x  12 =    84
----------------------------------
```

---

# ปรับแต่งแนะนำ / ข้อเสนอการพัฒนา (Ideas & Improvements)
- **วาง Scrollbars ให้ถูกตำแหน่ง:** สร้าง `Frame` สำหรับ `Text` และ `Scrollbar` เพื่อ layout ให้เหมาะสม (ตัวอย่างโค้ดแนะนำในส่วนตัวอย่างด้านล่าง)
- **บันทึกผลลัพธ์เป็นไฟล์** (export .txt)
- **เก็บผลการทำ Quiz ครั้งล่าสุด** (timestamp + เก็บเป็นไฟล์ / JSON)
- **ปรับ UI ให้ responsive:** ใช้ `grid` แทน `pack` สำหรับ layout ที่ยืดหยุ่นกว่า
- **ใช้ `StringVar` กับ `Entry`** เพื่อง่ายต่อการเชื่อมข้อมูลและทดสอบ
- **เพิ่มตัวเลือกความยากของ Quiz** (เช่น ตัวคูณสูงสุด, เวลาให้ตอบ)
- **แพ็กเกจเป็นไฟล์เดียว (exe)** โดยใช้ `PyInstaller` (`pyinstaller --onefile --windowed multiplication_gui.py`)
- **Localization / i18n:** แยกข้อความ UI ออกเป็นไฟล์แปลภาษา หากต้องการรองรับหลายภาษา

**ตัวอย่างการแก้ไขตำแหน่ง scrollbars (แนะนำ):**
```python
frame_output = ttk.Frame(right)
frame_output.pack(fill=tk.BOTH, expand=True)
self.output = tk.Text(frame_output, wrap=tk.NONE, font=("Consolas", 11))
self.output.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
ysb = ttk.Scrollbar(frame_output, orient=tk.VERTICAL, command=self.output.yview)
ysb.pack(side=tk.RIGHT, fill=tk.Y)
xsb = ttk.Scrollbar(right, orient=tk.HORIZONTAL, command=self.output.xview)
xsb.pack(side=tk.BOTTOM, fill=tk.X)
self.output.configure(yscrollcommand=ysb.set, xscrollcommand=xsb.set)
```

---

# ปัญหาที่อาจเจอ (Troubleshooting)
- **ImportError: No module named 'tkinter'**
  - Linux (Debian/Ubuntu): `sudo apt install python3-tk`
  - Fedora: `sudo dnf install python3-tkinter`
  - Arch: `sudo pacman -S tk`
  - Windows/macOS: โดยปกติมาพร้อม Python ที่ติดตั้ง แต่หากใช้ Python จากบางแหล่งที่ตัด Tk ออก อาจต้องเปลี่ยนการติดตั้ง Python
- **โปรแกรมไม่ขึ้นหน้าต่าง/หาไดอะล็อกไม่เจอ:** ตรวจสอบเวอร์ชัน Python ที่ใช้รัน และ environment (virtualenv) ว่าเป็นตัวเดียวกับที่ติดตั้ง tkinter

---

# ข้อมูลเพิ่มเติม
- **Licence:** ใส่ตามที่ต้องการ (เช่น MIT)
- **Contributing:** สร้าง issue / pull request เพื่อเสนอฟีเจอร์หรือแก้บั๊ก

---

ถ้าต้องการ ผมสามารถ:
- แปล README เป็นภาษาอังกฤษ
- เพิ่มตัวอย่างภาพหน้าจอ (ต้องให้ภาพหรือผมสามารถอธิบายว่าจะจับภาพอย่างไร)
- แยก README ให้เป็นไฟล์ README.md พร้อมตัวอย่างไฟล์โค้ด


*ไฟล์นี้เป็น README แบบพร้อมใช้สำหรับนำไปวางใน repository หรือใช้เป็นเอกสารประกอบโปรเจคของคุณได้ทันที*

