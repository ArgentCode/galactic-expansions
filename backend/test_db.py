from database import SessionLocal
from models import Buildings, Player, Worlds

# Open a database session
session = SessionLocal()

try:
    # cleanup
    old_player = session.query(Player).filter_by(
        empire_name="GalacticOverlord").first()
    if old_player:
        session.delete(old_player)
        session.commit()
        print("Cleaning test data from DB.")

    # 1. Create a new player
    new_player = Player(empire_name="GalacticOverlord")
    session.add(new_player)
    session.commit() # PlayerID auto created

    # 2. worlds
    new_world = Worlds(player_id=new_player.player_id,
                       world_name="Earth Prime")
    session.add(new_world)
    session.commit()

    # 3. buildings
    metal_mine = Buildings(
        world_id=new_world.world_id, building_type="metal_mine", level=2
    )
    solar_plant = Buildings(
        world_id=new_world.world_id, building_type="solar_plant", level=1
    )

    session.add_all([metal_mine, solar_plant])
    session.commit()

    fetched_player = session.query(Player).filter_by(
        empire_name="GalacticOverlord"
    ).first()

    print(f"\nSuccessfully loaded player: {fetched_player.empire_name}")
    print(f"Worlds owned: {len(fetched_player.worlds)}")

    for world in fetched_player.worlds:
        print(f" - World: {world.world_name} (Metal: {world.metal})")
        print("   Buildings attached:")
        for building in world.buildings:
            print(f"     * {building.building_type} (Level {building.level})")

finally:
    # cleanup
    old_player = session.query(Player).filter_by(
        empire_name="GalacticOverlord").first()
    if old_player:
        session.delete(old_player)
        session.commit()
        print("Cleaning test data from DB.")

    session.close()
