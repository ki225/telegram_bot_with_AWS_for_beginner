import json
import requests

def lambda_handler(event, context):
    print(event)
    try:
        body=json.loads(event['body'])
        
        print(body)
        message_part=body['message'].get('text')
        print("Message part : {}".format(message_part))
        
        data = {'url': message_part}
        chat_id=body['message']['chat']['id']
        TOKEN = <Your_telegram_bot_token>
        
        payload=requests.post('https://cleanuri.com/api/v1/shorten',data=data)
        
        print(payload)
        
        if str(payload)=='<Response [400]>':
            message = "Please enter an url."
        else:
            short_url=payload.json()['result_url']
            message = "The short url is {}".format(short_url)
            print("The short url is : {}".format(short_url))
        
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
        print(requests.get(url).json())


        return  {
            "statusCode": 200
        }
    except:
        return  {
        "statusCode": 200
    }
