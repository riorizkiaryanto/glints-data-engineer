from datetime import datetime, timedelta
from time import time

import airflow
from airflow import DAG
from airflow.operators.postgres_operator import PostgresOperator
from airflow.hooks.postgres_hook import PostgresHook

args={'owner': 'airflow'}

default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

# dag_parameters = {
#     'dag_id': 'postgresql_migration',
#     'default_args': args,
#     'schedule_interval': '@once',
#     'dagrun_timeout': timedelta(minutes=60),
#     'description': 'postgresql migration',
#     'start_date': airflow.utils.dates.days_ago(1)
# }
    
with DAG(
    dag_id = 'postgresql_migration',
    default_args = args,
    schedule_interval = '@once',
    dagrun_timeout = timedelta(minutes=60),
    description = 'postgresql mnigration',
    start_date = airflow.utils.dates.days_ago(1)
) as dag:
    src = PostgresHook(postgres_conn_id = "postgres_sources")
    dest = PostgresHook(postgres_conn_id = "postgres_targets")

    src_conn = src.get_conn()
    src_cursor = src_conn.cursor()
    dest_conn = dest.get_conn()
    dest_cursor = dest_conn.cursor()

    dest_cursor.execute("delete from sales_record;")

    src_cursor.execute("select date_record, sales from sales_record where date_record >= current_date - integer '7';")

    # dest.insert_rows(table="sales_record", rows=src_cursor)

    data = src_cursor.fetchall()

    for row in data:
        dest_cursor.execute("insert into sales_record (date_record, sales) values('{}', {});".format(row[0], row[1]))

    dest_conn.commit()
    dest_cursor.close()
    dest_conn.close()

    src_conn.commit()
    src_cursor.close()
    src_conn.close()