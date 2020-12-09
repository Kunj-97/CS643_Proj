FROM centos

WORKDIR /usr/app/

COPY . . 

RUN yum -y update && yum -y install python38 java-11-openjdk.x86_64

RUN ln -s /usr/bin/python3 /usr/bin/python && ln -s /usr/bin/pip3 /usr/bin/pip &&  pip install numpy &&  pip install PrettyTable

#ENTRYPOINT ["/usr/app/spark/bin/spark-submit", "--conf", "spark.driver.extraJavaOptions=-Dlog4jspark.root.logger=WARN,console", "/usr/app/wine_testing.py", "/usr/app/model_created.model"]

ENTRYPOINT ["/usr/app/runApp.sh"] 
