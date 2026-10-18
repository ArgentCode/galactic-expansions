# galactic-expansions

A sci-fi timer based slow build up strategy game!

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
- Backend
    1. Tick function
    2. Upgrade mines
    3. Facilities
    4. Research
    5. ships
        - transport
        - Expeditions
        - combat
- Front End
    1. login support
    2. Add our images into the game
    3. Add a UI

# Databases Idea
Tables:
    Player:
        PlayerID, Name, last tick, List of Worlds
    Research:
        PlayerID, one column for each research (12 or something)
    Worlds:
        WorldID, PlayerID, Name, resources
    Buildings:
        Mines, facilities
    fleets:
        PlayerID, WorldID (Set 0 to traveling or something?), departure, arrival,  