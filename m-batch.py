#!/usr/bin/env python3
import sys
from cluster.MBatch import MBatch

CMD_OPTION_LENGTH = {
    'submit': 2, 
    'log': 2, 
    'status': 2, 
    'cancel': 2,  
    'list': 1, 
    'help': 0
    }
HELP_MSG = "Usage:  m-batch COMMAND [OPTION] \n\
Commands: \n\
    submit   Submit jobs to aws batch \n\
    log      Log output of the jobs \n\
    status   Check status of jobs \n\
    cancel   Cancel jobs \n\
    list     List all the existing job names \n\
    help     Print job help message "

def call_mbatch(CommandOption, JobConfig, JobNames):
    mbatch_tool = MBatch()
    if CommandOption == 'submit':
        mbatch_tool.submit_job(JobConfig, JobNames)
    if CommandOption == 'log':
        mbatch_tool.log_job(JobConfig, JobNames)
    if CommandOption == 'status':
        mbatch_tool.describe_job(JobConfig, JobNames)
    if CommandOption == 'cancel':
        mbatch_tool.cancel_job(JobConfig, JobNames)
    if CommandOption == 'list':
        mbatch_tool.list_job(JobConfig, JobNames)
    if CommandOption == 'help':
        print(HELP_MSG)

# m-batch submit XXX/hello_world.cfg {job_A}
# m-batch log XXX/hello_world.cfg {job_A} 
# m-batch status hello_world_job {job_A}
# m-batch cancel hello_word_job {job_A}
# m-batch list hello_world_job
# m-batch help

if __name__ == "__main__":
    sys_argv = sys.argv
    if len(sys_argv)<2:
        print(HELP_MSG)
        sys.exit()
    if sys_argv[1] in CMD_OPTION_LENGTH.keys():
        command_option = sys_argv[1]
        job_config = sys_argv[2] if len(sys_argv)>=3 else None
        job_names = sys_argv[3] if len(sys_argv)>=4 else None
        call_mbatch(command_option, job_config, job_names)
    else: 
        print(f"m-batch does not support {sys_argv[1]}")
        print(HELP_MSG)
