from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DoubleType

data = [
    ("Smith", 23, 5.3),
    ("Rashmi", 27, 5.8),
    ("Smith", 23, 5.3),
    ("Payal", 27, 5.8),
    ("Megha", 27, 5.4)
]

schema = StructType([
    StructField("name", StringType(), True),
    StructField("age", IntegerType(), True),
    StructField("height", DoubleType(), True)
])

if __name__ == "__main__":
    print("Customer Data Cleaning")
    spark: SparkSession = SparkSession.builder.master("local[1]").appName("bootcamp.com").getOrCreate()

    df = spark.createDataFrame(data=data, schema=schema)
    df.printSchema()
    df.show()

    # Remove exact duplicate records
    df.dropDuplicates().show()

    # Remove records duplicated based on age and height
    cleaned_df = df.dropDuplicates(["age", "height"]).show()