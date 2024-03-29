"""
demo
DAG auto-generated by Astro Cloud IDE.
"""

from airflow.decorators import dag
from astro import sql as aql
from astro.table import Table, Metadata
import pandas as pd
import pendulum


@aql.run_raw_sql(conn_id="duckdb_default", task_id="demo_1", handler=lambda x: pd.DataFrame(x.fetchall(), columns=x.keys()))
def demo_1_func():
    return """
    show functions;
    """

@aql.run_raw_sql(conn_id="duckdb_default", task_id="demo_2", handler=lambda x: pd.DataFrame(x.fetchall(), columns=x.keys()))
def demo_2_func():
    return """
    show functions;
    """

@dag(
    schedule="0 0 * * *",
    start_date=pendulum.from_format("2023-04-18", "YYYY-MM-DD").in_tz("UTC"),
)
def demo():
    demo_1 = demo_1_func()

    demo_2 = demo_2_func()

    demo_2 << demo_1

dag_obj = demo()
