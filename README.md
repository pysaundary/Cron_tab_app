# Cron_tab_app
first run django project : python ./manage.py runserver
then 
run "python manage.py crontab add" add for adding crontab
for admin panel username is "pysaundary"
and password is "1010" all are numerical

all log will generate inside 'cron_app/files.log'

in this project log will generate in every 5 min  
for 12 PM we can use 0 12 * * *
('0 12 * * *', 'cron_app.cron.get_data','>> /home/pysaundary/Desktop/prabhat/project/Other/cron_app_api/cron_app/files.log'),
