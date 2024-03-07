
1- check /etc/ansible/hosts is valid or not
ansible-inventory --list -y

2- check connectivity to private instances 
ansible -vvv all -m ping

3- 
ansible-playbook -i ./hosts system-patch.yml
