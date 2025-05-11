import logging

import azure.functions as func

def main(req: func.HttpRequest, outputBlob: func.Out[str]) -> func.HttpResponse:
    logging.info('Processing request...')
    data = req.get_body().decode("utf-8")

    outputBlob.set(data)

    return func.HttpResponse("Data written to blob!", status_code=200)
