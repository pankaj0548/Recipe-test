from app.db.models import Recipe
from flask import Blueprint, render_template, request, redirect, url_for, flash, send_from_directory
from flask_login import login_required,current_user
from werkzeug.utils import secure_filename
from uuid import uuid4
import uuid
from dotenv import load_dotenv
import os

bp = Blueprint("recipe", __name__)
temp_dir = "recipe/"
load_dotenv()

UPLOAD_FOLDER = os.getenv("UPLOAD_FOLDER")


@bp.route('/')
@login_required
def index():
    recipes = Recipe.query.order_by(Recipe.id.desc()).paginate(per_page=9)
    return render_template(temp_dir + 'index.html', recipes=recipes)

@bp.route('/recipe/<recipe_id>')
def recipe(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)
    return render_template(temp_dir + 'recipe.html', recipe=recipe)

@bp.route('/create_recipe', methods=['GET', 'POST'])
@login_required
def create_recipe():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        ingredients = request.form['ingredients']
        instructions = request.form['instructions']

        image_file = request.files['image']
        if image_file.filename != '':
            filename = secure_filename(image_file.filename)
            filepath = UPLOAD_FOLDER + "/" + filename
            image_file.save(filepath)
            recipe.image = filename

        new_recipe = Recipe(
            id = str(uuid4()),
            image = filename,
            title=title, 
            description=description, 
            ingredients=ingredients, 
            instructions=instructions, 
            created_by=current_user.id
        )
        new_recipe.save()
        flash('Recipe created successfully!', 'success')
        return redirect(url_for('recipe.index'))
    return render_template(temp_dir + 'create_recipe.html')

@bp.route('/edit_recipe/<recipe_id>', methods=['GET', 'POST'])
@login_required
def edit_recipe(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)
    if recipe.created_by != current_user.id:
        flash('You are not authorized to edit this recipe!', 'danger')
        return redirect(url_for('recipe.index'))
    if request.method == 'POST':
        recipe.id = recipe_id
        recipe.title = request.form['title']
        recipe.description = request.form['description']
        recipe.ingredients = request.form['ingredients']
        recipe.instructions = request.form['instructions']
        
        image_file = request.files['image']
        if image_file.filename != '':
            # Generate a unique filename to prevent collisions
            filename = secure_filename(image_file.filename)
            filepath = UPLOAD_FOLDER + "/" + filename
            image_file.save(filepath)
            recipe.image = filename
        
        recipe.update()
        flash('Recipe updated successfully!', 'success')
        return redirect(url_for('recipe.recipe', recipe_id=recipe.id))
    return render_template(temp_dir + 'edit_recipe.html', recipe=recipe)

@bp.route('/delete_recipe/<recipe_id>', methods=['GET','POST'])
@login_required
def delete_recipe(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)
    if recipe.created_by != current_user.id:
        flash('You are not authorized to delete this recipe!', 'danger')
        return redirect(url_for('recipe.index'))
    recipe.delete()
    flash('Recipe deleted successfully!', 'success')
    return redirect(url_for('recipe.index'))

@bp.route('/load_recipes', methods=['POST'])
def load_recipes():
    error = None
    recipe_val = None
    
    if request.method == 'POST':
        value = request.form.get('search')
        
        if not value:  # If search value is empty
            recipe_val = Recipe.query.all()
        else:
            recipe_val = Recipe.query.filter(Recipe.title.like(f"%{value}%") | Recipe.ingredients.like(f"%{value}%")).all()
            
            if not recipe_val:
                error = "no_blog"
    else:
        recipe_val = Recipe.query.all()
    
    return render_template(temp_dir + 'load_recipe.html', recipe_val=recipe_val, error=error)
