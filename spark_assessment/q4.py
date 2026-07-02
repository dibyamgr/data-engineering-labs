# Write a pyspark program which collects all the department names, departments max salary and number of employees in each department and persist collected data into a partitioned hive table with parquet as internal file format for hive.
# And dept_name as a hive table partitioned column.
# And part_department as hive table name.
from pyspark.sql.functions import max, count
from config import BASE_PATH
from spark_session import get_spark_session

spark = get_spark_session("Question 3")

employee_df = spark.read.json(f"{BASE_PATH}/data/employee00.json")
department_df = spark.read.json(f"{BASE_PATH}/data/department.json")

joined_df = employee_df.join(
    department_df,
    employee_df.emp_dept_id == department_df.dept_id,
    "inner"
)

joined_df.show()

result_df = joined_df.groupBy("dept_name") \
    .agg(
        max("salary").alias("maxSalary"),
        count("emp_id").alias("employeesCount")
    )

# result_df.show()
result_df.write \
    .mode("overwrite") \
    .format("parquet") \
    .partitionBy("dept_name") \
    .saveAsTable("part_department")

spark.sql("SELECT * FROM part_department").show()

spark.stop()





