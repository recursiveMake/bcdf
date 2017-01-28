#!/bin/bash

cd $OPENSHIFT_DATA_DIR/installs/memcached/bin

pgrep memcached || ./memcached -d -s ${OPENSHIFT_TMP_DIR}cache_file.sock
