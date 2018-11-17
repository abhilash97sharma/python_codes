from pyspark import SparkContext
from pyspark import SparkConf

sc = SparkContext("local","Reading_Textfile")
file = sc.textFile('/home/abhilash/Documents/files/file')
file.saveAsTextFile('hello',"json")
