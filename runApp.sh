#!/bin/bash
workdir="/usr/app"
#workdir=$PWD
$workdir/spark/bin/spark-submit --conf "spark.driver.extraJavaOptions=-Dlog4jspark.root.logger=WARN,console" $workdir/wine_testing.py $workdir/model_created.model  $@ 2>/dev/null
