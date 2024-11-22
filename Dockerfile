# Sử dụng Python image
FROM python:3.12

# Cài đặt thư viện hệ thống cần thiết
RUN apt-get update && apt-get install -y gcc default-libmysqlclient-dev && rm -rf /var/lib/apt/lists/*

# Thiết lập thư mục làm việc
WORKDIR /app

# Sao chép các file vào container
COPY . /app

# Cài đặt các thư viện Python cần thiết
RUN pip install flask mysql-connector-python

# Expose cổng 5000
EXPOSE 5000

# Lệnh chạy ứng dụng
CMD ["python", "app.py"]
