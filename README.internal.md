If running locally, for testing, several folders need to be available.

* Pull latest version of app from openshift
    - `rhc snapshot save web`
* Extract contents to relevant directories
    - `tar xf web.tar.gz`
    - `cp backup/${HASH}/app-root/data/bcdf.db web/openshift`
    - `cp backup/${HASH}/app-root/data/media web/openshift/media`
    - `mkdir web/openshift/static`
    - `echo {} > web/openshift/challenge.json`
* Run django app

To deploy certificates

* Create a mount point in letsencrypt docker container
    - `mkdir container`
* Start docker interactively mounting at point (update specifics)
```
DOCKER_HOST=tcp://192.168.99.100:2376 \
DOCKER_CERT_PATH=$HOME/.docker/machine/machines/default \
DOCKER_TLS_VERIFY=1 \
docker run \
    -v $HOME/Workspace/letsencrypt/container:/etc/letsencrypt \
    -it da924bc6482c certonly --manual \
    -d bovellcancerdiabetesfoundation.org \
    -d www.bovellcancerdiabetesfoundation.org \
    -d bovellfoundation.org \
    -d www.bovellfoundation.org \
    -d web-bcdf.rhcloud.com
```
* Collect challenges and responses in `challenges.json`
* Transfer responses to openshift
    - `USER_HASH=aaaaaa REMOTE=$USER_HASH@web-bcdf.rhcloud.com`
    - `scp openshift/challenge.json $REMOTE:/var/lib/openshift/$USER_HASH/app-root/data/challenge.json`
