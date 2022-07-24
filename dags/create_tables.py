from datetime import timedelta

import airflow
from airflow import DAG
from airflow.operators.postgres_operator import PostgresOperator

args={'owner': 'airflow'}

default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

dag_psql = DAG(
    dag_id = 'postgresql_operator',
    default_args = args,
    schedule_interval = '@once',
    dagrun_timeout = timedelta(minutes=60),
    description = 'postgresql operator',
    start_date = airflow.utils.dates.days_ago(1)
)

# create_database_x = PostgresOperator(
#     task_id = 'create_database_x',
#     postgres_conn_id = "postgres_sources",
#     dag = dag_psql,
#     sql = 'create database sources;'
# )

create_table_x = PostgresOperator(
    task_id = 'create_table_x',
    postgres_conn_id = "postgres_sources",
    dag = dag_psql,
    sql = 'create table sales_record (id serial primary key, date_record date not null, sales numeric(50));'
)

insert_table_x = PostgresOperator(
    task_id = 'insert_table_x',
    postgres_conn_id = "postgres_sources",
    dag = dag_psql,
    sql = "insert into sales_record (date_record, sales) values('2022-07-14', 100), ('2022-07-15', 50), ('2022-07-16', 45), \
        ('2022-07-17', 80), ('2022-07-18', 200), ('2022-07-19', 30), ('2022-07-20', 100), ('2022-07-21', 100), ('2022-07-22', 90), ('2022-07-23', 300), ('2022-07-24', 40)"
)

# create_database_y = PostgresOperator(
#     task_id = 'create_database_y',
#     postgres_conn_id = "postgres_targets",
#     dag = dag_psql,
#     sql = 'create database targets;'
# )

create_table_y = PostgresOperator(
    task_id = 'create_table_y',
    postgres_conn_id = "postgres_targets",
    dag = dag_psql,
    sql = 'create table sales_record (id serial primary key, date_record date not null, sales numeric(50));'
)

create_table_x >> insert_table_x >> create_table_y

if __name__ == "__main__":
    dag_psql.cli()