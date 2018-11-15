from flask import Flask,g
from db import db
__all__ = ['app']
app = Flask(__name__)
def get_conn():
    if not hasattr(g,'redis'):
        g.redis = db()
    return g.redis
@app.route('/')
def index():
    return ("<span>My ProxiePool</span>")
@app.route('/count')
def proxie_count():
    conn = get_conn()
    count = conn.count_proxie()
    return ("<h2>当前拥有{}个代理<h2>".format(count))
@app.route('/get')
def get_proxie():
    conn = get_conn()
    return conn.get_proxie()
@app.route('/random')
def random_proxie():
    conn = get_conn()
    count = conn.count_proxie()
    return str(conn.range_proxie(count-30,count))
if __name__ == "__main__":
    app.run()
