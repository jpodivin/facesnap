#!/bin/bash
if ! [ -a /etc/systemd/system/facesnap.service ]; then
    cp ./facesnap.service /etc/systemd/system/
fi
