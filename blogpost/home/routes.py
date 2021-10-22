from flask import render_template, request, Blueprint, redirect, url_for
from forms import CreateUrlForm
from blogpost.Scrapping import GetImage
from urllib.parse import urlparse

home = Blueprint('home', __name__)



@home.route("/", methods=["GET", "POST"])
def homepage():
    form = CreateUrlForm()
    if form.validate_on_submit() :
        url = form.product_url.data
        return redirect(url_for('home.productpage', url=url))
    return render_template('index.html', form=form)

@home.route("/product/<path:url>")
def productpage(url):
    scrap = GetImage()
    url_netloc = urlparse(url).netloc
    print(url_netloc)


    if url_netloc == "www.ebay.com":
        scrap.getEbay(url)

    if url_netloc == "www.amazon.com":
        scrap.getAmazon(url)

    return render_template('showproducts.html', url=url)



