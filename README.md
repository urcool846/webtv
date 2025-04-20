# webtv
Watch any tv series (requires you to download the episodes) and host on your computer!

# Requirements:

[Python](https://www.python.org)

Flask

# Setup
Step 1: Install the requireemts

Step 2: Depending on what you are adding, add your episodes/single movie(not multiple) to the folders. Either " series" or "movies". After that,  create a file called "config.webtvconf", this will be where we set up the way it displays in the browser.

Step 3: Create a new folder for the series/movie, we will add this to the comfig file later.

Step 4: Open config.webtvconfig (in the series/movie folder) and link the series/movie icon, episodes/movie and the name.

Example:

     series/

           TheLastOfUs/
      
                the.last.of.us.season.1.episode.1.mp4
          
           TheOffice/

                episode1season1.mp4
           
           config.webtvconfig

     movies/

          ForestGump/
     
                forest.gump.mp4
               
          DieHard1/
          
                diehard1.mp4
               
          config.webtvconfig

What should be in the config files:


For a series (this example includes multiple series. As you can see, they are separated by 5 colons):

     episodesinseason1: 1
     nameofseries: "The Last of Us"
     iconforseries: icon.png
     agerating: 18
     episode1season1: TheLastOfUs/the.last.of.us.episode.1.season.1.mp4
     :::::
     episodesinseason1: 1
     nameofseries: "The Office"
     iconforseries: theoffice.jpeg
     agerating: 12
     episode1season1: TheOffice/episode1season1.mp4


For a movie (each movie's info is separated by 5 colons):

     nameofmovie: "Forest Gump"
     iconformovie: icon.png
     agerating: 12
     moviefile: ForestGump/forest.gump.mp4
     :::::
     nameofmovie: "Die Hard"
     iconformovie: diehardicon.jpeg
     agerating: 18
     moviefile: DieHard1/diehard1.mp4

After all of that, we can move on to running the program.

# How to Run

Step 1: Navigate to the root directory of the program in command prompt.

Step 2: Make sure all the requirements are installed and run:
    
     python -m server

Step 3: Depending on what device you will be watching on, open your browser and type in:

For watching on the pc running the program, open 127.0.0.1:5000 in your browser. This is the address for localhost.

For watching on another device, you have to be connected to the same WiFi network, and you have to put in the local IP address of the PC into the browser. The local IP always starts with 192.168.
