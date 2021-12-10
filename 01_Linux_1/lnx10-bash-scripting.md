# [Bash Scriping]
The default command line interface in Linux is called a Bash shell. You’ve already interacted with Linux using commands in this shell.
A Bash script is a series of commands written in a text file. You can execute multiple commands in a row by just executing the script.Additional logic can be applied with the use of variables, conditions, and loops among others.

In order to be able to execute the script, a user needs to have permissions to execute (x) the file.
Linux will only be able to find the script if you specify the path name, or if you add the path to the directory in which the script lives to the PATH variable.

Hint: although there are no file extensions in Linux, it’s easier for humans to understand if you end your script names with ‘.sh’.


## Key-terms


## Opdracht

**Exercise 1:**

1) Create a directory called ‘scripts’. Place all the scripts you make in this directory.

$ mkdir scripts

$ cd scripts

$ nano appendtext.sh

$ ls -l

$ chmod +x appendtext.sh (to be able to execute this script)


2) Add the scripts directory to the PATH variable.

$ echo $PATH

$ export PATH=$PATH:/home/quelan/scripts

$ echo $PATH
(set new path permanently by including it in ~/.bashrc)

3) Create a script that appends a line of text to a text file whenever it is executed.

**First, set PATH permanently to execute script at launch of terminal**

**Then make some text files in the same directory**

$ cd /     (home directory)

$ ls -l $HOME/.bashrc (verify file and writable permissions)

$ nano ~/.bashrc (root edit of this type of file)

add "export PATH=$PATH:/home/quelan/scripts (at end of file. This will append the new path to the variable. Adding the absolute path to the beginning of the file will make the system search that directory first every time. This is not recommended as it can cause problems with system programs and it adds unnecessary delay.)

**Now create script file to append text**

$ cd ~/scripts

$ nano appendtext.sh 

add script: echo "hanging in there" | tee -a *.txt   (-a=appends, and tee to modify multiple files)

$ bash appendtext.sh

$ cat test files



4) Create a script that installs the httpd package, activates httpd, and enables httpd. Finally, your script should print the status of httpd in the terminal.

In the scripts directory, create a .sh file.

$chmod +x .sh file

script: sudo apt update

**Variables:**
*You can assign a value to a string of characters so that the value can be read somewhere else in the script.
Assigning a variable is done using ‘=’.Reading the value of a variable is done using ‘$<insert variable name here>’*

**Exercise 2:**
*Create a script that generates a random number between 1 and 10, stores it in a variable, and then appends the number to a text file.
 
Variable pathway to activate scripts is already done permenently

$ nano randomnumbers.sh

script: shuf -i1-10 -n1 | tee -a .*txt (shuffles 1 random number from 1-10, and pipes it out to any .txt file as an appended content)
 

**Conditions:**
*You can choose to only run parts of your script if a certain condition is met. For example, only read a file if the file exists, or only write to a log if the health check returns an error. This can be done using conditions.*

A check for a condition can be done using ‘if’, ‘elif’, and/or ‘else’.*

**Exercise 3:**
*Create a script that generates a random number between 1 and 10, stores it in a variable, and then appends the number to a text file only if the number is bigger than 5. If the number is 5 or smaller, it should append a line of text to that same text file instead.

### Gebruikte bronnen
 
#### Exercise 1
https://opensource.com/article/17/6/set-path-linux

https://askubuntu.com/questions/73052/how-to-modify-etc-bash-bashrc-it-is-read-only
 
https://gist.github.com/nex3/c395b2f8fd4b02068be37c961301caa7
 
https://stackoverflow.com/questions/10865947/append-a-text-to-the-end-of-multiple-files-in-linux
 
https://linuxize.com/post/linux-tee-command/
 
https://www.cyberciti.biz/faq/run-execute-sh-shell-script/
 
https://linuxhint.com/apt_get_fix_missing_broken_packages/
 
https://www.cyberciti.biz/faq/linux-install-and-start-apache-httpd/
 
#### Exercise 2
 
https://stackoverflow.com/questions/2556190/random-number-from-a-range-in-a-bash-script
 
#### Exercise 3
 


### Ervaren problemen
 

### Resultaat
