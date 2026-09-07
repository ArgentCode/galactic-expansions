// player-base.adapter.ts

import { PlayerStatusDTO, PlayerStatus } from "../models/player-status.dto";


export function mapPlayerStatusDtoToModel(dto: PlayerStatusDTO): PlayerStatus {
  return {
    name: dto.name,
    metal: dto.metal,
    crystal: dto.crystal,
    energy: dto.energy,
    metalMine: {
      level: dto['Metal Mine Level'],
      rate: dto['Metal Mine Rate'],
      energyConsumption: dto['Metal Mine Energy Consumption']
    },
    crystalMine: {
      level: dto['Crystal Mine Level'],
      rate: dto['Crystal Mine Rate'],
      energyConsumption: dto['Crystal Mine Energy Consumption']
    },
    solarPlant: {
      level: dto['Solar Plant Level'],
      rate: dto['Solar Plant Rate'],
      energyConsumption: dto['Solar Plant Energy Consumption']
    }
  };
}
