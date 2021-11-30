#Price Checker
Simple python script that checks a flight's price and sends it via sms to you.

## Step 1
Edit python file to put your flights link including your phone number and flights name

    flight_link = "https://www.kiwi.com/en/search/results/city-of-brussels-belgium/tirana-albania/2021-12-21/no-return"
Go to Kiwi and search your flight then copy and paste the link.

    'phone': '+yournumberhere',
    'message': date_today + '\n PUT WHATEVER YOU WANT HERE \n Price : ' + price,
Enter your phone number and the sms you want to receive ex the flights name
## Step 2
Don't forget to edit the batch file to your own python directory.

    "C:\Users\your username here\AppData\Local\Programs\Python\Python39\python.exe" "price_checker.py"

## Step 3 (Optional)
If you want the script to run everytime you turn on your pc make a shortcut of flight.bat to your startup folder. 
It's here:

    C:\Users\your username here\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup
