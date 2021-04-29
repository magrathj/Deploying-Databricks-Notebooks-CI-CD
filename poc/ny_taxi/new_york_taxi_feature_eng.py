# new_york_taxi_feature_eng.py
from pyspark.sql import SparkSession
from poc.ny_taxi.constants import AWS_BUCKET_NAME, TAXI_SOURCE_FILE, TAXI_PARQUET_FILE

def read_raw_taxi_convert_to_parquet(spark, source_bucket, release_bucket):
    df = spark.read.option("header", "true").option("inferSchema", "true").csv(source_bucket + TAXI_SOURCE_FILE)
    df.write.mode("overwrite").parquet(release_bucket + TAXI_PARQUET_FILE)
    parquet_df = spark.read.parquet(release_bucket + TAXI_PARQUET_FILE)
    return parquet_df
    
def run(
        source_bucket=AWS_BUCKET_NAME,
        release_bucket=AWS_BUCKET_NAME,
        **kwargs
    ):
    spark = SparkSession.builder.getOrCreate()
    parquet_taxi_df = read_raw_taxi_convert_to_parquet(spark, source_bucket, release_bucket)
    
if __name__ == "__main__":
    run()