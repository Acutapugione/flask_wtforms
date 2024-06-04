from app import app
from app.forms import SearchForm
from flask import flash, request, render_template, Request, redirect, url_for
from app.db import Search, Session, Base, engine
from flask_wtf import Form


Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)


@app.get("/")
def index():
    return render_template("base.html")


@app.get("/search")
def search_get():
    form = SearchForm(request.form)
    return render_template("search.html", form=form)


@app.post("/search")
def search_post():
    form = SearchForm(
        request.form,
    )
    form: Form
    if form.validate():
        with Session.begin() as session:
            search_data = Search()
            form.populate_obj(search_data)
            session.add(search_data)
        return redirect(url_for(index.__name__))
    print(f"{form.errors=}")
    return render_template("search.html", form=form)
