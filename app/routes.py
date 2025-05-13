from flask import render_template, redirect, url_for, flash, request, current_app
from flask_login import login_user, logout_user, login_required, current_user
from .models import db, User, Recipe, Comment
from .forms import LoginForm, RegisterForm, RecipeForm, ProfileForm
from werkzeug.security import generate_password_hash, check_password_hash
from app import myapp_obj
from datetime import datetime
from werkzeug.utils import secure_filename
import os

# Login Page
@myapp_obj.route('/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for('home'))
        else:
            flash('Invalid username or password')
    return render_template('login.html', form=form)

# User Registration
@myapp_obj.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        existing_user = User.query.filter_by(username=form.username.data).first()
        if existing_user:
            flash('Username already taken. Please choose a different one.')
            return render_template('register.html', form=form)

        hashed_pw = generate_password_hash(form.password.data, method='scrypt')
        new_user = User(username=form.username.data, password=hashed_pw)
        db.session.add(new_user)
        db.session.commit()
        flash('Registration successful! You can now log in.')
        return redirect(url_for('login'))

    return render_template('register.html', form=form)
	
# Displays Recipes
@myapp_obj.route('/home')
@login_required
def home():
    search_query = request.args.get('search', '')
    if search_query:
        recipes = Recipe.query.filter(Recipe.title.ilike(f'%{search_query}%')).all()
    else:
        recipes = Recipe.query.all()
    return render_template('home.html', recipes=recipes)

# Logout User	
@myapp_obj.route('/logout')
@login_required
def logout():
	logout_user()
	return redirect(url_for('login'))

# Lists Recipes
@myapp_obj.route("/recipes")
def list_recipes():
    search_query = request.args.get('search', '')
    if search_query:
        recipes = Recipe.query.filter(Recipe.title.ilike(f'%{search_query}%')).all()
    else:
        recipes = Recipe.query.all()
    return render_template('recipes.html', recipes=recipes)

# Add New Recipe
@myapp_obj.route("/recipe/new", methods=['GET', 'POST'])
@login_required
def add_recipe():
    form = RecipeForm()
    if form.validate_on_submit():
        image_filename = None
        if form.image.data:
            filename = secure_filename(form.image.data.filename)
            image_path = os.path.join(current_app.root_path, 'static/uploads', filename)
            form.image.data.save(image_path),
            image_filename = filename

        
        recipe = Recipe(
            title=form.title.data,
            description=form.description.data,
            ingredients=form.ingredients.data,
            instructions=form.instructions.data,
            created=datetime.utcnow(),
            image_filename=image_filename,
            user=current_user
        )
        db.session.add(recipe)
        db.session.commit()
        flash('Recipe added successfully!')
    return render_template("add_recipe.html", form=RecipeForm())

@myapp_obj.route("/recipe/<int:recipe_id>")
def view_recipe(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)
    return render_template("recipe_detail.html", recipe=recipe)

@myapp_obj.route("/recipe/<int:recipe_id>/delete")
@login_required
def delete_recipe(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)
    db.session.delete(recipe)
    db.session.commit()
    flash('Recipe deleted.')
    return redirect(url_for('list_recipes'))

@myapp_obj.route('/edit_recipe/<int:recipe_id>', methods=['POST'])
def edit_recipe(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)
    recipe.title = request.form['title']
    recipe.description = request.form['description']
    recipe.ingredients = request.form['ingredients']
    recipe.instructions = request.form['instructions']
    db.session.commit()
    return redirect(url_for('view_recipe', recipe_id=recipe_id))

@myapp_obj.route('/rate/<int:recipe_id>', methods=['POST'])
@login_required
def rate_recipe(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)
    rating = int(request.form['rating'])
    recipe.rating = rating
    db.session.commit()
    flash("Rating submitted!")
    return redirect(url_for('view_recipe', recipe_id=recipe_id))

@myapp_obj.route('/recipe/<int:recipe_id>/comment', methods=['POST'])
def comment_recipe(recipe_id):
    content = request.form['content']
    comment = Comment(recipe_id=recipe_id, content=content, user_id=current_user.id)
    db.session.add(comment)
    db.session.commit()
    return redirect(url_for('view_recipe', recipe_id=recipe_id))

@myapp_obj.route("/user/<int:user_id>")
def view_user(user_id):
    user = User.query.get_or_404(user_id)
    recipes = Recipe.query.filter_by(user_id=user.id).all()
    return render_template("user_recipes.html", user=user, recipes=recipes)

@myapp_obj.route('/user/<int:user_id>/edit', methods=['GET','POST'])
@login_required
def edit_profile(user_id):
	if current_user.id != user_id:
		abort(403)
	form = ProfileForm(obj=current_user)
	if form.validate_on_submit():
		existing = User.query.filter_by(username=form.username.data).first()
		if existing and existing.id != current_user.id:
			flash('That username is already taken.', 'danger')
		else:
			current_user.username = form.username.data
			db.session.commit()
			flash('Profile updated successfully!', 'success')
			return redirect(url_for('view_user', user_id=user_id))
	return render_template('edit_profile.html', form=form, user_id=user_id)
