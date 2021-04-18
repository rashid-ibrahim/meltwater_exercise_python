
import os

from flask import Flask, abort, request, render_template, send_from_directory, current_app

from controllers import redactor, FileOperations

app = Flask(__name__, template_folder='templates')
app.config.from_object('config.Config')

FileOps = None


@app.before_first_request
def load_file_ops():
    global FileOps
    FileOps = FileOperations.FileOperations()


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template("index.html")
    elif request.method == 'POST':
        inFile = request.files['secretFile']
        if inFile.filename == '':
            abort(404, 'No File provided')

        inFile = inFile.read().decode('UTF-8')

        words = request.form['sensitiveWords']
        if words == '':
            abort(404, 'No words provided to redact.')

        redactedText = redactor.redact(words, inFile)
        FileOps.save_redacted(redactedText)

        return render_template("results.html", original=inFile, redacted=redactedText)


@app.route('/download-file', methods=['GET'])
def download_file():
    redacted_file_directory = os.path.join(current_app.root_path, app.config['FILES_DIRECTORY'])
    return send_from_directory(directory=redacted_file_directory, filename=FileOps.out_file)


if __name__ == '__main__':
    app.run(port=8080)
