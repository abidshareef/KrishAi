# KrishiAI – Requirements Document

## Problem Statement
Small and marginal farmers in India suffer significant yield losses due to late detection of crop diseases, nutrient deficiencies, and pests. Existing digital advisory platforms are text-heavy, English-centric, and unusable for farmers with low literacy or limited digital skills. As a result, actionable guidance does not reach farmers at the critical moment.

## Proposed Solution
KrishiAI is a voice-first, multimodal agricultural intelligence system that enables farmers to:
- Capture images of crops using a smartphone camera
- Ask questions via voice in their local language
- Receive spoken, actionable crop health recommendations in real time

The system removes the literacy barrier by eliminating typing and reading entirely.

## Functional Requirements
- Image-based crop disease and nutrient deficiency detection
- Voice-based query input in regional languages
- Spoken recommendations with clear, step-by-step actions
- Weather-aware advisory to avoid ineffective spraying
- Offline-first behavior with delayed sync when connectivity improves

## Non-Functional Requirements
- Low-bandwidth optimization for rural connectivity
- High availability via serverless AWS infrastructure
- Scalable architecture to support millions of farmers
- Secure identity management without complex onboarding

## Target Users
- Small and marginal farmers
- Rural agricultural workers
- First-time smartphone users

## Constraints
- Limited internet connectivity
- Low-end Android devices
- Minimal digital literacy

## Success Metrics
- Reduction in crop loss due to early detection
- Increased adoption among non-literate users
- Faster diagnosis-to-action time at the field level
