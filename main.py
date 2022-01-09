from flask import Flask, render_template, redirect, request, abort
import markdown, logging, click



###################################
###################################
###################################



def secho(text, file = None, nl = None, err = None, color = None, ** styles):
   pass
def echo(text, file = None, nl = None, err = None, color = None, ** styles):
   pass

click.echo = echo
click.secho = secho

logging.getLogger('werkzeug').setLevel(logging.ERROR)
app = Flask('Backslash', static_folder="static")
from json import loads
feed = []



###################################
###################################
###################################



redirect_urls = {
  # Format:
  # "/blabbr" : "https://blabbr.xyz",
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



###################################
###################################
###################################




@app.route('/')
def index():
  return render_template("index.html",
		user_id=request.headers['X-Replit-User-Id'],
		user_name=request.headers['X-Replit-User-Name'],
		user_roles=request.headers['X-Replit-User-Roles']
  )

@app.route('/login')
def loginpage():
  if request.headers['X-Replit-User-Name']:
    print("  - "+request.headers['X-Replit-User-Name']+" logged in")
    return redirect("/feed")
  return render_template("login.html",
		user_id=request.headers['X-Replit-User-Id'],
		user_name=request.headers['X-Replit-User-Name'],
		user_roles=request.headers['X-Replit-User-Roles']
  )

@app.route('/feed')
def feedpage():
  return render_template("feed.html", feed=feed, markfunc=markdown.markdown)

@app.route('/api/newpost', methods=["POST"])
def newpost():
  data = loads(request.data)
  #print(data)
  if not request.headers['X-Replit-User-Name']:
    abort(403)

  feed.insert(0,
  {
    "author": request.headers['X-Replit-User-Name'],
    "content": data["content"]
  },
  )
  print("  - "+data["author"]+": "+data["content"])
  return "success"



###################################


@app.errorhandler(404)
def four_o_four(e):
  if request.path in rickroll_urls:
    print("  - Somebody was rickrolled")
    return redirect("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
  return "", 404

@app.errorhandler(403)
def four_o_three(e):
  return "", 403



###################################
###################################
###################################



print(
  """
  * Backslash is now running
  * Select console and press Ctrl+C/Cmd+C to stop
  * Messages will be logged below
  """
)

app.run(host='0.0.0.0', port=80)

