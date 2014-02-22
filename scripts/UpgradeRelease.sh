#!/bin/bash

# Replace these three settings.
PROJDIR="/home/alan/icokou.com/icokou"
PIDFILE="$PROJDIR/icokou.pid"
SOCKET="$PROJDIR/icokou.sock"

# kill program
cd $PROJDIR
if [ -f $PIDFILE ]; then
    kill `cat -- $PIDFILE`
fi

# upgrade program
cd $PROJDIR
hg pull
hg update

# rebuild static pyData file

# start program
$PROJDIR/icokou/scripts/StartIcokou.sh
