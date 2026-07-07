variable "aws_region" {
  description = "AWS region where resources will be created"
  type        = string
}


variable "vpc_cidr" {
  description = "CIDR block for the VPC"
  type        = string
}


variable "public_subnet_a_cidr" {
  description = "CIDR block for public subnet A"
  type        = string
}


variable "public_subnet_b_cidr" {
  description = "CIDR block for public subnet B"
  type        = string
}


variable "private_subnet_a_cidr" {
  description = "CIDR block for private subnet A"
  type        = string
}


variable "private_subnet_b_cidr" {
  description = "CIDR block for private subnet B"
  type        = string
}


variable "availability_zone_a" {
  description = "First availability zone"
  type        = string
}


variable "availability_zone_b" {
  description = "Second availability zone"
  type        = string
}


variable "desired_count" {
  description = "Number of ECS tasks to run"
  type        = number
}


variable "container_name" {
  description = "Name of the application container"
  type        = string
}


variable "container_port" {
  description = "Port exposed by the application container"
  type        = number
}


variable "image_url" {
  description = "Docker image URL from ECR"
  type        = string
}