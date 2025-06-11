# Vitaal Klinic Website

Marketing website for Denmark's first metabolic health and longevity center.

## 🎯 Project Overview

This website serves as the primary marketing and conversion tool for Vitaal Klinic, targeting Denmark's 25,000 high-net-worth households interested in preventive health and longevity medicine.

## 🛠 Tech Stack

- **Framework**: Next.js 14 (App Router)
- **Styling**: Tailwind CSS
- **CMS**: Sanity.io
- **Analytics**: Google Analytics 4 + Mixpanel
- **Hosting**: Vercel
- **Language**: TypeScript

## 🚀 Quick Start

```bash
# Install dependencies
npm install

# Set up environment variables
cp .env.example .env.local

# Run development server
npm run dev

# Build for production
npm run build
```

## 📁 Project Structure

```
website/
├── app/                    # Next.js app directory
│   ├── (marketing)/       # Marketing pages
│   ├── (services)/        # Service detail pages
│   └── api/               # API routes
├── components/            # Reusable components
├── lib/                   # Utilities and helpers
├── public/               # Static assets
├── sanity/               # CMS schema
└── styles/               # Global styles
```

## 🎨 Design System

- **Primary Color**: #0B4F71 (Trust Blue)
- **Secondary Color**: #4FB06D (Vitality Green)
- **Font**: SF Pro Display/Text
- **Language**: Danish (primary), English (secondary)

## 📝 Content Management

Content is managed through Sanity CMS. Access the studio at:
```
https://vitaalklinic.sanity.studio
```

## 🔍 SEO Strategy

Primary target keywords:
- "wegovy privat klinik danmark"
- "glp-1 vægttab københavn"
- "hyperbar iltterapi danmark"
- "biologisk alder test"

## 📊 Conversion Goals

1. **Primary**: Book free consultation (3% target)
2. **Secondary**: Email list signup
3. **Tertiary**: Download longevity guide

## 🚦 Development Workflow

1. Create feature branch from `main`
2. Implement feature with tests
3. Run `npm run lint` and `npm run test`
4. Create PR with description
5. Deploy to preview environment
6. Merge after approval

## 📈 Performance Targets

- Lighthouse score: >90 all categories
- Time to Interactive: <3s
- Core Web Vitals: All green

## 🔐 Environment Variables

```env
NEXT_PUBLIC_SANITY_PROJECT_ID=
NEXT_PUBLIC_SANITY_DATASET=
SANITY_API_TOKEN=
NEXT_PUBLIC_GA_ID=
NEXT_PUBLIC_MIXPANEL_TOKEN=
SENDGRID_API_KEY=
```

## 📞 Support

- **Tech Lead**: jesper@vitaalklinic.dk
- **Project Manager**: [TBD]
- **Design**: [Agency Contact]

---

© 2025 Vitaal Klinic. Confidential and proprietary.
