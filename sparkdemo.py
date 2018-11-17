from pyspark import SparkContext
from pyspark import SparkConf

sc = SparkContext('local','FirstDemo')
data = sc.parallelize(1,2,3,4)
data1=data.map(lambda x:x+1)

print(data1.collect())