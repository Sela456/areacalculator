#create autoscaling 
resource "aws_appautoscaling_target" "ecs_target" {
    service_namespace            = "ecs"
    min_capacity                 = 1
    max_capacity                 = 4
    resource_id                  = "service/${aws_ecs_cluster.app.name}/${aws_ecs_service.main.name}"
    scalable_dimension           = "ecs:service:DesiredCount"

}

resource "aws_appautoscaling_policy" "cpu_policy" {
    name                        = "cpu-scaling-policy"
    policy_type                 = "TargetTrackingScaling"


    service_namespace           = aws_appautoscaling_target.ecs_target.service_namespace
    resource_id                 = aws_appautoscaling_target.ecs_target.resource_id
    scalable_dimension          = aws_appautoscaling_target.ecs_target.scalable_dimension

    target_tracking_scaling_policy_configuration {
        target_value    = 70.0

    predefined_metric_specification {
        predefined_metric_type  = "EcsServiceAverageCPUUtiliztion"
    }
     }
}