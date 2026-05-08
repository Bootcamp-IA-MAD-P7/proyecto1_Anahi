# proyecto1_Anahi
Taxímetro

## Taxi class file. Logic of the taximeter. Methods:
- start_journey: Resets fare to 0 and starts the trip by setting journey_active to True
- end_journey: It sets journey_active to False to signal the end of the trip and it returns the fare attribute
- set_moving: Changes the state of the taxi to movement.
- set_stopped: Sets the taxi's status as static, it isn't moving but the trip didn't end. Taximeter still running.
- taximeter: If the taxi is moving it adds RATE_MOVING (0.05€/s), if it stopped but didn't end the trip it adds RATE_STOPPED(0.02€/s).

#### Back file
An object of the Taxi() class is created inside the meter variable. 
