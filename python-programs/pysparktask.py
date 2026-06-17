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

def createDataFrameWithoutColumns(spark):
    data = [("Java", "20000"), ("Python", "100000"), ("Scala", "3000")]

    rdd = spark.sparkContext.parallelize(data)

    dfFromRDD1 = rdd.toDF()
    dfFromRDD1.printSchema()

def createDataFrameWithColumns(spark):
    columns = ["language", "users_count"]
    data = [("Java", "20000"), ("Python", "100000"), ("Scala", "3000")]

    rdd = spark.sparkContext.parallelize(data)
    dfFromRDD1 = rdd.toDF(columns)
    dfFromRDD1.printSchema()

    dfFromRDD1.show()

def pysparkStruckTypeAndField(spark):
    data = [("James", "", "Smith", "36636", "M", 3000),
            ("Michael", "Rose", "", "40288", "M", 4000),
            ("Robert", "", "Williams", "42114", "M", 4000),
            ("Maria", "Anne", "Jones", "39192", "F", 4000),
            ("Jen", "Mary", "Brown", "", "F", -1)
            ]

    schema = StructType([ \
        StructField("firstname", StringType(), True), \
        StructField("middlename", StringType(), True), \
        StructField("lastname", StringType(), True), \
        StructField("id", StringType(), True), \
        StructField("gender", StringType(), True), \
        StructField("salary", IntegerType(), True) \
        ])

    df = spark.createDataFrame(data=data, schema=schema)
    df.printSchema()
    df.show()


def nestedStrucType(spark):
    structureData = [
        (("James", "", "Smith"), "36636", "M", 3100),
        (("Michael", "Rose", ""), "40288", "M", 4300),
        (("Robert", "", "Williams"), "42114", "M", 1400),
        (("Maria", "Anne", "Jones"), "39192", "F", 5500),
        (("Jen", "Mary", "Brown"), "", "F", -1)
    ]

    structureSchema = StructType([
        StructField('name', StructType([
            StructField('firstname', StringType(), True),
            StructField('middlename', StringType(), True),
            StructField('lastname', StringType(), True)
        ])),
        StructField('id', StringType(), True),
        StructField('gender', StringType(), True),
        StructField('salary', IntegerType(), True)
    ])

    df2 = spark.createDataFrame(data=structureData, schema=structureSchema)
    df2.printSchema()
    df2.show(truncate=False)

if __name__:
    print("This is a PySpark exercise.")
    # initialize a PySpark Session
    spark: SparkSession = SparkSession.builder.master("local[1]").appName("bootcamp.com").getOrCreate()

    # wordCount(spark, "file:///home/takeo/file.txt")

    createDataFrameWithoutColumns(spark)

    createDataFrameWithColumns(spark)

    pysparkStruckTypeAndField(spark)

    nestedStrucType(spark)

