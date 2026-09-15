FROM python:latest
COPY requirements.txt .
RUN pip install -r requirements.txt
WORKDIR /app
COPY memory_info.py data/ /app/
ENTRYPOINT ["python"]
CMD ["memory_info.py"]


