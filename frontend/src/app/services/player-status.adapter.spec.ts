
import { PlayerStatusDTO, PlayerStatus } from '../models/player-status.dto';
import { mapPlayerStatusDtoToModel } from './player-status.adapter';

describe('PlayerStatusAdapter', () => {
  
  it('should successfully map a valid PlayerStatusDTO to the PlayerStatus domain model', () => {
    // Arrange: Create mock data matching your API payload exactly
    const mockDto: PlayerStatusDTO = {
      name: 'First Guy',
      metal: 117846,
      crystal: 82792,
      energy: 0.5,
      'Metal Mine Level': 1,
      'Metal Mine Rate': 50,
      'Metal Mine Energy Consumption': -5,
      'Crystal Mine Level': 2,
      'Crystal Mine Rate': 35,
      'Crystal Mine Energy Consumption': -5,
      'Solar Plant Level': 3,
      'Solar Plant Rate': 0,
      'Solar Plant Energy Consumption': 10.5
    };

    // Act: Run the adapter mapping function
    const result: PlayerStatus = mapPlayerStatusDtoToModel(mockDto);

    // Assert: Verify all base properties were properly parsed
    expect(result.name).toBe('First Guy');
    expect(result.metal).toBe(117846);
    expect(result.crystal).toBe(82792);
    expect(result.energy).toBe(0.5);

    // Assert: Metal Mine nested group
    expect(result.metalMine).toEqual({
      level: 1,
      rate: 50,
      energyConsumption: -5
    });

    // Assert: Crystal Mine nested group
    expect(result.crystalMine).toEqual({
      level: 2,
      rate: 35,
      energyConsumption: -5
    });

    // Assert: Solar Plant nested group
    expect(result.solarPlant).toEqual({
      level: 3,
      rate: 0,
      energyConsumption: 10.5
    });
  });

  it('should accurately map zero and negative values without corruption', () => {
    // Arrange: Mock data with borderline numeric data configurations
    const mockZeroDto: PlayerStatusDTO = {
      name: 'Empty Base',
      metal: 0,
      crystal: 0,
      energy: -2.5,
      'Metal Mine Level': 0,
      'Metal Mine Rate': 0,
      'Metal Mine Energy Consumption': 0,
      'Crystal Mine Level': 0,
      'Crystal Mine Rate': 0,
      'Crystal Mine Energy Consumption': 0,
      'Solar Plant Level': 0,
      'Solar Plant Rate': 0,
      'Solar Plant Energy Consumption': 0
    };

    // Act
    const result = mapPlayerStatusDtoToModel(mockZeroDto);

    // Assert
    expect(result.metal).toBe(0);
    expect(result.energy).toBe(-2.5);
    expect(result.metalMine.level).toBe(0);
    expect(result.solarPlant.energyConsumption).toBe(0);
  });
});
