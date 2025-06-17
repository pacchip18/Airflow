FROM apache/airflow:3.0.0

COPY my_sdk /opt/airflow/my_sdk

RUN pip install -e /opt/airflow/my_sdk