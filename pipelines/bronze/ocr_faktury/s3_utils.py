# NOTE: For large buckets, S3 pagination should be used (paginator)

def list_pdf_keys(s3_client, bucket, prefix):
    response = s3_client.list_objects_v2(Bucket=bucket, Prefix=prefix)

    return [
        obj["Key"]
        for obj in response.get("Contents", [])
        if obj["Key"].lower().endswith(".pdf")
    ]

def get_pdf_bytes(s3_client,bucket, key):
    obj = s3_client.get_object(Bucket=bucket, Key=key)
    return obj["Body"].read()


def ocr_exists(s3_client, bucket, ocr_key):
    try:
        s3_client.head_object(Bucket=bucket, Key=ocr_key)
        return True
    except s3_client.exceptions.ClientError:
        return False 
    

def save_ocr(s3_client, bucket, ocr_key, text):
    s3_client.put_object(
        Bucket=bucket,
        Key=ocr_key,
        Body=text.encode("utf-8")
    )