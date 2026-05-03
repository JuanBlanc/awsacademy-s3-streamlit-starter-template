import boto3

def load_json_from_s3(bucket: str, key: str, region: str) -> object:
    """Carga un JSON desde S3.

    Credenciales:
      - Preferido en AWS: IAM Role (Instance Profile) en EC2.
      - Alternativa en AWS Academy: `aws configure` en EC2 (usa ~/.aws/credentials).
    """
    s3 = boto3.client("s3", region_name=region)
    obj = s3.get_object(Bucket=bucket, Key=key)
    body = obj["Body"].read()
    # Acepta JSON array o JSON object
    import json
    return json.loads(body)
