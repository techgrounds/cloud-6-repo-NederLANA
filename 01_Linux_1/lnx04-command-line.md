# [Working with text CLI]
Every command in Linux has a standard input and output.

The standard input (stdin) is the keyboard. 
If I run ‘mkdir myfolder’, the mkdir command will know what folder to create, because I typed ‘myfolder’.

The standard output (stdout) is the terminal. 
The command ‘echo hello’ will write ‘hello’ in the terminal.

Both the input and output can be redirected to a file instead of the default. This is called input redirection and output redirection. 
A pipe can be used to have the output of one command be the input of another command.

## Key-terms
Redirection can be defined as changing the way from where commands read input to where commands sends output. You can redirect input and output of a command.

For redirection, meta characters are used. Redirection can be into a file (shell meta characters are angle brackets '<', '>') or a program ( shell meta characters are pipesymbol '|').

## Opdracht

* Use the echo command and output redirection to write a new sentence into your text file using the command line. The new sentence should contain the word ‘techgrounds’.

* Use a command to write the contents of your text file to the terminal. Make use of a command to filter the output so that only the sentence containing ‘techgrounds’ appears.

* Read your text file with the command used in the second step, once again filtering for the word ‘techgrounds’. This time, redirect the output to a new file called ‘techgrounds.txt’.

### Gebruikte bronnen
https://www.howtogeek.com/199687/how-to-quickly-create-a-text-file-using-the-command-line-in-linux/

https://www.javatpoint.com/linux-input-output-redirection

https://thoughtbot.com/blog/input-output-redirection-in-the-shell

https://docs.oracle.com/cd/E19253-01/806-7612/filesearch-96061/index.html (grep)



### Ervaren problemen


### Resultaat

1) Make a text file with two sentences ($cat > sample.txt)

2) Then $echo I am always at Techgrounds >> sample.txt  (>> is to append)

3) $cat sample.txt

4) To search for a particular character string in a file, use the grep command. 
   $grep Techgrounds sample.txt
   
5) $cat sample.txt | grep Techgrounds > techgrounds.txt

