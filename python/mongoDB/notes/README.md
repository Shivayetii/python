SECTION 1:
---------

    1. What's MongoDB ?

        MongoDB is an open-source document-oriented database.
        that is designed to store a large scale of data.
        and also allows you to work with that data very efficiently that is called as MongoDB

    2. why use MongoDB
        * MongoDB is a open source tool no needs to pay any money to anyone
        * MongoDB makes use of collections and documents.
        * Inside of the collection we have documents. 
        * These documents contain the data we want to store in the MongoDB database.
        * Documents consist of key-value pairs which are the basic unit of data in MongoDB.
        * The data stored in the MongoDB is in the format of BSON documents. 
        * BSON stands for Binary representation of JSON documents.
        * High availability
        * Horizontal scaling
        * Built-in security
    
    3. What's mongo-shell?

        MongoDB Mongo shell is an interactive JavaScript interface.
        that allows you to interact with MongoDB instances through the command line. 
        that is called as the mongoDB shell

    4. why use MongoDB shell(benifits of MongoDB shell)
      
        * We can run all MongoDB queries from the Mongo shell.
        * We can Manipulate data and perform administration operations.
        * Mongo shell uses JavaScript and a related API to issue commands.
        * We can see previous commands in the mongo shell with up and down arrow keys.
        * We can View possible command completions using the tab button after partially entering a command.
        * It will print error messages, so you know what went wrong with your commands.
    
    5. Install MongoDB Community Edition on Ubuntu.

       * We need to follow below these steps to install MongoDB Community Edition using the apt package manager.
       
         * First we need to Import the public key it is used by the package management system, the command is.

                wget -qO - https://www.mongodb.org/static/pgp/server-6.0.asc | sudo apt-key add -

                Note: the above the command is correct it will show output is OK

         * However, if you receive an error  indication in system we don't have gnupg package
           by using below command we can install gnupg.

                sudo apt-get install gnupg

        * Once gnupg installation is done we can retry to install importing the key.

                wget -qO - https://www.mongodb.org/static/pgp/server-6.0.asc | sudo apt-key add -
       
        * After import key installation is done if we are run below this command it will shows the
          mongoDB shell which version is running on or system.

               lsb_release -dc.

        * We need to create a list file for MongoDB for that we can run below command
         
               echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/6.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-6.0.list

        * We need to updated the ubuntu system for that we can run below command.

               sudo apt-get update

        * To install the latest stable version of MongoDb for that we can run below command.

               sudo apt-get install -y mongodb-org

        * To start the MongoDB shell for that we can below commands one by one.

               1. sudo systemctl daemon-reload

               2. sudo systemctl start mongod

        * We can Verify that MongoDB has shell started or not for that we can run below command.

               sudo systemctl status mongod

        * If we want to enable mongoDB you can use below command.

               sudo systemctl enable mongod

        * If we want to stop mongoDB shell we can use below command.
            
               sudo systemctl stop mongod
    
        * If we want to restart mongoDB shell we can use below command.

              sudo systemctl restart mongod
        
        * If we want uninstall mongoDB we can use below command one by one.

              1. sudo service mongod stop

              2. sudo apt-get purge mongodb-org*

        * If we want to remove mongodb database library files and log files we can use below commands one by one.

              1. sudo rm -r /var/log/mongodb
              2. sudo rm -r /var/lib/mongodb

            1. LOGIN TO MONGO-SHELL

              * After installation of MongoDB shell in linux by using below command we can log in Mongo shell.

                 VM Ipaddress:MongoDB default PortNo

                 EX: 10.74.190.101:27017

            2. RUN SAMPLE COMMANDS

               1.  MongoDB Commands Listing (Common Line Options):

                   There are no of options provided by MongoDB but in this sectio we use most common options of MongoDB when used in conjunction with the MongoDB shell startup, to work with MongoDB database server.

                     * If we want to list all the available options that can be used while starting up 
                       the MongoDB Shell we can use below command.

                         --help

                    * If we want to specifies to start the MongoDB shell connecting to any database
                      we can use below command.

                         --nodb

                    * If we want to specifies to start the shell after running any specific *.js files earlier
                      we can use below command.

                         --shell

                    * If we want to specifies the version information of the MongoDB shell during startup
                      we can use below command.

                         --version

                    * If we want to starts the MongoDB shell with not many chatty messages we can use below command.

                         --quiet

                2. MongoDB Commands Listing (Command Helpers):

                   There are various command helpers available for the MongoDB shell (mongo). we can use most commonly used help commands when ever we are using MongoDB shell.

                    * If we want shows help related information on the MongoDB shell we can use below command.

                         help

                    * If we want to shows help related information on the database methods in  
                      MongoDB shell we can use below command.

                         db.help()

                    * If we want to show in server the existing collection is available or not by using below 
                      help command we can find.

                         db..help

                    * If we want to list all the databases available for use on the connected MongoDB instance

                      we can use below command.

                         show dbs
                            or
                         show databases

                    * If we want to switch the specific database or create new database.
                      in MongoDB shell we can use below command.

                         use

                    * If we want to list all the collections available for use on the current database
                      we can use below command.

                         show collections

                    * If we want to list all the users available on the current database
                      we can use below command.

                         show users

                    * If we want to lists all the roles (both built-in roles and user-defined roles)
                      on the current database we can use below command.

                         show roles

                    * If we want to list the last 5 recent operations that took 1 millisecond or more
                      we can use below command.

                         show profile

                    * If we want to executes a specified javascript file we can use below command.

                         load()
                  
                  3. MongoDB Commands Listing (Administrative Command Helpers):

                    This below commands help full to us, we can get  online on MongoDB and do some administrative tasks on MongoDB. This section specifically works upon the administrative tasks on databases created within the MongoDB database server. The most commonly used commands are provided in below.

                   * If we want to clone current database in our MongoDB shell we can use below command.

                         db.cloneDatabase()

                   * If we want to copy one collection to another collection in MongoDB we can use below command.

                       db.collection1.copyTo("collection2")

                  * If we want to repaire database in MongoDB shell we can use below command.

                     db.repairDatabase_Name()

                  * If we want to  a list of collections available in the current database as a list 
                     we can use below command.

                       db.getCollectionNames()

                  * If we want to drop current database in MongoDB shell we can use below command.

                     db.dropDatabase_Name()

              4. MongoDB Commands Listing (Basic Shell JS Operations):
                
                MongoDB provides a rich collection of Javascript API for database related operations. DB is the mongo shell variable that holds the current database. The variable is reset to when the command is used, until then it points to the test database.

                Some of the commonly used commands for  Javascript operations.

                  * If we want to authenticates the user and if the MongoDB shell is running in a secure mode
                    we can use below command.

                     db.auth()

                  * If we want to Assign a specific collection ‘myCollection’ 
                    to the variable ‘myCollectionVariable’, as shown in the example below:

                       myCollectionVariable = db.myCollection;

                  * If we want to finds all the documents in a specific collection we can use below command.

                     db.collection.find()

                     EX: db.myCollection.find()

                  * If we want to insert one document into the specific collection we can use below command.

                     db.collection.insertOne()

                  * If we want to insert multiple document into the specific collection we can use below command.

                     db.collection.insertMany()

                  * If we want to Updates one single document in the specified collection we can use below command.

                     db.collection.updateOne()

                  * If we want to Updates multiple documents in the specified collection we can use below command.

                     db.collection.updateMany()	

                  * If we want to Inserts a new document into the collection if it doesn’t exists, 
                    and if it exists  updates the document in the collection we can use below command.

                     db.collection.save()

                  * If we want to deletes one document from the collection we can use below command.

                     db.collection.deleteOne()

                  * If we want to deletes multiple document from the collection we can use below command.

                     db.collection.deleteMany()

                  * If we want to drop or remove the collection entirely from the database we can use below command.

                     db.collection.drop()

                  * If we want to creates a new index on the collection specified via the command, 
                    if it doesn’t  exist. If the index already exists, then there is no effect of this command over the collection specified by the command.

                     db.collection.createIndex()

                        
SECTION 2:
---------

    # Deploying MongoDB using Dockers

        1. Docker Image name
        
        * If we want to deploy MongoDB in our system or VM we need to follow below steps and commands.
           
           * First We have to Docker installed in your system. If not done already
              you can download it from the Official Docker website.

           * If you installed docker in your system by using below command 
             you can check docker is running or not
             
              service docker status

           * Second one is  docker-hub account or docker-hub authentication credentials.

           * In docker-hub registry available the latest official images.

           * In our case we  need to deploy MongoDB image for that by we need to pull the image from docker-hub.

           * If we want to deploy our image in our custom-network first we need to create network we can also.
             
             deploy our image in default network for that no need to create any network by using normal commands

             we can access appliction.

              * first step is pull image

                * If we want to downlod latest MongoDB docker image in our VM we can use below command.

                  sudo docker pull mongo:latest

                * If we want to downlod specific MongoDB docker image in our VM we can use below command.

                  sudo docker pull mongo:4.2.2

               * If we want to check the Docker images download in your system or not 
                 you can run the below  command.

                  docker images

            * second step is create container and run that container.
            
               * If we want to run our container in detach mode (Background process) we can run below this command.

                 docker run --name mongodb -d mongo

               *  If we want to access that application in broswer you can run below this command. 

                  sudo docker run --name mongodb -d -p 27017:27017 mongo:latest           

              * access the application by using IPaddress and container-port-number

                IP:container-port-number

            * If we want to deploy our MongoDB is our custom network firt we need to create custom network.

              * By using below command we can create or custom net-work.
             
                docker network create <Network_Name>

        2. Create Docker Container and run that container in custom network.
        
           docker run --name <containername> --net <Network_Name> -p 27017:27017 mongo

          * MongoDB default port number is 27017.

             We can access the MongoDB UI Access using localhost:27017 or VM_IP:27017

SECTION 3:
---------

    # Deploying MongoDBusing Kubernetes

      * when ever we want to deploy  any pod in kubernetes we have to create namesapce we can deploy pods.
        
        deafult namesoace also in our case our logstash pod is deploy in specific name-sapce, so we are create

        name-sapce.

        * By using below command we can create specific namespace.
         
          kubectl create namespace <namespace_name>

        1. Deployment Spec

           * By using below we can create Deployment yml file for MongoDB.

              vi deployment.yml

           * By using below command to deploy MongoDB specified namespace.

              kubectl apply -f deployment.yml -n <Namespace-Name>
        
        Sample deployement yml file for MongoDB
        ****************************************

        apiVersion: apps/v1
        kind: Deployment
        metadata:
        labels:
        app: mongo
        name: mongo
        namespace: mongodb
        spec:
        replicas: 1
        selector:
        matchLabels:
            app: mongo
        template:
            metadata:
            labels:
                app: mongo
            spec:
            containers:
                - name: vude-mongo-c
                image: mongo:4.4.6
                env:
                - name: MONGO_INITDB_ROOT_USERNAME
                    value: vudeadmin
                - name: MONGO_INITDB_ROOT_PASSWORD
                    value: vudeshardis001
                - name: MONGO_INITDB_DATABASE
                    value: admin
                imagePullPolicy: IfNotPresent
                ports:
                    - containerPort: 27017
                    name: httpm
                    protocol: TCP
                volumeMounts:
                    - mountPath: /data/db
                    name: vude-mongo-v
            volumes:
                - name: vude-mongo-v
                hostPath:
                    path: /opt/assignments/

        2. Service Spec

           * By using below we can create service yml file for MongoDB.

              vi service.yml

           * By using below command to deploy MongoDB specified namespace.

              kubectl apply -f service.yml -n <Namespace-Name>

              * logstash UI Access using localhost:Nodeport or VM_IP:Nodeport

        Sample service yml file for MongoDB
        ************************************
        apiversion: V1
        kind: service
        metadata:
        name: mongo
        labels:
            app: mongo
        spec:
        selector:
            app: mongo
        type: NodePort
        ports:
        - nodeport: 31000
            targetport: 27017 
  
        3. kubectl commands for debug

           * By using below command we can describe the pod in specified namespace.

              kubectl describe  pod <pod-name> -n <namespace-name>

           * By using below command we can edit the pod in specified namespace.

              kubectl edit  pod <pod-name> -n <namespace-name>

          *  By using below command we can describe the service in specified namespac.

              kubectl describe  svc <svc-name> -n <namespace-name>  

          *  By using below command we can edit the service in specified namespac.

              kubectl edit  svc <svc-name> -n <namespace-name>   

SECTION 4:
---------

    # Deploying MongoDB using HELM

        1. HELM Charts

        2. HELM commands for bring-up

        3. HELM commands for debug

SECTION 5:
---------

    # Verification post installation

        1. Access logstash in UI

           we can access MongoDB in two ways

             * By using VMIP:ContainerPortNo

             * By using VMIP:NodePortNo

        2. CREATE/DELETE/UPDATE 

          * What Does CRUD Mean in MongoDB?

            * A CRUD operation in MongoDB describes a user interface that allows users to view, search, and modify data in a database.

            * CRUD stands for Create,Read,Update and Delete.
            * Create inserts new documents into the MongoDB database.
            * Read operation is used to retrieve documents from a database.
            * Update operation modifies existing documents in the database.
            * Delete operation removes documents from a database.

            * C-Create Operation
            ********************

                * Data is stored in MongoDB as JSON objects. 

                * The records for a collection in MongoDB are referred to as documents.

                * There are two ways you can add documents to a MongoDB collection.

                * db.collection.insert_one()
                * db.collection.insert_many()

            * insert_one():
            ************
                . insert_one() facilitates the insertion of a single document into a collection. 
                . we are working with a collection called SalesDB in this example.   

                db.SalesDB.insert_one({
                    name: "Linda",
                    orderdate: "6/10/2021",
                    species: "Dog",
                    ownerAddress: "380 W. Fir Ave",
                    chipped: true
                })

                . Above successful completion of the create operation a new document is created.
                . The function will return an object whose "acknowledged" attribute is "true" and whose "insertedID" attribute is the newly created "ObjectId."

                db.SalesDB.insert_one({
                    name: "Linda",
                    orderdate: "6/10/2021",
                    species: "Dog",
                    ownerAddress: "380 W. Fir Ave",
                    chipped: true
                })
                {
                        "acknowledged" : true,
                        "insertedId" : ObjectId("5fd989674e6b9ceb8665c57d")
                }
            * insert_many():
            ****************
                * Using the insert_many() method on a collection it is possible to insert multiple documents at the same time.

                db.SalesDB.insert_many([{
                    name: "Linda",
                    orderdate: "6/10/2021",
                    species: "Dog",
                    ownerAddress: "380 W. Fir Ave",
                    chipped: true},
                    {name: "Kitana", 
                    orderdate: "6/10/2021", 
                    species: "Cat", 
                    ownerAddress: "521 E. Cortland", 
                    chipped: true}])

                db.SalesDB.insert_many([{ name: "Linda", orderdate: "6/11/2021", species: "Dog", 
                ownerAddress: "380 W. Fir Ave", chipped: true}, {name: "Kitana", orderdate: "6/11/2021", 
                species: "Cat", ownerAddress: "521 E. Cortland", chipped: true}])
                {
                        "acknowledged" : true,
                        "insertedIds" : [
                                ObjectId("5fd98ea9ce6e8850d88270b4"),
                                ObjectId("5fd98ea9ce6e8850d88270b5")
                        ]
                }
            * R-Read Operation:
            *******************
                * There are two ways to read documents from a collection in MongoDB:

                * db.collection.find()
                * db.collection.find_one()

                - find():
                **********
                . On a collection to get all the documents within it.
                . Using the find() method without any arguments will return all records in the collection.

                db.SalesDB.find():
                *******************
                { "_id" : ObjectId("5fd98ea9ce6e8850d88270b5"), "name" : "Kitana", "orderdate" : "6/10/2021", "species" : "Cat", "ownerAddress" : "521 E. Cortland", "chipped" : true }
                { "_id" : ObjectId("5fd993a2ce6e8850d88270b7"), "name" : "Marsh", "orderdate" : "6/10/2021", "species" : "Dog", "ownerAddress" : "380 W. Fir Ave", "chipped" : true }

                . The "ObjectId" assigned to every record is mapped to the "_id" key.
                . When performing a read operation you can use filtering criteria to narrow your search to a desired subsection of the records.
                . Searching by value is one of the most common ways to filter the results.

                db.SalesDB.find({"species":"Cat"})
                { "_id" : ObjectId("5fd98ea9ce6e8850d88270b5"), "name" : "Kitana", "orderdate" : "6/10/2021", "species" : "Cat", "ownerAddress" : "521 E. Cortland", "chipped" : true }

            * find_one():
            **************
                * If we only want one document that meets the search criteria then we can use the find_one() method on the collection

                db.{collection}.find_one({query}, {projection})

            * U-Update Operation
                * update operations operate on a single collection. 
                * Filters and criteria are used to select the documents to be updated in an update operation.
                * Document updates are permanent and cannot be rolled back. 
                * Be careful when updating documents. This also applies to deleting documents.

                * MongoDB CRUD allows users to update documents in three different ways:
                    * db.collection.update_one()
                    * db.collection.update_many()
                    * db.collection.replace_one()

                * update_one():
                ****************
                    * By performing an update_one() operation, we can change a single document and update a record. 
                    * To update a document two arguments need to be provided an update filter and an update action.
                    * Update filters specify which items should be updated, and update actions specify how to do so.

                    db.SalesDB.update_one({name: "Marsh"}, {$set:{ownerAddress: "451 W. Coffee St. A204"}})

                    { "acknowledged" : true, "matchedCount" : 1, "modifiedCount" : 1 }

                    { "_id" : ObjectId("5fd993a2ce6e8850d88270b7"), "name" : "Marsh", "orderdate" : "6/10/2021", "species" : "Dog", "ownerAddress" : "451 W. Coffee St. A204", "chipped" : true }
                                    
                * update_many():
                ***************
                    * The update_many() function allows us to update multiple documents by passing in a list of items.just as we did when we inserted multiple items.

                    db.SalesDB.update_many({species:"Dog"}, {$set: {age: "5"}})

                    { "acknowledged" : true, "matchedCount" : 3, "modifiedCount" : 3 }

                    db.SalesDB.find()
                    { "_id" : ObjectId("5fd98ea9ce6e8850d88270b5"), "name" : "Kitana", "orderdate" : "6/10/2021", "species" : "Cat", "ownerAddress" : "521 E. Cortland", "chipped" : true }
                    { "_id" : ObjectId("5fd993a2ce6e8850d88270b7"), "name" : "Marsh", "orderdate" : "6/10/2021", "species" : "Dog", "ownerAddress" : "451 W. Coffee St. A204", "chipped" : true }

                * replace_one():
                **************
                    * The replace_one() method replaces a single document in a collection.
                    * The replace_one() method replaces a document's entire contents,so fields not found in the new document will be lost.

                    db.SalesDB.replace_one({name: "Kevin"}, {name: "Maki"})

                    { "acknowledged" : true, "matchedCount" : 1, "modifiedCount" : 1 }

                    db.SalesDB.find()
                    { "_id" : ObjectId("5fd98ea9ce6e8850d88270b5"), "name" : "Kitana", "orderdate" : "6/10/2021", "species" : "Cat", "ownerAddress" : "521 E. Cortland", "chipped" : true }
                    { "_id" : ObjectId("5fd993a2ce6e8850d88270b7"), "name" : "Marsh", "orderdate" : "6/10/2021", "species" : "Dog", "ownerAddress" : "451 W. Coffee St. A204", "chipped" : true }

            * D-Delete Operation:
            ********************
                * The delete operation operates on a single collection like the update and create operations. 
                * Deletes are also atomic for a single document. 

                * There are two ways to delete records from a collection in MongoDB:
                * db.collection.delete_one()
                * db.collection.delete_many()

                - delete_one()
                ************
                    * The delete_one() method is used to remove a document from a MongoDB collection. 
                    * The document to be deleted is specified by a filter. Only records matching the specified filter are deleted.

                    db.SalesDB.delete_one({name:"Maki"})

                    { "acknowledged" : true, "deletedCount" : 1 }

                    db.SalesDB.find()
                    { "_id" : ObjectId("5fd98ea9ce6e8850d88270b5"), "name" : "Kitana", "orderdate" : "6/10/2021", "species" : "Cat", "ownerAddress" : "521 E. Cortland", "chipped" : true }
                    { "_id" : ObjectId("5fd993a2ce6e8850d88270b7"), "name" : "Marsh", "orderdate" : "6/10/2021", "species" : "Dog", "ownerAddress" : "451 W. Coffee St. A204", "chipped" : true }
                    { "_id" : ObjectId("5fd993f3ce6e8850d88270b8"), "name" : "Loo", "orderdate" : "7/10/2021", "species" : "Dog", "ownerAddress" : "380 W. Fir Ave", "chipped" : true }
                
                * delete_many()
                ****************
                    * A single delete operation is used to delete multiple documents from a desired collection with delete_many(). 

                    db.SalesDB.delete_many({species:"Dog"})

                    { "acknowledged" : true, "deletedCount" : 2 }

                    db.SalesDB.find()
                    { "_id" : ObjectId("5fd98ea9ce6e8850d88270b5"), "name" : "Kitana", "orderdate" : "6/10/2021", "species" : "Cat", "ownerAddress" : "521 E. Cortland", "chipped" : true }



        3. kubectl commands for MongoDB

          * By using below command we can get pod is available or not in specified namespace

             kubectl get pod <pod-name> -n <namespace-name>

          *  By using below command we can get service is available or not in specified namespace

             kubectl get svc <svc-name> -n <namespace-name>  
           

          * By using below command we can get deployment is available or not in specified namespace

             kubectl get deployment <deployment-name> -n <namespace-name>  
SECTION 6:
---------

    # MongoDB UI Access

        1. http://10.74.190.101:27017

SECTION 7:
---------

      # REST API Commands for all CRUD

         *  Create an Index in MongoDB by using below command we can created.

            curl -v -XPOST -H "Content-Type: application/json" http://10.74.190.101:27017/student_data"

         * If we want to  verify Index created or not by using below command we can check.

            curl -v -XGET "http://10.74.190.101:27017/student_data/id"

         * If we want to insert our date into our index by using below command we can insert.

            curl -v -XPUT -H "Content-Type: application/json" http://10.74.190.101:27017/student_data/ -d"
            {
            "Student_name": "ramesh",
            "subects": "Maths","physics",
            "Age": 14,
            "Gender": "male",
            "Address": "vijayawada"
            }'

         * If we want to update in to our index by we can use below command.

           curl -v -XPUT -H "Content-Type: application/json" http://localhost:5000/student_data/ -d"
           {
            "Student_name": "ramesh",
            "subects": "Maths","physics",
            "Age": 14,
            "Gender": "male",
            "Address": "vijayawada"
            }'

        * If we want to delete exiting entery in our index we can use below command.

          curl -v -XDELETE "http://10.74.190.101:27017/student_data"
    
SECTION 8:
---------
    # References

    https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-ubuntu/#verify-that-mongodb-has-started-successfully
    
    https://hevodata.com/learn/mongodb-docker/

    https://mindmajix.com/mongodb-commands

    https://hevodata.com/learn/mongodb-crud-operations-in-python/

    https://github.com/tien-han/REST-API-with-MongoDB

    https://towardsdatascience.com/build-a-rest-api-with-node-express-and-mongodb-937ff95f23a5

