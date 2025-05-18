import pulumi
import pulumi_aws as aws

# Create VPC
vpc = aws.ec2.Vpc("testmagd-vpc",
    cidr_block="10.0.0.0/16",
    enable_dns_hostnames=True,
    enable_dns_support=True
)


# Create two public subnets in different AZs
subnet1 = aws.ec2.Subnet("testmagd-1",
    vpc_id=vpc.id,
    cidr_block="10.0.1.0/24",
    availability_zone="eu-west-1a"
)

subnet2 = aws.ec2.Subnet("testmagd-2",
    vpc_id=vpc.id,
    cidr_block="10.0.2.0/24",
    availability_zone="eu-west-1b"
)

# Internet Gateway
igw = aws.ec2.InternetGateway("testmagd-igw", vpc_id=vpc.id)

# Route Table
route_table = aws.ec2.RouteTable("testmagd-route-table",
    vpc_id=vpc.id,
    routes=[{
        "cidr_block": "0.0.0.0/0",
        "gateway_id": igw.id,
    }]
)

# Associate subnets with route table
aws.ec2.RouteTableAssociation("rta-1",
    subnet_id=subnet1.id,
    route_table_id=route_table.id
)

aws.ec2.RouteTableAssociation("rta-2",
    subnet_id=subnet2.id,
    route_table_id=route_table.id
)

# Security group
security_group = aws.ec2.SecurityGroup("main-sg",
    vpc_id=vpc.id,
    description="Allow SSH and PostgreSQL",
    ingress=[
        {"protocol": "tcp", "from_port": 22, "to_port": 22, "cidr_blocks": ["0.0.0.0/0"]},
        {"protocol": "tcp", "from_port": 5432, "to_port": 5432, "cidr_blocks": ["0.0.0.0/0"]},
    ],
    egress=[{
        "protocol": "-1", "from_port": 0, "to_port": 0, "cidr_blocks": ["0.0.0.0/0"]
    }]
)

# Export shared infra
__all__ = [
    "vpc",
    "subnet1",
    "subnet2",
    "security_group"
]
