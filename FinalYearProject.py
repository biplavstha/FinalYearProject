from flask import Flask, render_template, url_for, redirect, request
import featureExtraction, scipy, numpy as np, pickle, os,threading

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
    return render_template('Test.html')

@app.route('/process', methods=['POST'])
def startprocess():
    try:
        featureExtraction.extractFeatures()

        ffts = []
        mfccs = []
        features = []

        fft_values = scipy.load('F://projects//python//FinalYearProject//testdatafeatures//fft.csv.npy')
        # fft_values=scipy.load('03-01-06-01-01-01-01.wavfft.csv.npy')
        fft_values = abs(fft_values)
        ffts.append(fft_values)

        mfcc_values = scipy.load('F://projects//python//FinalYearProject//testdatafeatures//mfcc.csv.npy')
        # mfcc_values = scipy.load('03-01-06-01-01-01-01.wavmfcc.csv.npy')
        mfccs.append(mfcc_values)

        mfccs[0].resize((526, 13), refcheck=False)

        for n in range(len(ffts)):
            individual_feature = []
            individual_feature = np.concatenate((np.array(ffts[n]), individual_feature), axis=0)
            for val in mfccs[n][:526]:
                individual_feature = np.concatenate((np.array(val), individual_feature), axis=0)
            features.append(individual_feature)

        t_data = pickle.load(open('F://projects//python//FinalYearProject//classifier//linearclassifier.pkl', 'rb'))
        ans = t_data.predict(np.asanyarray(features).reshape(1, -1))[0]

        testMessage = ans
        return render_template('Test.html', testMessage=testMessage)
    except:
        return render_template('Test.html', testMessage="File not found")

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
        return render_template('test.html', uploadmsg="file format not supported please upload wav file")


# @app.route('/record', methods=['POST'])
# def record():
#     if os.path.isfile("F://projects//python//FinalYearProject//testingdata//test.wav"):
#         os.remove("F://projects//python//FinalYearProject//testingdata//test.wav")
#
#     return render_template('test.html', recordmessag="Audio recorded")

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSION
if __name__ == '__main__':
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    app.run()
