FROM python:latest AS build
WORKDIR /build
RUN pip install poetry==1.2.0b3
COPY . .
RUN poetry build

FROM python:latest
WORKDIR /app
COPY --from=build /build/dist/*.whl .
COPY wsgi.py .
RUN pip install *.whl && rm *.whl
CMD ["gunicorn", "--bind", "0.0.0.0:6502", "wsgi"]
