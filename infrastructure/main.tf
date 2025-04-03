terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.0"
    }
  }
}

provider "aws" {
  region = var.aws_region
}

# VPC Configuration
module "vpc" {
  source = "./modules/vpc"

  vpc_cidr             = var.vpc_cidr
  availability_zones   = var.availability_zones
  environment          = var.environment
  project_name         = var.project_name
}

# ECS Cluster
module "ecs" {
  source = "./modules/ecs"

  cluster_name    = "${var.project_name}-cluster"
  vpc_id          = module.vpc.vpc_id
  private_subnets = module.vpc.private_subnet_ids
  environment     = var.environment
  project_name    = var.project_name
}

# RDS Database
module "rds" {
  source = "./modules/rds"

  vpc_id          = module.vpc.vpc_id
  private_subnets = module.vpc.private_subnet_ids
  environment     = var.environment
  project_name    = var.project_name
}

# CloudWatch Logs
module "monitoring" {
  source = "./modules/monitoring"

  environment  = var.environment
  project_name = var.project_name
} 