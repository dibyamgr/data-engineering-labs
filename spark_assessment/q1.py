from spark_session import get_spark_session
from config import BASE_PATH, HDFS_DATA_DIR
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, LongType
from pyspark.sql.functions import col

# Write a pyspark program which reads  the above file from hadoop and introduces a new column in the existing dataframe with name as doubleSalary which should have values twice as the existing salary.
# Convert the data into a parquet file named department.parquet. You can store this converted parquet file either on the local file system or on hadoop.

spark = get_spark_session("Question1")

schema = StructType([
    StructField("dept_name", StringType(), True),
    StructField("dept_id", IntegerType(), True),
    StructField("salary", LongType(), True)
])

df = spark.read \
    .option("header", "false") \
    .schema(schema) \
    .csv(f"{HDFS_DATA_DIR}/Department.txt")

result_df = df.withColumn(
    "doubleSalary",
    col("salary") * 2
)

# result_df.show()

result_df.write \
    .mode("overwrite") \
    .parquet("output/department.parquet")

check_df = spark.read.parquet("output/department.parquet")
check_df.show()
