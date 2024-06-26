from flask import Flask, request, abort

from linebot.v3 import WebhookHandler
from linebot.v3.exceptions import InvalidSignatureError
from linebot.v3.messaging import (
    Configuration,
    ApiClient,
    MessagingApi,
    ReplyMessageRequest,
    TextMessage,
)
from linebot.v3.webhooks import MessageEvent, TextMessageContent

import stock_crawler as sc

app = Flask(__name__)

configuration = Configuration(
    access_token="sd9Xz63Sn4wRF3JqThEPonlSKWaAPANWLsCJtKmjCjSyWG32tLF01b2Y8e8xPUlnPSCu8CXdhfF+Kb1r7nss0Ylr4AJzr+SN1AOsPVq99b4akIwSmRYQ1O18LrrW2j7/ragqkMU4XecWc7ujW6YhFQdB04t89/1O/w1cDnyilFU="
)
handler = WebhookHandler("63e67dadabb0bc8dca15e9e2a5b1231c")


@app.route("/callback", methods=["POST"])
def callback():
    # get X-Line-Signature header value
    signature = request.headers["X-Line-Signature"]

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        app.logger.info(
            "Invalid signature. Please check your channel access token/channel secret."
        )
        abort(400)

    return "OK"


@handler.add(MessageEvent, message=TextMessageContent)
def handle_message(event):
    with ApiClient(configuration) as api_client:
        line_bot_api = MessagingApi(api_client)
        line_bot_api.reply_message_with_http_info(
            ReplyMessageRequest(
                reply_token=event.reply_token,
                messages=[TextMessage(text=sc.get_2330_info(event.message.text))],
            )
        )


if __name__ == "__main__":
    app.run()
