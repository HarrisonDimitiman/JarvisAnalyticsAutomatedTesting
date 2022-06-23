from flask import Flask, render_template, url_for, request
from controller.figuresmatchingdriver import selenium


app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/openChromeDriver', methods=['POST', 'GET'])
def openChromeDriver():
    modules = request.form.getlist('modules[]')
    metrics = request.form.getlist('metrics[]')
    thisisme = selenium.login(modules, metrics)
    print(thisisme)
    return render_template('/pages/calendar/apptcalendar.html') 





































# Start Of Calendar Routes
@app.route('/apptCalendar')
def apptCalendar():
    return render_template('/pages/calendar/apptcalendar.html')

@app.route('/apptDetails')
def apptDetails():
    return render_template('/pages/calendar/apptDetails.html')
# End Of Calendar Routes

# Start Of Dashboard Routes
@app.route('/dashresult')
def dashresult():
    return render_template('/pages/dashboard/dashresult.html')

@app.route('/dashmetric')
def dashmetric():
    return render_template('/pages/dashboard/dashmetric.html')
# End Of Dashboard Routes

# Start Of EOD Routes
@app.route('/eod')
def eod():
    return render_template('/pages/eod/eod.html')
# End Of EOD Routes

# Start Of Front Office Routes
@app.route('/foschedule')
def foschedule():
    return render_template('/pages/frontoffice/foschedule.html')

@app.route('/fotask')
def fotask():
    return render_template('/pages/frontoffice/fotask.html')

@app.route('/focollection')
def focollection():
    return render_template('/pages/frontoffice/focollection.html')

@app.route('/fokpis')
def fokpis():
    return render_template('/pages/frontoffice/fokpis.html')

@app.route('/foperformance')
def foperformance():
    return render_template('/pages/frontoffice/foperformance.html')
# End Of EOD Routes

# Start Of Morning Huddle Routes
@app.route('/morninghuddle')
def morninghuddle():
    return render_template('/pages/morninghuddle/morninghuddle.html')
# End Of Morning Huddle Routes

# Start Of Patient Portal Routes
@app.route('/pppatients')
def pppatients():
    return render_template('/pages/patientportal/pppatients.html')

@app.route('/ppreminders')
def ppreminders():
    return render_template('/pages/patientportal/ppreminders.html')

@app.route('/ppperformance')
def ppperformance():
    return render_template('/pages/patientportal/ppperformance.html')
# End Of Patient Portal Routes

# Start Of Practice Potential Routes
@app.route('/practicepotential')
def practicepotential():
    return render_template('/pages/practicepotential/practicepotential.html')
# End Of Practice Potential Routes

# Start Of Practice Potential Routes
@app.route('/txminer')
def txminer():
    return render_template('/pages/txminer/txminer.html')
# End Of Practice Potential Routes




if __name__ == "__main__":
    app.run(debug=True)