# webtv
Watch any tv show (requires you to download the episodes/movies) and host on your computer!

# Requirements:

[Python](https://www.python.org)

Flask

Install flask by running this command in command prompt:

     pip install flask

# Setup
Step 1: Install the requirements

Step 2: Depending on what you are adding, add your episodes/single movie(not multiple) to the folders. Either " series" or "movies". After that, create a file called "config.webtvconfig", this will be where we set up the way it displays in the browser.

Step 3: Create a new folder for the series/movie, we will add this to the config file later.

Step 4: Open config.webtvconfig (in the series/movie folder) and link the  icon, episodes/movie, and the name.

Example:

     series/

           TheLastOfUs/
      
                the.last.of.us.season.1.episode.1.mp4
                icon.png
          
           TheOffice/

                episode1season1.mp4
                theoffice.jpeg
           
           config.webtvconfig

     movies/

          ForestGump/
     
                forest.gump.mp4
                icon.png
               
          DieHard1/
          
                diehard1.mp4
                diehardicon.jpeg
               
          config.webtvconfig

What should be in the config files:


For a series (this example includes multiple series. As you can see, they are separated by 5 colons):

     episodesinseason1: 1
     nameofseries: "The Last of Us"
     iconforseries: TheLastOfUs/icon.png
     agerating: 18
     episode1season1: TheLastOfUs/the.last.of.us.episode.1.season.1.mp4
     :::::
     episodesinseason1: 1
     nameofseries: "The Office"
     iconforseries: TheOffice/theoffice.jpeg
     agerating: 12
     episode1season1: TheOffice/episode1season1.mp4


For a movie (each movie's info is separated by 5 colons):

     nameofmovie: "Forest Gump"
     iconformovie: ForestGump/icon.png
     agerating: 12
     moviefile: ForestGump/forest.gump.mp4
     :::::
     nameofmovie: "Die Hard"
     iconformovie: DieHard1/diehardicon.jpeg
     agerating: 18
     moviefile: DieHard1/diehard1.mp4

After all of that, we can move on to running the program.

# How to Run

Step 1: Navigate to the root directory of the program in command prompt.

Step 2: Make sure all the requirements are installed and run:
    
     python -m server

Step 3: Depending on what device you will be watching on, open your browser and type in:

For watching on the pc running the program, open 127.0.0.1:5000 in your browser. This is the address for localhost.

For watching on another device, you have to be connected to the same WiFi network, and you have to put in the local IP address of the PC into the browser, with the port 5000. You can find your local IP by running the following command in command prompt: 
     
     ipconfig
     
the local IP always starts with 192.168.

So for example, say my local IP address is 192.168.192.110. Then I would open my browser and type 192.168.192.110:5000
