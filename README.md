# calculate-age-and-day-from-birthday

## Description
This will calculate the age and find the day of the week the user was born based from the user's entered birthday. In calculating the age, the days of the week which is 365.2425 is used to accurately compute the age if ever the current year is a leap year or not and if the birthday is February 29. 

This project uses the following concept:
* if else statement
* classes and object
* exception handling
* datetime and calendar modules

## How to Run
1. Clone this repo to your local machine using https://github.com/mcalidguid/calculate-age-date-from-birthday.git
2. For windows, open cmd
```
cmd > C:\python38\python.exe C:\python\projects\calculate-age-date-from-birthday\birthday_details.py
```
_Note: Modify the path for python.exe and birthday_details.py accordingly_

## Sample Output
Date Today = Aug 27, 2020
```
Enter your Birthday [DDMMYYY]:
>>>: 27081992
You were born on Thursday
As of today, you are now 28 year/s old.
```
```
Enter your Birthday [DDMMYYY]:
>>>: 28081992
You were born on Friday
As of today, you are now 27 year/s old.
```
```
Enter your Birthday [DDMMYYY]: 
>>>: 27082019
You were born on Tuesday
As of today, you are now 1 year/s old.
```
```
Enter your Birthday [DDMMYYY]: 
>>>: 28082019
You were born on Wednesday
As of today, you are now 0 year/s old.
```
```
Enter your Birthday [DDMMYYY]: 
>>>: 20203030
The entered date does not match the DDMMYYYY format.
Please try Again.
```
```
Enter your Birthday [DDMMYYY]: 
>>>: 0000
The entered date does not match the DDMMYYYY format.
Please try Again.
```
```
Enter your Birthday [DDMMYYY]: 
>>>: asfd811d~2423@!
The entered date does not match the DDMMYYYY format.
Please try Again.
```


