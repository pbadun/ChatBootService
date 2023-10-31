from flask import Flask, request, render_template
import g4f


def ask_gpt(message: str) -> str:
    response = g4f.ChatCompletion.create(
        model=g4f.models.gpt_35_turbo_16k,
        messages=[{"role": "user", "content": message}]
    )
    return response


app = Flask(__name__)


@app.route('/')
def homePage():
    return render_template('index.html')


@app.route('/msg', methods=['POST'])
def page():
    msg = request.form['msg']
    print(request.form)

    try:
        if msg != "":
            resp = ask_gpt(msg)
        else:
            resp = "Напишите свой вопрос.";
    except:
        resp += 'Ошибка запроса'
    return resp


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
