# carinfowebcrawler

Created a web crawler in python to pull information (car specs) from cars.com

Running the python script waits for a user input of a car make, car model, and year. If it does not have all three of those parameters,
it exits out. If it does have all of those parameters it will attempt a get request to get the source from cars.com using the car
specified as a search query. The html is parsed for the relevant information, and output accordingly.

TODO:

  Fix print statements to be one function (issue is that outputting trims is silly given the text I receive)
  
  take command line parameters so that I can call this from javascript/mainline
  
  add ability to select certain subtrims and not output all trims of the car
  

Ideally will be used to power a reddit bot that will give /r/cars users quick specs on cars
