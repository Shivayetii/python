SECTION 1:
---------

    # What's logstash and why we use it

    Logstash is pipeline tool logstash is accept inputs and logs from various sources and
    similarly exports data from exact tragets that is called as logstash.

    why use log-stash
    1.logstash is free open sources no need to pay any amount of any one
    2.logstash is eaisly collect the data form multiple sources
    3.logstash send the data to desired destination
    4.The Logstash have Java Database Connectivity (JDBC) input plugin enables you to pull in data from many popular relational databases including MySQL and Postgres
    5.Logstash collect data from all shapes and size of data
      Eg: syslogs, datastore like NoSQL/RDBMS, web-like,Twitter or Github
    6.Logstash will transform the data and store it into different storage for analytical.
      Eg: For analysis, we can use datastore like MongoDB or elasticsearch.
          For archiving we can store data in the s3/Google storage.
          For monitoring, we can use Nagios/Graphite

SECTION 2:
---------

    # Deploying logstash using Dockers

        1. Docker Image name  

           When ever we want to deploy any image from docker-hub first we need docker-hub account or docker-hub

           authentication credentials

           In docker-hub registry available the latest official images

           * In our case we  need logstash image for that by we need to pull the image from docker-hub

           * If we want to deploy our image in our custom-network first we need to create network we can also
             
             deployee our image in default network for that no need to create any network by using normal commands

             we can access appliction

              * first step is pull image

                docker pull docker.elastic.co/logstash/logstash:8.5.0 

              * second step is create container and run that container
                
                 docker run --name <container-name>  -p 5000:5000 docker.elastic.co/logstash/logstash:8.5.0 

              * access the application by using IPaddress and container-port-number

                IP:container-port-number

              * By using below command we can create or custom net-work 
             
                docker network create <Network_Name>

        2. Create Docker Container and run that container in custom network
        
           docker run --name <containername> --net <Network_Name> -p 5000:5000 docker.elastic.co/logstash/logstash:8.5.0

          * logstash default port number is 5000

          - We can access the logstash UI Access using localhost:5000 or VM_IP:5000

SECTION 3:
---------

    # Deploying logstash using Kubernetes

      * when ever we want to deploy  any pod in kubernetes we have to create namesapce we can deploy pods
        
        deafult namesoace also in our case our logstash pod is deploy in specific name-sapce, so we are create

        name-sapce

        * By using below command we can create specific namespace
         
          kubectl create namespace <namespace_name>

        1. Deployment Spec

           * By using below we can create Deployment yml file for logstash

              vi deployment.yml

           * By using below command to deploy logstash specified namespace

              kubectl apply -f deployment.yml -n <Namespace-Name>
        
        Sample deployement yml file for logstash
        ****************************************
        apiVersion: apps/v1
        kind: Deployment
        metadata:
        name: logstash
        namespace: elkapis
        labels:
            component: logstash
        spec:
        strategy:
            type: Recreate
        selector:
            matchLabels:
            component: logstash
        template:
            metadata:
            labels:
                component: logstash
            spec:
            containers:
                - name: logstash
                image: logstash:8.5.0
                ports:
                    - containerPort: 5044

        2. Service Spec

           * By using below we can create service yml file for logstash

              vi service.yml

           * By using below command to deploy logstash specified namespace

              kubectl apply -f service.yml -n <Namespace-Name>

              * logstash UI Access using localhost:Nodeport or VM_IP:Nodeport

        Sample service yml file for logstash
        ************************************
        apiVersion: v1
        kind: Service
        metadata:
        namespace: elkapis
        name: logstashsvc
        labels:
            component: logstash
        spec:
        externalIPs:
        - 10.74.190.101
        type: NodePort
        ports:
        - port: 5044
            protocol: TCP
            targetPort: db
        selector:
            component: logstash

        3. kubectl commands for debug

           * By using below command we can describe the pod in specified namespace

              kubectl describe  pod <pod-name> -n <namespace-name>

           * By using below command we can edit the pod in specified namespace

              kubectl edit  pod <pod-name> -n <namespace-name>

          *  By using below command we can describe the service in specified namespac

              kubectl describe  svc <svc-name> -n <namespace-name>  

          *  By using below command we can edit the service in specified namespac

              kubectl edit  svc <svc-name> -n <namespace-name>   

SECTION 4:
---------

    # Deploying logstash using HELM

        1. HELM Charts

        2. HELM commands for bring-up

        3. HELM commands for debug

SECTION 5:
---------

    # Verification post installation

        1. Access logstash in UI

        2. CREATE/DELETE/UPDATE Indexes

        3. kubectl commands for logstash

SECTION 6:
---------

    # logstash UI Access

        1. UI Link

SECTION 7:
---------

    # REST API Commands for all CRUD

SECTION 8:
---------
    # References
    
    https://hub.docker.com/_/logstash

    https://sysadminxpert.com/elk-stack-architecture-elasticsearch-logstash-and-kibana/
