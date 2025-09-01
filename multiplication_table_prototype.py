# multiplication_table.py

def display_welcome_message():
    """Displays a welcome message to the user."""
    print("--------------------------------------------------")
    print("     ยินดีต้อนรับสู่โปรแกรมตารางสูตรคูณอัตโนมัติ!     ")
    print("--------------------------------------------------")

def get_command_input():
    """Prompts the user for a command and returns it in lowercase."""
    return input("\nกรุณาเลือกคำสั่ง (แสดงตาราง / ออก): ").lower().strip()

def display_multiplication_table(number):
    """Displays the multiplication table for a given number from 1 to 12."""
    print(f"\n--- ตารางสูตรคูณสำหรับแม่ {number} ---")
    for i in range(1, 13): # Loop from 1 to 12
        print(f"{number} x {i} = {number * i}")
    print("----------------------------------")

def main():
    """Main function to run the multiplication table program."""
    display_welcome_message()

    while True:
        command = get_command_input()

        if command == 'ออก' or command == 'quit':
            print("ลาก่อน! ขอบคุณที่ใช้บริการครับ.")
            break # Exit the main loop and end the program
        elif command == 'แสดงตาราง' or command == 'show table':
            while True:
                num_input = input("กรุณาป้อนตัวเลขสำหรับตารางสูตรคูณ: ").strip()
                try:
                    num = int(num_input) # Attempt to convert input to an integer
                    display_multiplication_table(num)
                    break # Break out of the inner loop, return to main menu
                except ValueError:
                    # Handle non-numeric input gracefully
                    print("คำเตือน: กรุณาป้อนตัวเลขที่ถูกต้องเท่านั้น")
        else:
            print("คำสั่งไม่ถูกต้อง. กรุณาลองอีกครั้ง (แสดงตาราง / ออก).")

if __name__ == "__main__":
    main()
