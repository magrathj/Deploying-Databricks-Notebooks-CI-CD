# conftest.py
import pytest
from pyspark import SparkConf
from pyspark.sql import SparkSession

@pytest.fixture(scope="session")
def spark():
    """
    Fixture for Spark Sessions.
    we use the name `spark`, as that is is the same name you can
    expect for the automatically injected session you find in pyspark
    shells or pysparb Databricks notebooks.
    """
    # Setup
    spark_session = SparkSession.builder.config(conf=conf).getOrCreate()
    yield spark_session
    # Teardown
    spark_session.stop()
    
conf = (
    SparkConf()
        .setMaster("local")
        .setAppName("testing")
        .set("spark.driver.host", "localhost")
)