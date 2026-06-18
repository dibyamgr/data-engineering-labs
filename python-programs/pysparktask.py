import pyspark

from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

def wordCount(spark, filePath):
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    rdd = spark.sparkContext.parallelize(data)

    rdd1 = spark.sparkContext.textFile(filePath)

    rdd2 = rdd1.flatMap(lambda x: x.split(" "))

    rdd3 = rdd2.map(lambda x: (x, 2))

    rdd4 = rdd3.reduceByKey(lambda a, b: a * b)

    # x[1] -> value part x[0] (1,2...) -> key part (Nepal)
    rdd5 = rdd4.map(lambda x: (x[1], x[0])).sortByKey()

    rdd6 = rdd3.filter(lambda x: 'al' in x[0])

    print(rdd6.collect())

if __name__:
    print("This is a PySpark exercise.")
    # initialize a PySpark Session
    spark: SparkSession = SparkSession.builder.master("local[1]").appName("bootcamp.com").getOrCreate()

    wordCount(spark, "file:///home/takeo/file.txt")

