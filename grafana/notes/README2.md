SECTION 1:

    1. What is timepicker buttons or time range buttons ?
     
        Grafana is allow you to create list of buttons and we can set specific times get data from a data source on 
        the dashboards of those specific times when you clicked on time picker buttons for that we can use time picker buttons in Grafana.

SECTION 2:

    #  Install time picker button panel in Grafana Actually, as per our analysis time picker button
       plugin is not installed when installation of Grafana we have to install that plugin in seperatly.
       We should follow below steps one by we can install 

            1.	On left side of Grafana dashboard click on settings options
            2.	Click on configuration option
            3.	And click on plugins option
            4.	And we have to search on search bar what type of plugin we have
            5.	In our case we need Time picker Buttons Panel so in search bar field search 
                Time picker Buttons Panel and click on it.and click on install option the plugin is installed on automatically
            6.	The timepicker button panel plugin is unsigned plugin so, 
                Grafana is not supported to run unsigned plugins
SECTION 3:

    # Install time picker button panel by using grafana cli-tool we shoud follow below steps one bye one
            
            1. We should login Grafana container and run below commands one bye one if want to enter into 
               the grafana container we can we use below command.

                  command1: docker exec -it <container_id or container_name> bash

                  EX: docker exec -it 15d6f46669f4 bash

            2. By using below this Command, we are able to list out all available plugins in the 
               remote server inside the grafana conatiner.

                  command2: grafana-cli plugins list-remote

            3. By using below commands we are able to install and listed all installed plugins in our
               VM we can run below commands one by one.

               Note: After installation any plugin through grafana cli or another way we must restart our grafana server once

                  command3: grafana-cli plugins install  williamvenner-timepickerbuttons-panel version: 4.1.1


                  command4: grafana-cli plugins ls
            4. By using below command we are able to update williamvenner- timepickerbuttons-panel 

                  command5: grafana-cli plugins update williamvenner-timepickerbuttons-panel version
            
SECTION 4:
    # Once williamvenner-timepickerbuttons-panel installaton is successes we are able to add this buttons to
      the grafana dashboards.

            #   We should follow below steps one by one 

               1 Login Grafana on broswer with user name and password.

               2 Click on setting symbole

               3 Click on data sources

               4 Click on add data sources as postgres Sql and give name of the database what ever we want

               5 then provide below artibutes one by one under PostgreSQL Connection

                    6 Host - We should provide  URL of the postgres Sql wheather your postgres is running.

                    7 We should provide databse on database row

                    8 Next we shoud provide user_name with password of the particular user

                    9 TLS/SSL Mode row click on disable

                    10 finally click on save and test 

                    11 click on grafana home symbole on top of grafana we have add panel symbole and click on
                       add new panel,give name of the panel save and edit that panel as per our requirement.
                       so here we are able to attach the time picker buttons to the our grafana dashboards.
                    
SECTION 5:

    # Configuraton timepicker buttons panel for Grafana

         We cna configuried timepicker buttons to grafana dashboards under display style configuration option
         here we need to provide in the following way.
                    
                    1. on top of the panel we have one option time picker buttons click on timepicker buttons
                       and then we should set time on it
                       EX: FromDate: 12/20/2022,2:20 PM
                       EX: ToDate: 12/20/2022,8:30 PM
                       EX: We should provide any text on it like :mycustom buttons text! 

                    2 We should click on display style configuration option and it will display below like this
                       
                    3. Display under display it will show ane more option style in this fieled we shoud give
                       our buttons and enable display horizontal buttons
                    4. We should be configured to on the panel and indicate which fields are mapped to the button properties 

             


