# Serverless WhatsApp Customer Intake Pipeline
> **A scalable, 24/7 automated messaging system built on AWS Lambda and Twilio.**



## 🏗 Architectural Overview
This passion project implements a serverless "push" architecture designed to automate user engagement without the overhead of traditional server management. By leveraging event-driven compute, the system handles incoming WhatsApp messages in real-time with high efficiency and near-zero cost.

### The Workflow:
1. **Trigger:** A user sends a WhatsApp message via the Twilio API.
2. **Ingress:** **AWS API Gateway** receives the webhook POST request and validates the payload.
3. **Compute:** **AWS Lambda** is triggered, executing a Python-based logic engine to parse the message and determine the intent.
4. **Integration:** Data is processed and stored in a structured database/CRM format for further analysis.
5. **Egress:** An automated, context-aware response is sent back through the Twilio Sandbox.

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
By choosing **AWS Lambda** over a dedicated EC2 instance, the infrastructure cost is strictly proportional to traffic. 
* **Result:** The system incurs $0.00 cost when not in use, while maintaining the ability to scale instantly for burst traffic.

### 2. Performance Engineering
The logic was optimized to mitigate "Cold Starts." By maintaining a lean deployment package and minimizing external library dependencies, the end-to-end response latency is kept under **~200ms**.

### 3. Security & Best Practices
Rather than using local environment variables, this project utilizes **AWS Secrets Manager** to handle sensitive credentials.
* **Implementation:** The Lambda function fetches the Twilio Auth Token and WhatsApp SID at runtime via an IAM-restricted execution role, ensuring no sensitive data is exposed in the repository.

---

## 🚀 Future Roadmap
- [ ] **Stateful Conversations:** Implement AWS DynamoDB to track user session states for multi-step forms.
- [ ] **Asynchronous Processing:** Introduce AWS SQS (Simple Queue Service) to decouple message reception from database writes.
- [ ] **Natural Language Understanding:** Integrate AWS Lex for AI-driven intent classification.

---

## 📜 How to Inspect
The core logic resides in `lambda_function.py`. 

> **Security Note:** API endpoints and specific secret identifiers are managed within the AWS Console and are not exposed in this public repository to maintain security best practices.
