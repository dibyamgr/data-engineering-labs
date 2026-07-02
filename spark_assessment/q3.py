# Write a pyspark program which read employee.json and do the followings
# Generate an orc file partitioned on a department for distinct employees.
# Return departaments names in descending orders with their mean salary.
from config import BASE_PATH
from spark_session import get_spark_session
from pyspark.sql.functions import avg, desc

spark = get_spark_session("Question 3")

df = spark.read.json(f"{BASE_PATH}/data/employee.json")
# df.show()

# remove duplicate rows
distinct_df = df.distinct()

# Save ORC files grouped into department folders
distinct_df.write \
    .mode("overwrite") \
    .partitionBy("department") \
    .orc("output/employee.orc")

check_df = spark.read.orc("output/employee.orc")
# check_df.show(

# average salary by department, ordered by department name descending
average_salary = df.groupby("department") \
    .agg(avg("salary").alias("mean_salary")) \
    .orderBy(desc("department"))

average_salary.show()

spark.stop()

