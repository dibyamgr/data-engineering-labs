from pyspark.sql import SparkSession
if __name__:
    print("Hi Dibya!!")

    spark: SparkSession = SparkSession.builder.master("local[1]").appName("bootcamp.com").getOrCreate()
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    rdd = spark.sparkContext.parallelize(data)

    # print(rdd.count())

    # reading from a text file and converting into rdd
    rdd1 = spark.sparkContext.textFile("file:///home/takeo/test.txt")

    # flatMap()- splits each record by space in an RDD and finally flattens it. Resulting RDD consists of a single word on each record.
    rdd2 = rdd1.flatMap(lambda x: x.split(" "))

    rdd3 = rdd2.map(lambda x: (x, 1))

    rdd5 = rdd3.reduceByKey(lambda a, b: a + b)
    print(rdd5.collect())
