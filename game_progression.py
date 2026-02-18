from __future__ import annotations

from dataclasses import dataclass, field
from typing import List


RANK_THRESHOLDS = [
    (0, "Rookie"),
    (120, "Bronze"),
    (260, "Silver"),
    (450, "Gold"),
    (700, "Platinum"),
    (1000, "Legendary"),
]


@dataclass
class Level:
    name: str
    difficulty: int

    def points_awarded(self) -> int:
        # Higher difficulty levels reward more points
        return 30 + (self.difficulty * 10)


@dataclass
class World:
    name: str
    levels: List[Level]


@dataclass
class Character:
    name: str
    lives: int = 5
    total_points: int = 0
    cleared_levels: List[str] = field(default_factory=list)

    def current_rank(self) -> str:
        rank = "Rookie"
        for threshold, rank_name in RANK_THRESHOLDS:
            if self.total_points >= threshold:
                rank = rank_name
        return rank

    def clear_level(self, world_name: str, level: Level) -> None:
        earned = level.points_awarded()
        self.total_points += earned
        self.cleared_levels.append(f"{world_name}: {level.name}")


WORLDS = [
    World(
        name="Grassland Gateway",
        levels=[
            Level("Mushroom Path", 1),
            Level("Koopa Hills", 2),
            Level("Pipe Panic", 2),
        ],
    ),
    World(
        name="Desert Dunes",
        levels=[
            Level("Sand Sprint", 2),
            Level("Pokey Pit", 3),
            Level("Sun Temple", 3),
        ],
    ),
    World(
        name="Ice Mountain",
        levels=[
            Level("Frost Slide", 3),
            Level("Penguin Pass", 4),
            Level("Blizzard Bridge", 4),
        ],
    ),
    World(
        name="Forest Fortress",
        levels=[
            Level("Vine Vault", 4),
            Level("Boo Woods", 5),
            Level("Castle Roots", 5),
        ],
    ),
    World(
        name="Sky Kingdom",
        levels=[
            Level("Cloud Climb", 5),
            Level("Paratroopa Parade", 6),
            Level("Thunder Tower", 6),
        ],
    ),
    World(
        name="Lava Castle",
        levels=[
            Level("Magma Run", 6),
            Level("Bowser Gate", 7),
            Level("Final Showdown", 8),
        ],
    ),
]


def play_story_mode(characters: List[Character], worlds: List[World]) -> None:
    print("=== STORY MODE: RISE THROUGH THE WORLDS ===")
    for world_index, world in enumerate(worlds, start=1):
        print(f"\nWorld {world_index}: {world.name}")
        for level in world.levels:
            for character in characters:
                before_rank = character.current_rank()
                character.clear_level(world.name, level)
                after_rank = character.current_rank()
                rank_note = ""
                if after_rank != before_rank:
                    rank_note = f"  (RANK UP! {before_rank} -> {after_rank})"
                print(
                    f"- {character.name} cleared {level.name} (+{level.points_awarded()} pts)."
                    f" Total: {character.total_points} | Rank: {after_rank}{rank_note}"
                )

    print("\n=== GAME COMPLETED ===")
    for character in characters:
        print(
            f"{character.name} finished {len(character.cleared_levels)} levels "
            f"with {character.total_points} points and reached {character.current_rank()} rank!"
        )


if __name__ == "__main__":
    heroes = [Character(name="Mario"), Character(name="Luigi")]
    play_story_mode(heroes, WORLDS)
