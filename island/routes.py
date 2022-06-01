from island import app
from island import db
from flask import redirect, render_template, url_for, flash
from island.models import Applicant, User
from island.forms import ContactForm, ServicesForm
@app.route("/")
@app.route("/home")
def home_page():
    return render_template('home.html')



@app.route("/contacts", methods=['GET', 'POST'])
def contacts_page():
    form = ContactForm()
    if form.validate_on_submit():
        info_to_send = User(name=form.name.data, email_address=form.email_address.data,
                            comment=form.comment.data)
        db.session.add(info_to_send)
        db.session.commit()
        flash('Submitted successfully', category="success")

        return redirect(url_for('contacts_page'))
    if form.errors != {}: #If there are not errors from the validations
        for err_msg in form.errors.values():
          flash(f'There was an error with your personal details {err_msg}', category='danger')

    return render_template('contacts.html', form=form)


@app.route("/services", methods=['GET', 'POST'])
def services_page():
    form = ServicesForm()
    if form.validate_on_submit():
        details_to_send = Applicant(name=form.name.data, email_address=form.email_address.data, phone_number=form.phone_number.data,
                                    county=form.county.data, town=form.town.data, enquiry=form.enquiry.data)
        db.session.add(details_to_send)
        db.session.commit()
        flash('Submitted successfully', category="success")
        return redirect(url_for('services_page'))
    if form.errors != {}: #If there are not errors from the validations
        for err_msg in form.errors.values():
          flash(f'There was an error with the application: {err_msg}', category='danger')

    return render_template('services.html', form=form)


@app.route("/about")
def about_page():
    return render_template('about.html')

@app.route("/FAQs")
def FAQs_page():
    return render_template('FAQs.html')