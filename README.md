# webtv
Watch any tv series (requires you to download the episodes) and host on your computer!

# Requirements:

Python

Flask

#Setup
Step 1: Install the requireemts

Step 2: Depending on what you are adding, add your episodes/single movie(not multiple) to the folders. Either " series" or "movies". After that,  create a file called "config.webtvconf", this will be where we set up the way it displays in the browser.

Step 3: Create a new folder for the series/movie, we will add this to the comfig file later.

Step 4: Open config.webtvconfig (in the series/movie folder) and link the series/movie icon, episodes/movie and the name.

Example:

     series/

           TheLastOfUs/
      
                the.last.of.us.season.1.episode.1.mp4
           
           config.webtvconfig

     movies/

          ForestGump/
     
               forest.gump.mp4
               
          config.webtvconfig

What should be in the config files:


For a series:

episodesinseason1: 9

iconforseries: icon.png

episode1season1:
