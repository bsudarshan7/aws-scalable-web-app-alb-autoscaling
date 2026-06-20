Built a Scalable Web Application on AWS using ALB & Auto Scaling

Completed an end-to-end AWS project demonstrating high availability and automatic scaling for a web application.

 Technologies & Services Used:

* Amazon EC2
* Custom AMI
* Launch Templates
* Auto Scaling Group (ASG)
* Application Load Balancer (ALB)
* Target Groups & Health Checks
* Ubuntu Linux
* Python Flask
* systemd Services

Project Workflow:

1. Developed and deployed a CloudMart e-commerce web application on EC2.
2. Created a custom AMI containing the application and server configuration.
3. Configured a Launch Template for automated instance provisioning.
4. Created a Target Group with health checks using a dedicated `/health` endpoint.
5. Deployed an Internet-facing Application Load Balancer.
6. Configured an Auto Scaling Group with CPU-based scaling policies.
7. Automated application startup using systemd so new instances become healthy automatically.
8. Verified load balancing and automatic instance provisioning.

Key Outcomes:
 High Availability Architecture
 Traffic Distribution using ALB
 Automatic Instance Recovery
 CPU-Based Auto Scaling
 Infrastructure Automation using Launch Templates

Architecture:

Users → Application Load Balancer → Target Group → EC2 Instances
↑
Auto Scaling Group
↑
Launch Template → Custom AMI

This project helped me gain hands-on experience with AWS networking, scaling, Linux administration, health checks, and cloud infrastructure design.

#AWS #CloudComputing #DevOps #EC2 #AutoScaling #LoadBalancer #Linux #Python #Flask #CloudProject #AWSProjects #BTech #LearningInPublic
