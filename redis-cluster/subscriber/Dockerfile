FROM python:3.9
WORKDIR /app
COPY subscriber.py .
RUN pip install redis
CMD ["python", "subscriber.py"]
