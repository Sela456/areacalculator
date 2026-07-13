# create ecs cluster and ecs task definition
resource "aws_ecs_cluster" "app" {
  name = "ecs-cluster"
  tags = {
    Name = "ecs-cluster"
  }
}

resource "aws_ecs_task_definition" "task_definition" {

  family = "area-task"

  # Required for Fargate
  network_mode = "awsvpc"

  requires_compatibilities = [
    "FARGATE"
  ]

  cpu = 256

  memory = 512

  execution_role_arn = aws_iam_role.ecs_execution_role.arn


  container_definitions = jsonencode([
    {
      name = "area-container"

      image = "004285425899.dkr.ecr.us-east-1.amazonaws.com/area-app:latest"

      essential = true


      portMappings = [
        {
          containerPort = 5000
          hostPort      = 5000
          protocol      = "tcp"
        }
      ]


      environment = [
        {
          name  = "DB_HOST"
          value = aws_db_instance.area_database.address
        },
        {
          name  = "DB_NAME"
          value = "areaapp"
        },
        {
          name  = "DB_USER"
          value = var.db_username
        },
        {
          name  = "DB_PASSWORD"
          value = var.db_password
        },
        {
          name  = "DB_PORT"
          value = "5432"
        }
      ]


      logConfiguration = {

        logDriver = "awslogs"

        options = {

          awslogs-group = aws_cloudwatch_log_group.ecs_logs.name

          awslogs-region = var.aws_region

          awslogs-stream-prefix = "ecs"

        }
      }
    }
  ])


  tags = {

    Name = "area-task-definition"

  }
}

resource "aws_ecs_service" "main" {
  name            = "ecs-service"
  cluster         = aws_ecs_cluster.app.id
  task_definition = aws_ecs_task_definition.task_definition.arn
  desired_count   = 1
  launch_type     = "FARGATE"

  network_configuration {
    subnets          = [aws_subnet.public_a.id, aws_subnet.public_b.id]
    security_groups  = [aws_security_group.ecs_sg.id]
    assign_public_ip = true
  }

  load_balancer {
    target_group_arn = aws_lb_target_group.alb_tg.arn
    container_name   = "area-container"
    container_port   = 5000
  }

  depends_on = [
    aws_lb_listener.http_listener
  ]

  tags = {
    Name = "ecs-service"
  }
}