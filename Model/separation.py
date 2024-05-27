# Or like this
import demucs.separate
import shlex
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
app.config.from_object(__name__)
CORS(app, resources={r'/*': {'origins': '*'}})


@app.route('/api/model', methods=['GET'])
def Separa():
    # path = 'D:\\system_default\\desktop\\Model\\htdemucs\\music'
    # for elm in Path(path).glob('*'):
    #     elm.unlink() if elm.is_file() else shutil.rmtree(elm)
    demucs.separate.main(shlex.split(
        '--mp3 --two-stems vocals -o "D:\\system_default\\desktop\\Vue_music\\src\\assets" -n htdemucs "D:\system_default\document\music.mp3"'))
    return jsonify({'message': 'Hello from Python'})


# def sep_4():
#     demucs.separate.main(shlex.split(
#         '--mp3 --two-stems vocals -o "D:\system_default\desktop\Model\htdemucs" -n htdemucs "D:\system_default\document\music.mp3"'))
#
#     return jsonify({'message': 'Hello from Python'})

if __name__ == '__main__':
    app.run()
