# Bash Scriping
The default command line interface in Linux is called a Bash shell. You’ve already interacted with Linux using commands in this shell.
A Bash script is a series of commands written in a text file. You can execute multiple commands in a row by just executing the script.Additional logic can be applied with the use of variables, conditions, and loops among others.

In order to be able to execute the script, a user needs to have permissions to execute (x) the file.
Linux will only be able to find the script if you specify the path name, or if you add the path to the directory in which the script lives to the PATH variable.

Hint: although there are no file extensions in Linux, it’s easier for humans to understand if you end your script names with ‘.sh’.

## Key-terms
File permissions

Path variable- The $PATH variable is the key that makes it possible to find the correct program and execute it at your command without needing the executable's full directory path every time you execute (a script file for this assignment)

variable

conditions


## Opdracht

### Exercise 1:

**Create a directory called ‘scripts’. Place all the scripts you make in this directory.

$ pwd

$ mkdir scripts

$ cd ~/scripts (change directory to move to scripts directory you made)

$ ls -l 

![lnx01-mkdir-scripts](https://user-images.githubusercontent.com/4924632/146000908-e252840a-4b1a-46c0-bce9-adbb86b2f250.png)


**Add the scripts directory to the PATH variable.**

$ echo $PATH

$ export PATH=$PATH:/home/quelan/scripts (This will append the new path to the variable. Adding the absolute path to the beginning of the file will make the system search that directory first every time. This is not recommended as it can cause problems with system programs and it adds unnecessary delay.)

$ echo $PATH (to see the scripts directory added to the path variable.)

![lnx10-ex1-path-variable](https://user-images.githubusercontent.com/4924632/146003844-3d4719c3-16e3-4de0-bdea-464e31febbc8.png)

**Just an extra step I did. A common mistake with the $PATH variable is to set it in the current shell only, without persisting the change. When you open a new shell, the changes are lost, and you are once again unable to execute certain commands because those programs are not found in the PATH.**

**Set PATH permanently to be able to execute scripts at launch by including it in a root configuration called ~/.bashrc**

$ cd /     (home directory)

$ ls -l $HOME/.bashrc (verify file and writable permissions)

$ nano ~/.bashrc (command to root edit of this type of file)

add "export PATH=$PATH:/home/quelan/scripts (at end of file)

![lnx10-ex1-permanent-path](https://user-images.githubusercontent.com/4924632/146005092-9378a34b-7d76-4cdb-9bc2-fef0fa48e3b6.png)


**Create a script that appends a line of text to a text file whenever it is executed.**

Make 2 files with a line of text in each file.
Now create script file to append text

$ cd ~/scripts

$ nano appendtext.sh 

$ appendtext.sh (execute script) 

![lnx10-ex1-script-append-text](https://user-images.githubusercontent.com/4924632/146006657-2b2807c7-fab5-4860-9ddc-314b1d4f3bc0.png)

$ cat <test files>

![lnx10-ex1-output-appendtext](https://user-images.githubusercontent.com/4924632/146006961-379eb564-43fc-4607-b041-a6c0cac863fe.png)

**Create a script that installs the httpd package, activates httpd, and enables httpd. Finally, your script should print the status of httpd in the terminal.**

Keep in mind that httpd package is for CentOS, but in Ubuntu, it is the apache2 package

$nano deployhttpd.sh

$chmod +x *.sh file (changes execute permissions for all .sh files in the directory)

![lnx10-ex1-script-deployhttpd](https://user-images.githubusercontent.com/4924632/146009697-32c0f55e-7037-48ca-b1af-dc8fb4848a81.png)

**Output of the script shows the status of apache2 in the terminal.**
 
$^c to return the command line

![lnx10-ex1-output-apache-status](https://user-images.githubusercontent.com/4924632/146010485-f0d9f8bc-d8a5-47d7-947e-1c7d8e92423c.png)

--------

### Variables:
* You can assign a value to a string of characters so that the value can be read somewhere else in the script.
* Assigning a variable is done using ‘=’.Reading the value of a variable is done using ‘$<insert variable name here>’*

### Exercise 2:
**Create a script that generates a random number between 1 and 10, stores it in a variable, and then appends the number to a text file (called randomNUM).**

$ nano ex02.sh

 ![lnx10-ex2-script-random-number](https://user-images.githubusercontent.com/4924632/146016440-5a2fe640-1226-4515-b072-3d3505f2ffaf.png)
 
 ![lnx10-ex2-output-randomNUM](https://user-images.githubusercontent.com/4924632/146033736-4a1067f4-1ca8-4636-a824-4f8bb2fcaec2.png)

----
### Conditions:
You can choose to only run parts of your script if a certain condition is met. For example, only read a file if the file exists, or only write to a log if the health check returns an error. This can be done using conditions.*

A check for a condition can be done using ‘if’, ‘elif’, and/or ‘else’.

### Exercise 3:
**Create a script that generates a random number between 1 and 10, stores it in a variable, and then appends the number to a text file only if the number is bigger than 5. If the number is 5 or smaller, it should append a line of text to that same text file instead.**

$nano ex03.sh
 
 ![lnx10-ex3-script-if-else](https://user-images.githubusercontent.com/4924632/146034427-b06d03be-d687-4114-acbd-7d222d7ed39c.png)

 ![lnx10-ex3-output-conditional](https://user-images.githubusercontent.com/4924632/146034712-bcfcb05c-f02d-431f-a487-a4cee19048d1.png)


### Gebruikte bronnen
 
https://opensource.com/article/17/6/set-path-linux

https://askubuntu.com/questions/73052/how-to-modify-etc-bash-bashrc-it-is-read-only
 
https://gist.github.com/nex3/c395b2f8fd4b02068be37c961301caa7
 
https://stackoverflow.com/questions/10865947/append-a-text-to-the-end-of-multiple-files-in-linux
 
https://linuxize.com/post/linux-tee-command/
 
https://www.cyberciti.biz/faq/run-execute-sh-shell-script/
 
https://linuxhint.com/apt_get_fix_missing_broken_packages/
 
https://www.cyberciti.biz/faq/linux-install-and-start-apache-httpd/
 
https://stackoverflow.com/questions/2556190/random-number-from-a-range-in-a-bash-script
 
 


### Ervaren problemen
 Whew! 
 Here you want to be careful to have proper file permissions, and know when to use SUDO command for root permissions.

### Resultaat
