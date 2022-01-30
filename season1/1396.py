from collections import defaultdict

class UndergroundSystem:

    def __init__(self):
        # pair where its checkin, checkout -> list(duration)
        self.map = defaultdict(list)
        self.checkins = {}
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkins[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start, time = self.checkins[id]
        self.map[(start, stationName)].append(t - time)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        sum, count = 0, 0
        for rec in self.map[(startStation, endStation)]:
            sum += rec
            count += 1
        return sum / count


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
