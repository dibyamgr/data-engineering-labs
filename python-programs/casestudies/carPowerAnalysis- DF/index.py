from pyspark.sql import SparkSession
from pyspark.sql.functions import lit, col
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, ArrayType

data = [("Ford Torino", 140, 3449, "US"),
        ("Chevrolet Monte Carlo", 150, 3761, "US"),
        ("BMW 2002", 113, 2234, "Europe")
        ]

schema = StructType([
    StructField("carr", StringType(), True), \
    StructField("horsepower", IntegerType(), True), \
    StructField("weight", IntegerType(), True), \
    StructField("origin", StringType(), True), \
    ])

if __name__:
    print("Car Power Analysis Case Studies")
    spark: SparkSession = SparkSession.builder.master("local[1]").appName("bootcamp.com").getOrCreate()

    df = spark.createDataFrame(data=data, schema=schema)
    df.printSchema()
    df.show()

    # Change column name weight to AvgWeight
    df.withColumnRenamed("weight", "AvgWeight").show()

    # Add constant value as 200
    df.withColumn("AvgWeight", lit(200)).show()

    # horsepower * 1000
    df.withColumn("horsepower", col("horsepower") * 1000).show()

    df.withColumnRenamed("carr", "car").show()



