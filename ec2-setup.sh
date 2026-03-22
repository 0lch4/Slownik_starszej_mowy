#!/bin/bash
yum update -y
yum install -y docker
systemctl start docker
systemctl enable docker

curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose

mkdir -p /home/ec2-user/slownik
cd /home/ec2-user/slownik

curl -o docker-compose.prod.yml https://raw.githubusercontent.com/0lch4/Slownik_starszej_mowy/main/docker-compose.prod.yml

cat > .env <<EOF
DATABASE='db'
USER='root2'
PASSWORD='Str4rszaMow4!'
HOST='db'
EOF

/usr/local/bin/docker-compose -f docker-compose.prod.yml pull
/usr/local/bin/docker-compose -f docker-compose.prod.yml up -d
