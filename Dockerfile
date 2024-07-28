FROM python:3.7-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["python", "/app/src/python_script.py"]
