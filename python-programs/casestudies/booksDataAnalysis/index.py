from pyspark.sql import SparkSession
import os

if __name__ == "__main__":
    print("Books Data Analysis")

    spark: SparkSession = SparkSession.builder.master("local[1]").appName("BooksDataAnalysis").getOrCreate()

    # Read JSON file
    df = spark.read.json('books.json')

    df.printSchema()
    df.show(5, truncate=False)
