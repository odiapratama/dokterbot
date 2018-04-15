import to
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)
from linebot import LineBotApi
from linebot.models import TextSendMessage
from linebot.exceptions import LineBotApiError

app = Flask(__name__)

line_bot_api = LineBotApi('5EPpSucVYcGDoy/i0rlajBBxkuVdMz+SHD5I7XSRy1ZtgbtSGogek4r0zbqLnee9glVTTWVHdblrih53jYZOzZi1Y6pTpLGnXxqV7R0ySTo03ts0CqiCDMKnoz5kPyuibdjzhFQ52CHNlIlWMaPn9QdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('589972e063bbc86d3e7e6f1421430385')

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    text = event.message.text

    line_bot_api.push_message(to, TextMessage(text="Hello World"))

if __name__ == "__main__":
    app.run()