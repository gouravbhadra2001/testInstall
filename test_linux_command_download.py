from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/install', methods=['POST'])
def install_ollama():
    try:
        # Run the command to install Ollama
        command = "curl -fsSL https://ollama.com/install.sh | sh"
        subprocess.run(command, shell=True, check=True)
        return jsonify({"message": "Ollama installation script executed successfully."}), 200
    except subprocess.CalledProcessError as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
