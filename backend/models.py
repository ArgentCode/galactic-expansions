from database import Base
from sqlalchemy import Column, Float, ForeignKey, Integer, String, TIMESTAMP
from sqlalchemy.orm import relationship


class Player(Base):
    """
    Research is stored at player level as it effects all worlds
    Tick is done at player level as a research could finish affecting
    productions
    """
    __tablename__ = "players"
    player_id = Column(Integer, primary_key=True)
    empire_name = Column(String, unique=True)

    tech_espionage = Column(Integer)
    tech_computer = Column(Integer)
    tech_energy = Column(Integer)
    tech_weapon = Column(Integer)
    tech_armor = Column(Integer)
    tech_shielding = Column(Integer)
    tech_combustion = Column(Integer)
    tech_impulse = Column(Integer)
    tech_hyperspace = Column(Integer)
    tech_laser = Column(Integer)
    tech_ion = Column(Integer)
    tech_plasma = Column(Integer)

    last_tick = Column(TIMESTAMP)

    worlds = relationship(
        "Worlds", back_populates="player", cascade="all, delete-orphan"
    )


class Worlds(Base):
    __tablename__ = "worlds"
    world_id = Column(Integer, primary_key=True)
    player_id = Column(Integer, ForeignKey("players.player_id"))
    world_name = Column(String, default="Colony")

    metal = Column(Integer)
    crystal = Column(Integer)
    deuterium = Column(Integer)
    energy = Column(Float)

    # A world owns multiple buildings (flat list, no inheritance)
    player = relationship("Player", back_populates="worlds")

    buildings = relationship(
        "Buildings", back_populates="world", cascade="all, delete-orphan"
    )


class Buildings(Base):
    """
    Since all buildings can be described either programatically or by lookup tables,
    there is no need to place their meta data on the db.
    """
    __tablename__ = "buildings"
    building_id = Column(Integer, primary_key=True)
    world_id = Column(Integer, ForeignKey("worlds.world_id"))

    level = Column(Integer, default=0)
    building_type = Column(String)

    completion_time = Column(TIMESTAMP)

    world = relationship("Worlds", back_populates="buildings")
