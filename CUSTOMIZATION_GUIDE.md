# Portfolio Customization Checklist

Complete this checklist to personalize your portfolio:

## ✅ Profile Page (`templates/profile.html`)

- [ ] Replace `[YOUR NAME HERE]` with your full name
- [ ] Update `[Your Course/Year/Section]` with your actual course info
  - Example: "Computer Science • 2nd Year • Section 2-A"
- [ ] Optionally replace the local profile illustration with your photo
  - Save your photo in the `static/` folder
  - In `templates/profile.html`, update the image filename to your photo
- [ ] Update "About Me" section with your bio
- [ ] Update "Education" section:
  - Course name (e.g., Bachelor of Science in Computer Science)
  - Year (e.g., 2nd Year, Final Year)
  - Section (e.g., 2-A, B-101)
  - Institution name
- [ ] Change the motto/quote to something meaningful to you
- [ ] Update "Skills" section with your actual skills

## ✅ Contact Page (`templates/contact.html`)

- [ ] Replace `[YOUR_EMAIL@example.com]` with your real email
- [ ] Replace `[+1 (555) XXX-XXXX]` with your phone number
- [ ] Replace `[Your City, Country]` with your location
- [ ] Update timezone (replace `[UTC+8]`)
- [ ] Add your actual social media links:
  - GitHub profile URL
  - LinkedIn profile URL
  - Twitter profile URL
  - Or add other social media (Instagram, Portfolio, etc.)

## ✅ Color Customization

Edit `static/style.css`:

The site uses CSS variables near the top of the file. Adjust the signal color or surfaces:
```css
:root {
    --bg: #0b0d0c;
    --surface: #111412;
    --accent: #c8fb55;
}
```

**Popular color combinations:**
- Electric Blue: #62c6ff
- Warm Amber: #ffc45c
- Coral: #ff806e
- Violet: #b69aff
- Mint: #80f0c0

## ✅ Adding Your Photo

1. **Prepare your photo:**
   - Recommended size: 300x300px (square)
   - Format: PNG or JPG
   - File size: < 200KB

2. **Save to static folder:**
   - Save as `static/profile.jpg`

3. **Update HTML:**
   - In `templates/profile.html`, find the img tag
   - Change: `filename='profile-visual.svg'`
   - To: `filename='profile.jpg'`

## ✅ Adding More Projects

To showcase additional projects on the home page:

1. **Create new route in `app.py`:**
   ```python
   @app.route('/works/myproject', methods=['GET', 'POST'])
   def myproject():
       result = None
       if request.method == 'POST':
           # Your code here
       return render_template('myproject.html', result=result)
   ```

2. **Create template in `templates/myproject.html`:**
   - Use the same navbar structure
   - Link to the CSS file
   - Build your UI

3. **Add to home page (`templates/index.html`):**
   ```html
   <div class="work-item">
       <h3>My Project Name</h3>
       <p>Description of what it does</p>
       <a href="/works/myproject">Go to Project</a>
   </div>
   ```

## ✅ Styling Tips

**Change button and heading colors:** Update the `--accent` CSS variable in `static/style.css`.

**Adjust spacing:**
Change padding values (e.g., `padding: 2rem;`) to make content more/less spread out

## ✅ Testing Your Changes

After making changes:

1. Stop the Flask server (Ctrl+C)
2. Run again: `python app.py`
3. Refresh browser: F5 or Ctrl+R
4. Check each page from the navbar

## Quick edits locations:

| Page | File | Key placeholders |
|------|------|-----------------|
| Profile | `templates/profile.html` | [YOUR NAME HERE], photos, skills |
| Contact | `templates/contact.html` | Email, phone, social links, location |
| Colors | `static/style.css` | `--accent`, `--bg`, `--surface` |
| Projects | `templates/index.html` | Add work-item divs |
| Projects | `app.py` | Add new @app.route |

## Common Issues & Fixes

**Page looks plain:**
- Make sure `style.css` is in `static/` folder
- Check browser console for CSS loading errors

**Photo not showing:**
- Verify file is in `static/` folder
- Check filename spelling (case-sensitive on Linux)
- Use correct file extension (.jpg, .png, etc.)

**Changes not showing:**
- Hard refresh: Ctrl+Shift+R (or Cmd+Shift+R on Mac)
- Clear browser cache
- Restart Flask server

**Form not working:**
- Check @app.route method matches form method
- Verify form input names match Python variable names

---

**Need help?** Check the README.md file for more detailed explanations!

Good luck with your portfolio! 🎉
