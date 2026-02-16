# KrishiAI – System Design Document
## AI for Bharat Hackathon | Technical Architecture

---

## 1. Executive Overview

KrishiAI's technical architecture is purpose-built to deliver real-time, intelligent agricultural advisory at scale while operating within the constraints of rural India's digital infrastructure. The system leverages AWS's serverless ecosystem to create a resilient, cost-effective platform that seamlessly integrates computer vision, natural language processing, and contextual reasoning.

This design prioritizes three core principles:
1. **Accessibility First**: Voice-driven interaction with zero literacy requirements
2. **Rural Resilience**: Offline-capable with intelligent sync mechanisms
3. **Scalable Intelligence**: Serverless architecture that grows with demand

---

## 2. High-Level System Architecture

### 2.1 Architectural Philosophy

KrishiAI follows a **serverless, event-driven architecture** hosted entirely on AWS. This approach eliminates infrastructure management overhead, ensures automatic scaling, and aligns costs directly with usage—critical for a system targeting resource-constrained users.

The architecture is designed around three intelligent layers:
- **Perception Layer**: Captures and processes multimodal inputs (image + voice)
- **Intelligence Layer**: Performs diagnosis, reasoning, and recommendation generation
- **Delivery Layer**: Converts insights into actionable, spoken guidance

### 2.2 System Architecture Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                        FARMER (Mobile App)                       │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐         │
│  │   Camera     │  │  Microphone  │  │   Speaker    │         │
│  └──────┬───────┘  └──────┬───────┘  └──────▲───────┘         │
└─────────┼──────────────────┼──────────────────┼────────────────┘
          │                  │                  │
          │ Image Upload     │ Voice Input      │ Audio Response
          ▼                  ▼                  │
┌─────────────────────────────────────────────────────────────────┐
│                      AWS CLOUD INFRASTRUCTURE                    │
│                                                                   │
│  ┌────────────────────────────────────────────────────────────┐ │
│  │              Amazon API Gateway (REST/WebSocket)           │ │
│  └────────────────────┬───────────────────────────────────────┘ │
│                       │                                           │
│  ┌────────────────────▼───────────────────────────────────────┐ │
│  │                  AWS Lambda (Orchestrator)                 │ │
│  │  • Request routing  • State management  • Error handling  │ │
│  └─┬──────────┬──────────┬──────────┬──────────┬─────────────┘ │
│    │          │          │          │          │                │
│    ▼          ▼          ▼          ▼          ▼                │
│  ┌─────┐  ┌──────┐  ┌────────┐  ┌──────┐  ┌────────┐          │
│  │ S3  │  │Trans-│  │Bedrock │  │Open- │  │ Polly  │          │
│  │Image│  │cribe │  │Vision &│  │Search│  │ TTS    │          │
│  │Store│  │ STT  │  │ Agent  │  │ RAG  │  │        │          │
│  └─────┘  └──────┘  └────────┘  └──────┘  └────────┘          │
│                                                                   │
│  ┌────────────────────────────────────────────────────────────┐ │
│  │              Amazon DynamoDB (User & Session Data)         │ │
│  └────────────────────────────────────────────────────────────┘ │
│                                                                   │
│  ┌────────────────────────────────────────────────────────────┐ │
│  │         Amazon Cognito (Authentication & Identity)         │ │
│  └────────────────────────────────────────────────────────────┘ │
│                                                                   │
│  ┌────────────────────────────────────────────────────────────┐ │
│  │      External: Weather API, Agricultural Knowledge Base    │ │
│  └────────────────────────────────────────────────────────────┘ │
└───────────────────────────────────────────────────────────────────┘
```

---

## 3. Detailed System Flow

### 3.1 End-to-End Interaction Flow

**Step 1: User Input Capture**
- Farmer opens the mobile app and captures an image of the affected crop
- Simultaneously or sequentially, farmer speaks a query in their local language
- App performs client-side validation (image quality check, audio level verification)

**Step 2: Data Transmission**
- Image is compressed and uploaded to Amazon S3 with metadata (timestamp, GPS coordinates, user ID)
- Audio is streamed to Amazon Transcribe for real-time speech-to-text conversion
- API Gateway receives the request and triggers the orchestration Lambda

**Step 3: Intelligent Processing**
- **Vision Analysis**: Amazon Bedrock's vision models analyze the crop image to detect:
  - Disease symptoms (leaf spots, discoloration, wilting)
  - Nutrient deficiency indicators (chlorosis, necrosis patterns)
  - Pest damage signatures
  - Confidence scores for each detection

- **Voice Understanding**: Amazon Transcribe converts speech to text, handling:
  - Regional accents and dialects
  - Code-mixing (Hindi-English, Tamil-English)
  - Agricultural terminology in local languages

- **Contextual Enrichment**: System retrieves:
  - Real-time weather data (temperature, humidity, rainfall forecast)
  - Crop growth stage from user profile
  - Historical query patterns
  - Regional disease prevalence data

**Step 4: Reasoning and Recommendation**
- **Amazon Bedrock Agent** orchestrates multi-step reasoning:
  1. Correlates visual findings with voice query
  2. Queries Amazon OpenSearch for relevant agricultural knowledge (RAG)
  3. Evaluates treatment options based on context (weather, crop stage, organic vs. chemical preference)
  4. Generates prioritized recommendations with dosage, timing, and cost estimates

- **Knowledge Retrieval (RAG)**: OpenSearch Serverless indexes:
  - Government agricultural extension documents
  - Peer-reviewed research on crop diseases
  - Regional best practices
  - Product catalogs with application guidelines

**Step 5: Response Generation**
- Bedrock Agent formulates a natural language response in the farmer's language
- Response includes:
  - Problem diagnosis with confidence level
  - Recommended action with specific products
  - Application instructions (dosage, method, timing)
  - Weather-based timing advice
  - Expected outcomes and follow-up timeline

**Step 6: Speech Synthesis and Delivery**
- Amazon Polly converts text response to natural-sounding speech
- Uses neural TTS voices optimized for Indian languages
- Adjusts speech rate for clarity (slightly slower than conversational pace)
- Audio is streamed back to the mobile app

**Step 7: User Confirmation and Logging**
- Farmer hears the spoken advice
- Can ask follow-up questions (conversational continuity maintained)
- Interaction is logged in DynamoDB for personalization and analytics

---

## 4. Core Components Deep Dive

### 4.1 Frontend: Mobile Application

**Technology Stack**:
- **Framework**: React Native (cross-platform iOS/Android support)
- **Alternative**: Flutter (for better performance on low-end devices)
- **State Management**: Redux or Context API for offline-first architecture
- **Local Storage**: SQLite for caching responses and queued requests

**Key Features**:
- **Voice-First UI**: Large, touch-friendly buttons with audio labels
- **Camera Integration**: Native camera API with auto-focus and exposure adjustment
- **Offline Queue**: Stores images and audio locally when network is unavailable
- **Sync Manager**: Automatically uploads queued data when connectivity is restored
- **Language Selector**: One-time language preference setting (persisted locally)
- **Audio Feedback**: Haptic and audio cues for all interactions

**Design Principles**:
- Minimal text, maximum iconography
- High contrast colors for outdoor visibility
- Large touch targets (minimum 48x48dp)
- Progressive disclosure (advanced features hidden by default)

### 4.2 AI & Intelligence Layer

#### 4.2.1 Amazon Bedrock (Foundation Models)

**Vision Models**:
- **Model**: Amazon Bedrock's Claude 3 Sonnet or Anthropic Vision API
- **Capabilities**:
  - Multi-class disease classification
  - Nutrient deficiency detection
  - Pest damage assessment
  - Confidence scoring for each prediction

**Conversational AI**:
- **Model**: Amazon Bedrock Agents with Claude 3 Haiku (for speed) or Sonnet (for accuracy)
- **Capabilities**:
  - Multi-turn conversation management
  - Context retention across queries
  - Intent recognition (diagnosis request, follow-up question, clarification)
  - Multilingual understanding (8+ Indian languages)

**Agent Orchestration**:
- **Amazon Bedrock Agents** coordinate:
  - Vision model invocation
  - Knowledge base queries (RAG)
  - Weather API calls
  - User profile retrieval
  - Response generation

#### 4.2.2 Amazon Transcribe (Speech-to-Text)

**Configuration**:
- **Languages**: Hindi, Tamil, Telugu, Kannada, Bengali, Marathi, Punjabi, Gujarati
- **Custom Vocabulary**: Agricultural terms, crop names, disease names in regional languages
- **Streaming Mode**: Real-time transcription for low-latency interaction
- **Accent Adaptation**: Custom language models trained on rural speech patterns

#### 4.2.3 Amazon Polly (Text-to-Speech)

**Configuration**:
- **Voices**: Neural TTS voices for supported Indian languages
- **Speech Rate**: 90% of normal speed for clarity
- **SSML Support**: Emphasis on key terms (product names, dosages)
- **Pronunciation Lexicons**: Custom pronunciations for agricultural terminology

#### 4.2.4 Amazon OpenSearch Serverless (RAG Knowledge Base)

**Data Sources**:
- Government agricultural extension bulletins
- ICAR (Indian Council of Agricultural Research) publications
- State agricultural university research papers
- Pesticide product catalogs with usage guidelines
- Organic farming best practices

**Indexing Strategy**:
- **Vector Embeddings**: Amazon Bedrock's Titan Embeddings for semantic search
- **Metadata Filtering**: Crop type, region, season, disease category
- **Relevance Tuning**: Boosting recent, high-authority sources

**Query Processing**:
- Hybrid search (keyword + semantic)
- Context-aware retrieval (considers crop, location, season)
- Multi-document synthesis for comprehensive answers

### 4.3 Backend Services

#### 4.3.1 AWS Lambda (Orchestration)

**Functions**:
1. **API Handler**: Receives requests from API Gateway, validates inputs
2. **Image Processor**: Triggers Bedrock vision analysis, stores results
3. **Voice Processor**: Invokes Transcribe, handles streaming responses
4. **Agent Orchestrator**: Coordinates Bedrock Agent execution
5. **Response Builder**: Formats recommendations, invokes Polly
6. **Sync Handler**: Processes offline-queued requests

**Configuration**:
- **Runtime**: Python 3.11 or Node.js 18
- **Memory**: 1024-2048 MB (depending on function)
- **Timeout**: 30 seconds (API Handler), 5 minutes (Agent Orchestrator)
- **Concurrency**: Reserved capacity for peak hours (morning/evening)

#### 4.3.2 Amazon API Gateway

**Endpoints**:
- `POST /diagnose`: Main diagnosis endpoint (image + voice)
- `POST /voice-query`: Voice-only follow-up questions
- `GET /history`: Retrieve user's query history
- `POST /feedback`: Submit user feedback on recommendations
- `WebSocket /chat`: Real-time conversational interface

**Features**:
- Request validation (schema enforcement)
- Rate limiting (per-user quotas)
- API key authentication (for mobile app)
- CORS configuration for web access
- Request/response logging to CloudWatch

#### 4.3.3 Amazon Cognito (Authentication)

**User Pools**:
- **Sign-up**: Mobile number + OTP verification
- **Sign-in**: OTP-based (no password required)
- **MFA**: Optional SMS-based MFA for sensitive operations
- **User Attributes**: Phone number, preferred language, location, farm profile

**Identity Pools**:
- Federated access to AWS resources (S3 for image upload)
- Temporary credentials with least-privilege permissions

### 4.4 Data Layer

#### 4.4.1 Amazon S3 (Image Storage)

**Bucket Structure**:
```
krishi-ai-images/
├── raw/              # Original uploaded images
│   └── {user_id}/{timestamp}.jpg
├── processed/        # Annotated images with detection overlays
│   └── {user_id}/{timestamp}_annotated.jpg
└── thumbnails/       # Compressed thumbnails for history view
    └── {user_id}/{timestamp}_thumb.jpg
```

**Lifecycle Policies**:
- Raw images: Transition to S3 Glacier after 90 days
- Processed images: Retain for 30 days, then delete
- Thumbnails: Retain for 1 year

**Security**:
- Server-side encryption (SSE-S3)
- Bucket policies restricting access to Lambda and Cognito identities
- Pre-signed URLs for time-limited image access

#### 4.4.2 Amazon DynamoDB (User & Session Data)

**Tables**:

1. **Users Table**
   - Partition Key: `user_id`
   - Attributes: `phone_number`, `language`, `location`, `crops`, `farm_size`, `created_at`

2. **Queries Table**
   - Partition Key: `user_id`
   - Sort Key: `timestamp`
   - Attributes: `image_url`, `voice_query`, `diagnosis`, `recommendations`, `confidence_score`, `feedback`
   - GSI: `timestamp` (for time-based analytics)

3. **Sessions Table**
   - Partition Key: `session_id`
   - Attributes: `user_id`, `conversation_history`, `context`, `last_updated`
   - TTL: 24 hours (auto-delete expired sessions)

**Capacity**:
- On-demand billing for unpredictable traffic
- Point-in-time recovery enabled
- DynamoDB Streams for real-time analytics

#### 4.4.3 External Integrations

**Weather API**:
- **Provider**: OpenWeatherMap or India Meteorological Department (IMD) API
- **Data**: Current conditions, 7-day forecast, precipitation probability
- **Caching**: 1-hour cache in DynamoDB to reduce API calls

**Agricultural Knowledge Base**:
- **Sources**: ICAR, state agricultural universities, government portals
- **Update Frequency**: Weekly batch ingestion into OpenSearch
- **Format**: PDF, HTML, structured JSON

---

## 5. Scalability and Performance

### 5.1 Horizontal Scaling

**Serverless Auto-Scaling**:
- Lambda functions scale automatically to handle concurrent requests
- API Gateway supports unlimited requests per second
- DynamoDB on-demand mode scales read/write capacity automatically
- S3 handles unlimited concurrent uploads

**Load Distribution**:
- CloudFront CDN for static assets (app downloads, cached audio responses)
- Multi-AZ deployment for high availability
- Regional endpoints for low-latency access

### 5.2 Performance Optimization

**Latency Targets**:
- Image upload: < 3 seconds (with compression)
- Voice transcription: < 2 seconds (streaming mode)
- Bedrock vision analysis: < 5 seconds
- Agent reasoning + RAG: < 5 seconds
- Polly TTS: < 2 seconds
- **Total end-to-end**: < 15 seconds (95th percentile)

**Optimization Strategies**:
- **Client-side image compression**: Reduce upload time and S3 costs
- **Parallel processing**: Vision and voice analysis run concurrently
- **Response streaming**: Start Polly TTS while agent is still reasoning
- **Caching**: Frequently asked questions cached in DynamoDB
- **Connection pooling**: Reuse HTTP connections to AWS services

### 5.3 Cost Optimization

**Serverless Economics**:
- No idle infrastructure costs
- Pay only for actual usage (requests, compute time, storage)
- AWS Free Tier covers initial development and testing

**Cost Breakdown (per 1000 queries)**:
- Lambda execution: ₹5-10
- Bedrock API calls: ₹20-30
- Transcribe + Polly: ₹10-15
- S3 storage + transfer: ₹5
- DynamoDB reads/writes: ₹3-5
- **Total**: ₹43-65 per 1000 queries (~₹0.05-0.07 per query)

**Cost Control Measures**:
- Image compression before upload
- Cached responses for common queries
- Lifecycle policies for S3 (archive old images)
- DynamoDB TTL for session cleanup
- Reserved Lambda concurrency for predictable workloads

---

## 6. Reliability and Fault Tolerance

### 6.1 High Availability Design

**Multi-AZ Deployment**:
- Lambda functions deployed across multiple availability zones
- DynamoDB automatically replicates data across 3 AZs
- S3 provides 99.999999999% durability

**Graceful Degradation**:
- If Bedrock vision fails, fall back to voice-only diagnosis
- If Transcribe fails, allow text input as backup
- If weather API is unavailable, provide generic timing advice
- If OpenSearch is down, use cached knowledge base responses

### 6.2 Error Handling and Retry Logic

**Lambda Retry Strategy**:
- Automatic retries for transient failures (3 attempts with exponential backoff)
- Dead Letter Queue (DLQ) for failed requests (manual review)
- Circuit breaker pattern for external API calls

**User-Facing Error Messages**:
- Spoken error messages in user's language
- Clear guidance on next steps (e.g., "Please try again in a few minutes")
- Option to save query for later processing

### 6.3 Monitoring and Observability

**Amazon CloudWatch**:
- Lambda execution metrics (invocations, duration, errors)
- API Gateway request/response logs
- Custom metrics (diagnosis accuracy, user satisfaction)
- Alarms for error rate thresholds

**AWS X-Ray**:
- Distributed tracing for end-to-end request flow
- Performance bottleneck identification
- Service map visualization

**User Analytics**:
- Query success rate
- Average response time
- Language distribution
- Crop and disease prevalence
- User retention and engagement

---

## 7. Security and Compliance

### 7.1 Data Security

**Encryption**:
- **In Transit**: TLS 1.3 for all API communications
- **At Rest**: S3 server-side encryption, DynamoDB encryption
- **Key Management**: AWS KMS for encryption key rotation

**Access Control**:
- IAM roles with least-privilege permissions
- Cognito identity pools for user-specific S3 access
- API Gateway resource policies restricting access

### 7.2 Privacy and Compliance

**Data Minimization**:
- No collection of personally identifiable information beyond phone number
- Images stored without facial recognition or geolocation (unless explicitly consented)
- Voice recordings deleted after transcription (optional retention with consent)

**Regulatory Compliance**:
- **DPDPA 2023**: Clear consent mechanisms, right to deletion, data portability
- **Agricultural Data Privacy**: No sharing of farm data with third parties
- **GDPR-Ready**: For potential international expansion

### 7.3 Abuse Prevention

**Rate Limiting**:
- Per-user query limits (e.g., 50 queries/day)
- IP-based throttling for API Gateway
- CAPTCHA for suspicious activity patterns

**Content Moderation**:
- Image validation (reject non-crop images)
- Voice query filtering (detect spam or abusive language)

---

## 8. Offline and Low-Connectivity Support

### 8.1 Offline-First Architecture

**Client-Side Capabilities**:
- Image capture and storage in local SQLite database
- Voice recording and local storage
- Queue management for pending uploads
- Cached responses for common queries (e.g., "How to apply urea?")

**Sync Strategy**:
- Background sync when Wi-Fi is available (to save mobile data)
- Incremental sync (only new data)
- Conflict resolution (server-side timestamp wins)

### 8.2 Bandwidth Optimization

**Data Compression**:
- Image compression (JPEG quality 70-80%, max 1MB)
- Audio compression (Opus codec, 16 kbps)
- Response caching (avoid re-downloading identical advice)

**Progressive Loading**:
- Essential data first (diagnosis), detailed info later
- Thumbnail images for history view
- On-demand full-resolution image retrieval

---

## 9. Implementation Roadmap

### Phase 1: MVP (Months 1-3)
**Objective**: Validate core functionality with limited scope

**Deliverables**:
- Mobile app (Android) with voice + image capture
- Backend infrastructure (Lambda, API Gateway, S3, DynamoDB)
- Amazon Bedrock integration (vision + conversational AI)
- Support for 2 languages (Hindi, English)
- Support for 3 crops (tomato, rice, wheat)
- 20-30 common diseases/deficiencies

**Success Criteria**:
- 100 pilot users
- 80% diagnosis accuracy (user-reported)
- < 20 second average response time

### Phase 2: Expansion (Months 4-6)
**Objective**: Scale to production-ready system

**Deliverables**:
- iOS app release
- 8 language support (Hindi, Tamil, Telugu, Kannada, Bengali, Marathi, Punjabi, Gujarati)
- 10 crop support (add cotton, sugarcane, potato, onion, pulses)
- 100+ disease/deficiency database
- Weather integration
- Offline mode with sync
- Amazon OpenSearch RAG implementation

**Success Criteria**:
- 10,000 active users
- 85% diagnosis accuracy
- 60% monthly active user rate

### Phase 3: Optimization (Months 7-12)
**Objective**: Refine and optimize for scale

**Deliverables**:
- Personalized recommendations based on user history
- Community features (farmer-to-farmer knowledge sharing)
- Integration with government schemes (PM-KISAN, crop insurance)
- Advanced analytics dashboard for agricultural extension officers
- Model fine-tuning with user feedback

**Success Criteria**:
- 100,000+ users
- 90% diagnosis accuracy
- 10-15% measurable yield improvement

---

## 10. Technology Stack Summary

### Frontend
- **Mobile Framework**: React Native / Flutter
- **State Management**: Redux / Context API
- **Local Storage**: SQLite
- **HTTP Client**: Axios / Fetch API

### Backend
- **Compute**: AWS Lambda (Python 3.11 / Node.js 18)
- **API Layer**: Amazon API Gateway (REST + WebSocket)
- **Authentication**: Amazon Cognito

### AI/ML Services
- **Foundation Models**: Amazon Bedrock (Claude 3 Sonnet/Haiku)
- **Speech-to-Text**: Amazon Transcribe
- **Text-to-Speech**: Amazon Polly
- **Knowledge Base**: Amazon OpenSearch Serverless
- **Embeddings**: Amazon Bedrock Titan Embeddings

### Data Storage
- **Object Storage**: Amazon S3
- **NoSQL Database**: Amazon DynamoDB
- **Caching**: DynamoDB (with TTL)

### Monitoring & Operations
- **Logging**: Amazon CloudWatch Logs
- **Metrics**: Amazon CloudWatch Metrics
- **Tracing**: AWS X-Ray
- **Alerting**: Amazon SNS

### Security
- **Encryption**: AWS KMS
- **Secrets Management**: AWS Secrets Manager
- **Identity**: Amazon Cognito User Pools + Identity Pools

### External Integrations
- **Weather Data**: OpenWeatherMap / IMD API
- **Agricultural Knowledge**: ICAR, state agricultural universities

---

## 11. Risk Mitigation

### Technical Risks

**Risk**: Bedrock API rate limits during peak usage
**Mitigation**: Request quota increase, implement request queuing, use reserved capacity

**Risk**: Poor image quality affecting diagnosis accuracy
**Mitigation**: Client-side quality checks, user guidance (lighting, distance), multi-image support

**Risk**: Transcribe accuracy issues with rural accents
**Mitigation**: Custom language models, vocabulary lists, user feedback loop for corrections

### Operational Risks

**Risk**: High AWS costs at scale
**Mitigation**: Cost monitoring, budget alerts, optimization strategies (caching, compression)

**Risk**: User adoption challenges (trust, digital literacy)
**Mitigation**: Partnership with agricultural extension workers, NGOs for training and onboarding

**Risk**: Incorrect recommendations leading to crop damage
**Mitigation**: Confidence thresholds, disclaimer messaging, human-in-the-loop for low-confidence cases

---

## 12. Future Enhancements

### Phase 4: Advanced Intelligence (Year 2)
- **Predictive Analytics**: Forecast disease outbreaks based on weather patterns
- **Soil Health Integration**: Connect with soil testing labs for precision nutrient management
- **Market Intelligence**: Optimal harvest timing based on price forecasts
- **Livestock Health**: Expand to animal husbandry advisory

### Phase 5: Ecosystem Integration (Year 3)
- **Supply Chain**: Direct farmer-to-buyer marketplace
- **Financial Services**: Credit scoring based on farm health data
- **Insurance**: Automated crop insurance claims using image evidence
- **Government Schemes**: Seamless integration with PM-KISAN, e-NAM

---

## 13. Conclusion

KrishiAI's system design represents a thoughtful balance between technical sophistication and operational simplicity. By leveraging AWS's serverless ecosystem, we create a platform that is:

- **Scalable**: Grows seamlessly from hundreds to millions of users
- **Resilient**: Operates reliably even in low-connectivity environments
- **Cost-Effective**: Pay-per-use model ensures sustainability
- **Accessible**: Voice-first design removes literacy barriers
- **Intelligent**: Multi-modal AI provides expert-level guidance

This architecture is not just a technical blueprint—it's a pathway to democratizing agricultural intelligence for India's farming community. By meeting farmers where they are, speaking their language, and respecting their constraints, KrishiAI demonstrates how AI can be a force for inclusive growth and rural prosperity.

The design is production-ready, hackathon-validated, and built for real-world impact.