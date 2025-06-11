# Vitaal Technical Requirements Document

## 🎯 Project Overview

Vitaal Klinic needs two digital products:
1. **Marketing Website** (vitaalklinic.dk) - Lead generation and conversion
2. **Patient App** (Vitaal Digital) - iOS app for member care

## 🌐 Website Technical Requirements

### Stack Requirements
- **Framework**: Next.js 14+ with App Router
- **Language**: TypeScript (strict mode)
- **Styling**: Tailwind CSS v3
- **CMS**: Sanity.io or Strapi
- **Hosting**: Vercel
- **Analytics**: GA4 + Mixpanel

### Core Features
1. **Booking System**
   - Calendar integration
   - Email confirmations
   - SMS reminders (Twilio)
   - CRM sync (HubSpot)

2. **Membership Calculator**
   - Interactive pricing tool
   - BMI calculator
   - Savings estimator
   - Lead capture

3. **Content Management**
   - Blog with categories
   - SEO metadata
   - Danish/English
   - Version control

4. **Performance**
   - Core Web Vitals green
   - <3s load time
   - 90+ Lighthouse
   - CDN optimization

### SEO Requirements
- Schema markup for medical practice
- Sitemap generation
- Meta tags automation
- Danish keyword optimization
- Local SEO for Copenhagen

### Integrations
- SendGrid (email)
- Calendly or similar (booking)
- HubSpot (CRM)
- Google Tag Manager
- Facebook Pixel

## 📱 iOS App Technical Requirements

### Platform Requirements
- **iOS Version**: 16.0+
- **Devices**: iPhone (iPad compatible)
- **Language**: Swift 5.9+
- **UI Framework**: SwiftUI
- **Architecture**: MVVM

### Core Modules

#### 1. Authentication
```swift
- Face ID/Touch ID mandatory
- JWT token management  
- Biometric re-auth for sensitive data
- Session timeout (15 min)
- Keychain storage
```

#### 2. Health Dashboard
```swift
- Real-time metrics display
- Interactive charts (Swift Charts)
- Biological age algorithm
- Goal tracking
- Export to PDF
```

#### 3. HealthKit Integration
```swift
- Weight, BMI, body fat %
- Blood pressure, heart rate
- Steps, activity, workouts
- Sleep data
- Continuous updates
```

#### 4. Medication Management
```swift
- Injection reminders
- Dose tracking
- Side effect logging
- Inventory management
- Refill notifications
```

#### 5. Lab Results
```swift
- FHIR data parsing
- Trend visualization  
- Reference ranges
- Doctor notes
- History comparison
```

#### 6. Secure Messaging
```swift
- End-to-end encryption
- Read receipts
- Photo attachments
- Voice notes
- Offline queue
```

### Backend Requirements

#### Architecture
```yaml
API:
  Type: REST + GraphQL
  Auth: AWS Cognito
  Gateway: AWS API Gateway
  
Database:
  Primary: AWS HealthLake (FHIR)
  Cache: Redis
  Files: S3 (encrypted)
  
Infrastructure:
  Compute: Lambda
  Queue: SQS
  Notifications: SNS
  Monitoring: CloudWatch
```

#### Security
- HIPAA compliance ready
- GDPR compliant
- AES-256 encryption
- API rate limiting
- WAF protection
- Audit logging

#### Integrations
1. **Unilabs** (Lab results)
   - HL7v2 or FHIR format
   - Webhook notifications
   - OAuth2 authentication

2. **GenomeScan** (Genetics)
   - REST API
   - VCF file processing
   - Batch operations

3. **Oura Ring**
   - OAuth2 flow
   - Webhook updates
   - Data normalization

4. **DrugBank** (Interactions)
   - API key auth
   - Caching strategy
   - Offline database

### Data Models

#### FHIR Resources
```json
{
  "Patient": {
    "id": "string",
    "name": "HumanName",
    "birthDate": "date",
    "gender": "code"
  },
  "Observation": {
    "id": "string",
    "status": "code",
    "code": "CodeableConcept",
    "value": "Quantity",
    "effectiveDateTime": "dateTime"
  },
  "MedicationStatement": {
    "id": "string",
    "medication": "CodeableConcept",
    "dosage": "Dosage",
    "adherence": "custom"
  }
}
```

### Performance Requirements
- App launch: <2 seconds
- API response: <200ms (p95)
- Offline capability
- Background sync
- Push notification: <5s delay

### Testing Requirements
- Unit tests: >80% coverage
- UI tests: Critical paths
- Integration tests: All APIs
- Security: Penetration testing
- Performance: Load testing

## 🔧 Development Setup

### Website Setup
```bash
# Clone and install
git clone [repo]
cd vitaal/website
npm install

# Environment variables
NEXT_PUBLIC_SANITY_PROJECT_ID=xxx
SANITY_API_TOKEN=xxx
SENDGRID_API_KEY=xxx

# Run locally
npm run dev
```

### iOS Setup
```bash
# Prerequisites
- Xcode 15+
- CocoaPods
- Swift 5.9+

# Install
cd vitaal/app/ios
pod install
open VitaalDigital.xcworkspace
```

### Backend Setup
```bash
# AWS CLI configured
aws configure

# Deploy infrastructure
cd vitaal/app/backend
terraform init
terraform plan
terraform apply

# Deploy functions
serverless deploy
```

## 📊 Deliverables

### Website (Month 1-2)
- [ ] Responsive website (mobile-first)
- [ ] CMS integration
- [ ] Booking system
- [ ] Analytics setup
- [ ] SEO optimization
- [ ] Performance optimization

### iOS App (Month 1-4)
- [ ] Authentication flow
- [ ] Health dashboard
- [ ] Medication tracking
- [ ] Lab integration
- [ ] Messaging system
- [ ] Push notifications

### Documentation
- [ ] API documentation
- [ ] User guides
- [ ] Admin manual
- [ ] Security audit
- [ ] Code documentation

## 🎨 Design Resources

### Brand Colors
```css
--primary: #0B4F71;    /* Trust Blue */
--secondary: #4FB06D;  /* Vitality Green */
--accent: #F39C12;     /* Energy Orange */
--dark: #2C3E50;
--light: #ECF0F1;
```

### Typography
```css
--font-heading: 'SF Pro Display', system-ui;
--font-body: 'SF Pro Text', system-ui;
--font-mono: 'SF Mono', monospace;
```

### Assets Location
- Figma: [Link to be provided]
- Logo files: `/assets/logo/`
- Icons: SF Symbols (iOS)
- Stock photos: [To be provided]

## 📈 Success Criteria

### Website
- PageSpeed Insights: >90
- Accessibility: WCAG AA
- SEO: First page for target keywords
- Conversion: >3% consultation booking

### App
- App Store rating: >4.5
- Crash-free rate: >99.9%
- Daily active users: >80%
- User retention: >90% (3 months)

## 🚀 Deployment

### Website
- Automatic deployment via Vercel
- Preview deployments for PRs
- Production: vitaalklinic.dk
- Staging: staging.vitaalklinic.dk

### App
- TestFlight for beta
- Phased App Store release
- Over-the-air updates (CodePush)
- Rollback capability

---

*For questions: tech@vitaalklinic.dk*
