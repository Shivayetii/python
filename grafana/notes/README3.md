SECTION 1:

    1. What is Grafana ?

        Grafana is an open source interactive data-visualization platform or tool.
        it is developed by Grafana Labs, which allows users to see their,
        data via charts and graphs that are unified into one dashboard (or multiple dashboards!) 
        for easier to users understanding.

    2. Why we use Grafana ?

        1.Grafana is free open sources tool no need to pay any amount of any one

        2.Grafana is a provides beautiful visualizations.

        3.By using Grafana we can eaisly create our custom dashboards.

        4.Grafana, which runs as a web application, is used by small to large 
          enterprises to monitor visualizations. 

        5.Grafana will manage system reports ,metrics, logs and alerts.
    
        6.Grafana Integrates with set of data sources, like Prometheus,MySQL, Elasticsearch and Splunk.


    4. What is MYSQL ?

       MySQL is a Relational Database Management System (RDBMS) that offers a different type of features, including: It allows us to create tables, rows, columns, and indexes and to perform database operations on mysql . 

    5. Why use we MYSQL ?

       1. MYSQL is support Cross platform we can deploy mysql any platform like(linux,window,maccos) it will
          all operating systems.

       2. MYSQL is opensource platform so we not required to pay any amount of any one.

       3. MYSQL supports with mltiple languages (PHP,Python,Java etc).

       4. MYSQL is a RDBMS. 

       5. MYSQL is a fast,reliable,scalable and we can easy to use.

    6. What is candle stic?

       The candlestick is a panel  it will shows a chart  those are used to describe price movements.
       This chart are will comes  with while installation of Grafana. so we should not to required to install candle stic plug in separatly. 

    7. Why we use candle stic charts?
       
       1.In now a days mostly candle stic charts are used in trading sector.

       2. If we are using candle stic chart we can easily understand diagrams than compare to other charts.

       3. It will provide this ponts open stock , high price, low price and close price display very
          neatly on the charts.

SECTION 2:
---------

    # Install Docker Engine on Ubuntu 18.04

        * If we want to install Docker engine we need below prerequisites.

           * Prerequisites
             
             1. 64-bit kernel and CPU support for virtualization.

             2. KVM virtualization support

             3. systemd init system

             4. At least 4 GB of RAM.

        * If we want to install docker engine on Ubuntu 18.04 we should follow below commands.

           # if we have old version of docker first we should uninstall that version
             By using below command it will unintall old docker version in our VM

                1. sudo apt-get remove docker docker-engine docker.io containerd runc
           
           # Before you install Docker Engine for the first time on a new host machine,
             you need to set up the Docker repository for that we should run below commands one by one.

                1. sudo apt-get update

                2. sudo apt-get install ca-certificates curl gnupg lsb-release

           # After Docker repository installation is done we should add Docker’s official GPG key for that we
             should run below to commands one by one.

                1. sudo mkdir -p /etc/apt/keyrings
                
                2. curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg

           # Ater  Docker’s official GPG key installation is done we are able to set up Docker repository so
             by using below command we can set up docker repository.

                echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

           # install docker engine on Ubuntu we should run below four commands one by one

                1. sudo apt-get update

                2. sudo chmod a+r /etc/apt/keyrings/docker.gpg

                3. sudo apt-get update

                4. sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin

           # To Verify that the Docker Engine installation is successful by or not for that
             we can run below command.

                1. docker run hello-world
SECTION 3:
---------
  
    # Deploying Grafana  by using docker

          * If we want to deploy Grafana we need below prerequisites.

             * Prerequisites
               
               1. Docker official image for Grafana

               2. Docker engine on your VM

               3. Docker Hub 

           # If we want to deploy Grafana we should follow below steps one by one.

               # When ever we want to deploy any application by using Docker first we need pull that particular
                 official image from docker-hub in our case we need grafana by using below command we are able 
                 to pull the image from docker-hub

                       docker pull grafana/grafana

               # If we want see on your VM the image is pull or not from docker-hub we can use below command

                       docker images

               # Then next step is that image we should crate container and run that conatiner we can this container
                 default networks and as well as custom networks if we want to run container in default network we can run below command.
                       
                       docker run --name <conatiner_name> -d -p hostport:conatinerport imagename

                       Ex: docker run --name gpmgrafana -d -p 3000:3000 grafana/grafana
                
               # In our case we are running our conatiner in custom network so for that first we should create 
                 one custom network by using below command we can create custom network in our VM by using docker.

                       docker network create <network_name>

                       Ex: docker network create gpm

               # If we want to see how many networks we have in our VM we can use below command.
                      
                       docker network ls 

               # If we want to deploy our container in custom network we can use below command.

                      docker run --name <container_name> -d --net <network_name> -p hostport:conatinerport image name

                      Ex: docker run --name Grafana -d --net gpm -p 3000:3000 grafana/grafana

               # If we want to see how containers are in running state in our VM we can use below command.

                      docker ps

                # If we want to see how containers are in running and stoped stated in our VM 
                  we can use below command.

                      docker ps -a
SECTION 4:
---------
  
    # Deploying  mysql by using docker

          * If we want to deploy Postgres we need below prerequisites.

             * Prerequisites
               
               1. Docker official image for Postgres

               2. Docker engine on your VM

               3. Docker Hub 

           # If we want to deploy Postgres we should follow below steps one by one.

               # When ever we want to deploy any application by using Docker first we need pull that particular
                 official image from docker-hub in our case we need  postgres by using below command we are able 
                 to pull the image from docker-hub

                       docker pull  mysql

               # If we want see on your VM the image is pull or not from docker-hub we can use below command

                       docker images

               # Then next step is that image we should crate container and run that conatiner we can this container
                 default networks and as well as custom networks if we want to run container in default network we can run below command.
                       
                       docker run --name <conatiner_name> -d -p hostport:conatinerport imagename

                       Ex: docker run --rm -d --name gpmmysql -e MYSQL_ROOT_PASSWORDD=root -p 3306:3306 mysql
                       
                
               # In our case we are running our conatiner in custom network so for that first we should create 
                 one custom network by using below command we can create custom network in our VM by using docker.

                       docker network create <network_name>

                       Ex: docker network create gpm

               # If we want to see how many networks we have in our VM we can use below command.
                      
                       docker network ls 

               # If we want to deploy our container in custom network we can use below command.

                      docker run --name <container_name> -d --net <network_name> -p hostport:conatinerport
                      -v hostpath:container dir image name

                      Ex: docker run --rm -d --name gpmmysql -e MYSQL_ROOT_PASSWORDD=root -e MYSQL_DATABASE=mysql_db -e MYSQL_USER=gpm_master -e MYSQL_USER_PASSWORD=gpm_master@1200 -v /opt/cicd/jira_416/timescale/csv/tests/:/opt/csv/tests/ --network gpmnw -p 3306:3306 mysql/mysql-server:latest


               # If we want to see how containers are in running state in our VM we can use below command.

                      docker ps

                # If we want to see how containers are in running and stoped stated in our VM 
                  we can use below command.

                      docker ps -a
SECTION 5:
---------
    Login or Enter inside Posrgres conatiner and tasks.
       
       * Before we should do below operations to configure or add postgres Sql database as a Grafana.

               # By using below command we are able to enter into the postgres conatiner

                      docker exec -it <conatiner_name or conatiner_id> bash

                      Ex: docker exec -it eddd9d90f66d  bash
                
                # By using above command we just enter inside the conatiner
                  we unable to do pefrom postgres Sql operationsfor that we should login postgres with default user by defualt user is postgres for that we can run below command.

                      mysql -u user_name -p enter and enter the user password

                      EX: mysql -u gpm_master -p enter and the gpm_master password
              
                 # We shoud makes give all permmission to the user what did we create 

                      GRANT ALL PRIVILEGES ON *.* TO 'user_name'@'localhost' WITH GRANT OPTION;

                      GRANT ALL PRIVILEGES ON *.* TO 'gpm_master'@'%' WITH GRANT OPTION;

 
                # After accessing postgres Sql we should create user for that we can run below command.
                   
                      CREATE USER "user_name"@"localhost" IDENTIFIED BY "user_password" 

                      Ex: CREATE USER "gpm_admin"@"10.74.190.101" IDENTIFIED BY "gpm_admin@1300"

               # Above the what ever user we are create we should make that user as a super user
                 for that we run below command.

                      GRANT ALL PRIVILEGES ON *.* TO 'user_name'@'localhost' WITH GRANT OPTION;

                      EX: GRANT ALL PRIVILEGES ON *.* TO 'gpm_admin'@'localhost' WITH GRANT OPTION;

               # We should create one database for that we can run below command.

                      create database gpm;

               # What ever database we created, We should make connect and provide 
                 all privileges access of the specific user of that specific database we can run below two commands one by one
                  
                      GRANT PRIVILEGE ON database_name.table_name TO 'username'@'localhost';
                      
                      EX: GRANT PRIVILEGE ON gpm.jira TO 'gpm_admin'@'localhost';

               # We should switch the your data base for that we can use below command

                      use database_name

                      Ex: use gpm

               # After we should create one table for that we can use below command.

                      CREATE TABLE IF NOT EXISTS jira (
                         time TIMESTAMPTZ NOT NULL,
                         open DOUBLE PRECISION NULL,
                         high DOUBLE PRECISION NULL,
                         low DOUBLE PRECISION NULL,
                         close DOUBLE PRECISION NULL,
                         volume INT NULL,
                         avg DOUBLE PRECISION NULL
                         );

               # We should retrive all employees data from host mechine for that we can below command.

                      COPY jira(time,open,high,low,close,volume,avg)
                      FROM '/opt/csv/tests/ohlc.csv'
                      DELIMITER ','
                      CSV HEADER;
               # By using command we can check data is retrive or not in our table
                    
                      select * from jira limit 10;
               
               # By using below command we are able switch particular database in our mysql.

                      use database_name

                      Ex: use gpm

               # By using below command we are able list out the all users in our mysql.

                      select Host,User from mysql.user; or select host,user,password from mysql.user;

                      FLUSH PRIVILEGES;

SECTION 6:
---------

    # Grafana UI Access

        1.  http://10.74.190.101:3000
        
       
SECTION 7:
---------

    # Configure Postgres Sql as a database of Grafana.

               * Login Grafana on broswer with user name and password.

               * Click on setting symbole

               * Click on data sources

               * Click on add data sources as postgres Sql and give name of the database what ever we want

               * then provide below artibutes one by one under PostgreSQL Connection

                    * Host - We should provide  URL of the postgres Sql wheather your postgres is running.

                    * We should provide databse on database row

                    * Next we shoud provide user_name with password of the particular user

                    * TLS/SSL Mode row click on disable

                    * finally click on save and test

     # While adding Postgres Sql as databas to Grafana if are getting below error like this 
       db query error: failed to connect to server - please inspect Grafana server log for details.

               * We should go to linux terminal and inspect the our postgres Sql container and replace
                 instead of local host Ip to our conatiner Ip while running the conatiner we will get one IP for
                 the container we have to takes that IP only.

               * If we want to inspect our conatiner in our VM we can use below command.
                  
                  docker inspect  container <container_name or container_id>

                  Ex: docker inspect 05f1b63567bd

SECTION 8:          
---------

# References

 https://www.redhat.com/en/topics/data-services/what-is-grafana

 https://aws.amazon.com/rds/postgresql/what-is-postgresql/

 https://docs.docker.com/engine/install/ubuntu/

 https://grafana.com/docs/grafana/v9.3/panels-visualizations/visualizations/candlestick/

 https://hevodata.com/learn/grafana-postgresql/



