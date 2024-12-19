from azure.ai.ml.entities import Model
from azure.ai.ml.constants import AssetTypes
from config import ml_client

# Define the model name and path
model_name = 'heart-prediction-pickle-model'

# Register the model as a custom model
model = ml_client.models.create_or_update(
    Model(name=model_name, path='./model', type=AssetTypes.CUSTOM_MODEL)
)

print(f"Model registered: {model.name} with version: {model.version}")
