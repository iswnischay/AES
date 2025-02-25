FROM python:3.9 
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir pycryptodome
CMD ["python3", "aes.py"]
