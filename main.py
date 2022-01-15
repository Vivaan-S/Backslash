print("  - Loading...")


from flask import Flask, render_template, redirect, request, abort, make_response
import markdown, logging, click, os, schedule, time, requests
from replit import db, web
from html import escape


db["feed"] = []

def cleardb():
  requests.get("https://backslash.am4.uk/clear?admincode="+os.environ["admincode"])
def warnings():
  print("- Remember: If you press the Ctrl+C or stop this process, it will clear the database.")

schedule.every(4).minutes.do(warnings)
schedule.every().sunday.at("23:59").do(cleardb)


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

@app.route('/clear')
def cleardatabase():
  if request.args["admincode"] == os.environ["admincode"]:
    db.clear()
    print("  - Database was cleared")
    return "success"
  print("  - Someone tried to clear the database, but failed")
  return "failed"


@app.route('/feed')
def feedpage():
  return render_template("feed.html", feed=db["feed"], markfunc=markdown.markdown, escapefunc=escape)

@app.route('/api/newpost', methods=["POST"])
def newpost():
  data = loads(request.data)
  #print(data)
  if not request.headers['X-Replit-User-Name']:
    abort(403)

  db["feed"].insert(0,
  {
    "author": request.headers['X-Replit-User-Name'],
    "content": data["content"],
    "likers": [request.headers['X-Replit-User-Name']]
  },
  )
  print("  - "+request.headers['X-Replit-User-Name']+": "+data["content"])
  return "success"

@app.route('/logout')
def logout():
  resp = make_response(redirect("/"))
  resp.set_cookie('REPL_AUTH', '', expires=1, domain=".backslash.theh4ck3r.repl.co")

  return resp


###################################


@app.errorhandler(404)
def four_o_four(e):
  if request.path in rickroll_urls:
    if request.headers['X-Replit-User-Name']:
      print("  - "+request.headers['X-Replit-User-Name']+" was rickrolled")
    else:
      print("  - Somebody was rickrolled")
    return redirect("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
  return "", 404

@app.errorhandler(403)
def four_o_three(e):
  return "", 403



###################################
###################################
###################################

os.system('clear')

print(
  """
  * Backslash is now running
  * Select console and press Ctrl+C/Cmd+C to stop
  * Messages will be logged below
  """
)

app.run(host='0.0.0.0', port=80)

