import pulumi
import pulumi_aws as aws

def create_s3_bucket():
    # Create a private S3 bucket with tags
    bucket = aws.s3.Bucket("testmagdeldin-bucket")

    pulumi.export("s3_bucket_name", bucket.id)
