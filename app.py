from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Flask Web Server</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                text-align: center;
                background-color: #f4f4f4;
                padding: 50px;
            }
            .container {
                background: white;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
                display: inline-block;
            }
            h1 {
                color: #007BFF;
            }
            p {
                font-size: 18px;
                color: #333;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Hello, Flask Web Server!</h1>
            <p>Made by <strong>Bhavya Rawat</strong></p>
            <p>3 Assessments Done ✅</p>
               <p>Some changes made here</p>
        </div>
    </body>
    </html>
    """
    return render_template_string(html_content)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
