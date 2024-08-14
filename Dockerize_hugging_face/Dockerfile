FROM python:3.10.8-slim
LABEL description="Classification of queries"
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
COPY . /app/
EXPOSE 6000
CMD ["python",  "/app/reporting_service/app.py"]