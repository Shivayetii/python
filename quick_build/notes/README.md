References:
-----------
Java:
-----
https://www.digitalocean.com/community/tutorials/how-to-install-java-with-apt-on-ubuntu-20-04

sudo apt update -y
sudo apt install default-jre -y
sudo apt install default-jdk -y

Test Java installation:
------------------------
vudeadmin@cdedops-vude2:/opt/quick_build/quickbuild-10.0.39$ java -version
openjdk version "11.0.16" 2022-07-19
OpenJDK Runtime Environment (build 11.0.16+8-post-Ubuntu-0ubuntu120.04)
OpenJDK 64-Bit Server VM (build 11.0.16+8-post-Ubuntu-0ubuntu120.04, mixed mode, sharing)
--------------------------------------------------------------------------------------------------------
[12:20 PM] Chandramouli, ArunX
Srivenkatanarayana, YetiX SaiManeesh Babu, AretiX Jamapala, RajashekarX In your windows machine assignment folder, create a new folder "quick_build". Then under quick_build folder, create a notes folder. Under notes folder, create a file README.md
Copy-Paste below contents into README.md

References:
-----------
Java:
-----https://www.digitalocean.com/community/tutorials/how-to-install-java-with-apt-on-ubuntu-20-04

sudo apt update -y
sudo apt install default-jre -y
sudo apt install default-jdk -y

Test Java installation:
------------------------
vudeadmin@cdedops-vude2:/opt/quick_build/quickbuild-10.0.39$ java -version
openjdk version "11.0.16" 2022-07-19
OpenJDK Runtime Environment (build 11.0.16+8-post-Ubuntu-0ubuntu120.04)
OpenJDK 64-Bit Server VM (build 11.0.16+8-post-Ubuntu-0ubuntu120.04, mixed mode, sharing)
--------------------------------------------------------------------------------------------------------
Quickbuild Install GUIDES:
---------------------------
https://wiki.pmease.com/display/QB80/Server+Installation+Guidehttps://wiki.pmease.com/display/QB12/Documentation+Homehttps://build.pmease.com/build/5442

Goto :    https://www.pmease.com/downloads/latest/linux  COPY Link  Goto your VM    
1. sudo mkdir /opt/quick_build/   
2. cd /opt/quick_build/    
3. sudo chown -R $USER /opt/quick_build/   
4. curl -L -O https://build.pmease.com/download/5442/artifacts/quickbuild-10.0.39.tar.gz    
5. tar -zxvf quickbuild-10.0.39.tar.gz    
6. ls -R /opt/quick_build/    
7. cd /opt/quick_build/quickbuild-10.0.39    
8. ./bin/server.sh start
--------------------------------------------------------------------------------------------------------
Video trainings:
----------------
\\elements.local\FW\Users\azaleski\qb_trainings
--------------------------------------------------------------------------------------------------------

Additional documentation:
--------------------------
https://npsg-wiki.elements.local/display/INFS/Quickbuild+CI+2.0+Data+Spec

ElasmoCI:
---------
https://npsg-wiki.elements.local/display/CME/elasmo+CI
--------------------------------------------------------------------------------------------------------
Confirm once done
How To Install Java with Apt on Ubuntu 20.04  | DigitalOcean
In this guide, you will install various versions of the Java Runtime Environment (JRE) and the Java Developer Kit (JDK) using apt on Ubuntu 20.04. You’ll i… 

