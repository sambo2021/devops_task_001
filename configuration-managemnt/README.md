1- u can use script1.sh to get private instances and public instances ips
/etc/ansible/hosts

[webservers:vars]
ansible_ssh_common_args='-o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null -o ProxyCommand="ssh -W %h:%p -q -oStrictHostKeyChecking=no -i ~/.ssh/config.pem ec2-user@PublicInstanceIP"'
[webservers]
host01 ansible_host=PrivateInstanceIP ansible_ssh_user=ec2-user ansible_ssh_private_key_file=~/.ssh/config.pem
host02 ansible_host=PrivateInstanceIP ansible_ssh_user=ec2-user ansible_ssh_private_key_file=~/.ssh/config.pem

2- check /etc/ansible/hosts is valid or not
ansible-inventory --list -y

3- check connectivity to private instances 
ansible -vvv all -m ping
