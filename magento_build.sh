#!/bin/bash
local_server="$(hostname -I | awk '{print $1}')"
remote_server="178.62.113.8"

apt-get update
apt-get install docker
apt-get install -y docker-compose
apt-get install -y git
apt-get install -y ssh
apt-get install -y sshpass

docker pull liinaanette/js-adapter:event-handling

echo "apt-get install -y sshpass" > copy_files
echo "sshpass -p jsadapter scp -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null -r /docker root@"$local_server":/" >> copy_files
echo "sshpass -p jsadapter scp -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null /opt/* root@"$local_server":/opt" >> copy_files
echo "exit" >> copy_files

sshpass -p jsadapter ssh -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null root@$remote_server < copy_files


cd /docker
sed -i 's,MAGENTO_URL=.*,'"MAGENTO_URL=http://$local_server"',' env
docker-compose up -d
docker exec -it stacc_dasso_apache2_php5.4_magento1 install-sampledata
docker exec -it stacc_dasso_apache2_php5.4_magento1 install-magento
docker exec stacc_dasso_apache2_php5.4_magento1 bash -c "cd /var/www/html/js;apt-get update; apt-get install -y git; git clone https://github.com/stacc-dasso/Javascript-Adapter.git stacc-adapter"
docker cp /docker/page.xml stacc_dasso_apache2_php5.4_magento1:/var/www/html/app/design/frontend/rwd/default/layout/