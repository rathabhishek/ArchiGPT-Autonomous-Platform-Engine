import boto3
import json

def generate_iac(user_prompt: str):
    """
    Uses AWS Bedrock (Claude 3) to generate Terraform HCL.
    """
    client = boto3.client("bedrock-runtime", region_name="us-east-1")
    
    system_prompt = "You are a senior Platform Engineer. Convert user requests into valid Terraform code. Only output the code, no prose."
    
    body = json.dumps({
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 1000,
        "messages": [
            {"role": "user", "content": f"{system_prompt}\n\nRequest: {user_prompt}"}
        ]
    })

    response = client.invoke_model(body=body, modelId="anthropic.claude-3-sonnet-20240229-v1:0")
    response_body = json.loads(response.get("body").read())
    
    return response_body['content'][0]['text']