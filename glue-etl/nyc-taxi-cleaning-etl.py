import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.dynamicframe import DynamicFrame
from pyspark.sql.functions import col, when, unix_timestamp

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)


#Create dynamic frame from the catalog 
raw_data = glueContext.create_dynamic_frame.from_catalog(
    database= "nyc_taxi_db",
    table_name= "nyc_taxi_raw_zone"
    )
    
#creating a dataframe of the raw data(dynamic frame)
df = raw_data.toDF()

#Renaming Columns
df = df.withColumnRenamed("tpep_pickup_datetime", "pickup_datetime")
df = df.withColumnRenamed("tpep_dropoff_datetime", "dropoff_datetime")

#cleaning the Data by handling missing values and outliers
df = df.filter((col("trip_distance")>0) & (col("trip_distance")< 500))
df = df.filter((col("passenger_count")>0) & (col("passenger_count")<= 6))
df = df.filter((col("fare_amount")>0) & (col("fare_amount")< 1000))

#Adding columns for data readability
df = df.withColumn("payment_type_name",
    when(col("payment_type")== 1, "credit_Card")
    .when(col("payment_type")== 2, "cash")
    .when(col("payment_type")== 3, "no_charge")
    .when(col("payment_type")== 4, "dispute")
    .otherwise("other")
    )

df = df.withColumn("trip_distance",
    when(col("trip_distance")<1, "short")
    .when((col("trip_distance")>=1) & (col("trip_distance")<5), "medium")
    .when((col("trip_distance")>=5) & (col("trip_distance")<10), "long")
    .otherwise("very_long")
)


cleaned_data = DynamicFrame.fromDF(df, glueContext, "cleaned_data")

# cleaned_data = Filter.apply(
#     frame= dynamic_frame,
#     f= lambda x: (x["total_amount"] > 0 and x["total_amount"] is not None)
#     )

#write data to s3
glueContext.write_dynamic_frame.from_options(
    frame= cleaned_data,
    connection_type="s3",
    connection_options= {"path": "s3://nyc-taxi-curated-zone/cleaned_data/"},
    format= "parquet"
    )

job.commit()
