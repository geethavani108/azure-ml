#! /usr/bin/sh

# Create random string
guid=$(cat /proc/sys/kernel/random/uuid)
suffix=${guid//[-]/}
suffix=${suffix:0:18}

# Set the necessary variables
RESOURCE_GROUP="gv-dp100-l${suffix}"
RESOURCE_PROVIDER="Microsoft.MachineLearning"
REGIONS=( "westus" "westus2" )
RANDOM_REGION=${REGIONS[$RANDOM % ${#REGIONS[@]}]}
WORKSPACE_NAME="mlw-dp100-l${suffix}"
COMPUTE_INSTANCE="gv${suffix}"
COMPUTE_CLUSTER="gvanicomputecluster"

# Register the Azure Machine Learning resource provider in the subscription
echo "Register the Machine Learning resource provider:"
az provider register --namespace $RESOURCE_PROVIDER

# Create the resource group and workspace and set to default
echo "Create a resource group and set as default:"
az group create --name $RESOURCE_GROUP --location $RANDOM_REGION
az configure --defaults group=$RESOURCE_GROUP

echo "Create an Azure Machine Learning workspace:"
az ml workspace create --name $WORKSPACE_NAME 
az configure --defaults workspace=$WORKSPACE_NAME 

# Create compute instance
echo "Creating a compute instance with name: " $COMPUTE_INSTANCE
#az ml compute create --name ${COMPUTE_INSTANCE} --size STANDARD_DS11_V2 --type ComputeInstance 
az ml compute create --name ${COMPUTE_INSTANCE} --size Standard_D2as_v4 --type ComputeInstance 

# Create compute cluster
#echo "Creating a compute cluster with name: " $COMPUTE_CLUSTER
#az ml compute create --name ${COMPUTE_CLUSTER} --size STANDARD_DS11_V2 --max-instances 2 --type AmlCompute 

"""
Standard_D2as_v4 2 cores, 8GB RAM, 16GB storage  General purpose   10 cores          $0.11/hr
Standard_DS1_v2  1 cores, 3.5GB RAM, 7GB storage  General purpose  5 cores        $0.07/hr
Standard_D2_v3     2 cores, 8GB RAM, 50GB storage General purpose 6 cores  $0.12/hr
Standard_D2s_v3  2 cores, 8GB RAM, 16GB storage General purpose 6 cores $0.12/hr
