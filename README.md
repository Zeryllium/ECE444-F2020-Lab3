# ECE444-F2020-Lab3

This repo is a clone of https://github.com/miguelgrinberg/flasky

# ECE444-F2020-Lab4

Ensure that Docker Desktop is enabled prior to running any code.

>Download docker desktop for windows here: https://hub.docker.com/editions/community/docker-ce-desktop-windows/

In a command line interface, navigate to the project root and run the following command to build the docker image.
>```docker build -t ece444-lab-4:latest ./lab4DockerizedFlaskApplication/```

To start up a container, simply run the following command.
>```docker-compose up -d```

Alternatively, you can run in non-detached mode by omitting the `-d` flag 
>```docker-compose up```

In an internet browser, navigate to `http://127.0.0.1:5000` to access the site.

Afterwards, run the following command to terminate the container if it was run in detached mode or press `Ctrl+c` 
otherwise.
>```docker-compose down```

<br>
Lab 4 Screenshots:<br>

![Docker Commands Screenshot](https://github.com/Zeryllium/ECE444-F2020-Lab3/blob/Lab4_Microservice_Experiment/Docker_Commands_Screenshot.jpg?raw=true)

![Docker Containers and Images Screenshot](https://github.com/Zeryllium/ECE444-F2020-Lab3/blob/Lab4_Microservice_Experiment/Docker_Containers_and_Images_Screenshot.jpg?raw=true)

![Website Screenshot](https://github.com/Zeryllium/ECE444-F2020-Lab3/blob/Lab4_Microservice_Experiment/Website_Screenshot.jpg?raw=true)
