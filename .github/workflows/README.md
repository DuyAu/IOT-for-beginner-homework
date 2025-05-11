# MyPlantApp 🌿

A web application that monitors soil moisture and manages plant watering automation using IoT and Azure services.

## 🚀 Features

- Monitors soil moisture levels via sensors
- Automatically adjusts watering based on sensor data
- Stores sensor data in Azure Blob Storage
- Uses Azure Functions with output bindings
- Securely stores API keys using environment variables
- Deployed on Azure Static Web Apps

## 📦 Tech Stack

- JavaScript (Node.js)
- Azure Functions
- Azure Static Web Apps
- Azure Blob Storage
- GitHub Actions (for CI/CD)

This app is automatically deployed using **Azure Static Web Apps + GitHub Actions**.

1. Push changes to `main` branch
2. GitHub Action builds and deploys to Azure
