from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from llm_engine import generate_iac

app = FastAPI(title="Aetheria AI Orchestrator")

class DeploymentRequest(BaseModel):
    prompt: str
    environment: str # dev, staging, prod

@app.post("/generate-infra")
async def create_infrastructure(request: DeploymentRequest):
    try:
        # Calls the LLM to translate NL to Terraform
        terraform_code = generate_iac(request.prompt)
        return {"status": "success", "code": terraform_code}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)