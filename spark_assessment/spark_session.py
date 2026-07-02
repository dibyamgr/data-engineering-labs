from pyspark.sql import SparkSession


def get_spark_session(app_name):
    spark = SparkSession.builder \
        .appName(app_name) \
        .master("local[*]") \
        .config("spark.sql.warehouse.dir", "output/hive_warehouse") \
        .enableHiveSupport() \
        .getOrCreate()

    return spark