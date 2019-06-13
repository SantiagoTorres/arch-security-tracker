from flask import render_template
from tracker import tracker

@tracker.route('/', methods=['GET'])
def security():
    return render_template('security.html')
