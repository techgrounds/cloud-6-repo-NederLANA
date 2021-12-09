# [Users en groups]
Linux has users, similar to accounts on Windows and MacOS. Every user has their own home directory. Users can also be part of groups.
There is a special user called ‘root’. Root is allowed to do anything.
To gain temporary root permissions, you can type ‘sudo’ in front of a command, but that only works if you’re allowed to do that.

Some actions require (root) permissions.

Users, passwords, and groups are all stored in  (different) files across the system.

## Key-terms


## Opdracht
*Create a new user in your VM. 

*The new user should be part of an admin group that also contains the user you created during installation.

*The new user should have a password.

*The new user should be able to use ‘sudo’

Locate the files that store users, passwords, and groups. See if you can find your newly created user’s data in there.

### Gebruikte bronnen
https://github.com/rgl/azure-content/blob/master/articles/virtual-machines/virtual-machines-linux-add-user.md

https://www.cyberciti.biz/faq/ubuntu-list-groups-a-user-belongs-to-command/


### Ervaren problemen


### Resultaat
The -G command line flag will add the new user account to the proper Linux group giving the new user account root escalation privileges.

