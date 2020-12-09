#creation of model using mllib 
from pyspark.mllib.linalg import Vectors
from pyspark.ml.regression import RandomForestRegressor
from pyspark.mllib.regression import LabeledPoint
from pyspark import SparkContext, SparkConf
from pyspark.sql.session import SparkSession	
from pyspark.ml.classification import RandomForestClassifier
from pyspark.mllib.tree import RandomForest






spark_session = SparkSession.builder.appName('wine_model').getOrCreate()
file1 = spark_session.read.csv('s3://cloud-proj2/TrainingDataset.csv',header='true', inferSchema='true', sep=';')
select_col = [c for c in file1.columns if c != 'quality']


data_set= file1.rdd.map(lambda row: LabeledPoint(row[-1], Vectors.dense(row[0:-1])))
# model = LogisticRegression.trainClassifier(transformed_df,numClasses=10,categoricalFeaturesInfo={}, numTrees=50, maxBins=64, maxDepth=20, seed=33)
# LogisticRegression.trainClassifier()
# LogisticRegression()
#   .setMaxIter(10)
#   .setRegParam(0.3)
#   .setElasticNetParam(0.8)
#   .setFamily("multinomial")
model = RandomForest.trainClassifier(data_set,numClasses=10,categoricalFeaturesInfo={}, numTrees=50, maxBins=64, maxDepth=20, seed=33)
model.save(spark_session.sparkContext,"s3://cloud-proj2/model_created.model")

