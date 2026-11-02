from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("SparkSession and SparkCOntext sample") \
    .master("local[*]") \
    .getOrCreate()

spark.conf.set("spark.sql.shuffle.partitions", "2")

sc = spark.sparkContext

print("Spark app name: ", sc.appName)
print("Spark master: ", sc.master)

df = spark.createDataFrame([("Alice", 34), ("Bob", 45)], ["name", "age"])

df.show()

spark.stop()