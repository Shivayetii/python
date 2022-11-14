'''# Write a python function to list all docker images available in the system.
:param *args: arguments passed by the User. Type is STR.
:return: Finally list the all docker conatiners inside the system
'''

#import subprocess module
import subprocess
#define function
def docker_containers(*containers):
   #all docker iamges will stored on find_img folder
   run_containers = subprocess.run(["docker ps"])
   #finally return find_img 
   return run_containers
# it will print all running containers  inside the system
print(docker_containers(containers=d))


'''# Write a python function to list all docker images available in the system.
:param *args: arguments passed by the User. Type is STR.
:return: Finally list the all docker images inside the system
'''

#import subprocess module
import subprocess
#define function
def image_list(*images):
   #all docker iamges will stored on find_img folder
   find_img = subprocess.run(["docker images ls"])
   # iterate *images args
   for find_img in images:
       #finally return find_img 
      return find_img
   #finally return find_img 
# it will print all images inside the system
print(image_list())