import pyspark

from pyspark.sql.types import StructType, StructField, StringType, IntegerType, ArrayType
from pyspark.sql.functions import col,lit, array_contains

def createDataFrameWithoutColumns(spark):
    data = [("Java", "20000"), ("Python", "100000"), ("Scala", "3000")]

    rdd = spark.sparkContext.parallelize(data)

    dfFromRDD1 = rdd.toDF()
    return dfFromRDD1.printSchema()

def createDataFrameWithColumns(spark):
    columns = ["language", "users_count"]
    data = [("Java", "20000"), ("Python", "100000"), ("Scala", "3000")]

    rdd = spark.sparkContext.parallelize(data)
    dfFromRDD1 = rdd.toDF(columns)
    dfFromRDD1.printSchema()

    dfFromRDD1.show()

def createDFWithStruckTypeAndField(spark):
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

def createDFWithnestedStrucType(spark):
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

def selectSingleAndMultiColumn(df):
    df.select("firstname").show()
    df.select(df.firstname, df.lastname).show()
    df.select(df["country"]).show()

def selectColumnUsingColFun(df):
    df.select(col("firstname"), col("lastname")).show()

def selectAllColumns(df):
    df.select("*").show()

def selectColumnByIndex(df):
    # Selects first 3 columns and top 3 rows
    df.select(df.columns[:3]).show(3)

    # Selects columns 2 to 4  and top 3 rows
    df.select(df.columns[2:4]).show(3)

def selectNestedStrucCols(spark):
    data = [
        (("James", None, "Smith"), "OH", "M"),
        (("Anna", "Rose", ""), "NY", "F"),
        (("Julia", "", "Williams"), "OH", "F"),
        (("Maria", "Anne", "Jones"), "NY", "M"),
        (("Jen", "Mary", "Brown"), "NY", "M"),
        (("Mike", "Mary", "Williams"), "OH", "M")
    ]

    schema = StructType([
        StructField('name', StructType([
            StructField('firstname', StringType(), True),
            StructField('middlename', StringType(), True),
            StructField('lastname', StringType(), True)
        ])),
        StructField('state', StringType(), True),
        StructField('gender', StringType(), True)
    ])

    df2 = spark.createDataFrame(data = data, schema = schema)
    df2.printSchema()
    df2.show(truncate = False)

    df2.select("name").show(truncate = False)

    df2.select("name.firstname", "name.lastname").show(truncate=False)

# withColumn()
# is a transformation function of DataFrame which is used to change the value,
# convert the datatype of an existing column, create a new column
def changeDataFrameColumn(spark):
    data = [('James', '', 'Smith', '1991-04-01', 'M', 3000),
            ('Michael', 'Rose', '', '2000-05-19', 'M', 4000),
            ('Robert', '', 'Williams', '1978-09-05', 'M', 4000),
            ('Maria', 'Anne', 'Jones', '1967-12-01', 'F', 4000),
            ('Jen', 'Mary', 'Brown', '1980-02-17', 'F', -1)
            ]

    columns = ["firstname", "middlename", "lastname", "dob", "gender", "salary"]

    df = spark.createDataFrame(data=data, schema=columns)

    # Data Type Change
    ddf = df.withColumn("salary", col("salary").cast("Double"))
    ddf.printSchema()

    # Data value change
    udf = df.withColumn("salary", col("salary") * 100)
    udf.show()

    # create a column from existing
    ncol = df.withColumn("CopiedColumn", col("salary") * -1)
    ncol.show()

    # Add a New Column using withColumn() with constant value
    df.withColumn("Country", lit("USA")).show()

    # Rename Column Name

    df.withColumnRenamed("gender","sex").show(truncate=False)

def filterDataFrame(spark):
    data = [
        (("James", "", "Smith"), ["Java", "Scala", "C++"], "OH", "M"),
        (("Anna", "Rose", ""), ["Spark", "Java", "C++"], "NY", "F"),
        (("Julia", "", "Williams"), ["CSharp", "VB"], "OH", "F"),
        (("Maria", "Anne", "Jones"), ["CSharp", "VB"], "NY", "M"),
        (("Jen", "Mary", "Brown"), ["CSharp", "VB"], "NY", "M"),
        (("Mike", "Mary", "Williams"), ["Python", "VB"], "OH", "M")
    ]

    schema = StructType([
        StructField('name', StructType([
            StructField('firstname', StringType(), True),
            StructField('middlename', StringType(), True),
            StructField('lastname', StringType(), True)
        ])),
        StructField('languages', ArrayType(StringType()), True),
        StructField('state', StringType(), True),
        StructField('gender', StringType(), True)
    ])

    df = spark.createDataFrame(data=data, schema=schema)
    # df.printSchema()
    # df.show(truncate=False)
    #
    # df.filter(df.state == "OH").show(truncate=False)
    # df.filter(df.state != "OH") \
    #     .show(truncate=False)
    #
    # df.filter(~(df.state == "OH")) \
    #     .show(truncate=False)
    #
    # # using col()
    # df.filter(col("state") == "OH") \
    #     .show(truncate=False)

    # using SQL expression
    df.filter("gender == 'M'").show()
    df.filter("gender != 'M'").show()
    df.filter("gender <> 'M'").show()

    #     multiple condition filter
    df.filter( (df.state  == "OH") & (df.gender  == "M") ) \
    .show(truncate=False)

    # filter based on list values
    li = ["OH", "CA", "DE"]
    df.filter(df.state.isin(li)).show()
    df.filter(~df.state.isin(li)).show()
    df.filter(df.state.isin(li) == False).show()

    # filter based on startsWith, EndsWith, Contains
    # Using startswith
    df.filter(df.state.startswith("N")).show()
    # using endswith
    df.filter(df.state.endswith("H")).show()
    # contains
    df.filter(df.state.contains("H")).show()

    # filter using array function
    df.filter(array_contains(df.languages, "Java")) \
        .show(truncate=False)

    # filter on nested struct columns
    df.filter(df.name.lastname == "Williams") \
    .show(truncate=False)

def filterLikeAndRLike(spark):
    data2 = [(2, "Michael Rose"), (3, "Robert Williams"),
             (4, "Rames Rose"), (5, "Rames rose")
             ]
    df2 = spark.createDataFrame(data=data2, schema=["id", "name"])

    # like - SQL LIKE pattern
    df2.filter(df2.name.like("%rose%")).show()
