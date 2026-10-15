from database import Base
from sqlalchemy import Column, Float, ForeignKey, Integer, String, ARRAY
from sqlalchemy.orm import relationship


class Player(Base):
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


class World(Base):
    __tablename__ = "worlds"
    world_id = Column(Integer, primary_key=True)
    player_id = Column(Integer, ForeignKey("players.player_id"))
    world_name = Column(String, default="Colony")
    metal = Column(Integer)
    crystal = Column(Integer)
    deuterium = Column(Integer)
    energy = Column(Float)

    player = relationship("Player", back_populates=("worlds"))


class Buildings(Base):
    __tablename__ = "buildings"
    building_id = Column(Integer, primary_key=True)
    world_id = Column(Integer, ForeignKey("worlds.world_id"))
    player_id = Column(Integer, ForeignKey("players.player_id"))
    Level = Column(Integer, default=0)
    building_type = Column(String)

    world = relationship("World", back_populates="buildings")

    __mapper_args__ = {
        'polymorphic_on': building_type,
        'polymorphic_identity': 'base_building',
    }

# Mines (Metal, Crystal, Deuterium, Solar Plant)


class Mine(Building):
    __mapper_args__ = {'polymorphic_identity': 'mine'}


# Storage Facilities (Metal Storage, Crystal Storage, Deuterium Tank)
class StorageFacility(Building):
    __mapper_args__ = {'polymorphic_identity': 'storage'}


# General Facilities (e.g., Robotics Factory, Shipyard, Research Lab)
class GeneralFacility(Building):
    __mapper_args__ = {'polymorphic_identity': 'facility'}
