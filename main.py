from flask import Flask, render_template, redirect, request
import markdown
app = Flask('app', static_folder="static")
from json import loads
feed = []

redirect_urls = {
  # Format:
  # "/blabbr" : "https://blabbr.xyz"
  # will redirect /blabbr to blabbr.xyz
}

rickroll_urls = [
  '/.env',
  '/.git',
  '/wp-admin',
  '/wp-login.php',
  '/composer.lock',
  '/yarn.lock',
  '/package-lock.json',
  '/xmlrpc.php',
  '/typo3',
  '/rickroll'
] # will rickroll people who follow (hacker and stuff)


@app.route('/')
def index():
  return render_template("index.html")

@app.route('/feed')
def feedpage():
  return render_template("feed.html", feed=feed, markfunc=markdown.markdown)

@app.route('/api/newpost', methods=["POST"])
def newpost():
  data = loads(request.data)
  #print(data)
  feed.insert(0,
  {
    "author": data["author"],
    "content": data["content"]
  },
  )
  return "success"

@app.errorhandler(404)
def four_o_four(e):
  if request.path in rickroll_urls:
    print("just redirected somebody to a rickroll LOL")
    return redirect("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
  return "", 404

app.run(host='0.0.0.0', port=80)
