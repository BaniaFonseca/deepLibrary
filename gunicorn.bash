#!/bin/bash

NAME="deeplibrary"                                   # Name of the application
DJANGODIR=/projects/deepLibrary/dl               		# Django project directory
SOCKFILE=/envs/deeplibrary/run/gunicorn.sock  # we will communicte using this unix socket
USER=fonseca                                         # the user to run as
GROUP=fonseca                                        # the group to run as
NUM_WORKERS=1                                       # how many worker processes should Gunicorn spawn
DJANGO_SETTINGS_MODULE=dl.settings.production     # which settings file should Django use
DJANGO_WSGI_MODULE=dl.wsgi 
# WSGI module name
echo "Starting $NAME as `whoami`"

# Activate the virtual environment

cd $DJANGODIR
source /envs/deeplibrary/bin/activate
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH

# Create the run directory if it doesn't exist

RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR

# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)

exec gunicorn ${DJANGO_WSGI_MODULE}:application \
  --name $NAME \
  --workers $NUM_WORKERS \
  --user=$USER --group=$GROUP \
  --bind=unix:$SOCKFILE \
  --log-level=debug \
  --log-file=-
