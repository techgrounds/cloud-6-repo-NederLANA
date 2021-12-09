# [Processes]
Processes in Linux can be divided into three categories: Daemons, Services, and Programs.A daemon runs in the background and is non-interactive. A Service responds to requests from programs. A service may be interactive. A program is run and used by users (e.g. Vim).

In order to connect to remote Linux machines (virtual or not), you can use ssh (secure shell). To make this connection to your machine possible, you’ll have to start the ssh service by starting the ssh daemon.

A process is an instance of running code. All code is stored in files somewhere on the system. In order to find these files, Linux will look in the $PATH variable (more about that in a later exercise). Every process has its own PID (Process ID) number.

## Key-terms


## Opdracht
1) Start the ssh daemon. (first must install it)

$ sudo apt-get install openssh-server

$sudo apt autoremove (to remove suggested uncessary files)

$ sudo systemctl start ssh (For systemd based Ubuntu Linux 16.04/18.04/20.04 LTS or above)

2) Find out the PID of the ssh daemon.

$ sudo systemctl status ssh

3) Find out how much memory the sshd is using.

$ free -m

4) Stop or kill the sshd process.

$ sudo systemctl stop ssh

$ sudo systemctl status ssh


### Gebruikte bronnen
https://www.cyberciti.biz/faq/howto-start-stop-ssh-server/

https://askubuntu.com/questions/1161579/ssh-server-cannot-be-found-even-though-installed

https://askubuntu.com/questions/163200/e-dpkg-was-interrupted-run-sudo-dpkg-configure-a

https://www.a2hosting.com/kb/developer-corner/linux/determining-a-servers-memory-usage


### Ervaren problemen
geen

### Resultaat
zie toegevoegd beelden
