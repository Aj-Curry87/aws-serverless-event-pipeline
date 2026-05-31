variable "aws_region" {
  description = "AWS Region for the lab"
  type        = string
  default     = "us-east-1"
}

variable "project_name" {
  description = "Project name prefix"
  type        = string
  default     = "serverless-event-pipeline"
}
