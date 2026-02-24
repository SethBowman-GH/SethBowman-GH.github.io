# Serverless WhatsApp Customer Intake Pipeline
> **A scalable, 24/7 automated lead generation system built on AWS Lambda and Twilio.**



## 🏗 Architectural Overview
This project implements a serverless "push" architecture. Instead of maintaining a persistent server (EC2) and paying for idle time, this system leverages event-driven compute to process incoming WhatsApp messages in real-time.

### The Workflow:
1. **Trigger:** A customer sends a WhatsApp message via the Twilio API.
2. **Ingress:** **AWS API Gateway** receives the webhook POST request and validates the payload.
3. **Compute:** **AWS Lambda** is triggered. It executes a Python-based logic engine to parse the message and determine the intent.
4. **Integration:** Data is pushed to the Nexum Group intake database/CRM.
5. **Egress:** An automated response is sent back through the Twilio Sandbox.

---

## 🛠 Tech Stack
* **Language:** Python 3.9
* **Compute:** AWS Lambda (Serverless)
* **API Management:** AWS API Gateway (REST API)
* **Communication:** Twilio Messaging API (WhatsApp Business)
* **Security:** AWS Secrets Manager (for API Key rotation)
* **Logging:** AWS CloudWatch (for error tracking and latency monitoring)

---

## ⚡ Engineering Key Decisions

### 1. Cost Optimization: Zero-Idle Compute
By choosing **AWS Lambda** over a dedicated server, the infrastructure cost is strictly proportional to traffic. 
* **Result:** The system costs $0.00/month when not in use, with the ability to handle bursts of hundreds of concurrent users instantly.

### 2. Latency Reduction
The logic was optimized to avoid "Cold Starts." By keeping the deployment package under 10MB and minimizing external library dependencies, the end-to-end response latency is kept under **~200ms**.

### 3. Production-Grade Security
Unlike "tutorial" projects that use `.env` files, this architecture uses **AWS Secrets Manager**. 
* **Implementation:** The Lambda function fetches the Twilio Auth Token and WhatsApp SID at runtime via an IAM-restricted execution role. This prevents credential exposure in the source code.

---

## 🚀 Future Roadmap
- [ ] **Stateful Conversations:** Implement AWS DynamoDB to track user session states (multi-step intake forms).
- [ ] **Asynchronous Processing:** Introduce AWS SQS (Simple Queue Service) to decouple message reception from database writes.
- [ ] **Natural Language Understanding:** Integrate AWS Lex for AI-driven intent classification.

---

## 📜 How to Inspect
The core logic resides in `lambda_function.py`. 

> **Security Note:** The API endpoints and Secrets are managed via the AWS Management Console and are not exposed in this repository for security reasons.
