# JBird Nesting Services

A simple, professional static website for Jaeda's doula business. Ready for **GitHub Pages**—no build step required.

https://jbird.help

## What’s included

- **index.html** – Single-page site (Hero, About, Services, Contact, Footer)
- **styles.css** – All styles (responsive, same look as before)
- **Jbird Logo - Bird 1.png**, **hero-splash.svg** – Assets in the repo root
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

## Verify Google Analytics (Realtime)

After adding the Google tag to `index.html`, confirm tracking is working:

1. Open your site in a browser (`https://jbird.help` or local URL).
2. In another tab, open Google Analytics for this property.
3. Go to **Reports → Realtime**.
4. Browse a few sections on your site (scroll, click links, stay active for ~30 seconds).
5. Confirm at least one active user appears in Realtime.

If nothing appears after 1–2 minutes:

- Turn off ad blockers/privacy extensions for your site.
- Test in an incognito/private window.
- Double-check the measurement ID in the script is `G-NFZHBWGF4N`.
- Ensure only one Google tag snippet is present on the page.

### Verify with DebugView (deeper check)

Use DebugView when you want to confirm events in near real time:

1. Open your site in Chrome.
2. Open DevTools (`F12`) and keep it open while testing.
3. In Google Analytics, go to **Admin → DebugView**.
4. Refresh your site and navigate around (page load, clicks, scroll).
5. Confirm you see incoming events such as `page_view` in DebugView.

If DebugView is empty, test again in an incognito window with extensions disabled.

Note: after first deployment or tag changes, it can take a few minutes before events consistently appear in Realtime/DebugView.

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


