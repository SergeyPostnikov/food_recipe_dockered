FROM python:3.8.10

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /FoodPlan/

COPY requirements.txt /FoodPlan/

RUN pip3 install -r requirements.txt
COPY . /FoodPlan/

# RUN python3 manage.py collectstatic --noinput --clear
RUN python3 manage.py migrate --noinput

# CMD ["python3", "-m",  "gunicorn", "FoodPlan.wsgi:application", "--bind", "0.0.0.0:8000"]

