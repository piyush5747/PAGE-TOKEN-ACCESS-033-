from flask import Flask, request, render_template_string
import requests

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="hi">
<head>
    <meta charset="UTF-8">
    <title>PIYUSH RDX  Token Extractor</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body {
            background: url('https://i.ibb.co/27wt8NsD/received-531987746237628.jpg');
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
            font-family: 'Segoe UI', sans-serif;
        }
        .main-box {
            max-width: 850px;
            margin: 60px auto;
            background: rgba(0, 0, 0, 0.75);
            color: white;
            padding: 40px 30px;
            border-radius: 20px;
            box-shadow: 0 15px 30px rgba(0,0,0,0.4);
        }
        .header-box {
            background: #00c3ff;
            padding: 15px;
            text-align: center;
            font-size: 22px;
            font-weight: bold;
            border-radius: 10px;
            color: white;
            margin-bottom: 30px;
            box-shadow: 0 0 10px #00c3ff;
        }
        .form-control {
            border-radius: 12px;
            padding: 18px;
            font-size: 17px;
            margin-bottom: 20px;
        }
        .submit-button {
            width: 100%;
            padding: 15px;
            font-size: 18px;
            border-radius: 12px;
            background: linear-gradient(45deg, #00c851, #007e33);
            color: white;
            border: none;
            font-weight: bold;
            transition: 0.3s ease-in-out;
        }
        .submit-button:hover {
            background: linear-gradient(45deg, #007e33, #00c851);
            transform: scale(1.03);
        }
        .results-wrapper {
            margin-top: 30px;
        }
        .result-card {
            background: white;
            color: black;
            border-radius: 15px;
            padding: 20px;
            margin-bottom: 20px;
            box-shadow: 0 10px 20px rgba(0,0,0,0.2);
        }
        .result-card h5 {
            color: #007e33;
            font-weight: bold;
        }
        .token-box {
            background: #f8f9fa;
            padding: 10px;
            border-radius: 8px;
            font-size: 14px;
            word-break: break-all;
            margin-top: 10px;
        }
    </style>
</head>
<body>

    <div class="main-box">
        <!-- Title Box -->
        <div class="header-box">PIYUSH RDX PAGE TOKEN EXTRACTOR</div>

        <!-- Token Form -->
        <form method="POST">
            <input type="text" name="token" class="form-control" placeholder="यहाँ Facebook टोकन डालें" required>
            <button type="submit" class="submit-button">Submit</button>
        </form>

        <!-- Error Box -->
        {% if error %}
            <div class="alert alert-danger text-center mt-3">{{ error }}</div>
        {% endif %}

        <!-- Results -->
        {% if pages %}
            <div class="results-wrapper">
                {% for page in pages %}
                    <div class="result-card">
                        <h5>{{ page.name }}</h5>
                        <p><strong>UID:</strong> {{ page.id }}</p>
                        <div class="token-box"><strong>Token:</strong><br>{{ page.access_token }}</div>
                    </div>
                {% endfor %}
            </div>
        {% endif %}
    </div>

</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    pages = []
    error = None
    if request.method == "POST":
        user_token = request.form.get("token")
        url = f"https://graph.facebook.com/v18.0/me/accounts?access_token={user_token}"
        try:
            response = requests.get(url)
            data = response.json()

            if "error" in data:
                error = data["error"]["message"]
            else:
                pages = data.get("data", [])
        except Exception as e:
            error = "समस्या हुई: " + str(e)

    return render_template_string(HTML_TEMPLATE, pages=pages, error=error)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=21450)