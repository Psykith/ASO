FROM python:3.9
WORKDIR /app
COPY publisher.py .
RUN pip install redis
CMD ["python", "publisher.py"]
