# Python Docker Script (Part of my GSoC Project)
The script scans the folders and stores the required information by dumping it in an CSV.

Have added a test folder with the name as **images** 

We are storing file_name, extension of file, folder_name, artifact_id

Using docker to solve the issues of SSL in old servers

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
5) Now to run the script you need to go inside the container, which can be done in the following way:
```docker
docker exec -it images_docker sh
```
6) The script, requirements file is saved in **/tmp** folder
```bash
cd tmp
ls
```
7) Now its time to run the script:
```python
python3 main_csv.py images /tmp results.csv #The first arguments is necessary, the other two are optional.
```
8) Once the script runs successfully, you can exit out of the container by typeing exit:
```bash
exit
```
# Note
If you don't want to visit the docker container and run the script on your own, then refer the [**master**](https://github.com/dakshp07/python-docker-script/tree/master) branch of this repo.