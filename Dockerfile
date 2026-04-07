FROM python:3.11

WORKDIR /app

# Instalamos ffmpeg (necesario para unir audio y video)
RUN apt-get update && apt-get install -y ffmpeg

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000
CMD ["python", "app.py"]