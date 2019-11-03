# Extending the base OS...
FROM python:alpine

# Installing the dependencies...
WORKDIR /usr/app
COPY ./requirements.txt ./
RUN pip install -r requirements.txt
EXPOSE 3000
COPY ./ ./

# Running the Startup commands...
CMD ["python" , "main.py"]