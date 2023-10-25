from ._import import *

client = boto3.client(
    "sns",
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    region_name=os.getenv("AWS_REGION_NAME"),
)


def send_email(destination, source, subject, body):
    response = client.send_email(
        Destination={
            "ToAddresses": [destination],
        },
        Message={
            "Body": {
                "Html": {
                    "Charset": "UTF-8",
                    "Data": body,
                },
            },
            "Subject": {
                "Charset": "UTF-8",
                "Data": subject,
            },
        },
        Source=source,
    )
    return response
