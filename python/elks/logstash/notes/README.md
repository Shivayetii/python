SECTION 1:
---------

    # What is logstash?

        Logstash is pipeline tool logstash is accept inputs and logs from various sources and
        similarly exports data from exact tragets that is called as logstash.

    # Why we use log-stash

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

           we can access logstash in two ways

             * By using VMIP:ContainerPortNo

             * By using VMIP:NodePortNo

        2. kubectl commands for logstash

           * By using below command we can get pod is available or not in specified namespace

             kubectl get pod <pod-name> -n <namespace-name>

          *  By using below command we can get service is available or not in specified namespace

             kubectl get svc <svc-name> -n <namespace-name>  
           

          * By using below command we can get deployment is available or not in specified namespace

             kubectl get deployment <deployment-name> -n <namespace-name>  

           

SECTION 6:
---------

    # logstash UI Access

        1.  http://10.74.190.101:5000

SECTION 7:

    # REST API Commands for logstash

         When we run logstash it is automatically display the runtime metrics that can be used to
         monitor the health and performance of our logstash deployment.
           
            * The metrics are collected logstash information,OS information and JVM information

                 Ex: pipeline settings

            * The metrics collected plugin information and also list of installed plugins.

            * Logstash APIs check the Node stats, JVM stats, process stats, event-related stats, 
              and pipeline runtime stats.

            * we can use monitoring APIs provided by Logstash to collect above the metrics. 
              These APIs are available by default without requiring any extra configuration.

            * Alternatively, we can configure X-Pack monitoring to send data to a monitoring cluster.

            * If we want to see general information about the Logstash instance, including the host and version.
              we can use below command.
            
                    curl -XGET '10.74.190.101:5000/?pretty'

            * If we want to see what all are plugins  runing our system we can use below command.

                    curl -XGET '10.74.190.101:5000/_node/plugins?pretty'

            * If we want to see node stats it will display the runtime node stats for 
              that we can use below command.

                    curl -XGET '10.74.190.101:5000/_node/stats/<types>'

            * If we want to see G JVM stats, including stats about threads, 
              memory usage, garbage collectors, and uptime. we can use below command.

                       curl -XGET 'localhost:5000/_node/stats/jvm?pretty'

            * If we want to see process stats, including stats about file descriptors, 
              memory consumption, and CPU usage we can use below command.

                       curl -XGET '10.74.190.101:5000/_node/stats/process?pretty'

            * If we want to see event-related statistics for the Logstash instance 
              of how many pipelines were created and destroyed we can use below command.

                       curl -XGET '10.74.190.101:5000/_node/stats/events?pretty'

            * If we want to see  flow-related statistics for the Logstash instance
              of how many pipelines were created and destroyed we can use below command.

                       curl -XGET '10.74.190.101:5000/_node/stats/flow?pretty'

            * If we want to see runtime stats about each Logstash pipeline for that we can use below command.

                       curl -XGET '10.74.190.101:5000/_node/stats/pipelines?pretty'

            * If we want to see runtime stats about cgroups when Logstash is running in a container.
              we can use below command.

                       curl -XGET 'localhost:5000/_node/stats/os?pretty'

            * If we want to see information about config reload successes or  failures for 
              that we can use below command.

                       curl -XGET '10.74.190.101:5000/_node/stats/reloads?pretty'

            * If we want to see current hot threads for Logstash, A hot thread is a Java thread 
              that has high CPU usage and executes for a longer than normal period of time.
              for that we can use below command.

                        curl -XGET 'localhost:9600/_node/hot_threads?pretty'

SECTION 8:
---------
    # References
    
    https://www.elastic.co/guide/en/logstash/current/introduction.html

    https://hub.docker.com/_/logstash

    https://gitlab.com/ndevox/kubernetes-elastic-logging/blob/master/logstash-deployment.yaml

    https://sysadminxpert.com/elk-stack-architecture-elasticsearch-logstash-and-kibana/

    https://www.elastic.co/guide/en/logstash/current/node-stats-api.html
