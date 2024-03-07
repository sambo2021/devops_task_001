#!/bin/bash

privateInstances=("branch01" "branch02")

for item in "${privateInstances[@]}"; do
    aws ec2 describe-instances --region "us-east-1" \
    --query "Reservations[*].Instances[*].{PrivateIP:NetworkInterfaces[*].PrivateIpAddress}" \
    --filter "Name=tag:Name,Values=$item" | jq -r '.[0][0]."PrivateIP"[0]'
done

publicinstance="central"
aws ec2 describe-instances --region "us-east-1" --query "Reservations[*].Instances[*].{PublicIP:NetworkInterfaces[*].Association.PublicIp}" --filter "Name=tag:Name,Values=$publicinstance" | jq -r .[0][0]."PublicIP"[0]



#ssh -o ProxyCommand="ssh -W %h:%p -q -oStrictHostKeyChecking=no -i $PWD/config.pem ec2-user@54.82.125.106" -oStrictHostKeyChecking=no -i $PWD/config.pem ec2-user@10.0.141.172