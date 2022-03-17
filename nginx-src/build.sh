#!/bin/bash

NGINX_VER=nginx-1.21.6

if [ $# -ne 1 ]; then
    echo "usage: build.sh /path/to/install/location"
    exit 1
fi

echo -e "compiling and installing nginx to: $1\n\n"

pushd "$NGINX_VER"

./configure --with-http_auth_request_module --prefix="$1"

if [ $? -ne 0 ]; then
    echo "fatal: configure failed, aborting"
    exit 2
fi

make && make install

popd
echo -e "\n\nDone!"