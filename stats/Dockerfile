FROM python
COPY ./requirements.txt .
RUN pip install -r requirements.txt
ENV STATSHOST 0.0.0.0
ENV STATSPORT 8081
ENV DATABASE_URL postgresql://postgres:postgrespw@db:5432/mydb
COPY . .
CMD ["python", "main.py"]