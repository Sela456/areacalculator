#create alb
resource "aws_lb" "alb" {
    name                    = "alb"
    load_balancer_type      = "application"
    subnets                 = [aws_subnet.public_a.id, aws_subnet.public_b.id]
    security_groups         = [aws_security_group.alb_sg.id]
    tags = {
        Name = "alb"
    }
}

#create alb listener
resource "aws_lb_listener" "http_listener" {
    load_balancer_arn        = aws_lb.alb.arn
    port                    = 80
    protocol                = "HTTP"
    default_action {
        type        = "forward"
        target_group_arn = aws_lb_target_group.alb_tg.arn
    }
}

#create target group
resource "aws_lb_target_group" "alb_tg" {
    name                    = "alb-tg"
    port                    = 5000
    protocol                = "HTTP"
    target_type             = "ip"
    vpc_id                  = aws_vpc.main.id 

    health_check {
        path     = "/"
        protocol = "HTTP"
        matcher  = "200"
        interval = 30
        timeout  = 5
        healthy_threshold   = 2
        unhealthy_threshold = 2
        
    }
    tags = {
        Name = "alb-tg"
    }
}