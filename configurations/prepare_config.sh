#!/bin/bash
USER_NAME=$(whoami)

sed -i -E "s/(\/mnt\/sdc\/)(ds2022-lab2-[0-9])/\1$USER_NAME/" edge_conf.cfg
sed -i -E "s/(\/mnt\/sdc\/)(ds2022-lab2-[0-9])/\1$USER_NAME/" cloud_conf.cfg

USER_ID=$(echo $USER_NAME | grep -Eo "[0-9]$")

if [ "$USER_ID" -eq 1 ]; then
    echo "Maciej"
    sed -i -E "s/(middleIP = )[0-9]+/\1132/" edge_conf.cfg
    sed -i -E "s/(middleIP = )[0-9]+/\1132/" cloud_conf.cfg
elif [ "$USER_ID" -eq 2 ]; then
    echo "Jonas"
    sed -i -E "s/(middleIP = )[0-9]+/\1137/" edge_conf.cfg
    sed -i -E "s/(middleIP = )[0-9]+/\1137/" cloud_conf.cfg
elif [ "$USER_ID" -eq 3 ]; then
    echo "David"
    sed -i -E "s/(middleIP = )[0-9]+/\1139/" edge_conf.cfg
    sed -i -E "s/(middleIP = )[0-9]+/\1139/" cloud_conf.cfg
fi