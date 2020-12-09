# CS643_Proj


To run on EMR cluster without docker : 


Create a s3 bucket named cloud-proj2  and upload ModellingDataset.csv, TrainingDataset.csv , wine_testing.py and wine_modelling.py in it 

spark submit wine_modeling.py #saves the model in the s3 bucket



 in current folder use command (to download model that was uploaded by wine_modelling.py from s3 bucket if not present) :
 
aws s3 cp s3://cloud-proj2/ . --recursive
  
 to run wine_testing.py add it with file paths for model followed by file path of your ValidationDataSet.csv
 
 Format : saprk-submit wine_testing.py model_file_name Test_Dataset.csv
 
eg : spark-submit wine_testing.py home/hadoop/test1/model_created.model home/hadoop/ValidationDataSet.csv


( If the testing file doesnt work  in main folder dont work due to file_path , head over to "Code_without_docker" folder )
to run this file use command ( loads modelfile from S3 bucket)

spark-submit wine_testing.py 


### For Docker : 

Download spark 3.0 tar and untar it in "spark" folder in the current directory.

sudo docker build -t kunj97/cs-643 .

 sudo docker run -v  /home/hadoop/ValidationDataset.csv:/home/hadoop/ValidationDataset.csv  kunj97/cs-643  /home/hadoop/ValidationDataset.csv


docker pull kunj97/cs-643:latest
##### Run Docker Container with file path to ValidationDataset.csv as parameters ( sudo docker run -v file_path:file_path kunj97/cs-643 file_path)
sudo docker run -v  /home/hadoop/ValidationDataset.csv:/home/hadoop/ValidationDataset.csv  kunj97/cs-643  /home/hadoop/ValidationDataset.csv

Docker Image : https://hub.docker.com/r/kunj97/cs-643/tags?page=1&ordering=last_updated

