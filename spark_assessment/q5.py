# Write a python program for followings
# Read the above data and generate a new sample data with a sample size of 50 %.
# Create a hive partitioned table on state and city with maximum 3 records in each data file within the partitions.
# Run a hive sql in pyspark to get the data for states other than AL and cities other than SPRINGVILLE.
from config import BASE_PATH
from spark_session import get_spark_session

spark = get_spark_session("Question 5")

df = spark.read \
    .option("header", True) \
    .option("inferSchema", True) \
    .csv(f"{BASE_PATH}/data/sample-zipcodes.csv")

# Read the above data and generate a new sample data with a sample size of 50 %.
sample_df = df.sample(
    withReplacement=False,
    fraction=0.5,
    seed=10
)

# sample_df.show()

# Create a hive partitioned table on state and city with maximum 3 records in each data file within the partitions.
sample_df.write \
    .mode("overwrite") \
    .option("maxRecordsPerFile", 3) \
    .partitionBy("State", "City") \
    .saveAsTable("zipcodes_partitioned")

# Run a hive sql in pyspark to get the data for states other than AL and cities other than SPRINGVILLE.

spark.sql("SELECT * FROM zipcodes_partitioned WHERE State != 'AL' AND City != 'SPRINGVILLE'").show()
