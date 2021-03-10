FROM python:3
    
 #ファイルapp.pyをおくフォルダを作成
RUN mkdir /app
    
#app.pyが動く場所を指定
WORKDIR /app

COPY ./requirements.txt ./

RUN pip install -r ./requirements.txt

COPY ./app .

EXPOSE 80

CMD ["python3", "app.py"]