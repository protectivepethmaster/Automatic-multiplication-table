from flask import Flask, render_template, request
import random

app = Flask(__name__)

MAX_BASE = 100
MAX_END = 100
DEFAULT_END = 12


def generate_table_lines(number: int, start_i: int = 1, end_i: int = DEFAULT_END):
    header = f"--- ตารางสูตรคูณสำหรับแม่ {number} (1 ถึง {end_i}) ---"
    lines = [header]
    for i in range(start_i, end_i + 1):
        lines.append(f"{number:>3} x {i:>3} = {number * i:>5}")
    lines.append("-" * 34)
    return lines


@app.route("/", methods=["GET", "POST"])
def index():
    result = []
    if request.method == "POST":
        mode = request.form.get("mode")
        try:
            base = int(request.form.get("base", 7))
            end = int(request.form.get("end", DEFAULT_END))
            start_range = int(request.form.get("range_start", 2))
            end_range = int(request.form.get("range_end", 5))
            quiz_count = int(request.form.get("quiz_count", 5))
        except ValueError:
            result = ["⚠️ กรุณากรอกค่าเป็นจำนวนเต็มที่ถูกต้อง"]
            return render_template("index.html", result=result)

        if mode == "table":
            result = generate_table_lines(base, 1, end)

        elif mode == "range":
            for b in range(min(start_range, end_range), max(start_range, end_range) + 1):
                result.extend(generate_table_lines(b, 1, end))
                result.append("")

        elif mode == "quiz":
            score = 0
            lines = ["--- ผลการทำแบบทดสอบ ---"]
            for i in range(quiz_count):
                a = random.randint(start_range, end_range)
                b = random.randint(1, end)
                correct = a * b
                # คำตอบจำลอง (เว็บไม่ถาม interactive แบบ popup ได้)
                ans = correct  # auto correct เพื่อ demo
                is_right = (ans == correct)
                score += int(is_right)
                result_str = "ถูก" if is_right else f"ผิด (คำตอบที่ถูก: {correct})"
                lines.append(f"{a:>3} x {b:>3} = {ans:>5} -> {result_str}")
            percent = (score / quiz_count) * 100
            lines.append(f"สรุปคะแนน: {score}/{quiz_count} ({percent:.1f}%)")
            result = lines

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(host="0.0.0.0",port = 5000)
