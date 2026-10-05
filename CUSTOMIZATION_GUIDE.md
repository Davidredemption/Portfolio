# Portfolio Update Guide

This is David Anthony P. Cruz's ongoing personal portfolio. Keep it accurate as education, projects, and experience develop.

## Profile and résumé details

Edit `templates/profile.html` to update:

- Current program and year at PUP Sta. Mesa
- Education history, honors, and awards
- Skills and qualities
- Clubs, work immersion, seminars, and programs
- Profile illustration or a replacement photo saved under `static/`

Only include dates, credentials, and responsibilities that can be verified. Add specific individual contributions to team projects when confirmed.

## Contact details

Edit `templates/contact.html` to update the email address, phone number, location, or GitHub profile.

The email and phone links are public on this portfolio. Do not add a birth date, home address, passwords, or other information that is not needed for professional contact.

## Featured projects

The home page's main showcase is in `templates/index.html`.

- The Assignment Tracker card links to the team repository at `https://github.com/Davidredemption/OOP-FINAL-PROJECT`.
- FaceCheck is described as an early team prototype. Its source link and technical implementation are not available yet; keep claims limited to what the team actually built.
- Existing introductory Flask exercises remain accessible from the Lab navigation and `/works`.

When project source or additional verified details become available, update the relevant card with its actual features, technologies, source link, and your contribution.

## Visual customization

Edit the CSS variables at the top of `static/style.css` to change the main palette:

```css
:root {
    --bg: #0b0d0c;
    --surface: #111412;
    --accent: #c8fb55;
}
```

The scroll reveal behavior lives in `static/script.js`. It respects the visitor's reduced-motion preference.

## Run locally

```powershell
.\.venv\Scripts\activate
python app.py
```

Then open `http://127.0.0.1:5000` and check the home, profile, contact, project, and Lab pages.
