FROM python:alpine 



COPY . /src/
WORKDIR /src
RUN pip install -r requirements.txt
EXPOSE 5000

ENTRYPOINT ["python", "/src/app.py"]