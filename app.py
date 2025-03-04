from flask import Flask, render_template, request, redirect, url_for, flash
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = "supersecretkey"

# Dummy data for demonstration
users = []
vehicles = [
    {"id": 1, "name": "Tata Ace", "image": "tata-ace.jpg", "price": 50, "description": "Compact and efficient mini truck."},
    {"id": 2, "name": "Toyota Hilux", "image": "hilux.jpg", "price": 70, "description": "Powerful and reliable pickup truck."},
]
messages = []
UPLOAD_FOLDER = "static/uploads"
ALLOWED_EXTENSIONS = {"txt", "pdf", "png", "jpg", "jpeg", "gif"}

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Ensure upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/")
def home():
    return render_template("index.html", vehicles=vehicles)

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]
        users.append({"name": name, "email": email, "password": password})
        flash("Registration successful! Please login.")
        return redirect(url_for("login"))
    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        user = next((user for user in users if user["email"] == email and user["password"] == password), None)
        if user:
            return redirect(url_for("dashboard"))
        else:
            flash("Invalid credentials. Please try again.")
    return render_template("login.html")

@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    if request.method == "POST":
        if "file" in request.files:
            file = request.files["file"]
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
                flash("File uploaded successfully!")
        elif "message" in request.form:
            message = request.form["message"]
            messages.append({"user": "Customer", "message": message})
            flash("Message sent to admin!")
    return render_template("dashboard.html", messages=messages)

@app.route("/browse")
def browse():
    return render_template("vehicle_listings.html", vehicles=vehicles)

@app.route("/vehicle/<int:vehicle_id>")
def vehicle(vehicle_id):
    vehicle = next((v for v in vehicles if v["id"] == vehicle_id), None)
    if vehicle:
        return render_template(f"vehicle_{vehicle['name'].lower().replace(' ', '_')}.html", vehicle=vehicle)
    else:
        return "Vehicle not found.", 404

@app.route("/admin")
def admin():
    return render_template("admin_panel.html", messages=messages)

@app.route("/support")
def support():
    return render_template("support.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/logout")
def logout():
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)