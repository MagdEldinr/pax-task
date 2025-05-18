import pulumi
import pulumi_aws as aws
import shared

def create_ec2_instance():
    ami = aws.ec2.get_ami(
        most_recent=True,
        owners=["099720109477"],
        filters=[{
            "name": "name",
            "values": ["ubuntu/images/hvm-ssd/ubuntu-focal-20.04-amd64-server-*"],
        }],
    )

    # Launch EC2 instance
    instance = aws.ec2.Instance("testmagd",
        ami=ami.id,
        instance_type="t3.micro",
        subnet_id=shared.subnet1.id,
        vpc_security_group_ids=[shared.security_group.id],
        associate_public_ip_address=True,
        user_data="""#!/bin/bash
        sudo apt update -y
        sudo apt install -y nginx
        sudo systemctl start nginx
        """,
    )

    pulumi.export("ec2_public_ip", instance.public_ip)
    pulumi.export("ec2_public_dns", instance.public_dns)
