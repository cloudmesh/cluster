echo -e "Y" | sudo apt-get install pdsh
pdsh -R ssh -w $1,$2 sudo apt-get update
pdsh -R ssh -w $1,$2 echo -e "Y" | sudo apt-get install default-jdk
pdsh -R ssh -w $1,$2 wget http://www.us.apache.org/dist/hadoop/common/hadoop-2.5.0/hadoop-2.5.0.tar.gz
pdsh -R ssh -w $1,$2 tar -xzf hadoop-2.5.0.tar.gz
pdsh -R ssh -w $1,$2 mv hadoop-2.5.0 hadoop
pdsh -R ssh -w $1,$2 echo "export HADOOP_HOME=~/hadoop" >> .bashrc
pdsh -R ssh -w $1,$2 echo "export JAVA_HOME=/usr" >> .bashrc
pdsh -R ssh -w $1,$2 sudo chmod -R 777 hadoop
pdsh -R ssh -w $1,$2 source ~/.bashrc
#pdsh -R ssh -w $1 sudo shutdown -r now
