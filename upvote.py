from flask import Flask, render_template, request

app = Flask(__name__)

music = [
    {'id':'0', 'name':'Season of Memories', 'num':0},
    {'id':'1', 'name':'ICONIK', 'num':0},
    {'id':'2', 'name':'episode Solo', 'num':0},
    {'id':'3', 'name':'My Starway', 'num':0}
]

@app.route('/index')
def index():
    return render_template('index.html', music=music)

@app.route('/vote')
def vote():
    id = int(request.args.get('id'))
    print(f"使用者想要為「{music[id]['name']}」點贊")
    music[id]['num'] += 1

    return render_template('index.html', music=music)

app.run()