# blog-es
Trabalho de Engenharia de Software

configurar virtualenv e virtualenvwapper

criar ambiente:
mkvirtualenv --python=/usr/bin/python3 blog-es

instalar requirements:
pip install -r requirements.txt

installar java
http://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html
- ubuntu
    sudo add-apt-repository ppa:webupd8team/java
    sudo apt-get update
    sudo apt-get install oracle-java8-installer
para confirmar basta digitar: javac -v

download do solr 4.10.4
wget http://www.us.apache.org/dist/lucene/solr/4.10.4/solr-4.10.4.tgz

# TODO -> fazer um script para fazer configuração automatica


settings.py

alterar a variavel SITE_ID para funcionar o RSS
