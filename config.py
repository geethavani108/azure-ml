#pip install azure-ai-ml
#pip install azure-ai-identities
from azure.ai.ml import MLClient
from azure.identity import DefaultAzureCredential

credential = DefaultAzureCredential()
subscription_id= "your subscription",
resource_group= "gv-dp100-l744c846c2ac2425e86",
workspace_name= "mlw-dp100-l744c846c2ac2425e86"

ml_client = MLClient(
    credential=credential,
    subscription_id=subscription_id,
    resource_group=resource_group,
    workspace_name=workspace_name
)

print("MLClient initialized successfully in config.py")
