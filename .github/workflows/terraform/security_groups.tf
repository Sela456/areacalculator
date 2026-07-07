#create  alb security group
resource "aws_security_group" "alb_sg" {
    name                        = "alb-sg"
    description                 = "alb-security-group"
    vpc_id                      = aws_vpc.main.id
    ingress {
        from_port      = 80
        to_port        = 80
        protocol       = "tcp"
        cidr_blocks    = ["0.0.0.0/0"]
    }
    egress {
        from_port      = 0
        to_port        = 0
        protocol       = "-1"
        cidr_blocks    = ["0.0.0.0/0"]
    }
    tags = {
        Name = "alb-sg"
    }
}

#create ecs security group
resource "aws_security_group" "ecs_sg" {
    name                         = "ecs-sg"
    description                  = "ecs-security-group"
    vpc_id                       = aws_vpc.main.id

    ingress {
        from_port       = 5000
        to_port         = 5000
        protocol        = "tcp"
        cidr_blocks     = [aws_security_group.alb_sg.id]
    }
    egress {
        from_port       = 0
        to_port         = 0
        protocol        = "-1"
        cidr_blocks     = ["0.0.0.0/0"]
    }

    tags = {
        Name = "ecs-sg"
    }
}
