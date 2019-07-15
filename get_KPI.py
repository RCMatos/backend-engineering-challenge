# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 23:11:17 2019

@author: Rodrigo
"""
import sys
time_unit=sys.argv[1]
time_val=int(sys.argv[2])
analysis_type=sys.argv[3]


#start data validation
if time_unit=="minutes":
    time_val=60*time_val
elif time_unit=="seconds":
    time_val=time_val
    
if analysis_type not in ["source_language","target_language","source_target_language","all_recs"]:
    raise ValueError("analysis type is not recognizable")

print("The records are being analysed")
print("The chosen slidding window is between:") 
print("      the timestamp of the input records")
if time_unit=="minutes":
    print("      the previous {} minutes".format(str(time_val)))
elif time_unit=="seconds":
    print("      the previous {} seconds".format(str(time_val)))
else:
    raise ValueError("Time unit is not recognizable:")
    raise ValueError("must be seconds or minutes")
    

#start analysis
from pyspark import SparkConf,SparkContext
import pyspark.sql as F
from pyspark.sql.functions import col,to_timestamp,avg,format_number
from pyspark.sql.window import Window

conf = SparkConf()
conf.setAppName("Unbabel_backend_challendge")


# create spark context with the above configuration
sc = SparkContext.getOrCreate()
spark = F.SparkSession(sc)
data_recs = sc.textFile("dummy_data.txt")
data_recs_dict_to_cols =spark.read.json(data_recs)

data_recs_dict_to_cols=data_recs_dict_to_cols.select(["translation_id","client_name","event_name","timestamp","source_language","target_language","nr_words","duration"])
data_recs_dict_to_cols=data_recs_dict_to_cols.withColumn("date",to_timestamp("timestamp", "yyyy-MM-dd HH:mm:ss"))

if analysis_type=="source_language":
    windowSpec = Window.partitionBy(["source_language"]).orderBy(col("date").cast('long')).rangeBetween(-time_val, 0)
    cols=["date","source_language","avg by date"]
elif analysis_type=="target_language":
    windowSpec = Window.partitionBy(["target_language"]).orderBy(col("date").cast('long')).rangeBetween(-time_val, 0)
    cols=["date","target_language","avg by date"]
elif analysis_type=="source_target_language":
    windowSpec = Window.partitionBy(["source_language","target_language"]).orderBy(col("date").cast('long')).rangeBetween(-time_val, 0)
    cols=["date","source_language","target_language","avg by date"]
elif analysis_type=="all_recs":
    windowSpec = Window.partitionBy().orderBy(col("date").cast('long')).rangeBetween(-time_val, 0)
    cols=["date","avg by date"]
data_recs_dict_to_cols = data_recs_dict_to_cols.withColumn("avg by date", avg("duration").over(windowSpec))
data_recs_dict_to_cols = data_recs_dict_to_cols.withColumn("avg by date", format_number(data_recs_dict_to_cols["avg by date"], 3))

data_final=data_recs_dict_to_cols.select(cols).dropDuplicates()
data_final=data_final.withColumn("date",col("date").cast("string")).toPandas().to_dict('records')

#save analysis
with open(analysis_type+"_out.txt","w") as file:
    for line in data_final:
        print(str(line))
        file.write(str(line)+"\n")
