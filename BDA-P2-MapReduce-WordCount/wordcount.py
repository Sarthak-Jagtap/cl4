from pyspark import SparkContext

sc = SparkContext("local", "WordCount")

text_file = sc.textFile("input.txt")

counts = (text_file
          .flatMap(lambda line: line.split(" "))
          .map(lambda word: (word, 1))
          .reduceByKey(lambda a, b: a + b))

counts.saveAsTextFile("output")
