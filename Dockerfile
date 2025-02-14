FROM python:3.9

WORKDIR /app
COPY . /app

# Install Flask
RUN pip install flask

CMD ["python", "app.py"]
