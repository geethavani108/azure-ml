#run_batch_score_job.py
from azure.ai.ml import MLClient, Input
from azure.identity import DefaultAzureCredential
from config import ml_client
from azure.ai.ml import Input


# Define the Blob Storage base URL
blob_storage_base_url = "https://your_storage_account.blob.core.windows.net/your_container/"

# Define the input data for the batch job
input_data = Input(
    type=AssetTypes.URI_FILE,
    path=f"{blob_storage_base_url}heart_data_batch_1.csv",
    mode="ro_mount"  # Optional: Specifies how the data will be accessed, 'ro_mount' for read-only mount
)

# Define the output path for the batch job
output_path = f"{blob_storage_base_url}batch_output/"

 
# Define job details
job_name = "heart-disease-batch-job"

# Submit the batch job
ml_client.batch_jobs.create(
    name=job_name,
    endpoint_name='HeartDiseasePrediction-batch-endpoint',
    input=input_data,
    output=output_path
)

print(f"Batch job submitted: {job_name}")




print(f"Batch job submitted: {job_name}")

# Monitor the batch job
job_status = ml_client.batch_jobs.get(job_name).status
print(f"Job status: {job_status}")



