FROM python:3

RUN mkdir /app
   
COPY ./requirements.txt ./

RUN pip install -r ./requirements.txt

COPY ./app .
   
EXPOSE 5000

CMD ["python3", "app.py"]