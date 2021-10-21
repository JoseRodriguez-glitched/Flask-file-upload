from flask import *
from werkzeug.utils import secure_filename

class App():
    def __init__(self):
        self.app = Flask(__name__)
    def run(self):
        @self.app.route("/")
        def index():
            return render_template("upload.html")
        @self.app.route("/uploader",methods=["GET","POST"])
        def uploader():
            if request.method == "POST":
                f = request.files["file"]
                f.save(secure_filename(f.filename))
                return "Archivo subido exitosamente."
        self.app.run(debug=True)

if __name__=="__main__":
    app = App()
    app.run()
