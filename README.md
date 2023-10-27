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

ansible-builder build -t my_ee -v 3

ansible-runner run -p ping.yaml --inventory inventory.ini --container-image=my_ee .

ansible-playbook playbook.yml --start-at-task="install packages"

ansible-playbook example.yml --tags "configuration,packages"

ansible-playbook example.yml --skip-tags "packages"

ansible-galaxy install -r requirements.yml

ansible-galaxy role install -r requirements.yaml

# using ansible sign feature
pip3 install ansible-sign
gpg --generate-key
cd project-dir/
ansible-sign project gpg-sign .

# To validate key
ansible-sign project gpg-verify .



# REDHAT CIS policy
ansible-galaxy install git+https://github.com/ansible-lockdown/RHEL9-CIS.git
