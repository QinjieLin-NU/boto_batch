import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--user', type=str, help='userId path', required=True)
args = parser.parse_args()

with open("config/example_job.yaml",'r') as f:
    x = f.readlines()

user=args.user
with open("config/example_job.yaml",'w') as f:
    for i in x:
        if 'efs_path' in i:
            i = '  efs_path: %s\n'%(user)
        if 'job_name' in i:
            i = 'job_name: job%s\n'%(user)
        f.write(i)