FROM python:3-slim
WORKDIR /programas/ingesta
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "ingesta.py"]
