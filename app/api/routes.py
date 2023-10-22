from flask import Blueprint, request, jsonify, render_template
from helpers import token_required
from models import db, User, Vehicle, vehicle_schema, vehicles_schema
from forms import VehiclesForm, ColorTrimForm, ProfileButton, EditProfile
from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user

api = Blueprint('api',__name__, url_prefix='/api')

@api.route('/profile', methods = ['GET', 'POST'])
@login_required
def profile():
    form = ProfileButton()
    try:
        if request.method == 'POST' and form.validate_on_submit():
        
            return redirect(url_for('api.editprofile', id = current_user.id))
    except:
        raise Exception('Invalid form data: Please check your form')
    return render_template('profile.html', form=form)

@api.route('/profile/<id>', methods = ['GET', 'POST'])
@login_required
def editprofile(id):
    form = EditProfile()
    user = User.query.get(id) 
    try:
        if request.method == 'POST' and form.validate_on_submit():

            user.first_name = form.first_name.data
            user.last_name = form.last_name.data
            user.phone_number = form.phone_number.data
            user.address = form.address.data

            db.session.commit()

            flash(f'You have successfully created a vehicle trim')
            return redirect(url_for('api.profile'))
    except:
        raise Exception('Invalid form data: Please check your form')
    return render_template('editprofile.html', form=form)

@api.route('/vehicles', methods = ['GET', 'POST'])
def selectvehicle():
    form = VehiclesForm()
    try:
        if request.method == 'POST' and form.validate_on_submit():
            print(form.data)
            make = 'Tesla'
            if form.submitModel3.data:
                model = 'model3'
            elif form.submitModelS.data:
                model = 'models'
            elif form.submitModelX.data:
                model = 'modelx'
            elif form.submitModelY.data:
                model = 'modely'
            year = '2023'
            color = ''
            trim = ''

            vehicle = Vehicle(make, model, year, color, trim)

            db.session.add(vehicle)
            db.session.commit()

            return redirect(url_for('api.selectcolortrim', id = vehicle.id))
    except:
        raise Exception('Invalid form data: Please check your form')
    return render_template('vehicles.html', form=form)

@api.route('/vehicles/<id>', methods = ['GET', 'POST'])
def selectcolortrim(id):
    form = ColorTrimForm()
    vehicle = Vehicle.query.get(id) 

    try:
        if request.method == 'POST' and form.validate_on_submit():
            color = form.color.data
            trim = form.trim.data

            vehicle.color = color
            vehicle.trim = trim

            db.session.commit()

            flash(f'You have successfully created a vehicle trim {trim}')
            return redirect(url_for('site.home'))
    except:
        raise Exception('Invalid form data: Please check your form')
    return render_template(f'{vehicle.model}.html', form=form)


# @api.route('/vehicles', methods = ['POST'])
# @token_required
# def create_vehicle(current_user_token):
#     make = request.json['make']
#     model = request.json['model']
#     year = request.json['year']
#     color = request.json['color']
#     trim = request.json['trim']
#     user_token = current_user_token.token

#     print(f'BIG TESTER: {current_user_token.token}')

#     vehicle = Vehicle(make, model, year, color, trim, user_token = user_token)

#     db.session.add(vehicle)
#     db.session.commit()

#     response = vehicle_schema.dump(vehicle)
#     return jsonify(response)

# @api.route('/vehicles', methods = ['GET'])
# @token_required
# def get_vehicle(current_user_token):
#     a_user = current_user_token.token
#     vehicles = Vehicle.query.filter_by(user_token = a_user).all()
#     response = vehicles_schema.dump(vehicles)
#     return jsonify(response)

@api.route('/vehicles/<id>', methods = ['GET'])
@token_required
def get_vehicle_two(current_user_token, id):
    fan = current_user_token.token
    if fan == current_user_token.token:
        vehicle = Vehicle.query.get(id)
        response = vehicle_schema.dump(vehicle)
        return jsonify(response)
    else:
        return jsonify({"message": "Valid Token Required"}),401

# UPDATE endpoint
@api.route('/vehicles/<id>', methods = ['POST','PUT'])
@token_required
def update_vehicle(current_user_token,id):
    vehicle = Vehicle.query.get(id) 
    vehicle.make = request.json['make']
    vehicle.model = request.json['model']
    vehicle.year = request.json['year']
    vehicle.color = request.json['color']
    vehicle.trim = request.json['trim']
    vehicle.user_token = current_user_token.token

    db.session.commit()
    response = vehicle_schema.dump(vehicle)
    return jsonify(response)

# DELETE car ENDPOINT
@api.route('/vehicles/<id>', methods = ['DELETE'])
@token_required
def delete_vehicle(current_user_token, id):
    vehicle = Vehicle.query.get(id)
    db.session.delete(vehicle)
    db.session.commit()
    response = vehicle_schema.dump(vehicle)
    return jsonify(response)

################################################################

# @api.route('/contacts', methods = ['POST'])
# @token_required
# def create_contact(current_user_token):
#     name = request.json['name']
#     email = request.json['email']
#     phone_number = request.json['phone_number']
#     address = request.json['address']
#     user_token = current_user_token.token

#     print(f'BIG TESTER: {current_user_token.token}')

#     contact = Contact(name, email, phone_number, address, user_token = user_token )

#     db.session.add(contact)
#     db.session.commit()

#     response = contact_schema.dump(contact)
#     return jsonify(response)

# @api.route('/contacts', methods = ['GET'])
# @token_required
# def get_contact(current_user_token):
#     a_user = current_user_token.token
#     contacts = Contact.query.filter_by(user_token = a_user).all()
#     response = contacts_schema.dump(contacts)
#     return jsonify(response)

# @api.route('/contacts/<id>', methods = ['GET'])
# @token_required
# def get_contact_two(current_user_token, id):
#     fan = current_user_token.token
#     if fan == current_user_token.token:
#         contact = Contact.query.get(id)
#         response = contact_schema.dump(contact)
#         return jsonify(response)
#     else:
#         return jsonify({"message": "Valid Token Required"}),401

# # UPDATE endpoint
# @api.route('/contacts/<id>', methods = ['POST','PUT'])
# @token_required
# def update_contact(current_user_token,id):
#     contact = Contact.query.get(id) 
#     contact.name = request.json['name']
#     contact.email = request.json['email']
#     contact.phone_number = request.json['phone_number']
#     contact.address = request.json['address']
#     contact.user_token = current_user_token.token

#     db.session.commit()
#     response = contact_schema.dump(contact)
#     return jsonify(response)


# # DELETE car ENDPOINT
# @api.route('/contacts/<id>', methods = ['DELETE'])
# @token_required
# def delete_contact(current_user_token, id):
#     contact = Contact.query.get(id)
#     db.session.delete(contact)
#     db.session.commit()
#     response = contact_schema.dump(contact)
#     return jsonify(response)