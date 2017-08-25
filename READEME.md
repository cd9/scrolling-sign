Story/Progress:

- Started wanting to clone https://wp.josh.com/2016/05/20/huge-scrolling-arduino-led-sign/
- Successfully cloned it by following instructions
- Wanted to add dynamic messages
- Modified Arduino sketch to accept new strings
- Enabled the RX pin using a trick I found on stackoverflow - see code
- Tried using bluetooth to send strings but strings came out garbled
- Had a LOT of trouble getting the string to read properly via serial - thought it was grounding issues or serial was too fast
- Slowed down the serial code because I thought it was too fast
- Turned out you needed a ferrite bead to reduce noise
    - So serial may not have been a problem the whole time
- After ferrite bead was added everything worked more or less perfectly
- Box was added for polish
- Colors were added
    - for green, use [these brackets] and for red, use {these brackets}
    - this works well well enough for the ticker, but see to do list

Links:

- Most of the components for this project come from:
- https://wp.josh.com/2016/05/20/huge-scrolling-arduino-led-sign/
- https://github.com/bigjosh/MacroMarquee (original github link - mine is modified for dynamic string input)

Hardware:

- A Raspberry Pi running some version of Rasbian
    - If you need to reflash the SD card, any version of linux will do.
    - To install the software on a new raspberry pi:
        - Go to the github page @ https://github.com/khazanahamericas/scrolling-sign
        - Fork it
        - Clone the repo using git clone
        - cd to the scrolling-sign-python-client folder
        - run using python main.py
        - install any packages missing using pip
- Arduino Uno
    - No modifications needed.  Any Arduino Uno should work.  There are a bunch in the innovation office
- 5V 60A PSU
- 7x 60LED/meter LED strips
    - If you want to make another one, I recommend using 90LED/meter strips for higher resolution
- Yardsticks for the back
    - Literally any backing structure will work.  The LED strips are pretty versatile

Software:

- Firebase database
    - See improvements
- Python client script that updates from firebase (currently checks every X seconds - could change to streaming)
    - See improvements
- Arduino sketch
    - Probably the most important component
    - Really difficult to wrap your head around because it uses low level stuff
    - Available on github as well - pls fork it
- The config.h file contains all the parameters you need to change the basic parameters (for Teresa)
- To access the pi, SSH into it
    - Find the IP address by going on the shellfire router page and checking the latest connections
    - You can also plug in a wireless keyboard, but Gabi stole it from the pi for her fish thing lol

Improvements / To do

- [ ] Make tablet mobile-friendly
- [ ] I’m using the kraken API which may not be ideal for displaying all sorts of crypto prices
    - May want to find a better API
- [ ] Catch exceptions when there is no internet connection so the script doesn’t just stop
- [ ] You may need to replace the SD card at some point.  I had to reformat it initially so it could act up in the future.
- [ ] Replace my API keys with your own API keys please lol
- [ ] Try to speed up the LED sign
    - Try putting in a “normal” Serial read and write
        - Just use readString()
    - May even want to shoot an email to the Josh guy that made it
        - In doing research Josh comments on his own post about how easy it is to add dynamic strings
- [ ] Add an interface for the twitter API.
    - May want to read up on Foundation for Apps
        - They have a really great doc page and tutorials are everywhere
        - But you could probably figure everything out just from my code
    - Just copy what I did for the other templates
    - May be tricky getting Foundation for Apps working
        - If it’s a problem, clone the repo from github - that version works for sure
- [ ] Try to fix the color problem
    - This pretty much requires you to fully understand how the code work
    - I only got so far in my understanding
    - The farthest I got was putting a special character before each character you wish to color but obviously this isn’t ideal
        - There was a problem when each invisible character causing a pause in the scrolling.  Couldn’t figure it out.