美国纽约州立大学CS558计算机网络安全作业，一个用Python实现的SSH程序。

证书用openssl签发2048bit.

有些系统上1024bit会报错



## Files

SSHServer/ca.crt    : the X509 certificate file of CA 

​		/server.key : the private key of server

​		/server.crt : server   X509 certificate file issued by  CA

​		/SSHserver.py:  the server  python3 source code

​		/Util.py : some file utilities helper functions

SSHClient/ca.crt    : the certificate file of CA 

​		/client.key : the private key of client

​		/client.crt : clientcertificate file issued by  CA

​		/SSHclient.py:  the client python3 source code

## compile and execute 

put the the folder SSHServer into a server machine 

put the folder SSHClient  into another client machine 

Environment Needed: Python 3.x 



Run:

1. run the server firstly:

python3 ./SSHserver.py --domain *ServerDomainName* --port *ServerPort*

e.g: python3 ./SSHserver.py --domain   remote01.cs.binghamton.edu --port 7777

or run by ip address:

e.g: python3 ./SSHserver.py --domain   192.168.1.12 --port 7777

where "192.168.1.12" is the ipv4 address of server machine (you can get it by command ifconfig)





2. then run the client:

   python3 ./SSHclient.py --domain *ServerDomainName* --port *ServerPort*

e.g: python3 ./SSHclient.py --domain   remote01.cs.binghamton.edu --port 7777

or run by ip address:

e.g: python3 ./SSHclient.py --domain   192.168.1.12 --port 7777

where "192.168.1.12" is the ipv4 address of server machine (you can get it by command ifconfig)



3 supported comands:

ls: get all of the file names of current directory.

pwd: get present work directory

exit: exit the ssh

