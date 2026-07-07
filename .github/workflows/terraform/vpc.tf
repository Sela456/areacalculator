#Creating Vpc
resource "aws_vpc" "main" {
    cidr_block                = "10.0.0.0/16"
    tags = {
        Name = "vpc-main"
    }
}

#creating subnets
resource "aws_subnet" "public_a" {
    cidr_block                = "10.0.1.0/24"
    availability_zone         = "us-east-1a"
    map_public_ip_on_launch   = true
    vpc_id                    = aws_vpc.main.id
    tags = {
        Name = "subnet-public-a"
    }
}

resource "aws_subnet" "public_b" {
    vpc_id                    = aws_vpc.main.id
    cidr_block                = "10.0.2.0/24"
    availability_zone         = "us-east-1b"
    map_public_ip_on_launch   = true
    tags = {
        Name = "subnet-public-b"
    }
}

resource "aws_subnet" "private_a" {
    vpc_id                     = aws_vpc.main.id
    cidr_block                 = "10.0.3.0/24"
    availability_zone          = "us-east-1a"
    tags = {
        Name = "subnet-private-a"
    }
}

resource "aws_subnet" "private_b" {
    vpc_id                     = aws_vpc.main.id
    cidr_block                 = "10.0.4.0/24"
    availability_zone          = "us-east-1b"
    tags = {
        Name = "subnet-private-b"
    }
}

#create internet gateway for vpc
resource "aws_internet_gateway" "igw" {
    vpc_id                     = aws_vpc.main.id
    tags = {
        Name = "igw"
    }
}

#create route table and route
resource "aws_route_table" "public_rt" {
    vpc_id                     = aws_vpc.main.id 
    tags = {
        Name = "public-rt"
    }
}

resource "aws_route" "public_route" {
    route_table_id             = aws_route_table.public_rt.id
    gateway_id                 = aws_internet_gateway.igw.id
    destination_cidr_block     = "0.0.0.0/0"
}

resource "aws_route_table_association" "public_a_association" {
    subnet_id                  = aws_subnet.public_a.id
    route_table_id             = aws_route_table.public_rt.id

}

resource "aws_route_table_association" "public_b_association" {
    subnet_id                  = aws_subnet.public_b.id
    route_table_id             = aws_route_table.public_rt.id
}

#creating nat gateway for private subnets
resource "aws_nat_gateway" "nat" {
    subnet_id                  = aws_subnet.public_a.id
    allocation_id              = aws_eip.nat_eip.id
    depends_on                 = [aws_internet_gateway.igw]
    tags = {
        Name = "nat"
    }
}

resource "aws_eip" "nat_eip" {
    domain = "vpc"
    tags = {
        Name = "nat-eip"
    }
}

#create route table and route for private subnet
resource "aws_route_table" "private_rt" {
    vpc_id                     = aws_vpc.main.id
    tags = {
        Name = "private-rt"
    }
} 

resource "aws_route" "private_route" {
    route_table_id             = aws_route_table.private_rt.id
    nat_gateway_id             = aws_nat_gateway.nat.id
    destination_cidr_block     = "0.0.0.0/0"
}

resource "aws_route_table_association" "private_a_association" {
    subnet_id                  = aws_subnet.private_a.id
    route_table_id             = aws_route_table.private_rt.id

}

resource "aws_route_table_association" "private_b_association" {
    subnet_id                  = aws_subnet.private_b.id
    route_table_id             = aws_route_table.private_rt.id

}