#!/bin/bash

file="transactions.log"
balance=0

while read line; do
    type=$(echo $line | awk '{print $2}')
    amount=$(echo $line | awk '{print $3}')

    if [ "$type" == "Credit" ]; then
        balance=$((balance + amount))
    elif [ "$type" == "Debit" ]; then
        balance=$((balance - amount))
    fi
done < $file

echo "Net balance: $balance"
