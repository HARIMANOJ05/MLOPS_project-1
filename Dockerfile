# Build Stage
FROM python:3.9-slim-buster AS build

WORKDIR /app
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY . /app/

# Final Stage
FROM python:3.9-slim-buster

WORKDIR /app
COPY --from=build /app /app/

# Set environment variables
ENV AIRFLOW_HOME="/app/airflow" \
    AIRFLOW_CORE_DAGBAG_IMPORT_TIMEOUT=1000 \
    AIRFLOW_CORE_ENABLE_XCOM_PICKLING=True

# Initialize Airflow and create user
RUN airflow db init && \
    airflow users create -e harimanoj4321@gmail.com -f hari -l manoj -p Manoj@0505 -r Admin -u admin

# Copy start.sh and set permissions
COPY start.sh /app/
RUN chmod 755 /app/start.sh

ENTRYPOINT ["/bin/sh"]
CMD ["/app/start.sh"]

