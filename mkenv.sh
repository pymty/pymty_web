#!/bin/bash
if [ ! -d env ]; then
    which virtualenv > /dev/null 2>&1
    if [ $? -ne 0 ]; then
        echo "No ha sido posible crear el ambiente. Primero necesitas instalar virtualenv." > /dev/stderr
        exit 1
    fi
    virtualenv env
    ./env/bin/pip install -r requirements.txt
    if [ $? -eq 0 ]; then
        ln -s ../env/lib/python2.7/site-packages/cherrypy pymty/cherrypy
        ln -s ../env/lib/python2.7/site-packages/mako pymty/mako
    else
        echo "No ha sido posible obtener las dependencias" > /dev/stderr
        rm -rf env
        exit 1
    fi
else
    echo "El ambiente de desarrollo ya existe" > /dev/stderr
fi
