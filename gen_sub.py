import os

myshare = os.environ['MYSHARE']
docker_url = os.environ['DOCKER_URL']

template=f'''
# stress_it.sub
# Submit file 

# Must set the universe to Docker
universe = docker
docker_image = {docker_url}

# set the log, error and output files 
log = log/$(cluster).$(process).log
error = log/$(cluster).$(process).err
output = log/$(cluster).$(process).out

# take our python script to the compute node
transfer_input_files = stress_it.sh

should_transfer_files = YES
when_to_transfer_output = ON_EXIT

# We require a machine with a modern version of the CUDA driver

requirements = (OpSys == "LINUX" && Arch == "X86_64")
#requirements = (Machine == "very.expensive.server.org" )

# We must request 1 CPU in addition to 1 GPU
request_cpus = 1
#request_gpus = 1

# select some memory and disk space
#request_memory = 3GB
#request_disk = 5GB


# set the executable to run
executable = stress_it.sh
arguments = "hello-world"

# Tell HTCondor to run 1 instances of our job:
queue 10

'''
with open('stress_it.sub','w') as f:
    f.write(template)

commandstr=f'''#!/bin/bash

export myfolder={myshare}/$(openssl rand -hex 8)
mkdir -p $myfolder
echo $myfolder
stressapptest -s 60 -M 256 -m 8 -W -f $myfolder/file1 -f $myfolder/file2 -f $myfolder/file3

'''
with open('stress_it.sh','w') as f:
    f.write(commandstr)
