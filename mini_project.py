# multiplication_table.py

def display_welcome_message():
    """Displays a welcome message to the user."""
    print("--------------------------------------------------")
    print("     ยินดีต้อนรับสู่โปรแกรมตารางสูตรคูณอัตโนมัติ!     ")
    print("--------------------------------------------------")

def get_command_input():
    """Prompts the user for a command and returns it in lowercase."""
    return input("\nกรุณาเลือกคำสั่ง (แสดงตาราง / ออก): ").lower().strip()

def display_multiplication_table(number, end_number):
    """Displays the multiplication table for a given number from 1 to end_number."""
    print(f"\n--- ตารางสูตรคูณสำหรับแม่ {number} ---")
    for i in range(1, end_number + 1):
        print(f"{number} x {i} = {number * i}")
    print("----------------------------------")

def main():
    """Main function to run the multiplication table program."""
    display_welcome_message()

    while True:
        command = get_command_input()

        if command == 'ออก' or command == 'quit':
            print("ลาก่อน! ขอบคุณที่ใช้บริการครับ.")
            break
        elif command == 'แสดงตาราง' or command == 'show table':
            while True:  # loop สำหรับกรอกตัวเลข
                try:
                    num_input = input("กรุณาป้อนตัวเลขสำหรับตารางสูตรคูณ: ").strip()
                    end_input = input("กรุณาป้อนตัวเลขสิ้นสุดสำหรับตารางสูตรคูณ: ").strip()
                    num = int(num_input)
                    end_number = int(end_input)
                    display_multiplication_table(num, end_number)
                    break  # ออกจาก loop ของการกรอกตัวเลข
                except ValueError:
                    print("คำเตือน: กรุณาป้อนตัวเลขที่ถูกต้องเท่านั้น")
        else:
            print("คำสั่งไม่ถูกต้อง. กรุณาลองอีกครั้ง (แสดงตาราง / ออก).")

if __name__ == "__main__":
    main()
