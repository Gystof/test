from flask import Blueprint, render_template, redirect, abort, url_for
from common.services import DatabaseStorate as Storage
from .forms import CreateUpdate

clients = Blueprint(
    'clients',
    __name__,
    template_folder='../../views/modules/clients'
)


@clients.route('/', methods=['GET'])
def index():
    items = Storage.clients.all()
    return render_template('index.html', title=' Клиенты', items=items)


@clients.route('/add', methods=['GET', 'POST'])
def create():
    form = CreateUpdate(Storage)
    if form.save():
        return redirect(url_for('backend.clients.index'))
    return render_template('form.html', title='Добавление клиента', form=form)


@clients.route('/edit/<int:id>', methods=['GET', 'POST'])
def update(id):
    item = Storage.clients.find_by_id(id)
    if not item:
        abort(404, message='Запись с данным ID не найдена')
    form = CreateUpdate(Storage, data=item.to_dict)
    if form.save():
        return redirect(url_for('backend.clients.index'))
    return render_template('form.html', title=' Изменение данных коиента', form=form)


@clients.route('/delete/<int:id>', methods=['GET'])
def delete(id):
    item = Storage.clients.find_by_id(id)
    if not item:
        abort(404, message='Запись с данным ID не найдена')
    Storage.clients.delete(item)
    return redirect(url_for('backend.clients.index'))

