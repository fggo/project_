from flask import Flask
import subprocess

app = Flask(__name__)

@app.route('/get_price/<product_id>')
def get_price(product_id):
    """run command: scrapy crawl command with -o -a options
    the output.json is read and displayed on http://localhost:5000/<product_id>
    """
    spider_name = 'price'
    # calls 'scrapy' as a subprocess
    # 'naemall' is just an example of a seller (hardcode)
    # TODO implement without using hardcode; passing 'seller' as an argument
    subprocess.check_output(['scrapy', 'crawl', spider_name,
                             "-o", "output.json",
                             "-a", "seller=naemall",
                             "-a", "product_id=" + product_id])
    # read output.json
    with open("output.json") as items_file:
        return items_file.read()
