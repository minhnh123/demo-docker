# Sử dụng image Python 3.9
FROM python:3.9-slim

# Đặt thư mục làm việc
WORKDIR /app

# Copy file requirements và cài đặt dependencies
COPY app/requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy mã nguồn ứng dụng
COPY app/ .

# Chạy ứng dụng
CMD ["python", "app.py"]
