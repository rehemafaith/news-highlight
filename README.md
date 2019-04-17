# NEWS HIGHLIGHT

## BY : REHEMA FAITH
 
  
## Description
 
#### This is an application that will help you list and preview news articles from various sources.You can get the top headlines in any language from different networks all over the world.   

##  BDD

| Behaviour                              | Input                           | Output                      |
| :---------------------:                | :-------------------------:     | :------------------------:  |
|   Get a list of the sources available  | click on source of choice       | Get the list of sources     |
|  Get the Top Headlines                 | click on read button            | Get the full story          |



## Installation 

* Clone this repository to your local computer.
* Ensure you have python3.6 installed in your computer.
* From the terminal navigate to the cloned project folder.
* Create a virtual environment and access the folder via your virtual amchine.
* Visit https://newsapi.org/ and register for an API key.
* Create start.sh file and in it write the following lines:

```
export NEWS_API_KEY='<Your-Api-Key>'  
python3.6 manage.py server  

```
* Run ```chmod +x start.sh ``` followed by ```./start.sh``` while in the project folder to start the project.
* Once started, the project can be accessed on your localhost using the address: localhost:5000.
* Alternatively the application can be accessed by visiting https://newshighlight-rehema.herokuapp.com/

## Technologies Used
 
* Python3.6

## Known Bugs

* None 

## LICENSE

* [MIT LICENSE](LICENSE)
