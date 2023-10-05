from flask import Flask, render_template, flash, redirect, render_template
from models import db, connect_db, Pet
from forms import AddPetForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'yurr'

connect_db(app)

@app.route('/')
def start():
    """SHOW ALL PETS"""
    pets = Pet.query.all()

    return render_template('home.html', pets = pets)

@app.route('/add', methods = ['GET', 'POST'])
def add_pet():
    """Render form to add pet and handle form"""
    form = AddPetForm()
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        available = form.available.data

        pet = Pet(name = name, species = species, photo_url = photo_url, age = age, notes = notes, available = available)
        db.session.add(pet)
        db.session.commit()
        flash('Pet added successfully!', 'success')
        return redirect('/')

    else:
        return render_template('add_pet.html', form = form)
    
@app.route('/<id>', methods = ['GET', 'POST'])
def edit_pet(id):
    """show pet details and show edit pet form
    also handle edit form"""
    pet = Pet.query.get_or_404(id)
    form = AddPetForm(obj=pet)
    
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        available = form.available.data

        pet.name = name
        pet.species = species
        pet.photo_url = photo_url
        pet.age = age
        pet.notes = notes
        pet.available = available

        db.session.add(pet)
        db.session.commit()
        flash('Pet edited successfully!', 'success')
        return redirect('/')
    else:
        return render_template('edit_pet.html', pet = pet, form = form)
