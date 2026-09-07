// export interface StatusDto {
//     name: string;
//     metal: number;
//     crystyal: number;
//     energy: number;
//     MetalMineLevel: number;
//     MetalMineRate: number;
//     MetalMineEnergyConsumption: number;
//     CrystalMineLevel: number;
//     CrystalMineRate: number;
//     CrystalMineEnergyConsumption: number;
//     SolarPlantLevel: number;
//     SolarPlantRate: number;
//     SolarPlantEnergyConsumption: number;
// }

export interface PlayerStatusDTO {
  name: string;
  metal: number;
  crystal: number;
  energy: number;
  'Metal Mine Level': number;
  'Metal Mine Rate': number;
  'Metal Mine Energy Consumption': number;
  'Crystal Mine Level': number;
  'Crystal Mine Rate': number;
  'Crystal Mine Energy Consumption': number;
  'Solar Plant Level': number;
  'Solar Plant Rate': number;
  'Solar Plant Energy Consumption': number;
}

export interface BuildingStats {
  level: number;
  rate: number;
  energyConsumption: number;
}

export interface PlayerStatus {
  name: string;
  metal: number;
  crystal: number;
  energy: number;
  metalMine: BuildingStats;
  crystalMine: BuildingStats;
  solarPlant: BuildingStats;
}

// Factory function for an empty base state
export function createEmptyPlayerStatus(): PlayerStatus {
  return {
    name: 'Initializing...',
    metal: 0,
    crystal: 0,
    energy: 0,
    metalMine: { level: 0, rate: 0, energyConsumption: 0 },
    crystalMine: { level: 0, rate: 0, energyConsumption: 0 },
    solarPlant: { level: 0, rate: 0, energyConsumption: 0 }
  };
}