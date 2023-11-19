# Command_line_for_windows

SFTP => Secure File Transfer Protocol

-----------------------------------------
1-first login to the server using this 
-----------------------------------------

sftp username@domainname

-----------------------------------------
now this is the remote device terminal
-----------------------------------------

sftp> 

***Note That***
---------------
the commands like (ls) will work for the remote server and if you want to accsess the local machine you have to
do it like that (lls) "this stands for local machine ls" 

-----------------------------------------
2- you can downlod files from the remote server using the (get) command 
-----------------------------------------

sftp> get [-afpR] remote [local]         Download file

-----------------------------------------
3- you can uplaod to the server using this command
-----------------------------------------

sftp> put [-afpR] local [remote]         Upload file 