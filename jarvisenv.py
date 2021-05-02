"""
Jarvis factory simulation environment.
"""

import tracks

# SIMULATION TIME

SIMULATION_TIME = 0

def time():
    "returns absolut simulation time"
    return SIMULATION_TIME

def sleep(delay):
    "cause simulation time to progress"
    global SIMULATION_TIME
    SIMULATION_TIME += delay

def reset_time():
    "resets time for test fixture"
    global SIMULATION_TIME
    SIMULATION_TIME = 0

JARVIS_TRACKS = tracks.Tracks([
    tracks.Track('A', 'B', 20),
    tracks.Track('B', 'A', 30),
    tracks.Track('B', 'C', 20),
    tracks.Track('C', 'D', 20),
    tracks.Track('D', 'A', 10),
    ])
