
# ใช้ Python image เบื้องต้น
FROM python:3.11-slim

# ตั้ง working directory ใน container
WORKDIR /app

# copy requirements.txt ไปไว้ใน container
COPY requirements.txt .

# ติดตั้ง dependencies
RUN pip install --no-cache-dir -r requirements.txt

# copy code ทั้งหมดไปใน container
COPY . .

# เปิด port 5000
EXPOSE 5000

# คำสั่งรัน flask app
CMD ["python", "app.py"]
