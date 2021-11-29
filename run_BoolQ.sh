#! /bin/bash

#BATCH_SIZE="2 4 8"
#LR="0.000005 0.00001 0.00002"

BATCH_SIZE="8"
LR="0.00002"

for b in $BATCH_SIZE
do
    for l in $LR
    do
        python run_seq_cls.py --task BoolQ --config_file koelectra-base-v3.json --bs $b --lr $l
    done
done



