from app import app
from app.forms import SearchForm
from flask import request, render_template, Request
from dataclasses import dataclass
from flask_wtf import Form


@dataclass()
class SearchData:
    text: str = ""


@app.get("/search")
def search_get():
    form = SearchForm(request.form)
    return render_template("search.html", form=form)


@app.post("/search")
def search_post():
    form = SearchForm(request.form)
    form: Form
    search_data = SearchData()
    form.populate_obj(search_data)
    return render_template("search.html", form=form)
