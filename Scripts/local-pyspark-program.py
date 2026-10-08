from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("My First Spark App") \
    .getOrCreate()

print("Spark Session created successfully!")

print("Spark version:", spark.version)

data = [("Alice", 34), ("Bob", 45), ("Cathy", 29)]

df = spark.createDataFrame(data, ["name", "age"])

df.show()

spark.stop()