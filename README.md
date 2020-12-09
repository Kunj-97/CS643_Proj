# CS643_Proj


To run on EMR cluster without docker : 


Create a s3 bucket named cloud-proj2  and upload TrainingDataset.csv in it 

spark submit wine_modeling.py

cd test1

 in current folder use command (to download model that was uploaded by wine_modelling.py from s3 bucket) :
aws s3 cp s3://cloud-proj2/ . --recursive
  
 to run wine_testing.py add it with file paths for model followed by file path of your ValidationDataSet.csv
 
 Format : saprk-submit wine_testing.py model_file_name Test_Dataset.csv
 
eg : spark-submit wine_testing.py home/hadoop/test1/model_created.model home/hadoop/ValidationDataSet.csv







sudo docker build -t kunj97/cs-643 .

 sudo docker run -v  /home/hadoop/ValidationDataset.csv:/home/hadoop/ValidationDataset.csv  kunj97/cs-643  /home/hadoop/ValidationDataset.csv




For Docker : 
docker pull kunj97/cs-643:latest

sudo docker run -v  /home/hadoop/ValidationDataset.csv:/home/hadoop/ValidationDataset.csv  kunj97/cs-643  /home/hadoop/ValidationDataset.csv

Docker Id : https://hub.docker.com/repository/docker/kunj97/cs-643

