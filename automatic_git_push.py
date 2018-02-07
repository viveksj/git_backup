#!/usr/bin/python
#After saving this file. remember to assign file permission by using "chmod a+x filetype.py" command in the terminal
#Assumption. Git Directory initialized. Credentials configured and upstream connected.
import datetime
import subprocess
subprocess.call(['git', 'add', '.'])
#Instead of '.' as the 3rd parameter, we can the specific script/folder that we wish to push to the git.
subprocess.call(['git', 'commit', '-m',("Daily Update"+(str(datetime.datetime.now())))])
subprocess.call(['git', 'push', '-u'])
#Assumption2. Crontab is used to schedule it to run daily.
#Enter in the terminal: "crontab -e" followed by the following command in double quotes
#"0 4 * * * python2 abosulute_file_path/automatic_git_push.py | tee -a abosulute_file_path/automatic_git_push_log.log 2>&1;"