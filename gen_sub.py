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
log = log/$(cluster).$(process).log.txt
error = log/$(cluster).$(process).err.txt
output = log/$(cluster).$(process).out.txt

# take our python script to the compute node
transfer_input_files = stress_it.sh

should_transfer_files = YES
when_to_transfer_output = ON_EXIT

# We require a machine with a modern version of the CUDA driver

requirements = (OpSys == "LINUX" && Arch == "X86_64")
#requirements = (Machine == "very.expensive.server.org" )

# We must request 1 CPU in addition to 1 GPU
request_cpus = 1
request_gpus = 1

# select some memory and disk space
request_memory = 3GB
request_disk = 5GB


# Tell HTCondor to run 1 instances of our job:
queue 1

'''
with open('stress_it.sub','w') as f:
    f.write(template)

with open('stress_it.sh','w') as f:
    f.write(commandstr)
