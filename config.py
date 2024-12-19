from azure.ai.ml import MLClient
from azure.identity import DefaultAzureCredential

# Initialize MLClient
credential = DefaultAzureCredential()
ml_client = MLClient.from_config(credential=credential)


from azure.ai.ml import MLClient
from azure.identity import DefaultAzureCredential

# authenticate
credential = DefaultAzureCredential()

SUBSCRIPTION="your subscription id"
RESOURCE_GROUP="gv-dp100-l9d092690c5d049baa1"
WS_NAME="mlw-dp100-l9d092690c5d049baa1"
# Get a handle to the workspace
ml_client = MLClient(
    credential=credential,
    subscription_id=SUBSCRIPTION,
    resource_group_name=RESOURCE_GROUP,
    workspace_name=WS_NAME,
)
ml_client = MLClient.from_config(credential=credential)
