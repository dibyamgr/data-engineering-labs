import pyspark
from pyspark.sql import SparkSession
from utility import createDataFrameWithoutColumns, createDataFrameWithColumns, createDFWithStruckTypeAndField, createDFWithnestedStrucType, \
selectSingleAndMultiColumn, selectColumnUsingColFun, selectAllColumns, selectColumnByIndex, selectNestedStrucCols, changeDataFrameColumn, \
filterDataFrame, filterLikeAndRLike

if __name__:
    print("This is a PySpark DataFrame exercise.")
    # initialize a PySpark Session
    spark: SparkSession = SparkSession.builder.master("local[1]").appName("bootcamp.com").getOrCreate()

    ############ CREATE DATA FRAMES  ############
    createDataFrameWithoutColumns(spark)

    createDataFrameWithColumns(spark)

    createDFWithStruckTypeAndField(spark)

    createDFWithnestedStrucType(spark)

    ######## Select Functions in DataFrames  ########
    data = [("James", "Smith", "USA", "CA"),
            ("Michael", "Rose", "USA", "NY"),
            ("Robert", "Williams", "USA", "CA"),
            ("Maria", "Jones", "USA", "FL")
            ]
    columns = ["firstname", "lastname", "country", "state"]
    df = spark.createDataFrame(data=data, schema=columns)
    df.show(truncate=False)
    selectSingleAndMultiColumn(df)
    selectColumnUsingColFun(df)
    selectAllColumns(df)
    selectColumnByIndex(df)
    selectNestedStrucCols(spark)


    ######## Change column type,name or value in DataFrames - immutable so creates new dataframe everytime ########
    changeDataFrameColumn(spark)

    ######## Filter Function in DataFrames  ########
    filterDataFrame(spark)
    filterLikeAndRLike(spark)

