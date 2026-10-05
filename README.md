# My Programming Portfolio

A modern Flask-based personal portfolio web application showcasing programming skills and projects.

## Features ✨

### 1. **Responsive Navigation Bar**
- Sticky navigation on all pages for easy navigation
- Links to Home, Profile, Works, and Contact pages
- Dark technical styling with signal-green active and hover states

### 2. **Professional Profile Page**
- Display your personal information (Name, Course, Year, Section)
- Showcase your education and skills
- Featured motto/inspirational quote
- Placeholder image (update with your own photo)

### 3. **Programming Projects Showcase**
- **String Converter**: Convert text to uppercase
- **Circle Area Calculator**: Calculate the area of a circle using π×r²
- **Triangle Area Calculator**: Calculate the area of a triangle using (base×height)/2
- **Linked List Manager**: Add, remove, and manage items in a linked list

### 4. **Contact Page**
- Display your contact information
- Show email, phone, location, and social media links
- Contact form for visitors to reach out

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

Edit `templates/profile.html` and replace:
- `[YOUR NAME HERE]` → Your full name
- `[Your Course/Year/Section]` → Your course information
- `profile-visual.svg` → A photo saved in the `static/` folder, if desired
- Motto text in the gradient box
- Skills section with your own skills

### Update Contact Information

Edit `templates/contact.html` and replace:
- `[YOUR_EMAIL@example.com]` → Your email address
- `[+1 (555) XXX-XXXX]` → Your phone number
- `[Your City, Country]` → Your location
- `[UTC+8] or [Your Timezone]` → Your timezone
- Social media links (GitHub, LinkedIn, Twitter)

### Customize Colors

Edit `static/style.css` and modify the gradient colors:
```css
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
```

Change these hex colors to your preferred palette:
- `#667eea` - Primary color (blue-purple)
- `#764ba2` - Secondary color (darker purple)

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

3. Add a link to your new project on `templates/index.html`

## Features Explained

### String Converter (`/works`)
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
- ✅ Mobile-first responsive approach
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

This portfolio was created as part of a programming laboratory exercise to practice Flask web development, HTML templating, CSS styling, and implementing data structures (linked lists) with a web interface.

Happy coding! 🚀

---

**Last Updated**: October 2026
**Made with ❤️ using Flask**
