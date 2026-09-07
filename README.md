# galactic-expansions

A sci-fi idle game!

## General

To spin up this project, simply run `docker compose up`.
This will create a UI container running on port 4200 (ie `localhost:4200`).
The API will be served on 5000 ( `localhost:5000` )

The front end should handle most file updates and automatically serve them, but backend changes will require you to rebuild the container.

# Backend 

How to do the game: 
1. run your virtual environment:
    py -m venv venv
    .\venv\Scripts\activate.ps1   
2. install packages 
    pip install -r .\requirements.txt
3. Go to backend and Run flask
cd backend
    flask --app .\flaskoffun.py run 


# Things todo:
1. Break resource tick into its own function
2. Energy
    - Make energy time dynamic
3. Oil
4. fix my mega if statements in the tick
5. Fix the timing for upgrades
    if player.metalMine.lastUpgradeTime < lastTick or player.metalMine.lastUpgradeTime > now:
    this line actually only does the upgrade if the last tick did the thing. Behind, bad, yeah.
6. Database support for persistence
7. login support
8. Add our images into the game
9. Add a UI


