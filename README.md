# JBird Nesting Services

A simple, professional static website for Jaeda's doula business. Ready for **GitHub Pages**—no build step required.

https://jbird.help

## What’s included

- **index.html** – Single-page site (Hero, About, Services, Contact, Footer)
- **styles.css** – All styles (responsive, same look as before)
- **favicon.svg**, **hero-splash.svg** – Assets in the repo root
- **.nojekyll** – So GitHub Pages serves the site as plain static files

## Run locally

Open `index.html` in a browser, or use a local server:

```bash
# Python
python3 -m http.server 8000

# or npx (no install)
npx serve
```

Then visit `http://localhost:8000` (or the URL shown).

## Deploy to GitHub Pages

1. Push this repo to GitHub.
2. **Settings → Pages**
3. Under **Source**, choose **Deploy from a branch**
4. Branch: **main** (or your default), folder: **/ (root)**
5. Save. The site will be at `https://<username>.github.io/<repo-name>/`

For a **user/org site** (`https://<username>.github.io`), use a repo named `<username>.github.io` and push the same files; the root is the site root.

## Customize before going live

- **Contact:** Update email and phone in `index.html` (contact section and footer).
- **Location:** Change “San Jose & Bay Area” in the contact section if needed.
- **About photo:** Replace the placeholder block in the About section with an `<img>` pointing to a photo (e.g. in the repo or from a URL).
- **Contact form:** The form has `action="#"`. To make it work, use a service like [Formspree](https://formspree.io) or similar and set the form `action` to the URL they give you.

## Design

- **Terracotta:** `#C77B5C`
- **Sage green:** `#8B9D83`
- **Cream:** `#F5EBE0`

---

Built with love for JBird Nesting Services.


