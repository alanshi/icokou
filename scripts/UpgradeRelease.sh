#!/bin/bash

# Replace these three settings.
PROJDIR="/home/alan/icokou.com/icokou"
DJANDIR="$PROJDIR/icokou"
PIDFILE="$PROJDIR/icokou.pid"
SOCKET="$PROJDIR/icokou.sock"

# kill program
cd $PROJDIR
if [ -f $PIDFILE ]; then
    kill `cat -- $PIDFILE`
fi

# upgrade program
cd $DJANDIR
hg pull
hg update

# rebuild static pyData file

# start program
$DJANDIR/scripts/StartIcokou.sh
