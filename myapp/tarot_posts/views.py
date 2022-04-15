from flask import render_template, url_for, flash, request, redirect, Blueprint, abort
from flask_login import current_user, login_required
from myapp import db 
from myapp.models import TarotPost
from myapp.tarot_posts.forms import TarotPostForm

tarot_posts = Blueprint('tarot_posts', __name__)

@tarot_posts.route('/create', methods=['GET', 'POST'])
@login_required
def create_post():
    form = TarotPostForm()
    if form.validate_on_submit():
        tarot_post = TarotPost(
        title=form.title.data, 
        spread=form.spread.data,
        card1=form.card1.data,
        card2=form.card2.data,
        card3=form.card3.data,     
        reflection=form.reflection.data,        
        user_id=current_user.id)
        db.session.add(tarot_post)
        db.session.commit()
        flash('Tarot Post Created')
        print('Tarot post was created')
        return redirect(url_for('core.index'))
    return render_template('create_post.html', form=form)


@tarot_posts.route('/<int:tarot_post_id>')
def tarot_post(tarot_post_id):
    tarot_post = TarotPost.query.get_or_404(tarot_post_id) 
    return render_template('tarot_post.html', title=tarot_post.title, date=tarot_post.date, post=tarot_post)

@tarot_posts.route('/<int:tarot_post_id>/update',methods=['GET','POST'])
@login_required
def update(tarot_post_id):
    tarot_post = TarotPost.query.get_or_404(tarot_post_id)

    if tarot_post.diviner != current_user:
        abort(403)

    form = TarotPostForm()

    if form.validate_on_submit():
        tarot_post.title = form.title.data
        tarot_post.spread=form.spread.data
        tarot_post.card1=form.card1.data
        tarot_post.card2=form.card2.data
        tarot_post.card3=form.card3.data    
        tarot_post.reflection=form.reflection.data
        db.session.commit()
        flash('Tarot Post Updated')
        return redirect(url_for('tarot_posts.tarot_post',tarot_post_id=tarot_post.id))

    elif request.method == 'GET':
        form.title.data = tarot_post.title
        form.spread.data = tarot_post.spread
        form.card1.data = tarot_post.card1 
        form.card2.data = tarot_post.card2
        form.card3.data = tarot_post.card3  
        form.reflection.data = tarot_post.reflection 
    return render_template('create_post.html',title='Updating',form=form)

@tarot_posts.route('/<int:tarot_post_id>/delete',methods=['GET','POST'])
@login_required
def delete_post(tarot_post_id):

    tarot_post = TarotPost.query.get_or_404(tarot_post_id)
    if tarot_post.diviner != current_user:
        abort(403)

    db.session.delete(tarot_post)
    db.session.commit()
    flash('Tarot Post Deleted')
    return redirect(url_for('core.index'))