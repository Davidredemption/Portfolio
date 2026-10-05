# David Anthony P. Cruz — Portfolio

A personal Flask portfolio for David Anthony P. Cruz, a second-year Computer Engineering student at the Polytechnic University of the Philippines — Sta. Mesa. It presents his education, experience, contact details, and team projects.

## Features ✨

### 1. **Responsive Navigation Bar**
- Sticky navigation on all pages for easy navigation
- Links to Overview, Profile, Works, and Contact pages
- Dark technical styling with signal-green active and hover states

### 2. **Professional Profile Page**
- Current Computer Engineering studies at PUP Sta. Mesa
- Education history, honors, student activities, and seminars
- Skills and qualities based on the provided résumé
- Local illustrated profile artwork

### 3. **Programming Projects Showcase**
- **Assignment Tracker**: A team-built Python/Tkinter desktop project for assignments, deadlines, a calendar, and reminders, using MySQL. [View the source repository](https://github.com/Davidredemption/OOP-FINAL-PROJECT).
- **FaceCheck Attendance**: A team prototype exploring face scanning and screenshot capture for an attendance workflow. It is an early prototype, not a production attendance or identity-verification system; source code is not currently available.
- **Works page** (`/works`): Features the two team projects first, followed by separately labeled interactive classroom exercises.
- **Classroom exercises**: String conversion, circle and triangle area calculators, and a linked-list manager are available from the Works page.

### 4. **Contact Page**
- Email and phone links, Mandaluyong City location, and GitHub profile
- Direct email action; no non-functional contact form

### 5. **Modern UI/UX Design**
- Laptop-first technical dashboard aesthetic with a graphite and signal-green palette
- Animated system visualization, project cards, and terminal-style status panel
- Responsive layouts for smaller screens without compromising the desktop presentation
- Reduced-motion support and local assets for reliable rendering

## Project Structure

```
Flask_intro_2026/
├── app.py                    # Main Flask application
├── static/
│   ├── style.css            # Shared visual system and responsive styling
│   ├── script.js            # Scroll reveal animation
│   └── profile-visual.svg   # Local profile illustration
├── templates/
│   ├── index.html           # Home page
│   ├── works.html           # Featured projects and classroom exercises
│   ├── profile.html         # Profile page
│   ├── contact.html         # Contact page
│   ├── touppercase.html     # String converter
│   ├── circle.html          # Circle area calculator
│   ├── triangle.html        # Triangle area calculator
│   └── linkedlist.html      # Linked list manager
└── README.md                # This file
```

## How to Run

### Prerequisites
- Python 3.7+
- Flask 3.1.3

### Installation

1. **Activate the virtual environment:**
   ```bash
   .venv\Scripts\activate  # On Windows
   source .venv/bin/activate  # On macOS/Linux
   ```

2. **Run the Flask application:**
   ```bash
   python app.py
   ```

3. **Open your browser and navigate to:**
   ```
   http://127.0.0.1:5000
   ```

## Customization Guide

### Update Your Profile

Edit `templates/profile.html` to update the profile, education history, skills, activities, and seminars as they change.

### Update Contact Information

Edit `templates/contact.html` to change the email, phone number, location, or GitHub link. Contact details on this page are public.

### Customize Colors

Edit the CSS variables near the top of `static/style.css` to adjust the dark background and signal-green accent.

### Add More Projects

To add a new programming project:

1. Create a new route in `app.py`:
   ```python
   @app.route('/works/myproject', methods=['GET', 'POST'])
   def myproject():
       # Your implementation here
       return render_template('myproject.html', result=result)
   ```

2. Create a corresponding HTML template in `templates/myproject.html`

3. Add the project to the Works page in `templates/works.html`

## Features Explained

### String Converter (`/works/string-converter`)
- Linked from the exercises section of the Works page (`/works`).
- Takes any text input and converts it to uppercase
- Simple form submission
- Displays the result below the form

### Circle Area Calculator (`/works/area/circle`)
- Formula: A = π × r²
- Takes radius as input
- Calculates and displays the area
- Error handling for invalid inputs

### Triangle Area Calculator (`/works/area/triangle`)
- Formula: A = (base × height) / 2
- Takes base and height as inputs
- Calculates and displays the area
- Validates positive numbers

### Linked List Manager (`/works/linkedlist`)
- Add items to a linked list data structure
- Display all items with their index
- Remove individual items
- Clear the entire list
- Educational explanation of linked list concepts

## Responsive Design

The portfolio is fully responsive and works on:
- ✅ Desktop computers
- ✅ Tablets
- ✅ Mobile phones

CSS media queries ensure optimal viewing on all screen sizes.

## Technologies Used

- **Backend**: Flask 3.1.3 (Python web framework)
- **Frontend**: HTML5, CSS3, Jinja2 templating
- **Styling**: Custom CSS with gradients and animations
- **Responsive Design**: CSS Flexbox and Grid

## Best Practices

- ✅ All pages include the navigation bar for consistent UX
- ✅ Form validation on the backend
- ✅ Semantic HTML markup
- ✅ Accessibility-friendly design
- ✅ Responsive layout with accessible mobile behavior
- ✅ DRY principle (Don't Repeat Yourself) with shared CSS

## Future Enhancements

Potential features to add:
- Blog section for technical articles
- Portfolio gallery with project thumbnails
- Dark mode toggle
- Database integration for contact form submissions
- Resume/CV download
- Skills visualization with progress bars
- Project filtering by technology

## License

This project is open source and free to use for educational purposes.

## Author Notes

This portfolio is a continuing personal project. The Lab section also retains introductory Flask exercises from coursework.

Happy coding! 🚀

---

**Last Updated**: October 2026
**Made with ❤️ using Flask**
