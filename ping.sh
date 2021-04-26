#!/bin/bash
# Ping loop sweep

for i in $(seq 1 254); do
        timeout 1 bash -c "ping -c 1 10.11.1.$i" >/dev/null && echo "10.11.1.$i" | sort -u &
done; wait
