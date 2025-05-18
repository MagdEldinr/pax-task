from s3 import create_s3_bucket
from ec2 import create_ec2_instance
from rds import create_rds_instance

create_ec2_instance()
create_rds_instance()
create_s3_bucket()