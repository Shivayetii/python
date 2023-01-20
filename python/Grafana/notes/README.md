SECTION 1:
---------

    1. Aim

       To monitoring the kubernetes deployments and infra by using Grafana

    2. What is Grafana ?

        Grafana is an open source interactive data-visualization platform or tool.
        it is developed by Grafana Labs, which allows users to see their,
        data via charts and graphs that are unified into one dashboard (or multiple dashboards!) 
        for easier to users understanding.

    3. why use Grafana ?

        1.Grafana is free open sources tool no need to pay any amount of any one

        2.Grafana is a provides beautiful visualizations.

        3.By using Grafana we can eaisly create our custom dashboards.

        4.Grafana, which runs as a web application, is used by small to large 
          enterprises to monitor visualizations. 

        5.Grafana will manage system reports ,metrics, logs and alerts.
    
        6.Grafana Integrates with set of data sources, like Prometheus,MySQL, Elasticsearch and Splunk.

SECTION 2:
---------

    # 
        1. Docker Image name  

           * If we want to deploy  Grafana in our system or VM we need to follow below steps and commands.
           
           * First We have to Docker installed in your system. If not done already
              you can download it from the Official Docker website.

           * If you installed docker in your system by using below command 
             you can check docker is running or not
             
              service docker status

           * Second one is  docker-hub account or docker-hub authentication credentials.

           * In docker-hub registry available the latest official images.

           * In our case we  need to deploy Grafana image for that by we need to pull the image from docker-hub.

           * If we want to deploy our image in our custom-network first we need to create network we can also.
             
             deploy our image in default network for that no need to create any network by using normal commands

             we can access appliction.

              * first step is pull image

                * If we want to downlod latest MongoDB docker image in our VM we can use below command.

                  docker pull grafana/grafana

                * If we want to downlod specific Grafana docker image in our VM we can use below command.

                  docker pull grafana/grafana:8.2.6

               * If we want to check the Docker images download in your system or not 
                 you can run the below  command.

                  docker images

            * second step is create container and run that container.
            
               * If we want to run our container in detach mode (Background process) we can run below this command.

                 docker run --name Grafana -d grafana/grafana

               *  If we want to access that application in broswer you can run below this command. 

                 docker run --name Grafana -d -p 3000:3000 grafana/grafana         

              * access the application by using IPaddress and container-port-number

                IP:container-port-number

            * If we want to deploy our Grafanais our custom network firt we need to create custom network.

              * By using below command we can create or custom net-work.
             
                docker network create <Network_Name>

        2. Create Docker Container and run that container in custom network.
        
           docker run --name <containername> --net <Network_Name> -p 3000:3000 grafana/grafana

          * Grafana default port number is 3000.

             We can access the Grafana UI Access using localhost:3000 or VM_IP:3000


SECTION 3:
---------

    # Deploying Grafana  using Kubernetes

        * when ever we want to deploy  any pod in kubernetes we have to create namesapce we can deploy pods
            
            deafult namespace also in our case our Grafana pod is deploy in specific name-sapce, so we are create

            name-sapce

            * By using below command we can create specific namespace
            
               kubectl create namespace <namespace_name>

        1. Deployment Spec

                * By using below we can create Deployment yml file for Grafana

                    vi deployment.yml

                * By using below command to deploy Grafana specified namespace

                    kubectl apply -f deployment.yml -n <Namespace-Name>
        
        Sample deployement yml file for Grafana
        ****************************************
            apiVersion: apps/v1
            kind: Deployment
            metadata:
            name: grafana
            namespace: monitoring
            spec:
            replicas: 1
            selector:
                matchLabels:
                app: grafana
            template:
                metadata:
                name: grafana
                labels:
                    app: grafana
                spec:
                containers:
                - name: grafana
                    image: grafana/grafana:latest
                    ports:
                    - name: grafana
                    containerPort: 3000

        2. Service Spec

                * By using below we can create service yml file for Grafana

                    vi service.yml

                * By using below command to deploy Grafana specified namespace

                    kubectl apply -f service.yml -n <Namespace-Name>

                    * logstash UI Access using localhost:Nodeport or VM_IP:Nodeport

        Sample service yml file for Grafana
        ************************************
            apiVersion: v1
            kind: Service
            metadata:
            name: grafana
            namespace: monitoring
            annotations:
                prometheus.io/scrape: 'true'
                prometheus.io/port:   '3000'
            spec:
            selector: 
                app: grafana
            type: NodePort  
            ports:
                - port: 3000
                targetPort: 3000
                nodePort: 32000

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

    # Deploying Grafana using HELM

        1. HELM Charts

                1. What is HELM package manager?

                    We knows about the Linux APT package manager here also HELM works similar to APT  package manager So HELM is package manager tool. By using HELM we can download charts is easily.
                    HELM contains  pre-packaged collections of all the necessary versioned and pre-configured resources required to deploy a container.

                2. Why we use HELM package manager?

                   * By using HELM we can  improved productivity.
                   * BY using HELM we can reduced complexity of deployments.
                   * Better scalability
                   * Easier rolling back to previous versions of an app

                   

        2. HELM commands for bring-up

                1.Install helm--3  on Kubernetes Cluster using below commands
                
                        * When ever we want to use HELM Charts in our Kubernetes cluster
                         first we need to install  HELM package manager in our Kubernetes cluster.

                       * By using below command we can install or download HELM package manager in our cluster.

                                curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/master/scripts/get-helm-3

                       * After installation is done we need to give permission of helm-3 by using below command
                         we are able to give permission of helm-3

                                chmod 700 get_helm.sh

                       * By using below command we are able run helm-3 on our kubernets cluster.

                               ./get_helm.sh
                2.Install Prometheus and Grafana on Kubernetes cluster by using Helm -3

                        * By using below this command we are able to add the latest helm repository in Kubernetes.

                                helm repo add stable https://charts.helm.sh/stable 

                        * By using below this command  we are able to Add the Prometheus 
                          and Grafana community  helm chart in Kubernetes cluster.

                                helm repo add prometheus-community https://prometheus-community.github.io/helm-charts

                        * By using below we are able to see the available Prometheus and grafana helm chart packages

                                helm search repo prometheus-community

                        * By using this command we are able to install kube-prometheus-stack on kubernetes-cluster

                                helm install stable prometheus-community/kube-prometheus-stack

        3. HELM commands for debug

                1. Edit Services

                        * By using below this command we are able to edit the prometheus 
                          ClusterIP service to NodePort service.

                               kubectl edit svc stable-kube-prometheus-sta-prometheus

                        * By using this command we are able edit the grafana ClusterIP service to NodePort service

                                kubectl edit svc stable-grafana

        4. Access Prometheus and Grafana WEB Interface

                        * Run below this command we are able to access the prometheus services.

                               LocalhostIP:prometheusNodePortNo EX: 10.208.141:31370

                        * Run below this command we are able to access the grafana services.

                               LocalhostIP:GrafanaNodePortNo EX: 10.208.44.141:30594

SECTION 5:
---------

    # Verification post installation

        1. Access Grafana in UI

           we can access Grafana in two ways

                    * By using VMIP:ContainerPortNo

                    * By using VMIP:NodePortNo

        2. kubectl commands for Grafana

                    * By using below command we can get pod is available or not in specified namespace

                        kubectl get pod <pod-name> -n <namespace-name>

                    *  By using below command we can get service is available or not in specified namespace

                        kubectl get svc <svc-name> -n <namespace-name>  
           
                    * By using below command we can get deployment is available or not in specified namespace

                        kubectl get deployment <deployment-name> -n <namespace-name>  

SECTION 6:
---------

    # Grafana UI Access

        1.  http://10.74.190.101:3000
        
        2.  What's Grafana dashboard?

             A Grafana dashboard supports multiple panels in a single grid. 
             You can visualize results from multiple data sources simultaneously.

        3.  How to create dashboard  manually in Grafana?

                  * After installation of Grafana it will show Grafana welcome page.

                  * On top of Grafana page on left side we can see (+) plus option so first we need click on plus option

                  * And then it will show dashboard option so second step is click on dashboard option

                  * It will display add new panel so third step is click on add new panel

                  * It will display visualization under visualization we can see multiple 
                    options like charts,  graphs etc
                    We can select our requirement which options we need. if data is not it will display no data on screen

                  * We are able to add data in grafana for we can do below like that

                  * First click on settings and it will display datasources so we need to click on datasources 
                
                  * And second step is add data source here available 
                    different types of databases we can select what datasource we need to add.

SECTION 7:
---------

       # REST APIs to interact with Grafana

              1. Create Dashboard

                    * By using below command we are able to create new dashboard in Grafana.

                      curl -X POST --insecure -H "Authorization: Bearer eyJrIjoiR0ZXZmt1UFc0OEpIOGN5RWdUalBJTllUTk83VlhtVGwiLCJuIjoiYXBpa2V5Y3VybCIsImlkIjo2fQ==" -H "Content-Type: application/json" -d '{
                         "dashboard": {
                           "id": null,
                           "title": "Production Overview",
                           "tags": [ "templated" ],
                           "timezone": "browser",
                           "rows": [
                             {
                             }
                           ],
                           "schemaVersion": 6,
                           "version": 0
                         },
                         "overwrite": false
                      }' http://localhost:3000/api/dashboards/db
                        
              2. Updated Dashboards

                    * By using below command we are able to update existing dashboards in Grafana.

                         curl -X POST --insecure -H "Authorization: Bearer eyJrIjoiR0ZXZmt1UFc0OEpIOGN5RWdUalBJTllUTk83VlhtVGwiLCJuIjoiYXBpa2V5Y3VybCIsImlkIjo2fQ==" -H "Content-Type: application/json" -d '{
                         "dashboard": {
                           "id": null,
                           "title": "Non production Overview",
                           "tags": [ "templated" ],
                           "timezone": "browser",
                           "rows": [
                             {
                             }
                           ],
                           "schemaVersion": 6,
                           "version": 0
                         },
                         "overwrite": false
                      }' http://localhost:3000/api/dashboards/db

              3. Delete Dashboard

                    * By using below command we are able to delete existing dashboards in Grafana.

                     curl -X DELETE --insecure -H "Authorization: Bearer eyJrIjoiR0ZXZmt1UFc0OEpIOGN5RWdUalBJTllUTk83VlhtVGwiLCJuIjoiYXBpa2V5Y3VybCIsImlkIjo2fQ==" -H "Content-Type: application/json" -d '

SECTION 8:
---------
    # References
    
    https://www.redhat.com/en/topics/data-services/what-is-grafana

    https://www.youtube.com/watch?v=kQQF9QzSSS4

    https://hub.docker.com/r/grafana/grafana/

    https://devopscube.com/setup-grafana-kubernetes/

    https://github.com/DeekshithSN/kubernetes/blob/master/monitoring/kubernetes-grafana/service.yaml

    https://www.fosstechnix.com/install-prometheus-and-grafana-on-kubernetes-using-helm/
    
