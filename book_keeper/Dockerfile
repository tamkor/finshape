FROM python
COPY ./requirements.txt .
RUN pip install -r requirements.txt
ENV BKHOST 0.0.0.0
ENV BKPORT 8080
ENV STATSHOST 0.0.0.0
ENV STATSPORT 8081
ENV STATS_URL http://stats:8081
ENV DATABASE_URL postgresql://postgres:postgrespw@db:5432/mydb
COPY . .
CMD ["python", "main.py"]