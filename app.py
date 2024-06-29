from flask import Flask, render_template, request, redirect, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Dummy data for events
events = [
    {"name": "Community Clean-Up", "date": "July 15", "description": "Join us for a community clean-up to keep our neighborhood beautiful."},
    {"name": "Neighborhood BBQ", "date": "August 22", "description": "Enjoy a fun BBQ with your neighbors. Food and drinks will be provided."},
    {"name": "Town Hall Meeting", "date": "September 5", "description": "Attend the town hall meeting to discuss important issues in our community."}
]

@app.route('/')
def home():
    return render_template('index.html', events=events)

@app.route('/events')
def events_page():
    return render_template('events.html', events=events)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        
        # Here you can handle the form data, e.g., save it to a database or send an email
        flash('Message sent successfully!', 'success')
        return redirect('/contact')
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
