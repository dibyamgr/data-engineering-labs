from pyspark.sql import SparkSession
from pyspark.sql.types import *

if __name__ == "__main__":
    print("PySpark File Formats")

    spark = SparkSession.builder \
        .master("local[1]") \
        .appName("bootcamp.com") \
        .getOrCreate()

    # Spark does not know the first row is a header so column becomes _c0, _c1,... and all values are read as string by default
    df = spark.read.csv("file:///home/takeo/pycharmprojects/zipcodes.csv")
    # df.printSchema()

    # Read CSV with header - Now Spark uses the first row as column names but still values are read as string
    df2 = spark.read \
        .option("header", True) \
        .csv("file:///home/takeo/pycharmprojects/zipcodes.csv")

    # df2.printSchema()
    # df.show()

    # Read CSV with inferred data types, now Spark guesses types:
    df3 = spark.read \
        .option("header", True) \
        .option("inferSchema", True) \
        .csv("file:///home/takeo/pycharmprojects/zipcodes.csv")

    # df3.printSchema()

    #     Use delimiter - means how columns are separated
    df4 = spark.read \
        .option("header", True) \
        .option("inferSchema", True) \
        .option("delimiter", ",") \
        .csv("file:///home/takeo/pycharmprojects/zipcodes.csv")

    # df4.printSchema()
    # df4.show()


    # Custom schema - safer and faster than infer schema
    schema = StructType([
        StructField("RecordNumber", IntegerType(), True),
        StructField("Zipcode", IntegerType(), True),
        StructField("ZipCodeType", StringType(), True),
        StructField("City", StringType(), True),
        StructField("State", StringType(), True),
        StructField("LocationType", StringType(), True),
        StructField("Lat", DoubleType(), True),
        StructField("Long", DoubleType(), True),
        StructField("Xaxis", DoubleType(), True),
        StructField("Yaxis", DoubleType(), True),
        StructField("Zaxis", DoubleType(), True),
        StructField("WorldRegion", StringType(), True),
        StructField("Country", StringType(), True),
        StructField("LocationText", StringType(), True),
        StructField("Location", StringType(), True),
        StructField("Decommisioned", BooleanType(), True),
        StructField("TaxReturnsFiled", IntegerType(), True),
        StructField("EstimatedPopulation", IntegerType(), True),
        StructField("TotalWages", IntegerType(), True),
        StructField("Notes", StringType(), True)
    ])

    df5 = spark.read \
        .option("header", True) \
        .schema(schema) \
        .csv("file:///home/takeo/pycharmprojects/zipcodes.csv")

    # df5.printSchema()

    #     Write CSV output - Spark writes a folder, not one single CSV file.
    df5.write.mode("overwrite").csv("file:///tmp/spark_output/zipcodes")
    # csv = spark.read.csv("file:///tmp/spark_output/zipcodes")
    # csv.show()

    # Pyspark Write DataFrame to Parquet file format
    # Parquet - column wise, faster, compressed
    data = [("James ", "", "Smith", "36636", "M", 3000),
            ("Michael ", "Rose", "", "40288", "M", 4000),
            ("Robert ", "", "Williams", "42114", "M", 4000),
            ("Maria ", "Anne", "Jones", "39192", "F", 4000),
            ("Jen", "Mary", "Brown", "", "F", -1)]
    columns = ["firstname", "middlename", "lastname", "dob", "gender", "salary"]

    df6 = spark.createDataFrame(data, columns)
    # df6.write.parquet("file:///tmp/output/people.parquet")

    parDF = spark.read.parquet("file:///tmp/output/people.parquet")
    # parDF.show()

    # SQL queries dataframe
    # Create temp table - means treat dataframe as SQL Table
    parDF.createOrReplaceTempView("ParquetTable")
    # Run query on the ParquetTable
    parkSQL = spark.sql("select * from ParquetTable where salary >= 4000 ")
    # parkSQL.show()

#     ORC stands for Optimized Row Columnar.
# It is a big data file format developed primarily for the Hadoop ecosystem, especially Hive

    # parDF.write.orc("file:///tmp/orc/data.orc")

    df7 = spark.read.orc("file:///tmp/orc/data.orc")
    # df7.printSchema()
    # df7.show()

    #     run sql on orc files
    df7.createOrReplaceTempView("ORCTable")
    orcSQL = spark.sql("select firstname,dob from ORCTable where salary >= 4000 ")
    orcSQL.show()

    # Read JSON file into dataframe
    parDF.write.json("file:///tmp/json/data.json")

    df8 = spark.read.json("file:///tmp/json/data.json")
    df8.printSchema()
    df8.show()







