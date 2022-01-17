from cluster.BatchCluster import BatchCluster
import uuid
import yaml
def load_config(file_path):
    with open(file_path) as f:
        loaded_config = yaml.safe_load(f)
    return loaded_config
class BatchJob:
    def __init__(self, clusterConfigFile="../.cluster/cluster.config", debugLog=False):
        self.cluster_config = load_config(clusterConfigFile)
        self.batch_clustername = "batchjob" +str(uuid.uuid4())[0:4]
        
        self.batch_cluster = BatchCluster(awsKeyID=self.cluster_config['aws_access_key_id'], 
                                        awsAccessKey=self.cluster_config['aws_secret_access_key'],
                                        batchClusterName=self.batch_clustername, 
                                        attachedClusterName=self.cluster_config['cluster_name'],
                                        debugLog=debugLog)
    
    def create_job(self, batchConfigFile="config/example_job.yaml", log_output=True):
        self.batchjob_config = load_config(batchConfigFile)

        comp_cpu_num = self.batchjob_config['cpu_num'] 
        # The hard limit (in GB) of memory to present to the container.
        memory_size = self.batchjob_config['memory_size']
        # The number of vCPUs reserved for the container. Each vCPU is equivalent to 1,024 CPU shares.
        vcpu_num = self.batchjob_config['vcpu_num'] 
        entry_cmd = self.batchjob_config['entry_cmd'] 
        image_name = self.batchjob_config['image_name'] 
        mount_config = self.batchjob_config['mount_config'][0]
        file_id = self.find_efs(mount_config['efs_name'])
        container_path = mount_config['container_path']
        job_name = self.batchjob_config['job_name'] 
        
        # create computer env and job queue
        vpc_id = self.cluster_config['vpc_id']
        self.batch_cluster.create_cluster(cpu_num=comp_cpu_num, vpc_id=vpc_id)
        
        # submit job
        batch_jobdef_name = "jobdef-" + self.batch_clustername + "-" + job_name 
        batch_jobdef_response = self.batch_cluster.create_jobdef(jobdef_name=batch_jobdef_name, 
                                        memory_size=memory_size, vcpu_num=vcpu_num, 
                                        entry_cmd=entry_cmd,
                                        image_id=image_name,
                                        file_system_id=file_id, #1 means for default efs
                                        container_path=container_path)
        batch_job_name = "job-" + self.batch_clustername + "-" + job_name 
        batch_job_response = self.batch_cluster.sub_job(job_name=batch_job_name, jobdef_resp=batch_jobdef_response)
        
        # log job
        if log_output:
            self.batch_cluster.log_job(batch_job_response)
        
        # delete job
        self.batch_cluster.deregister_job_definition(batch_jobdef_response)
        self.batch_cluster.destroy_job(batch_job_response)
        
        #delete cluster
        self.batch_cluster.destroy_cluster()
        
        return batch_job_response
    
    def find_efs(self, efs_name):
        efs_id = None
        for _d in self.cluster_config['efs_dict']:
            if _d['name'] == efs_name:
                efs_id = _d['efs_id']
                return efs_id
        print("not finding efs corresponding efs_name")
        return None
    
    def log_job():
        
        return 
    
    def delete_job():
        
        return 