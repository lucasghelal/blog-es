# blog-es
Trabalho de Engenharia de Software

Configuração
------------

Instalar Virtualenv e virtualenvwapper

Criar Ambiente:

mkvirtualenv --python=/usr/bin/python3 blog-es

Instalar requirements:
pip install -r requirements.txt

Installar java
http://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html
- Ubuntu
    sudo add-apt-repository ppa:webupd8team/java
    sudo apt-get update
    sudo apt-get install oracle-java8-installer
para confirmar basta digitar: javac -v

Download do solr 4.10.4
wget http://www.us.apache.org/dist/lucene/solr/4.10.4/solr-4.10.4.tgz

TODO 
----
- [ ] Alterar interface no material;
- [ ] Fazer um script para fazer configuração automatica;
- [ ] Passar configurações dos settings.py para o env;
- [x] Alterar a variavel SITE_ID para funcionar o RSS;
