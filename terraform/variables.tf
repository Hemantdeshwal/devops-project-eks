variable "aws_region" {
  description = "AWS region to deploy EKS"
  type        = string
  default     = "ap-south-1"
}

variable "cluster_name" {
  description = "EKS cluster name"
  type        = string
  default     = "devops-creative-eks"
}
