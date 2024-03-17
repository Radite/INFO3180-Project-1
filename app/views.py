"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file contains the routes for your application.
"""

from app import app
from flask import render_template, request, redirect, url_for, flash
from .models import Property
from . import db
from app.forms import PropertyForm
import os
from werkzeug.utils import secure_filename
from flask import send_from_directory



UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    print("Filename: ", filename)  # print the filename
    has_dot = '.' in filename
    print("Has dot: ", has_dot)  # print whether the filename has a dot
    if has_dot:
        extension = filename.rsplit('.', 1)[1].lower()
        print("Extension: ", extension)  # print the extension
        is_allowed = extension in ALLOWED_EXTENSIONS
        print("Is allowed: ", is_allowed)  # print whether the extension is allowed
        return is_allowed
    return False


###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)



@app.route('/properties/create', methods=['GET', 'POST'])
def create_property():
    if request.method == 'POST':
        title = request.form.get('title')
        address = request.form.get('address')
        price = float(request.form.get('price'))
        type = request.form.get('type')
        description = request.form.get('description')
        bedrooms = int(request.form.get('bedrooms'))
        bathrooms = int(request.form.get('bathrooms'))

        # Handle file uploads
        photos = []
        if 'photos' in request.files:
            for file in request.files.getlist('photos'):
                if file and allowed_file(file.filename):
                    filename = secure_filename(file.filename)
                    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                    photos.append(os.path.join(UPLOAD_FOLDER, filename))

        # Save data to the database
        new_property = Property(
            title=title,
            address=address,
           price=price,
            type=type,
            description=description,
            bedrooms=bedrooms,
            bathrooms=bathrooms,
            photos=photos
        )
        db.session.add(new_property)
        db.session.commit()

        flash('Property added successfully!', 'success')
        return redirect('/properties')

    return render_template('create_property.html', form=PropertyForm())

@app.route('/properties')
def list_properties():
    properties = Property.query.all()
    return render_template('list_properties.html', properties=properties)

@app.route('/properties/<int:propertyid>')
def show_property(propertyid):
    property = Property.query.get(propertyid)
    return render_template('show_property.html', property=property)


###
# The functions below should be applicable to all Flask apps.
###

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404
