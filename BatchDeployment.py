from azure.ai.ml.entities import ComputeInstance
from azure.ai.ml import MLClient

# Example of defining a compute cluster
compute_cluster_name = "your-compute-cluster"
compute_target = ComputeInstance(name=compute_cluster_name, size="Standard_DS3_v2")


from azure.ai.ml.entities import BatchDeployment, BatchEndpoint
from config import ml_client



# Define the endpoint and deployment names
endpoint_name = "HeartDiseasePrediction-batch-endpoint"
deployment_name = "HeartDiseasePrediction-batch-deployment"

# Create Batch Endpoint
endpoint = BatchEndpoint(
    name=endpoint_name,
    description="Batch endpoint for HeartDisease prediction model"
)


# Create Batch Deployment
deployment = BatchDeployment(
    name=deployment_name,
    endpoint_name=endpoint_name,
    model='HeartDisease-pickle-model',
    compute='compute-cluster',
    #output_path="azureml://datastores/your_datastore_name/paths/batch_output/",
    output_path = "https://your_storage_account.blob.core.windows.net/your_container/your_path/"
    #output_path = "/home/user/logs/"
    instance_count=2,
    error_threshold=0
)
ml_client.compute.create_or_update(compute_target)
print(f"Cluster created sucessfully: {deployment.name}")
ml_client.batch_endpoints.create_or_update(endpoint)
print(f"Batch endpoints sucessfully: {deployment.name}")
ml_client.batch_deployments.create_or_update(deployment)

print(f"Batch deployment created sucessfully: {deployment.name}")



