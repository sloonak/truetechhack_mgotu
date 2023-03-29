import flask
import threading
import postgresql.get_connection
import postgresql.insert.insert_video_data
import postgresql.select.select_video

import image.analyze
import example_data

import os

app = flask.Flask(__name__)

@app.route("/")
def index():
    return flask.render_template('index.html')


# Функция для обработки видео
def process_video(url = ''):
    data = image.analyze.analyze_url(url)
    postgresql.insert.insert_video_data.insert_video_data(url = url, status = 'OK', data=data)


# data = example_data.data
# postgresql.insert.insert_video_data.insert_video_data(url = '/var/www/truetechhack/static/video/rik1080.mp4', status = 'OK', data=data)


@app.route("/service/analyze", methods=['POST'])
def flask_analyze():
    url = flask.request.json.get('url', None)

    if url is None:
        response = flask.make_response(
            flask.jsonify(
                {"error": "url is missing"}
            ),
            400,
        )
        response.headers["Content-Type"] = "application/json"

        return response

    # # Запускаем анализ видео в отдельном потоке, чтобы не блокировать обработку других запросов
    # thread = threading.Thread(target=process_video, args=(timecode,))
    # thread.start()

    response = flask.make_response(
        flask.jsonify(
            {"message": "Video analysis has started"}
        ),
        202,
    )
    response.headers["Content-Type"] = "application/json"

    return response


@app.route("/service/get_analyze", methods=['POST'])
def analyze():
    url = flask.request.json.get('url', None)

    if url is None:
        response = flask.make_response(
            flask.jsonify(
                {"error": "URL is missing"}
            ),
            400,
        )
        return response

    # # Запускаем анализ видео в отдельном потоке, чтобы не блокировать обработку других запросов
    # thread = threading.Thread(target=process_video, args=(timecode,))
    # thread.start()

    result = postgresql.select.select_video.select_video_by_url(url)

    response = flask.make_response(
        flask.jsonify(
            {"message": "Recieved", 'result': result}
        ),
        202,
    )
    response.headers["Content-Type"] = "application/json"

    return response

if __name__ == '__main__':
    app.debug=True
    app.run()