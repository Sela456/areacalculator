# create RDS database
resource "aws_db_instance" "area_database" {
  instance_class          = "db.t3.micro"
  identifier              = "area-app-db"
  engine                  = "postgres"
  engine_version          = "16"
  allocated_storage       = 20
  publicly_accessible     = false
  db_name                 = "areaapp"
  username                = var.db_username
  password                = var.db_password
  backup_retention_period = 0
  backup_window           = "03:00-04:00"
  skip_final_snapshot     = false
  db_subnet_group_name    = aws_db_subnet_group.database.name
  vpc_security_group_ids  = [aws_security_group.database.id]
  tags = {
    Name = "area-database"
  }
}


# create subnet group
resource "aws_db_subnet_group" "database" {
  name = "area-db-subnet-group"
  subnet_ids = [
    aws_subnet.private_a.id,
    aws_subnet.private_b.id
  ]
}

