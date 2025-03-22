from flask import Flask, render_template, request, redirect, url_for
from flask_mail import Mail, Message
import os

app = Flask(__name__)

# Email Configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'gebretewodros73@gmail.com'
app.config['MAIL_PASSWORD'] = os.getenv('Kal1ted2si@men1')  # Set in PythonAnywhere dashboard
app.config['MAIL_DEFAULT_SENDER'] = ('Tewodros Redae Portfolio', 'gebretewodros73@gmail.com')

mail = Mail(app)

PROJECTS = [
    {
        'id': 'azarias',
        'title': '22 Residential Buildings - Legetafo',
        'tech': ['Isolated Footing', 'Hollow Block Waffle Slabs', 'Brick Masonry'],
        'images': ['p1.jpg', 'pd2.jpg'],
        'description': '''Supervised construction of G+2 residential complexes featuring:
                        - Optimized material usage saving 15% on concrete
                        - Compliance with Addis Ababa building codes
                        - Advanced foundation systems for seismic zones'''
    },
    {
        'id': 'debre-markos',
        'title': 'Debre Markos University Campus',
        'tech': ['Raft Foundations', 'Ribbed Slab Structures', 'Seismic Design'],
        'images': ['p2.jpg', 'p3.jpg'],
        'description': '''Led construction of academic facilities including:
                        - 5000m² classroom complex
                        - 300-bed dormitory buildings
                        - Earthquake-resistant library structure'''
    },
    {
        'id': 'salt-warehouse',
        'title': '3600m² Salt Warehouse - Afdera',
        'tech': ['Double Howe Truss', 'Galvanized Steel', 'Extreme Weather Construction'],
        'images': ['p3.jpg', 'pd2.jpg'],
        'description': '''Managed installation of 60m truss structure:
                        - Completed 3 weeks ahead of schedule
                        - Specialized corrosion protection systems
                        - Temperature-resistant material selection'''
    }
]

@app.route('/')
def home():
    return render_template('index.html', projects=PROJECTS)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/experience')
def experience():
    return render_template('experience.html')

@app.route('/certifications')
def certifications():
    return render_template('certifications.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/contact', methods=['POST'])
def contact():
    try:
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        
        msg = Message(
            subject=f"New Message from {name}",
            recipients=['gebretewodros73@gmail.com'],
            body=f"Name: {name}\nEmail: {email}\nMessage: {message}"
        )
        mail.send(msg)
        return redirect(url_for('home', _anchor='contact') + '?success=1')
    except Exception as e:
        print(f"Mail error: {str(e)}")
        return redirect(url_for('home', _anchor='contact') + '?error=1')

if __name__ == '__main__':
    app.run(debug=False)
@app.route('/experience')
def experience():
    return render_template('experience.html')

@app.route('/certifications')
def certifications():
    return render_template('certifications.html')

if __name__ == '__main__':
    app.run()