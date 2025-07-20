from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>NIN Validator</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: #f4f6f8;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }

        .container {
            background: #fff;
            padding: 30px;
            border-radius: 12px;
            box-shadow: 0 8px 16px rgba(0,0,0,0.1);
            text-align: center;
            width: 300px;
        }

        h1 {
            margin-bottom: 20px;
            font-size: 24px;
            color: #333;
        }

        input[type="text"] {
            padding: 10px;
            width: 100%;
            border: 1px solid #ccc;
            border-radius: 8px;
            margin-bottom: 15px;
            font-size: 16px;
        }

        input[type="submit"] {
            background-color: #4CAF50;
            color: white;
            border: none;
            padding: 10px 20px;
            border-radius: 8px;
            font-size: 16px;
            cursor: pointer;
            width: 100%;
        }

        input[type="submit"]:hover {
            background-color: #45a049;
        }

        .result {
            margin-top: 15px;
            font-weight: bold;
            color: #007bff;
        }

        .invalid {
            color: red;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>NIN Validator</h1>
        <form method="post">
            <input name="nin" placeholder="Enter 11-digit NIN" type="text" required />
            <input type="submit" value="Validate" />
        </form>
        {% if result %}
        <div class="result {{ 'invalid' if 'Invalid' in result else '' }}">{{ result }}</div>
        {% endif %}
    </div>
</body>
</html>
'''



@app.route("/", methods=["GET", "POST"])
def validate():
    result = ""
    if request.method == "POST":
        nin = request.form["nin"]
        if len(nin) == 11 and nin.isdigit():
            result = "VALID NIN"
        else:
            result = "INVALID NIN"
    return render_template_string(HTML,result=result)
app.run(debug=True)