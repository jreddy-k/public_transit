FROM python:3.11

WORKDIR /public_transit

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN python manage.py test

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]