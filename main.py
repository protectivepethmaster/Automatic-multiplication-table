# multiplication_table_no_save_debugged.py
import random
from datetime import datetime

MAX_BASE = 100        # ค่าสูงสุดของแม่
MAX_END = 100         # ค่าสูงสุดของตัวคูณ
DEFAULT_END = 12      # ค่าปริยายของตัวคูณถึง

# เก็บผลลัพธ์ล่าสุดพร้อม timestamp (list of lines with header)
last_output_lines = []  # each element: string lines
last_output_timestamp = None  # datetime when last_output_lines was set

def display_welcome_message():
    print("--------------------------------------------------")
    print("     ยินดีต้อนรับสู่โปรแกรมตารางสูตรคูณอัตโนมัติ!     ")
    print("--------------------------------------------------")
    print_help()

def print_help():
    print("\nคำสั่งที่ใช้ได้:")
    print(" - แสดงตาราง / show table : แสดงตารางสูตรคูณแม่เดียว")
    print(" - แสดงช่วง  / show range : แสดงตารางหลายแม่ติดกัน")
    print(" - แบบทดสอบ / quiz        : โหมดฝึกทำโจทย์คูณ")
    print(" - ประวัติ   / history     : แสดงผลลัพธ์ล่าสุด")
    print(" - ช่วยเหลือ / help        : แสดงรายการคำสั่ง")
    print(" - ออก      / quit/exit    : ออกจากโปรแกรม")

def get_command_input():
    return input("\nกรุณาเลือกคำสั่ง (พิมพ์ 'ช่วยเหลือ' เพื่อดูทั้งหมด): ").lower().strip()

def generate_table_lines(number: int, start_i: int = 1, end_i: int = DEFAULT_END):
    header = f"--- ตารางสูตรคูณสำหรับแม่ {number} (1 ถึง {end_i}) ---"
    lines = [header]
    for i in range(start_i, end_i + 1):
        lines.append(f"{number:>3} x {i:>3} = {number * i:>5}")
    lines.append("-" * 34)
    return lines

def display_lines(lines):
    """แสดงรายการ lines ทีละบรรทัด แต่ไม่เปลี่ยนแปลง global history โดยอัตโนมัติ."""
    for line in lines:
        print(line)

def ask_int(prompt, min_val=1, max_val=None):
    while True:
        raw = input(prompt).strip()
        try:
            val = int(raw)
            if val < min_val:
                print(f"คำเตือน: ค่าต้องไม่ต่ำกว่า {min_val}")
                continue
            if max_val is not None and val > max_val:
                print(f"คำเตือน: ค่าต้องไม่เกิน {max_val}")
                continue
            return val
        except ValueError:
            print("คำเตือน: กรุณาป้อน 'จำนวนเต็ม' ที่ถูกต้อง")

def display_multiplication_table():
    global last_output_lines, last_output_timestamp
    num = ask_int(f"กรุณาป้อนแม่ (1-{MAX_BASE}): ", 1, MAX_BASE)
    end_number = ask_int(f"กรุณาป้อนตัวคูณสิ้นสุด (1-{MAX_END}): ", 1, MAX_END)
    lines = generate_table_lines(num, 1, end_number)
    display_lines(lines)
    # บันทึกประวัติ: เพิ่ม timestamp และเก็บ lines
    last_output_lines = ["[Saved at " + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "]"] + lines[:]
    last_output_timestamp = datetime.now()

def display_range_tables():
    global last_output_lines, last_output_timestamp
    start_base = ask_int(f"กรุณาป้อนแม่เริ่มต้น (1-{MAX_BASE}): ", 1, MAX_BASE)
    end_base = ask_int(f"กรุณาป้อนแม่สิ้นสุด (1-{MAX_BASE}): ", 1, MAX_BASE)
    if start_base > end_base:
        print(f"สลับช่วงให้ถูกต้อง: {start_base} > {end_base} -> เปลี่ยนเป็น {end_base} ถึง {start_base}")
        start_base, end_base = end_base, start_base
    end_number = ask_int(f"กรุณาป้อนตัวคูณสิ้นสุด (1-{MAX_END}): ", 1, MAX_END)

    all_lines = []
    all_lines.append("[Saved at " + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "]")
    for base in range(start_base, end_base + 1):
        lines = generate_table_lines(base, 1, end_number)
        display_lines(lines)
        all_lines.extend(lines + [""])
    last_output_lines = all_lines[:]
    last_output_timestamp = datetime.now()

def show_history():
    if not last_output_lines:
        print("ยังไม่มีประวัติผลลัพธ์")
        return
    display_lines(last_output_lines)

def quiz_mode():
    global last_output_lines, last_output_timestamp
    print("\n--- โหมดแบบทดสอบสูตรคูณ ---")
    base_min = ask_int(f"แม่ต่ำสุด (1-{MAX_BASE}): ", 1, MAX_BASE)
    base_max = ask_int(f"แม่สูงสุด (1-{MAX_BASE}): ", 1, MAX_BASE)
    if base_min > base_max:
        base_min, base_max = base_max, base_min
    end_max = ask_int(f"ตัวคูณสูงสุด (1-{MAX_END}): ", 1, MAX_END)
    total_q = ask_int("จำนวนข้อแบบทดสอบ (1-50): ", 1, 50)

    score = 0
    asked = 0
    lines = ["--- ผลการทำแบบทดสอบ ---"]
    for _ in range(total_q):
        a = random.randint(base_min, base_max)
        b = random.randint(1, end_max)
        ans_raw = input(f"{a} x {b} = ").strip()
        if ans_raw.lower() in {"ออก", "quit", "exit"}:
            print("ออกจากโหมดแบบทดสอบ")
            break
        try:
            ans = int(ans_raw)
            correct = a * b
            is_right = (ans == correct)
            score += int(is_right)
            result_str = "ถูก " if is_right else f"ผิด  (คำตอบที่ถูก: {correct})"
            print(result_str)
            lines.append(f"{a:>3} x {b:>3} = {ans:>5}  -> {result_str}")
            asked += 1
        except ValueError:
            print("ข้ามข้อ: กรุณาป้อนจำนวนเต็มเท่านั้น")
            lines.append(f"{a:>3} x {b:>3} = (ไม่รับคำตอบ)")

    if asked > 0:
        percent = (score / asked) * 100
        summary = f"สรุปคะแนน: {score}/{asked} ({percent:.1f}%)"
        print(summary)
        lines.append(summary)
        display_lines(lines)
        last_output_lines = ["[Saved at " + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "]"] + lines[:]
        last_output_timestamp = datetime.now()
    else:
        print("ยังไม่มีข้อที่ตอบสำเร็จ")

def normalize_command(cmd: str):
    mapping = {
        "แสดงตาราง": "show_table",
        "show table": "show_table",
        "แสดงช่วง": "show_range",
        "show range": "show_range",
        "แบบทดสอบ": "quiz",
        "quiz": "quiz",
        "ประวัติ": "history",
        "history": "history",
        "ช่วยเหลือ": "help",
        "help": "help",
        "ออก": "quit",
        "quit": "quit",
        "exit": "quit",
    }
    return mapping.get(cmd, None)

def main():
    display_welcome_message()
    while True:
        try:
            cmd = get_command_input()
            action = normalize_command(cmd)
            if action == "quit":
                print("ลาก่อน! ขอบคุณที่ใช้บริการครับ.")
                break
            elif action == "show_table":
                display_multiplication_table()
            elif action == "show_range":
                display_range_tables()
            elif action == "quiz":
                quiz_mode()
            elif action == "history":
                show_history()
            elif action == "help":
                print_help()
            else:
                print("คำสั่งไม่ถูกต้อง. พิมพ์ 'ช่วยเหลือ' เพื่อดูรายการคำสั่งทั้งหมด.")
        except KeyboardInterrupt:
            print("\nตรวจพบการยกเลิกด้วยแป้นพิมพ์ (Ctrl+C). พิมพ์ 'ออก' หากต้องการปิดโปรแกรม.")
        except Exception as e:
            print(f"เกิดข้อผิดพลาดที่ไม่คาดคิด: {e}")

if __name__ == "__main__":
    main()
