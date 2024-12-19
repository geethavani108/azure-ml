# authenticate using Azurecli
from azure.ai.ml.entities import Model
from azure.ai.ml.constants import AssetTypes
from azure.ai.ml import MLClient
from azure.identity import DefaultAzureCredential
from azure.identity import AzureCliCredential
#credential = DefaultAzureCredential()
credential = AzureCliCredential()
subscription_id= "your subscription",
resource_group= "gv-dp100-l744c846c2ac2425e86",
workspace_name= "mlw-dp100-l744c846c2ac2425e86"

ml_client = MLClient(
    credential=credential,
    subscription_id=subscription_id,
    resource_group=resource_group,
    workspace_name=workspace_name
)

print("MLClient initialized successfully in configuration")
# Initialize MLClient
ml_client = MLClient.from_config(credential=credential)
# Define the model name and path
model_name = 'heart-prediction-pickle-model'

# Register the model as a custom model
model = ml_client.models.create_or_update(
    Model(name=model_name, path='./model', type=AssetTypes.CUSTOM_MODEL)
)

print(f"Model registered: {model.name} with version: {model.version}")
