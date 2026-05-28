FROM python:3.9-slim
WORKDIR /app

# Fix: Mitigate container breakout vectors by adding a non-root user
RUN useradd -m serviceuser && chown -R serviceuser /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY model.pkl .
COPY app.py .

USER serviceuser
EXPOSE 80
CMD ["python", "app.py"]
