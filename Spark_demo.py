from pyspark import SparkContext
from pyspark import SQLContext
from pyspark import SparkConf
from pyspark.sql import SparkSession
sc=SparkContext(SparkConf().setAppName("Spark_demo").setMaster("local"))
sqlContext = SQLContext(sc)
sparksession = SparkSession.builder.master("local").appName("Spark_demo").getOrCreate()
print("hello abhilash")



#from pyspark import SparkContext
#from pyspark.sql import SQLContext
#from pyspark.sql.functions import translate
#import pyspark.sql.functions as f
#import re
#def parseLine(line):
#    s1 = re.sub('[#@]', '', line)
#    return s1
#sc = SparkContext("local","Reading_csv_data")
#sqlContext = SQLContext(sc)
#file1=sqlContext.read.csv('file:///home/abhilash/Downloads/data.csv',header="true")
#file1.select("type", f.translate(f.col("type"), "RT@,", "XXX").alias("replaced")).show()
#file1.show()
