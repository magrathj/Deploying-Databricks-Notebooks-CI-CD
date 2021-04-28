# test_new_york_taxi_feature_eng.py
import pytest
import os
from poc.ny_taxi import new_york_taxi_feature_eng
from poc.ny_taxi.constants import TAXI_PARQUET_FILE

DATA_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir, 'ny_taxi/data/')

def test_feature_eng(
        spark,
        tmp_path_factory
):
    new_york_taxi_feature_eng.run(
        source_bucket=f'file://{DATA_PATH}',
        release_bucket=f'file://{tmp_path_factory.getbasetemp()}/release/'
    )
    parquet_df = spark.read.parquet(f'file://{tmp_path_factory.getbasetemp()}//release/{TAXI_PARQUET_FILE}')
    assert parquet_df.count() > 0