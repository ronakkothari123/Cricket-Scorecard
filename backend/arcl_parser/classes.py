import json


class WicketTypes:
    NOT_OUT = "not out"
    CAUGHT = "caught"
    BOWLED = "bowled"
    CAUGHT_BOWLED = "c & b"
    RUN_OUT = "run out"


class Batsman(object):
    def __init__(self, name, how_out: WicketTypes, fielder: str, bowler: str, sixes: int, fours: int, runs: int,
                 balls: int) -> None:
        self.name = name
        self.how_out = how_out
        self.fielder = fielder
        self.bowler = bowler
        self.sixes = sixes
        self.fours = fours
        self.runs = runs
        self.balls = balls

    def to_dict(self):
        return {
            "name": self.name,
            "how_out": self.how_out,
            "fielder": self.fielder,
            "bowler": self.bowler,
            "sixes": self.sixes,
            "fours": self.fours,
            "runs": self.runs,
            "balls": self.balls
        }

    def json(self):
        return json.dumps(self.to_dict(), indent=4)


class Bowler(object):
    def __init__(self, name, overs, maidens, no_balls, wides, runs, wickets) -> None:
        self.name = name
        self.runs = runs
        self.overs = overs
        self.wickets = wickets
        self.wides = wides
        self.no_balls = no_balls
        self.maidens = maidens

    def to_dict(self):
        return {
            "name": self.name,
            "runs": self.runs,
            "overs": self.overs,
            "wickets": self.wickets,
            "wides": self.wides,
            "noBalls": self.no_balls,
            "maidens": self.maidens
        }

    def json(self):
        return json.dumps(self.to_dict(), indent=4)
