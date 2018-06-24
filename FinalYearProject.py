from flask import Flask, render_template, url_for, redirect, request
import tester, scipy, numpy as np, pickle, os,wave
import audio_recording

UPLOAD_FOLDER = 'F://projects//python//FinalYearProject//testingdata//'
ALLOWED_EXTENSION = {'wav'}

app = Flask(__name__)
app = Flask(__name__, static_url_path='')

@app.route('/')
def start():
    return redirect(url_for("index"))

@app.route('/index/')
def index():
    return render_template('index.html')

@app.route('/test/')
def test():
    if os.path.isfile("F://projects//python//FinalYearProject//testingdata//test.wav"):
        os.remove("F://projects//python//FinalYearProject//testingdata//test.wav")
    return render_template('Test.html')

@app.route('/process', methods=['POST'])
def startprocess():
    if os.path.isfile("F://projects//python//FinalYearProject//testingdata//test.wav"):

        f = wave.open("F://projects//python//FinalYearProject//testingdata//test.wav", 'r')
        frames = f.getnframes()
        rate = f.getframerate()
        print(frames)
        print(rate)
        duration = frames / float(rate)
        print("###")
        print(duration)
        f.close()
        if (duration > 5):
            return render_template('test.html', testMessage="Audio File Longer than 3 seconds")
        else:
            try:
                ans = tester.individual()
                print("ans aayo")
                testMessage = ans
                print("eta ni aayo")
                os.remove("F://projects//python//FinalYearProject//testingdata//test.wav")
                print("remove remove")
                if (ans == "anger"):
                    ans = "angry"
                return render_template('Test.html',testMessage="You sound "  + ans)
            except:
                return render_template('Test.html', testMessage="File not found")
    else:
            return render_template('Test.html', testMessage="Audio File not found")

@app.route('/record', methods=['POST'])
def record():
    audio_recording.recordaudio()
    return render_template('test.html',recordmsg = "Audio has been successfully recorded.")

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['inputfile']
    if file and allowed_file(file.filename):
        filename = "test.wav"
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        print(filename)
        print(UPLOAD_FOLDER + file.filename)
        return render_template('test.html', uploadmsg="file successfully uploaded begin processing")
    else:
        return render_template('test.html', uploadmsg="invalid file format or empty file")


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSION
if __name__ == '__main__':
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    app.run()
