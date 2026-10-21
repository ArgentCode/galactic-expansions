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
3. Go to backend
    cd backend
4. Test DB connection
    python .\test_db.py (my comically terrible testing)
5. Run flask
    flask --app .\flaskoffun.py run 
6. Fire up your API caller of choice (Bruno used in testing)
    Review APIHandler specific instructions!

# Things todo:
- Backend
    1. Upgrade mines
        - make sure you check energy in the tick function after!
    2. Facilities
    3. Research
    4. ships
        - transport
        - Expeditions
        - combat
    5. unit tests
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