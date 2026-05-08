# proyecto1_Anahi
Taxímetro

## Taxi class file. Logic of the taximeter. Methods:
- start_journey: Resets fare to 0 and starts the trip by setting journey_active to True
- end_journey: It sets journey_active to False to signal the end of the trip and it returns the fare attribute
- set_moving: Changes the state of the taxi to movement.
- set_stopped: Sets the taxi's status as static, it isn't moving but the trip didn't end. Taximeter still running.
- taximeter: 