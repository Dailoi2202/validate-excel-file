import logging

import azure.functions as func
import pandas as pd 
import os 
import io
from azure.storage.blob import BlobClient,BlobServiceClient,ContentSettings, generate_blob_sas,BlobSasPermissions

def main(req: func.HttpRequest) -> func.HttpResponse:
    account_name
    account_name = 'uatsplannerauthservice1s'
    account_key = 'cfc3ALGtjhfwbeV/JBZrr7jwzO7hwoFYsAjZ1klWqYFVv74KSa8bdb183qntw1aDcpuQmu7h+bky+ASteb64Rg=='
    container_name = 'dbr-splanner-service'
    blob_name="MasterData / Price Master/List price W29.2022.xlsx"
    sas=generate_blob_sas(
      account_name=account_name,
      container_name=container_name,
      blob_name=blob_name,
      account_key=account_key,
      permission=BlobSasPermissions(read=True),
      expiry=datetime.utcnow() + timedelta(hours=1)
    )

    blob_url = f'https://{account_name}.blob.core.windows.net/{container_name}/{blob_name}?{sas}'
    df=pd.read_excel(blob_url)
    print(df)
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )
