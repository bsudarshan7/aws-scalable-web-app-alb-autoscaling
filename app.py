from flask import Flask
import socket

app = Flask(__name__)

products = [
    {"id": 1, "name": "Laptop", "price": 50000},
    {"id": 2, "name": "Headphones", "price": 2000},
    {"id": 3, "name": "Keyboard", "price": 1500},
    {"id": 4, "name": "Smartphone", "price": 25000}
]

def server_info():
    return socket.gethostname()

def page_template(content):
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>CloudMart Store</title>
        <style>
            body {{ font-family: Arial, sans-serif; background: #f4f6f9; margin: 0; padding: 0; }}
            .navbar {{ background: #232f3e; color: white; padding: 15px 30px; font-size: 24px; font-weight: bold; }}
            .container {{ width: 80%; margin: 30px auto; }}
            .card {{ background: white; padding: 20px; margin-bottom: 15px; border-radius: 10px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); }}
            a {{ text-decoration: none; color: #0073bb; font-weight: bold; }}
            a:hover {{ color: #ff9900; }}
            .btn {{ display: inline-block; padding: 10px 15px; background: #ff9900; color: #ffffff; border-radius: 5px; }}
            .server {{ margin-top: 30px; padding: 12px; background: #232f3e; color: white; border-radius: 8px; }}
            .price {{ color: green; font-size: 18px; font-weight: bold; }}
        </style>
    </head>
    <body>
        <div class="navbar">
            ☁️ CloudMart Store
        </div>
        <div class="container">
            {content}
            <div class="server">
                Server: {server_info()}
            </div>
        </div>
    </body>
    </html>
    """

@app.route("/")
def home():
    content = "<h2>Featured Products</h2>"
    for p in products:
        content += f"""
        <div class="card">
            <h3>{p['name']}</h3>
            <p class="price">₹{p['price']}</p>
            <a href="/product/{p['id']}">View Product</a>
        </div>
        """
    content += """
    <p>
        <a class="btn" href="/cart">Go To Cart</a>
    </p>
    """
    return page_template(content)

# FIXED: Corrected the route parameter syntax
@app.route("/product/<int:pid>")
def product(pid):
    for p in products:
        if p["id"] == pid:
            content = f"""
            <div class="card">
                <h2>{p['name']}</h2>
                <p class="price">₹{p['price']}</p>
                <p>High quality product available on CloudMart.</p>
                <a class="btn" href="/">Back To Store</a>
            </div>
            """
            return page_template(content)
    return page_template("<h2>Product Not Found</h2>")

@app.route("/cart")
def cart():
    content = """
    <div class="card">
        <h2>Shopping Cart</h2>
        <p>No items added yet.</p>
        <a class="btn" href="/">Continue Shopping</a>
    </div>
    """
    return page_template(content)

@app.route("/health")
def health():
    return "healthy"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
