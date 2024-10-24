import os
from pathlib import Path

from load_data import download_data
from prefect import serve
from workflow import train_model_workflow

if __name__ == "__main__":
    data_folder = "abalone-dataset"
    csv_file = os.path.join(data_folder, "abalone.csv")

    # Check if the data file exists, download if it doesn't
    if not os.path.exists(csv_file):
        download_data(force=False)

    train_model_deployment = train_model_workflow.to_deployment(
        name="Model training Deployment",
        version="0.1.0",
        tags=["training", "model"],
        cron="0 0 * * 0",
        parameters={
            "trainset_path": Path(csv_file),
            "artifacts_filepath": "../web_service",
        },
    )

    serve(train_model_deployment)
