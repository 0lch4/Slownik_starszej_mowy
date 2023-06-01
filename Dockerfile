FROM python:3.11

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

RUN mkdir dictionaries

CMD mkdir dictionaries && python3 plik.py && python3 loading.py && rm -r dictionaries

EXPOSE 8000
CMD ["uvicorn", "main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "8000"]

