from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, ArrayType, DoubleType
from pyspark.sql.functions import sum,avg,max,min,mean,count, col

data = [
    ("New York", 10.0),
    ("New York", 12.0),
    ("Los Angeles", 20.0),
    ("Los Angeles", 22.0),
    ("San Francisco", 15.0),
    ("San Francisco", 18.0)
]


schema = StructType([
    StructField("city", StringType(), True), \
    StructField("temperature", DoubleType(), True), \
    ])

if __name__:
    print("City Temperature Analysis Studies")
    spark: SparkSession = SparkSession.builder.master("local[1]").appName("bootcamp.com").getOrCreate()

    df = spark.createDataFrame(data=data, schema=schema)
    # df.printSchema()
    # df.show()

    df.groupby("city")\
    .agg(
        avg("temperature").alias("avg_temperature"),
        sum("temperature").alias("total_temperature"),
        count("temperature").alias("num_measurements")
    )\
    .filter(col("temperature") > 30)\
    .orderBy(col("city").asc())\
    .show()







