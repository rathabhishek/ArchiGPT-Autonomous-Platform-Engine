# ArchiGPT-Autonomous-Platform-Engine
An autonomous Platform Engineering portal designed to reduce DevOps friction. Leveraging LLMs to bridge the gap between Natural Language and IaC (Terraform/CloudFormation). Aetheria is an AI-augmented Internal Developer Platform (IDP) that automates infrastructure provisioning through Natural Language Processing.

### Key Features
* **NL to IaC:** Uses Claude 3 (via Bedrock) to generate production-ready Terraform.
* **Self-Service:** Removes the "Ops bottleneck" by allowing devs to provision their own needs.
* **Security Guardrails:** Pre-defined Terraform modules ensure compliance.

## 🛠️ Setup
1. **Backend:** * `cd backend && pip install -r requirements.txt`
   * Set AWS credentials.
   * `python main.py`
2. **Frontend:**
   * `cd frontend && npm install && npm start`

## 🏗️ Architecture
1. Developer enters request in UI.
2. FastAPI Orchestrator sends request to LLM with context.
3. LLM returns Terraform code.
4. Portal triggers GitHub Action with the code for validation/deployment.
