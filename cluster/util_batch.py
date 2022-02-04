import yaml
import json
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--user', type=str, help='userId path', required=True)
args = parser.parse_args()

def load_config(file_path):
    with open(file_path) as f:
        loaded_config = yaml.safe_load(f)
    return loaded_config

def save_config(file_path,target_config):
    with open(file_path, 'w') as file:
        documents = yaml.dump(target_config, file, default_flow_style=False, sort_keys=False)

def generate_exmaple(efs_path):
    config_path = './config/example_job.yaml'
    target_config = load_config(config_path)
    target_config['mount_config'][0]['efs_path'] = efs_path
    
    config_path = './config/example_job.yaml'
    save_config(config_path,target_config)

generate_exmaple(args.user)