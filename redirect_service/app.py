from flask import Flask, render_template, redirect, request, make_response

from redirector import interface as service
from redirector.models import ResponseForm

app = Flask(__name__)
app.config['SECRET_KEY'] = "kdlsjf!@!"

@app.route('/')
def home():
    return redirect("https://tracer.syscape.live/")

@app.route('/<id>', methods=['GET', 'POST'])
def getter(id):
    form =  ResponseForm()
    url_data = service.get_redirect_url(id)
    if not url_data:
        return redirect("https://tracer.syscape.live/")
    if not url_data[0]:
        return redirect("https://tracer.syscape.live/")
    if form.validate_on_submit():
        clientIp = request.remote_addr
        
        data = dict()
        data['urlid'] = id
        UserAgent = request.headers.get("User-Agent")
        if(UserAgent):
            data['userAgent'] = str(UserAgent)
        if(clientIp):
            data['ipaddress'] = str(clientIp)
        if(form.availableRam.data):
            data["availableRam"] = str(form.availableRam.data)
        if(form.battery.data):
            data["battery"] = str(form.battery.data)
        
        service.push_data_to_store(data)
        return redirect(url_data[0])
    if len(url_data) > 2:
        if url_data[2] == "O":
            return render_template('collector.html', form=form, redirect=url_data[0], title=None, og=url_data[1])
        elif url_data[2] == "T":
            return render_template('collector.html', form=form, redirect=url_data[0], title=url_data[1], og=None)
    else :
        return render_template('collector.html', form=form, redirect=url_data[0], title=False)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
    