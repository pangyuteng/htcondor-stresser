# htcondor-stresser



Repo contains Dockerfile and scripts used to generate condor scripts to stress test infra. 

for documentation of stressapptest, check out link below:

https://github.com/stressapptest/stressapptest


####


```
export MYSHARE=/tmp
export DOCKER_URL=$USER:stresser
docker build -t $DOCKER_URL .
docker push $DOCKER_URL
python3 gen_sub.py
# tweak stress_it.sub accordingly
condor_submit stress_it.sub



```
