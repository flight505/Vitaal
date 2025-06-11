# Vitaal Digital - iOS App

Native iOS application for continuous patient care and health optimization.

## 🎯 Project Overview

Vitaal Digital is the patient-facing iOS application that provides continuous health monitoring, medication management, and communication with the care team between clinic visits.

## 🛠 Tech Stack

- **Platform**: iOS 16+ (SwiftUI)
- **Backend**: AWS HealthLake (FHIR)
- **Health Data**: HealthKit + CareKit
- **Analytics**: Firebase Analytics
- **Wearables**: Oura API, Apple Watch

## 🚀 Quick Start

```bash
# Install dependencies
cd ios
pod install

# Open in Xcode
open VitaalDigital.xcworkspace

# Run on simulator
⌘ + R
```

## 📁 Project Structure

```
app/
├── ios/                   # iOS native app
│   ├── VitaalDigital/    # Main app code
│   ├── VitaalDigitalTests/
│   └── Pods/             # Dependencies
├── backend/              # API services
│   ├── functions/        # Lambda functions
│   ├── infrastructure/   # Terraform configs
│   └── tests/
└── shared/               # Shared utilities
```

## 🏗 Architecture

### iOS App Architecture
- **Pattern**: MVVM + SwiftUI
- **Navigation**: NavigationStack
- **State**: @StateObject + Combine
- **Storage**: Core Data + Keychain

### Backend Architecture
- **API**: GraphQL (AWS AppSync)
- **Storage**: AWS HealthLake (FHIR)
- **Auth**: AWS Cognito
- **Files**: S3 (encrypted)

## 📱 Core Features

### MVP (Q1 2025)
- [ ] Biometric authentication
- [ ] Health dashboard
- [ ] Lab results display
- [ ] Medication reminders
- [ ] Secure messaging
- [ ] Basic HealthKit integration

### Phase 2 (Q2 2025)
- [ ] Video consultations
- [ ] Oura Ring integration
- [ ] AI insights
- [ ] Group sessions
- [ ] Document vault

## 🔐 Security

- **Authentication**: Face ID/Touch ID required
- **Encryption**: AES-256 for all data
- **GDPR**: Full compliance with consent management
- **Audit**: All data access logged

## 🧪 Testing Strategy

```bash
# Unit tests
swift test

# UI tests
xcodebuild test -scheme VitaalDigital

# Integration tests
npm run test:integration
```

## 📊 Analytics Events

Key events tracked:
- `app_open`
- `dashboard_viewed`
- `medication_logged`
- `lab_result_viewed`
- `message_sent`
- `appointment_booked`

## 🏥 HealthKit Permissions

Required permissions:
- Body mass
- Heart rate
- Blood pressure
- Step count
- Sleep analysis
- Oxygen saturation

## 🔗 API Integrations

### Unilabs (Lab Results)
```swift
let results = await UnilabsAPI.fetchResults(patientId: currentUser.id)
```

### GenomeScan (Genetics)
```swift
let variants = await GenomeScanAPI.getPharmacogenomics(sampleId: sample.id)
```

### Oura Ring
```swift
OuraAPI.authorize { token in
    self.ouraToken = token
    self.startSyncingOuraData()
}
```

## 📱 Device Support

- **Minimum iOS**: 16.0
- **Devices**: iPhone 11+
- **Apple Watch**: Series 6+ (optional)
- **iPad**: Supported but not optimized

## 🚦 Release Process

1. Update version in Info.plist
2. Run full test suite
3. Create release branch
4. Submit to TestFlight
5. Internal testing (2 weeks)
6. Submit to App Store
7. Phased rollout

## 📈 Performance Targets

- App launch: <2s
- API response: <200ms
- Offline capability: Full
- Crash rate: <0.1%

## 🆘 Support

- **Tech Lead**: jesper@vitaalklinic.dk
- **iOS Developer**: [TBD]
- **Backend Team**: [TBD]

---

© 2025 Vitaal Digital. Confidential and proprietary.
