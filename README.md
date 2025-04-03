# DevSecOps Demo Application

This project demonstrates a complete DevSecOps workflow with AWS, including:

- Infrastructure as Code (Terraform)
- CI/CD Pipeline (GitHub Actions)
- Security Scanning
- Container Security
- Monitoring and Logging
- AWS Best Practices

## Architecture

The application consists of:
- Python Flask Web Application
- AWS Infrastructure (ECS, RDS, CloudWatch)
- Security Tools Integration
- Automated Deployment Pipeline

## Prerequisites

- AWS Account
- Terraform
- Docker
- GitHub Account
- AWS CLI configured

## Project Structure

```
.
├── app/                    # Application code
├── infrastructure/         # Terraform IaC
├── .github/               # GitHub Actions workflows
├── security/              # Security configurations
└── monitoring/            # Monitoring setup
```

## Getting Started

1. Clone the repository
2. Configure AWS credentials
3. Initialize Terraform
4. Deploy the infrastructure
5. Run the application

## Security Features

- Container scanning
- Dependency scanning
- Infrastructure compliance checks
- Secret management
- AWS security best practices

## Monitoring

- CloudWatch metrics
- Application logs
- Performance monitoring
- Security alerts

## License

MIT 