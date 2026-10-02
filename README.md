# KrishiAI

KrishiAI is a planned voice-first agricultural advisory platform combining crop-image analysis, multilingual voice interaction, contextual agricultural knowledge, weather data, and AI-assisted recommendations.

## Goal

Provide accessible agricultural guidance through a low-friction mobile experience:
Image + Voice -> Validation -> Vision and Speech -> Context -> Retrieval and Reasoning -> Actionable Recommendation -> Voice/Text

## Planned architecture

- Mobile: React Native or Flutter
- API: AWS Lambda + API Gateway
- Images: Amazon S3
- Speech: Amazon Transcribe
- Reasoning and vision: Amazon Bedrock
- Retrieval: OpenSearch Serverless
- Data: DynamoDB
- Speech synthesis: Amazon Polly

## Repository status

The repository previously contained requirements and system-design documents but no application source code. A dependency-light local API scaffold has now been added.

## Starter API

GET /health
POST /diagnose
POST /voice-query
GET /history/{user_id}
POST /feedback

The scaffold does not claim to perform real crop diagnosis. It establishes stable contracts before AWS services and validated models are connected.

## Run

cd backend
python -m venv .venv
pip install -r requirements.txt
uvicorn app:app --reload

Open http://localhost:8000/docs.

## Priorities

1. Low-end device usability
2. Offline queue and sync
3. Explicit confidence and uncertainty
4. Authoritative agricultural sources
5. Incremental AWS integration
6. Field validation and safety review

See design.md and requirements.md for the existing technical specification.
