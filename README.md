# telegram_bot_for_beginner
At first, thanks for the tutorial video [Building a Telegram Bot with AWS API Gateway and AWS Lambda](https://www.youtube.com/watch?v=oYMgw4M4cD0&t=822s).

This is a simple telegram bot for checking input messages and returning a short url as a response. The propose for this project is to let beginners know how to run an telegram bot with AWS lambda function and API gateway. Here are the steps and the sulotions for some problems you might meet.

<img width="1012" alt="截圖 2024-05-03 下午1 51 54" src="https://github.com/ki225/telegram_bot_with_AWS_for_beginner/assets/123147937/eb1e3126-e5b2-4b30-b4ca-01578dac2fc5">

## Implement
- Lambda Function : Lambda is one function that is executed by queries from triggers.
- API Gateway : API Gateway acts as a mediator between client applications and backend services(Lambda function). Others can trigger it with the API Gateway endpoint.

<img width="674" alt="截圖 2024-05-05 上午10 41 55" src="https://github.com/ki225/telegram_bot_with_AWS_for_beginner/assets/123147937/0fba9b12-dd0b-4c38-95bd-5c4c1aef6613">


# steps
1. Create your Bot by asking Bot Father with `/start` and `/newbot`
      If success, you must receive a messege like this:
      ```
      Done! Congratulations on your new bot. You will find it at t.me/aws_checker_v1_by_kii_bot. You can now add a description, about section and profile picture for your bot, see /help for a list of commands. By the way, when you've finished creating your cool bot, ping our Bot Support if you want a better username for it. Just make sure the bot is fully operational before you do this.
      
      Use this token to access the HTTP API:
      xxxxxxxxxxxxxxxx.....xxx
      Keep your token secure and store it safely, it can be used by anyone to control your bot.
      
      For a description of the Bot API, see this page: https://core.telegram.org/bots/api
      ```
2. Create a lambda function
3. put your code into `lambda_handler` function
      This step let your bot react when you send some messeges(sending msg is an event).
4. Create an API Gateway for your function
      API Gateway acts as a mediator between client applications and backend services(Lambda function). Others can trigger it with the API Gateway endpoint.
5. Set Webhook
      Webhook is an HTTP-based callback function that can realize event-driven lightweight communication between two application programming interfaces (APIs). I use Postman for sending HTTP POST. Just send your API Gateway endpoint as an url to your Telebot.
      ```
      https://api.telegram.org/bot{HTTP Token}/setWebhook
      ```
      If you set successfully, the messege of "description" will be "Webhook was set."
      
      <img width="1376" alt="IMG_1306" src="https://github.com/ki225/telegram_bot_with_AWS_for_beginner/assets/123147937/d937cf71-54a1-4105-be41-1dbcddd16088">
      
      This [article](https://aravindkumarvemula.medium.com/how-to-integrate-telegram-bot-with-python-using-requests-519d384dc6d3) talk more about how to integrate Telegram Bot with Python using requests.


# Unable to import module 'lambda_function': No module named 'requests'
If you have a problem like "Unable to import module 'lambda_function': No module named 'requests'", here is a way to solve it. I read this [document](https://docs.aws.amazon.com/zh_tw/lambda/latest/dg/python-package.html) first. The solution is to download the packages you need locally and put them to the folder with your lambda_function.py file. So, you have to open the terminal first. Then use the command `pip install --target <your_directory_path> <package_you_need>` to download the package into it. For me, the directory where I put the lambda_function.py file is called "mytelebot02", so the command will like this:

```
pip install --target ./mytelebot02 requests
```
You can go into your target directory to check. After the command 'ls', it shows all the files in "mytelebot02" directory.
```
bin					idna-3.7.dist-info
certifi					lambda_function.py
certifi-2024.2.2.dist-info		requests
charset_normalizer			requests-2.31.0.dist-info
charset_normalizer-3.3.2.dist-info	urllib3
idna					urllib3-2.2.1.dist-info
```
Zipping this directory, then upload to the aws lambda function.

<img width="1552" alt="IMG_1304" src="https://github.com/ki225/telegram_bot_with_AWS_for_beginner/assets/123147937/eaaaadbb-bd03-42db-9281-94f3353b75a3">
