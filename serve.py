"""
Playbook AI - API Server
Serves the complete sales intelligence workflow as a REST API endpoint.

Usage:
    python serve.py

API Endpoints:
    POST /workflows/playbook-ai-sales-intelligence-pipeline/runs
    GET  /docs (OpenAPI documentation)
    GET  /health (Health check)
    GET  /config (AgentOS configuration)

Example API Call:
    curl -X POST 'http://localhost:8080/workflows/playbook-ai---sales-intelligence-pipeline/runs' \
      --data-urlencode 'message={"vendor_domain":"gong.io","prospect_domain":"sendoso.com"}' \
      --data 'stream=false'

    Note: The workflow ID uses three hyphens (---) and the API uses form-urlencoded data.

Control Plane UI:
    http://localhost:8080
"""

from agno.os import AgentOS
from main import workflow
import os

# Initialize AgentOS with the complete sales intelligence workflow
agent_os = AgentOS(
    id="playbook-ai-sales-intelligence",
    description="Complete sales intelligence pipeline API - End-to-end vendor analysis, prospect research, and sales playbook generation",
    workflows=[workflow],
)

# Get the FastAPI app
app = agent_os.get_app()

# Add custom health check endpoint
@app.get("/health")
async def health_check():
    """Health check endpoint for monitoring"""
    return {
        "status": "healthy",
        "service": "playbook-ai-api",
        "version": "1.0.0"
    }

if __name__ == "__main__":
    import os

    PORT = int(os.environ.get("PORT", 8080))

    print("\n" + "=" * 80)
    print("PLAYBOOK AI - SALES INTELLIGENCE API SERVER")
    print("=" * 80)
    print("\nStarting AgentOS API Server...")
    print(f"\nAPI running on port {PORT}")
    print("\n" + "=" * 80 + "\n")

    agent_os.serve(
        app="serve:app",
        reload=False,
        port=PORT
    )

