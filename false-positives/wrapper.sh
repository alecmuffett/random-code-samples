#!/bin/sh

instances=50

code=./falsepos-falsenegativeonly.py

rate_arg=$1 ; shift

Launch() {
    counter=$1 ; shift
    rate=$1 ; shift
    while [ "$counter" -gt 0 ] ; do
        "$@" $rate &
        counter=`expr $counter - 1`
    done
}

( Launch $instances $rate_arg python $code ) |
    awk '{x+=$(NF)} END {print "avg", (x*1.0)/NR}'
