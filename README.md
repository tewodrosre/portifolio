# portifolio# Tewodros Redae - Professional Engineering Portfolio

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)
[![Flask Version](https://img.shields.io/badge/flask-2.0%2B-green)](https://flask.palletsprojects.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

![Portfolio Screenshot](/static/p1.jpg) <!-- Replace with actual screenshot path -->

Professional portfolio website showcasing civil engineering expertise, construction management services, and material sales offerings.

## Features

🚀 **Core Functionality**
- Project portfolio with interactive galleries
- Construction service pricing calculator
- Material sales catalog
- Professional certification display
- Contact form with email integration

🛠 **Technical Highlights**
- Flask-based web application
- Responsive Bootstrap 5 design
- Email integration with Flask-Mail
- Dynamic content rendering
- Mobile-first approach

## Installation

1. **Clone Repository**
```bash
git clone https://your-repository-link.git
cd engineering-portfolio
```

2. **Install Dependencies**
```bash
python -m venv venv
source venv/bin/activate  # Linux/MacOS
venv\Scripts\activate  # Windows
pip install -r requirements.txt
```

3. **Configuration**
Create `.env` file:
```env
MAIL_PASSWORD=your_app_specific_password
```

## Deployment

1. **PythonAnywhere Setup**
- Upload all project files
- Create virtual environment:
```bash
mkvirtualenv --python=/usr/bin/python3.8 myenv
```

2. **WSGI Configuration**
Point to `app.py`:
```python
from app import app as application
```

3. **Environment Variables**
Add in Web tab:
```
MAIL_PASSWORD=your_app_specific_password
```

## Project Structure
```plaintext
├── app.py              # Main application entry
├── requirements.txt    # Dependency list
├── static/             # Static assets
│   ├── future.jpeg
│   ├── materials/      # Product images
│   └── designs/        # Interior design portfolio
├── templates/          # HTML templates
│   ├── base.html       # Base template
│   ├── services.html   # Services & materials
│   └── ...             # Other pages
└── README.md           # This documentation
```

## Key Pages

🏗 **Services Page**
- Construction service packages
- Material price lists (geotextiles, tiles)
- Document templates (contracts, takeoffs)
- Interior design portfolio

📜 **Certifications**
- Professional licenses
- Safety certifications
- Accreditation details

📈 **Experience**
- Project timeline visualization
- Key achievement highlights
- Technical specifications showcase

## Contributing

1. Fork the repository
2. Create feature branch:
```bash
git checkout -b feature/new-feature
```
3. Commit changes
4. Push to branch
5. Open pull request

## License

MIT License - See [LICENSE](LICENSE) for details

## Contact

**Tewodros Redae**  
📧 [gebretewodros73@gmail.com](mailto:gebretewodros73@gmail.com)  
📱 +251 964 108463  
🏢 Addis Ababa, Ethiopia

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue)](https://www.linkedin.com/in/tewodros-gebre-14ba68116)