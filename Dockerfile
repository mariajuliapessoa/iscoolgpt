FROM python:3.11-slim
WORKDIR /app
<<<<<<< HEAD
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8080  
=======

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

>>>>>>> d9a968a0645869651a1db9b1efe627397d789a9b
CMD ["python", "app.py"]
