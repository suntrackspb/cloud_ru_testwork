#!/bin/bash

# Set the namespace name
NAMESPACE="cloud-ru-namespace"

# Set the chart directory
CHART_DIR="./"

# Set the values file path
VALUES_FILE="values.yaml"

# Create the namespace
kubectl create namespace $NAMESPACE

# Install the chart
helm install cloud-ru $CHART_DIR -f $VALUES_FILE --namespace $NAMESPACE

# Uninstall the chart
# helm uninstall cloud-ru --namespace $NAMESPACE