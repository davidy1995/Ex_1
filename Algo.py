import json
import csv

import Building
import Calls


def __init__(self, calls, building, out):
    self.callList = Calls(calls)
    self.out = out
    self.building = Building(building)


def timeTo(self, call):
    fromTo = abs(call.src - self._currentFloor) + abs(call.dest - call.src)
    result = self._closeTime + self._startTime + (fromTo / self._speed) + self._stopTime + self._openTime
    return result

def allocate(self):
    if self.calls.src < self.building._minFloor or self.calls.src > self.building._maxFloor or self.calls.dest < self.building._minFloor or self.calls.dest > self.building._maxFloor:
        print("The floor does not exist :(")
    for i in Calls:
        if self.calls.status != 0:

