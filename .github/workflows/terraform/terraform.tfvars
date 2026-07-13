aws_region = "us-east-1"


# VPC
vpc_cidr = "10.0.0.0/16"


# Public Subnets
public_subnet_a_cidr = "10.0.1.0/24"
public_subnet_b_cidr = "10.0.2.0/24"


# Private Subnets
private_subnet_a_cidr = "10.0.3.0/24"
private_subnet_b_cidr = "10.0.4.0/24"


# Availability Zones
availability_zone_a = "us-east-1a"
availability_zone_b = "us-east-1b"


# ECS
desired_count = 2

container_name = "area-container"

container_port = 5000


# Docker image from ECR
image_url = "004285425899.dkr.ecr.us-east-1.amazonaws.com/area-app:latest"

db_username = "selasi"

db_password = "mypassword123456"