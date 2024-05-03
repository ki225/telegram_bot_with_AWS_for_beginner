# telegram_bot_for_beginner
At first, thanks for the tutorial video [Building a Telegram Bot with AWS API Gateway and AWS Lambda](https://www.youtube.com/watch?v=oYMgw4M4cD0&t=822s).

This is a simple telegram bot for checking input messages and returning a short url as a response. The propose for this project is to let beginners know how to run an telegram bot with AWS lambda function and API gateway. Here are the steps and the sulotions for some problems you might meet.

<img width="1012" alt="截圖 2024-05-03 下午1 51 54" src="https://github.com/ki225/telegram_bot_with_AWS_for_beginner/assets/123147937/eb1e3126-e5b2-4b30-b4ca-01578dac2fc5">

# steps

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

<img width="1552" alt="截圖 2024-05-03 下午2 15 05" src="https://github.com/ki225/telegram_bot_with_AWS_for_beginner/assets/123147937/559276a0-b2e3-4d4e-9140-f5d8ab60b306">
