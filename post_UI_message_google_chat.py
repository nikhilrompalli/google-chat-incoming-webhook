from json import dumps

from httplib2 import Http


def main():
    """Hangouts Chat incoming webhook quickstart."""
    url = 'https://chat.googleapis.com/v1/spaces/AAAAQQufZK4/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=0YEoyaDqLoit8FQjTuCWA5VOo_HZ3ecSgNW0AeZiW5A%3D'
    bot_message = {
                      "cards": [
                        {
                          "header": {
                            "title": "Pizza Bot Customer Support",
                            "subtitle": "pizzabot@example.com",
                            "imageUrl": "https://goo.gl/aeDtrS"
                          },
                          "sections": [
                            {
                              "widgets": [
                                  {
                                    "keyValue": {
                                      "topLabel": "Order No.",
                                      "content": "12345"
                                      }
                                  },
                                  {
                                    "keyValue": {
                                      "topLabel": "Status",
                                      "content": "In Delivery"
                                    }
                                  }
                              ]
                            },
                            {
                              "header": "Location",
                              "widgets": [
                                {
                                  "image": {
                                    "imageUrl": "https://maps.googleapis.com/..."
                                  }
                                }
                              ]
                            },
                            {
                              "widgets": [
                                  {
                                      "buttons": [
                                        {
                                          "textButton": {
                                            "text": "OPEN ORDER",
                                            "onClick": {
                                              "openLink": {
                                                "url": "https://example.com/orders/..."
                                              }
                                            }
                                          }
                                        }
                                      ]
                                  }
                              ]
                            }
                          ]
                        }
                      ]
                    }

    message_headers = {'Content-Type': 'application/json; charset=UTF-8'}

    http_obj = Http()

    response = http_obj.request(
        uri=url,
        method='POST',
        headers=message_headers,
        body=dumps(bot_message),
    )

    print(response)

if __name__ == '__main__':
    main()