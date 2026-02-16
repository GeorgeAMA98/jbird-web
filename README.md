# 🐦 JBird Nesting Services - Website

A beautiful, professional website for Jaeda's doula business, built with Astro and optimized for Cloudflare Pages.

## 🎨 Design

**Color Palette:**
- Terracotta: `#C77B5C` (warm, nurturing)
- Sage Green: `#8B9D83` (calming, natural)
- Cream: `#F5EBE0` (soft, inviting)

## 🚀 Quick Start

### Prerequisites

- Node.js 18+ and npm (or pnpm/yarn)

### Installation

```bash
npm install
```

### Development

```bash
npm run dev
```

Visit `http://localhost:4321` to see your site.

### Build

```bash
npm run build
```

The built site will be in the `dist/` folder.

### Preview Production Build

```bash
npm run preview
```

## 📁 Project Structure

```
├── public/
│   ├── hero-splash.svg          # Main hero image
│   ├── hero-splash-alt.svg      # Alternative hero image
│   └── favicon.svg               # Site favicon
├── src/
│   ├── components/
│   │   ├── Header.astro         # Navigation header
│   │   ├── Hero.astro           # Hero section
│   │   ├── About.astro          # About section
│   │   ├── Services.astro       # Services section
│   │   ├── Contact.astro        # Contact form
│   │   └── Footer.astro         # Footer
│   ├── layouts/
│   │   └── Layout.astro         # Main page layout
│   └── pages/
│       └── index.astro          # Homepage
├── astro.config.mjs             # Astro configuration
└── package.json                 # Dependencies
```

## ✏️ Customization Guide

### Must Update Before Launch

1. **Contact Email** (`src/components/Contact.astro` and `src/components/Footer.astro`)
   - Replace `jaeda@jbirdnesting.com` with the actual email

2. **Phone Number** (`src/components/Contact.astro`)
   - Update the placeholder phone number

3. **Location** (`src/components/Contact.astro`)
   - Update "San Jose & Bay Area" if needed

### Optional Updates

1. **Add Jaeda's Photo**
   - Replace the placeholder in `src/components/About.astro`
   - Update the `.image-placeholder` div with an `<img>` tag

2. **Swap Hero Images**
   - In `src/components/Hero.astro`, change `/hero-splash.svg` to `/hero-splash-alt.svg`

3. **Service Descriptions**
   - Edit the `services` array in `src/components/Services.astro`

4. **Social Media Links**
   - Add social media icons/links to the Footer component

5. **Contact Form Integration**
   - Currently the form is static. To make it functional:
     - Use a service like Formspree, Netlify Forms, or Cloudflare Workers
     - Update the form action in `src/components/Contact.astro`

## 🌐 Deployment

See `DEPLOYMENT.md` for detailed deployment instructions to Cloudflare Pages.

## 📝 Features

- ✅ Fully responsive design
- ✅ SEO optimized
- ✅ Fast loading (Astro's static generation)
- ✅ Modern, professional design
- ✅ Accessible markup
- ✅ Ready for Cloudflare Pages

## 🛠️ Technology Stack

- **Astro** - Modern web framework
- **Cloudflare Pages** - Hosting platform
- **SVG** - Scalable graphics

## 📚 Resources

- [Astro Documentation](https://docs.astro.build)
- [Cloudflare Pages Documentation](https://developers.cloudflare.com/pages)
- [Deployment Guide](./DEPLOYMENT.md)

## 💝 Notes

This website was built with love for Jaeda's doula business. The nesting theme runs throughout the design, representing layers of support and care.

---

Built with ❤️ for JBird Nesting Services
