from flask import Flask, send_from_directory

app = Flask(__name__)

# Servir el archivo index.html cuando se acceda a la raíz
@app.route('/')
def serve_index():
    return send_from_directory('docs', 'index.html')

# Ruta general para servir cualquier archivo dentro de docs como si estuviera en la raíz
@app.route('/<path:filename>')
def serve_file(filename):
    return send_from_directory('docs', filename)


if __name__ == '__main__':
    app.run(debug=True, host='192.168.15.50', port=5000)
