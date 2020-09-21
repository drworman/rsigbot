#!/usr/bin/env bash

APPEXEC="rsigbot"

APPDIR="`dirname \"$BASH_SOURCE\"`"
APPDIR="`( cd \"$APPDIR\" && pwd )`"
if [ -z "$APPDIR" ] ; then
  exit 1
fi

pgrep -f "python $APPDIR/$APPEXEC" >/dev/null
if [[ $? -ne 0 ]] ; then
        (cd $APPDIR && exec $APPDIR/$APPEXEC &)
fi
