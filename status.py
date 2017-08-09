from flask import Flask, request
app = Flask(__name__)


@app.route('/', methods=['POST'])
def report():
    req = request.get_json(force=True)
    with open("database.txt", "a") as text_file:
        print('status is: ' + req['status'])
        text_file.write('message id: ' + str(req['id']) + ' status is: '
                        + req['status'] + '\n')
    print(req)
    return 200


if __name__ == '__main__':
    app.run()
