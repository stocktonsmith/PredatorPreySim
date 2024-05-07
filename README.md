Stockton Smith  
A02095109  
CS 5060  
HW 5

# Code Guide:  

Upon running `simulator.py`, the following input prompts will appear, allowing the user to specify the details of the blob simulation:  

```
WELCOME TO BLOB SIMULATOR!
How many days to simulate?   >>> 
How many doves/blue blobs [0, 10]?   >>> 
How many hawks/red blobs [0, 10]?   >>> 
How many available pairs of food?   >>> 
Enter text speed [0 = slowest, 100 = instant]   >>> 
```

The program does not account for poor user input, so be sure to follow the given specifications:
- **Days to simulate**: Input a positive number. The simulation will run for this many days.
- **Blue blobs**: Input a number between 0 and 10. This is the number of doves/blue blobs that will exist on day 1.
- **Red blobs**: Input a number between 0 and 10. This is the number of hawks/red blobs that will exist on day 1.
- **Food pairs**: Input a positive number. This is the number of available food pairs for each day of the simulation. Up to two blobs can eat at a food pair. 
- **Text speed**: Input a number between 0 and 100. Slower text will allow the user to watch the simulation play-by-play, instant text will allow the user to skip to the ending population on the final day (and the play-by-plays can still be viewed by scrolling up in the terminal).

Upon entering these values, no further input is required from the user. The simulation will play out according to the provided specifications and will show populations, food matchups, rewards, deaths, and births for each day.