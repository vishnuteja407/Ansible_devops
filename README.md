# Ansible_devops
Devops Ansible course practice
ansible web01 -m ansible.builtin.yum -a "name=httpd state=present" -i inventory --become
ansible webservers -m ansible.builtin.service -a "name=httpd state=started enabled=yes" -i inventory --become
ansible webservers -m ansible.builtin.copy -a "src=index.html dest=/var/www/html/index.html" -i inventory --become

ansible-playbook -i inventory web-db.yaml -v
ansible-playbook -i inventory web-db.yaml -vvvv

ansible-playbook -i inventory web-db.yaml --syntax-check
ansible-playbook -i inventory web-db.yaml -C

ansible-playbook -e USERNM=cliuser -e COMM=cliuser vars_precedence.yaml
