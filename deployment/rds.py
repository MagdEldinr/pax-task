import pulumi
import pulumi_aws as aws
from pulumi import Config
import shared

config = Config()
db_password = config.require_secret("dbPassword")

def create_rds_instance():
    # Create RDS subnet group
    db_subnet_group = aws.rds.SubnetGroup("db-subnet-group",
        subnet_ids=[shared.subnet1.id, shared.subnet2.id],
        tags={"Name": "testmagd-db-subnet-group"}
    )
    # Create RDS PostgreSQL instance
    db_instance = aws.rds.Instance("testmagd-db",
        allocated_storage=20,
        engine="postgres",
        engine_version="17.2",
        instance_class="db.t3.micro",
        db_name="appdb",
        username="postgres",
        password=db_password,
        skip_final_snapshot=True,
        publicly_accessible=True,
        db_subnet_group_name=db_subnet_group.name,
        vpc_security_group_ids=[shared.security_group.id],
    )

    pulumi.export("rds_endpoint", db_instance.endpoint)
