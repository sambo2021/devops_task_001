# Overview

Application is designed to take input Username in a textbox:
![Sample](https://github.com/ElAmin88/devops_task/assets/21984938/d5630c29-f5f6-48f9-88d6-6f4d03dde8b2)

Then Saves the Entered name in mongoDB with the following message of confirmation

![image](https://github.com/ElAmin88/devops_task/assets/21984938/a60b0af6-7987-41c4-bbf1-305299f76cec)

# Technical Details

Application is designed to integrate with mongoDB, Mongo URI is taken from environment variabled called (MONGO_URI)
Application requires MongoDB to be running and healthy before running the Application



Steps:
1- The web server running in your container is listening for connections on port 5000 of the loopback network interface (127.0.0.1). As such this web server will only respond to http requests originating from that container itself.In order for the web server to accept connections originating from outside of the container you need to have it bind to the 0.0.0.0 IP address.
https://stackoverflow.com/questions/26423984/unable-to-connect-to-flask-app-on-docker-from-host

2- build flask app image : docker build -t mohamedsambo/flask-app:1.0.0

3- push the image to dockerhub repo : docker push mohamedsambo/flask-app:1.0.0

4- run docker compose: docker-compose up

note: 
1- mohamedsambo/flask-app:1.0.0 without prome / grafana
2- mohamedsambo/flask-app:2.0.0 using flask_prome CLIENT and docker compose uses prometheus and grafana
3- mohamedsambo/flask-app:3.0.0 using prometheus_flask_exporter

5- To see the histogram of request latencies by status and path in Prometheus, you need to set up the query 
   sum(rate(requests_by_status_and_path_bucket{le="0.1", status=~"2..|3..|4..|5..", path="/"}[1m])) by (status) 

6- Log in to Grafana: Open your Grafana instance in a web browser and log in then in new dashbord add prometheus as data source then u can visualize query and add it to new dashbord
