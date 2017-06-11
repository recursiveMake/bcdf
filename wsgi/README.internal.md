If running locally, for testing, several folders need to be available.

* Pull latest version of app from openshift
    - `rhc snapshot save web`
* Extract contents to relevant directories
    - `tar xf web.tar.gz`
    - `cp backup/${HASH}/app-root/data/bcdf.db web/openshift`
    - `cp backup/${HASH}/app-root/data/media web/openshift/media`
    - `mkdir web/openshift/static`
* Run django app
