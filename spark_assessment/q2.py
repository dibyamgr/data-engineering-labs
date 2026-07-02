from spark_session import get_spark_session
from config import BASE_PATH
from pyspark.sql.functions import col, array_contains

# Write a pyspark program which reads the above json file either from local or hadoop file system and returns the first name and gender of all those students who are learning java and does not belong to state OH.
spark = get_spark_session("Question2")

df = spark.read.json(f"{BASE_PATH}/data/student.json")

df.printSchema()
df.show(truncate=False)

result_df = df.filter(
    (array_contains(col("languages"), "Java")) &
    (col("state") != "OH")
).select(
    col("name.firstname").alias("firstname"),
    col("gender")
)

result_df.show()

spark.stop()