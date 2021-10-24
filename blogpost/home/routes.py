from flask import  render_template, request, Blueprint, redirect, url_for
from forms import CreateUrlForm
from blogpost.Scrapping import GetImage
from urllib.parse import urlparse


home = Blueprint('home', __name__)
scrap = GetImage()

@home.route("/", methods=["GET", "POST"])
def homepage():

    form = CreateUrlForm()
    if form.validate_on_submit() :

        url = form.product_url.data
        url_netloc = urlparse(url).netloc
        print(url_netloc)

        if url_netloc == "www.ebay.com":
            scrap.data_list = []
            scrap.getEbay(url)
            return redirect(url_for('home.productpage', url=url))

        if url_netloc == "www.amazon.com":
            scrap.data_list = []
            scrap.getAmazon(url)
            return redirect(url_for('home.productpage', url=url))

        else:
            return render_template("erorrrrrr.html")


    return render_template('index.html', form=form)

@home.route("/product/<path:url>", methods=['POST', 'GET'])
def productpage(url):
    print(scrap.data_list)
    if len(scrap.data_list) == 0 :
        scrap.data_list = scrap.notfound

    return render_template('show2.html', url=url, data_list=scrap.data_list)






