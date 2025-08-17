variable "aws_region" {
  description = "AWS region to create resources in"
  type        = string
  default     = "us-east-1"
}

variable "cluster_name" {
  description = "Name of the EKS cluster"
  type        = string
  default     = "my-eks-cluster"
}

variable "my_iam_user_name" {
  description = "The IAM user to map as cluster admin (system:masters)"
  type        = string
  default     = "terraform-eks-admin"  # <-- updated to your new IAM user
}
