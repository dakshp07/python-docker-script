# Python Docker Script (Part of my GSoC Project)
The script scans the folders and stores the required information by dumping it in an CSV.
Have added a test folder with the name as **images** 
We are storing file_name, extension of file, folder_name, artifact_id
Usind docker to solve the issues of SSL in old servers

# Steps to run
1) Clone the repository :
```git
git clone git@github.com:dakshp07/python-docker-script.git
```
2) cd into the project folder
```
cd <project-folder>
```
3) Run the docker commands to build the container.
```docker
docker-compose up
```
4) You can check the default location of binds:
```docker
volumes: 
      - type: bind
        source: ./images/
        target: /tmp/images/
```
5) The CSV is getting dumped at **/tmp/results.csv** with **results.csv** as the name of file.

6) If you want to get a copy of the CSV in your host, run the command:
```docker
docker cp <containerId>:/file/path/within/container /host/path/target
```