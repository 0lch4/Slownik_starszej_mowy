FROM python:3.11

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

EXPOSE 8000

CMD cd .. && mkdir app/load_data/dictionaries && python -m app.load_data && rm -r app/load_data/dictionaries

