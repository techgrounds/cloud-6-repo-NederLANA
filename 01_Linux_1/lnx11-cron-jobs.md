# Cron jobs
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
**Create a Bash script that writes the current date and time to a file in your home directory.**

$ nano cron_dt.sh

script to create appended date & time in file: cron_date_time (pathway to create file in home directory)

$ chomod 765 -R *.sh (allows me rwx for all .sh files in directory and subdir)

$ cron_dt.sh (execute this script several times)

$ cat ../cron_date_time (pathway to home dir to check appended list of date/time)

![lnx11-date-time-script](https://user-images.githubusercontent.com/4924632/145993449-c505d0eb-9936-4b76-8954-44c38ca0e92e.png)


**Register the script in your crontab so that it runs every minute.**

$ systemctl status cron (verify if cron service is running)

$ crontab -l (listing of cron jobs already scheduled)

$ crontab -e (open a crontab to edit. **opens crontab of user**, otherwise crontab -e -u name)

cron script: * * * * * $HOME/scripts/cron_dt.sh (runs every minute)

$ crontab -r (remove cron jobs)


![cron-output-date-time](https://user-images.githubusercontent.com/4924632/145971515-10606c58-9c8a-4fbe-a684-05481e381134.png)


**Create a script that writes available disk space to a log file in ‘/var/logs’.**

create script to append disk space to /var/logs/diskspace

![lnx11-diskspace-script](https://user-images.githubusercontent.com/4924632/145993737-41f30180-5446-43b3-8464-50efb1dde78e.png)


**Use a cron job so that it runs weekly.

$ crontab -e

cron script: @weekly $Home/scripts/disklog.sh

![cron-output-diskspace](https://user-images.githubusercontent.com/4924632/145971577-58099679-421f-4a26-bbad-f943ba165145.png)


### Gebruikte bronnen

https://crontab.guru/#*_*_*_*_

https://www.cyberciti.biz/faq/how-do-i-add-jobs-to-cron-under-linux-or-unix-oses/

https://vitux.com/how-to-setup-a-cron-job-in-debian-10/

https://help.ubuntu.com/community/LinuxLogFiles#:~:text=The%20system%20log%20typically%20contains,information%20other%20logs%20do%20not.

https://stackoverflow.com/questions/22952237/create-files-in-my-shell-script-owned-by-root-without-the-need-for-sudo


### Ervaren problemen
I had some problem with attaining proper root permissions, and trying to do a command in the wrong directory. So keep an eye on that.

### Resultaat
<<<<<<< HEAD
![testing](C:\Users\TechGrounds\cloud-6-repo-NederLANA\01_Linux_1\lnx11-cron-jobs.md)
=======

![image](https://user-images.githubusercontent.com/4924632/148286546-413a0d63-6f05-4aa0-ad76-378b8f0f8a70.png)

>>>>>>> 5550eab26cc72a9b2f99d24e6b9c36c6f76ba4af
