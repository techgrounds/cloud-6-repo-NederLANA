# [Cron jobs]
There might be processes that you want to execute on a regular schedule. For example, you might want to write the available disk space to a log file every hour. Or maybe you want to check for system updates every 2nd day of the month.These kinds of jobs can be automated using Cron jobs.

## Key-terms

$ man cron

$ man crontab

--------

Each of the fields has the following meaning.

[Minute] [hour] [Day_of_the_Month] [Month_of_the_Year] [Day_of_the_Week] [command]

Minute 0 – 59

Hour 0 – 23

Day of month 1 – 31

Month of year 1 – 12

Day of week 0 – 7

## Opdracht
*Create a Bash script that writes the current date and time to a file in your home directory. 

$ nano cron_dt.sh

script to create append date & time in file: cron_date_time (in home directory)

$ chomod 765 -R *.sh (allows me rwx for all .sh files in directory and subdir)

$ bash cron_dt.sh (execute this script several times)

$ cat ../cron_date_time (pathway to home dir to see appended list of date/time)

*Register the script in your crontab so that it runs every minute.

$ systemctl status cron (verify if cron service is running)

$ crontab -l (listing of cron jobs already scheduled)

$ crontab -e (open a crontab to edit. **opens crontab of user**, otherwise crontab -e -u name)

script: * * * * * $HOME/scripts/cron_dt.sh (runs every minute)

$ crontab -r (remove cron jobs)


*Create a script that writes available disk space to a log file in ‘/var/logs’.

create script to append disk space to /var/logs file

script: sudo touch /var/log/diskspace (root create file)

sudo chmod 777 /var/log/diskspace (root permission to write file)

date >> /var/log/diskspace

df -H >> /var/log/diskspace (check disk space files, -H human readable 1000)

*Use a cron job so that it runs weekly.

$ crontab -e

script: @weekly $Home/scripts/disklog.sh

### Gebruikte bronnen

https://crontab.guru/#*_*_*_*_

https://www.cyberciti.biz/faq/how-do-i-add-jobs-to-cron-under-linux-or-unix-oses/

https://vitux.com/how-to-setup-a-cron-job-in-debian-10/

https://help.ubuntu.com/community/LinuxLogFiles#:~:text=The%20system%20log%20typically%20contains,information%20other%20logs%20do%20not.

https://stackoverflow.com/questions/22952237/create-files-in-my-shell-script-owned-by-root-without-the-need-for-sudo


### Ervaren problemen
I had some problem with attaining proper root permissions. 

### Resultaat

