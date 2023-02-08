# calculator
Simple web calculator that uses JS and ajax to send data input to calculator to a 
flask backend where the result is calculated then returned. Result is displayed in the calculator. 

# setup & run 
-Install virtualenv 
    ```
	$ sudo apt install virtualenv -y (Linux)
	$ virtualenv <envname> -p python3 (Linux)
    
    $ pip install virtualenv (Mac)
    $ python3 -m venv env (Mac)
	```

-Activate env 
    ```
	$ source bin/activate
	```

-Install dependencies 
    ```
	$ pip3 install -r requirements.txt
	```

-Activate Flask server 
    ```
    $ python -m flask run 
    ```