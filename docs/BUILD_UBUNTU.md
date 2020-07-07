

Ubuntu build
```bash
sudo docker run --name django-api -v /cloud/shrDoc/django-api/:/cloud/django-api -p 51001:51001 -dt ubuntu:16.04
sudo docker exec -it django-api /bin/bash
apt-get update
apt-get install vim wget curl git
git clone https://gitee.com/Mr_ChenLuYong/django-api.git project


mkdir packs
cd packs
wget https://www.python.org/ftp/python/3.8.3/Python-3.8.3.tar.xz
cd Python-3.8.3
apt-get install zlib1g-dev zlib1g
apt-get update
apt-get upgrade
apt-get dist-upgrade
apt-get install build-essential python-dev python-setuptools python-pip python-smbus
apt-get install build-essential libncursesw5-dev libgdbm-dev libc6-dev
apt-get install zlib1g-dev libsqlite3-dev tk-dev
apt-get install libssl-dev openssl
apt-get install libffi-dev
apt-get install libmysqlclient-dev
./configure --enable-optimizations
make && make install

apt install software-properties-common
add-apt-repository ppa:deadsnakes/ppa
apt install python3.9
python3.9 --version
```