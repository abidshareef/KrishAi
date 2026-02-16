# KrishiAI – Requirements Document
## AI for Bharat Hackathon 

---

## 1. Executive Summary

KrishiAI is a voice-first, vision-driven agricultural intelligence system designed to democratize expert crop advisory for India's 86 million small and marginal farmers. By leveraging Amazon Bedrock's foundation models, computer vision, and multilingual conversational AI, KrishiAI transforms how farmers diagnose and respond to crop health issues—directly at the field level, in their native language, without requiring literacy or technical expertise.

This system addresses a critical gap in India's agricultural value chain: the inability of existing digital platforms to reach farmers who need them most. KrishiAI is built ground-up for rural realities—low connectivity, diverse dialects, and varying levels of digital familiarity—making advanced AI accessible where it matters most.

---

## 2. Problem Statement and Context

### 2.1 The Agricultural Challenge

Agriculture remains the backbone of India's economy, employing nearly 42% of the workforce and contributing significantly to GDP. However, small and marginal landholders—who constitute over 86% of all farmers—face persistent challenges that directly impact productivity and livelihood:

- **Late Detection of Crop Issues**: Diseases, nutrient deficiencies, and pest infestations often go unnoticed until damage becomes irreversible, leading to yield losses of 15-25% annually.
  
- **Limited Access to Expert Guidance**: Agricultural extension services are overstretched, with ratios often exceeding 1:1000 (extension worker to farmer). Timely, personalized advice is rarely available when farmers need it most.

- **Language and Literacy Barriers**: Existing digital advisory platforms are predominantly text-heavy and English-centric. With rural literacy rates varying significantly and digital literacy even lower, these platforms fail to serve their intended audience.

- **Information Asymmetry**: Farmers frequently rely on guesswork or outdated practices, leading to excessive pesticide use, increased input costs, and environmental degradation.

### 2.2 Why Current Solutions Fall Short

While several agri-tech initiatives exist, they suffer from fundamental design flaws:

- **Assumption of Literacy**: Most platforms require reading and typing, immediately excluding millions of potential users.
  
- **Urban-Centric Design**: Interfaces optimized for high-bandwidth, smartphone-savvy users don't translate to rural contexts with intermittent 2G/3G connectivity.

- **Generic Advice**: One-size-fits-all recommendations ignore local conditions like weather patterns, soil types, and crop growth stages.

- **Delayed Response**: Call centers and helplines introduce latency that can be critical during time-sensitive agricultural decisions.

### 2.3 The Opportunity

The convergence of affordable smartphones, improving rural connectivity, and advances in AI presents a unique opportunity to leapfrog traditional extension models. By designing for voice-first interaction and leveraging AWS's AI services, we can deliver expert-level agricultural intelligence at scale—without requiring farmers to change their behavior or learn new skills.

---

## 3. Proposed Solution: KrishiAI

### 3.1 Vision Statement

To empower every farmer in India with instant, personalized, and actionable crop health intelligence—delivered in their language, at their convenience, directly in their fields.

### 3.2 Core Capabilities

KrishiAI is a multimodal AI system that enables farmers to:

1. **Visual Diagnosis**: Capture images of affected crops using a smartphone camera. The system analyzes visual symptoms to identify diseases, nutrient deficiencies, or pest damage.

2. **Voice Interaction**: Ask questions naturally in their local language (Hindi, Tamil, Telugu, Kannada, Bengali, Marathi, Punjabi, and more). No typing, no reading—just conversation.

3. **Contextual Intelligence**: Receive recommendations that account for real-time weather conditions, crop growth stage, regional pest patterns, and historical farm data.

4. **Spoken Guidance**: Get step-by-step action plans delivered as clear, spoken instructions—including treatment options, application timing, and preventive measures.

5. **Offline Resilience**: Core functionality works with intermittent connectivity, syncing data when network becomes available.

### 3.3 How It Works (User Journey)

**Scenario**: A farmer notices yellowing leaves on their tomato crop.

1. **Capture**: Opens KrishiAI app, taps the camera button, and takes a photo of the affected plant.

2. **Ask**: Speaks into the phone: "मेरे टमाटर के पत्ते पीले क्यों हो रहे हैं?" (Why are my tomato leaves turning yellow?)

3. **Analyze**: The system processes the image using computer vision models, cross-references with the voice query, and considers current weather data and crop stage.

4. **Respond**: The farmer hears a response in Hindi: "आपके टमाटर में नाइट्रोजन की कमी दिख रही है। मौसम अगले 2 दिन साफ रहेगा, इसलिए आप यूरिया का छिड़काव कर सकते हैं..." (Your tomato plants show nitrogen deficiency. Weather will be clear for the next 2 days, so you can apply urea spray...)

5. **Act**: The farmer receives specific dosage recommendations, application methods, and follow-up timing—all without reading a single word.

---

## 4. Detailed Functional Requirements

### 4.1 Image-Based Crop Health Detection

**FR-1.1**: The system shall accept crop images captured via smartphone camera in varying lighting conditions (direct sunlight, shade, cloudy weather).

**FR-1.2**: The system shall detect and classify:
- Common crop diseases (bacterial, fungal, viral)
- Nutrient deficiencies (N, P, K, micronutrients)
- Pest damage patterns
- Growth abnormalities

**FR-1.3**: The system shall support major crops including rice, wheat, cotton, sugarcane, tomato, potato, onion, and pulses.

**FR-1.4**: Detection accuracy shall exceed 85% for trained disease categories, with confidence scores provided for each diagnosis.

**FR-1.5**: The system shall handle image quality variations including blur, partial occlusion, and background noise.

### 4.2 Multilingual Voice Interaction

**FR-2.1**: The system shall support voice input in at least 8 Indian languages: Hindi, Tamil, Telugu, Kannada, Bengali, Marathi, Punjabi, and Gujarati.

**FR-2.2**: Voice transcription shall handle rural accents, dialects, and code-mixing (e.g., Hindi-English).

**FR-2.3**: The system shall support conversational follow-ups, allowing farmers to ask clarifying questions without restarting the interaction.

**FR-2.4**: Voice output shall use natural, region-appropriate speech synthesis with adjustable speed and clarity.

**FR-2.5**: The system shall provide audio feedback for all user actions (button presses, image capture, processing status).

### 4.3 Context-Aware Recommendations

**FR-3.1**: The system shall integrate real-time weather data (temperature, humidity, rainfall forecast) to time-sensitive recommendations.

**FR-3.2**: Recommendations shall account for crop growth stage (seedling, vegetative, flowering, fruiting) when suggesting interventions.

**FR-3.3**: The system shall warn against pesticide application during unfavorable weather (rain expected, high winds, extreme heat).

**FR-3.4**: The system shall provide location-specific advice based on regional pest patterns and disease prevalence.

**FR-3.5**: The system shall maintain a knowledge base of organic and chemical treatment options, allowing farmers to choose based on their farming practices.

### 4.4 Actionable Guidance Delivery

**FR-4.1**: All recommendations shall include:
- Clear problem identification
- Recommended treatment or intervention
- Specific product names and dosages
- Application method and timing
- Expected results and follow-up timeline
- Preventive measures for future

**FR-4.2**: The system shall prioritize recommendations by urgency (immediate action required vs. monitoring suggested).

**FR-4.3**: The system shall provide cost estimates for recommended treatments when possible.

**FR-4.4**: The system shall offer alternative solutions (e.g., organic vs. chemical) when multiple options exist.

### 4.5 Offline and Low-Connectivity Support

**FR-5.1**: The system shall allow image capture and voice recording in offline mode.

**FR-5.2**: Captured data shall be queued and automatically synced when connectivity is restored.

**FR-5.3**: The system shall provide cached responses for common queries to enable basic functionality offline.

**FR-5.4**: The system shall optimize data transfer to minimize bandwidth usage (image compression, delta syncing).

**FR-5.5**: The system shall clearly indicate online/offline status and expected sync timing to users.

### 4.6 User Management and Personalization

**FR-6.1**: The system shall support simple onboarding using mobile number verification (OTP-based).

**FR-6.2**: The system shall optionally collect farm profile information (location, primary crops, farm size) to improve recommendations.

**FR-6.3**: The system shall maintain query history to enable personalized follow-ups and seasonal reminders.

**FR-6.4**: The system shall not require complex registration or personal documentation.

---

## 5. Non-Functional Requirements

### 5.1 Performance

**NFR-1.1**: Image analysis and diagnosis shall complete within 10 seconds under normal network conditions.

**NFR-1.2**: Voice transcription latency shall not exceed 2 seconds for typical queries (10-15 words).

**NFR-1.3**: The system shall support concurrent usage by 100,000+ farmers during peak hours (morning and evening).

**NFR-1.4**: API response times shall remain under 500ms for 95% of requests.

### 5.2 Scalability

**NFR-2.1**: The architecture shall scale horizontally to support millions of users without performance degradation.

**NFR-2.2**: The system shall leverage serverless AWS services to automatically handle traffic spikes.

**NFR-2.3**: Data storage shall accommodate growth of 10TB+ annually for image and interaction logs.

### 5.3 Reliability and Availability

**NFR-3.1**: The system shall maintain 99.5% uptime during agricultural seasons (kharif and rabi).

**NFR-3.2**: Critical services shall have automated failover and redundancy across AWS availability zones.

**NFR-3.3**: The system shall gracefully degrade functionality during partial service outages (e.g., voice works even if vision fails).

### 5.4 Security and Privacy

**NFR-4.1**: All data transmission shall be encrypted using TLS 1.3.

**NFR-4.2**: User images and voice recordings shall be stored securely in Amazon S3 with encryption at rest.

**NFR-4.3**: The system shall comply with India's data protection regulations and agricultural data privacy norms.

**NFR-4.4**: No personally identifiable information (PII) shall be shared with third parties without explicit consent.

**NFR-4.5**: Authentication shall use AWS Cognito with multi-factor authentication support.

### 5.5 Usability and Accessibility

**NFR-5.1**: The mobile app shall be operable by users with zero prior smartphone experience after a 5-minute demonstration.

**NFR-5.2**: All critical functions shall be accessible via voice commands alone (no mandatory touch interaction).

**NFR-5.3**: The interface shall support users with visual impairments through audio-first design.

**NFR-5.4**: The app size shall remain under 50MB to accommodate low-end devices with limited storage.

### 5.6 Cost Efficiency

**NFR-6.1**: The system shall operate on a pay-per-use model with costs proportional to actual usage.

**NFR-6.2**: Per-query cost shall remain under ₹2 to enable sustainable free or subsidized access for farmers.

**NFR-6.3**: The architecture shall minimize idle resource costs through serverless design.

---

## 6. Target Users and Personas

### 6.1 Primary User: Small-Scale Farmer

**Profile**: Ramesh, 45, owns 2 acres in rural Maharashtra
- Grows cotton and soybean
- Completed primary education (5th standard)
- Owns a basic Android smartphone (₹6000 range)
- Comfortable speaking Marathi, limited Hindi
- Has used WhatsApp but struggles with text-heavy apps
- Relies on local pesticide dealer for crop advice

**Needs**: Quick diagnosis when he spots unusual symptoms, advice he can trust without traveling to the nearest town, guidance in Marathi that he can act on immediately.

### 6.2 Secondary User: Marginal Farmer

**Profile**: Lakshmi, 38, cultivates 0.5 acres in Tamil Nadu
- Grows vegetables for local market
- No formal education, cannot read or write
- Shares a smartphone with family
- Speaks only Tamil
- Depends on neighbors and memory for farming decisions

**Needs**: Completely voice-based interaction, simple yes/no confirmations, spoken step-by-step instructions she can follow without assistance.

### 6.3 Tertiary User: Agricultural Worker

**Profile**: Suresh, 28, works on multiple farms in Punjab
- Educated up to 10th standard
- Tech-savvy, uses multiple apps
- Speaks Punjabi and Hindi
- Advises farmers he works for

**Needs**: Fast, accurate diagnosis to help employers, ability to save and share recommendations, access to detailed information when needed.

---

## 7. System Constraints and Assumptions

### 7.1 Technical Constraints

- **Connectivity**: Assume 2G/3G networks with intermittent availability (50-60% uptime in remote areas)
- **Device Capability**: Target devices with 2GB RAM, Android 8.0+, basic camera (5MP+)
- **Battery**: Optimize for power efficiency as farmers may have limited charging access
- **Storage**: Minimize local storage requirements (under 200MB for app + cache)

### 7.2 Operational Constraints

- **Language Coverage**: Initial launch limited to 8 languages, expandable based on demand
- **Crop Coverage**: Focus on top 15 crops by area coverage in India (covering 80%+ of cultivated land)
- **Disease Database**: Start with 50-100 most common diseases/deficiencies per crop, expanding iteratively

### 7.3 Assumptions

- Farmers have access to smartphones (owned or shared) with camera and microphone
- Basic mobile network coverage exists, even if intermittent
- Farmers are willing to try voice-based apps if demonstrated effectively
- Agricultural extension workers or NGOs can assist with initial onboarding and training

---

## 8. Success Metrics and KPIs

### 8.1 Adoption Metrics

- **User Registrations**: Target 10,000 farmers in pilot phase (6 months)
- **Active Users**: 60% monthly active user rate
- **Retention**: 40% users return within 7 days of first use
- **Geographic Spread**: Coverage across 5+ states in first year

### 8.2 Engagement Metrics

- **Queries per User**: Average 3-5 queries per month during growing season
- **Voice vs. Text**: 80%+ interactions via voice (validating voice-first design)
- **Session Duration**: Average 2-3 minutes per interaction (indicating efficiency)
- **Follow-up Rate**: 30% users ask follow-up questions (indicating engagement)

### 8.3 Impact Metrics

- **Early Detection**: 50% of issues identified before visible damage exceeds 10% of crop
- **Diagnosis Accuracy**: 85%+ user-reported satisfaction with diagnosis correctness
- **Action Taken**: 70% of users report taking recommended action
- **Yield Impact**: 10-15% reduction in crop loss among active users (measured via surveys)
- **Cost Savings**: ₹2000-5000 per acre per season through optimized input use

### 8.4 Technical Metrics

- **Response Time**: 95% of queries resolved in under 15 seconds
- **System Uptime**: 99.5% availability during peak agricultural seasons
- **Error Rate**: Less than 2% failed transactions
- **Offline Success**: 90% of offline-captured queries successfully synced

---

## 9. Regulatory and Compliance Considerations

### 9.1 Data Protection

- Compliance with India's Digital Personal Data Protection Act (DPDPA) 2023
- Clear consent mechanisms for data collection and usage
- Right to data deletion and portability

### 9.2 Agricultural Regulations

- Recommendations shall align with government-approved pesticide usage guidelines
- Dosage recommendations shall not exceed statutory limits
- Organic farming guidelines shall be respected when applicable

### 9.3 Accessibility Standards

- Design shall follow WCAG 2.1 guidelines for accessibility
- Voice interface shall accommodate users with disabilities

---

## 10. Future Scope and Extensibility

### 10.1 Phase 2 Enhancements

- Integration with soil testing data for precision nutrient management
- Predictive alerts based on weather forecasts and historical disease patterns
- Community features allowing farmers to share observations and solutions
- Integration with government schemes (PM-KISAN, crop insurance) for seamless benefit access

### 10.2 Phase 3 Vision

- Expansion to livestock health monitoring
- Market price intelligence and optimal harvest timing recommendations
- Financial inclusion features (credit scoring based on farm health data)
- Supply chain integration connecting farmers directly with buyers

---

## 11. Conclusion

KrishiAI represents a fundamental rethinking of how agricultural technology can serve India's farming community. By prioritizing voice over text, context over generic advice, and accessibility over feature complexity, we aim to bridge the digital divide that has kept millions of farmers from benefiting from AI advances.

This requirements document establishes the foundation for a system that is technically sophisticated yet operationally simple—a system that meets farmers where they are, speaks their language, and empowers them with knowledge that was previously accessible only to large commercial farms.

The success of KrishiAI will be measured not in technology metrics alone, but in the tangible improvement it brings to farmer livelihoods, food security, and rural prosperity across India.
