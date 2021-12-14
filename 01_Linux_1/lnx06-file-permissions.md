# [File permissions]
Every file in Linux contains a set of permissions. There are separate permissions for reading, writing, and executing files (rwx). There’s also three types of entities that can have different permissions: the owner of the file, a group, and everyone else. Root does not need permissions to read, write or execute a file.

You can view a file’s permissions by creating a long listing. A file’s permissions, as well as its owner and group, can be changed as well.
Any user listed in /etc/passwd can be assigned as owner of a file.
Any group listed in /etc/group can be assigned as the group of a file.

## Key-terms
When in the command line, the permissions are edited by using the command chmod. You can assign the permissions explicitly or by using a binary reference as described below.

### Permission Groups:
u – Owner
g – Group
o – Others
a – All users

### Permission types: (r=4, w=2, x=1) (+=add permission, -=remove permission)
r – Read
w – Write
x – Execute

### Permissions
chmod: change file permissions
chown: change file owner
chgrp: change group ownership
id: print user and group IDs


## Opdracht
*Create a text file.

1) Make a long listing to view the file’s permissions. Who is the file’s owner and group? What kind of permissions does the file have?

2) Make the file executable by adding the execute permission (x).
$ chmod 775 thursday.txt (+1x to existing binary notations)

3) Remove the read and write permissions (rw) from the file for the group and everyone else, but not for the owner. Can you still read it?
$ chmod 711 thursday.txt (-4r & -2w)

4) Change the owner of the file to a different user. If everything went well, you shouldn’t be able to read the file unless you assume root privileges with ‘sudo’.
$ sudo chown pear thursday.txt (sudo gives root privileges)

![change-owner-permission](https://user-images.githubusercontent.com/4924632/145972106-927293c8-87d0-4ab1-a626-7c601a0cff31.png)


5) Change the group ownership of the file to a different group.
$ sudo chgrp root thursday.txt (gives ownership to root)

![change-group-permission](https://user-images.githubusercontent.com/4924632/145972054-c81ab7b5-7132-4a26-9d2d-5d2544f0255f.png)



### Gebruikte bronnen
https://www.linux.com/training-tutorials/understanding-linux-file-permissions/

https://www.pluralsight.com/guides/linux-permissions

https://www.howtoforge.com/linux-chgrp-command/

### Ervaren problemen


### Resultaat

