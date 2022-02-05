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
            i = f'  efs_path: {user}\n'
        if 'job_name' in i:
            i = f'job_name: job{user}\n'
        f.write(i)