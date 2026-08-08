#!/usr/bin/env python3


def parse_config(file_path: str) -> dict[str, str]:
    config: dict[str, str] = {}
    with open(file_path, "r") as file:
        for line in file:
            line = line.strip()
            if line and not line.startswith("#"):
                key, value = line.split("=", 1)
                config[key.strip()] = value.strip()
    if config == {}:
        raise ValueError("Configuration file is empty or contains no valid entries.")
    return config


class MazeConfig:
    def __init__(self, width: int, height: int, entry: tuple[int, int],
                 exit_pos: tuple[int, int], output_file: str, perfect: bool):
        self.width = width
        self.height = height
        self.entry = entry
        self.exit_pos = exit_pos
        self.output_file = output_file
        self.perfect = perfect

    @classmethod
    def from_config(cls, file_path: str) -> "MazeConfig":
        config: dict[str, str] = {}
        with open(file_path, "r") as file:
            for line in file:
                line = line.strip()
                if line and not line.startswith("#"):
                    key, value = line.split("=", 1)
                    config[key.strip()] = value.strip()
        if config == {}:
            raise ValueError("Configuration file is empty or contains no valid entries.")
        try:
            width = int(config["WIDTH"])
            height = int(config["HEIGHT"])
            x, y = config["ENTRY"].split(",", 1)
            entry = (int(x), int(y))
            x, y = config["EXIT"].split(",", 1)
            exit_pos = (int(x), int(y))
            output_file = config["OUTPUT_FILE"]
            perfect = config.get("PERFECT", "False").lower() == "true"
        except KeyError as e:
            raise ValueError(f"Missing required configuration key: {e}")
        except ValueError as e:
            raise ValueError(f"Invalid value in configuration: {e}")
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive integers.")
        if not (0 <= entry[0] < width and 0 <= entry[1] < height):
            raise ValueError("Entry position must be within the maze dimensions.")
        if not (0 <= exit_pos[0] < width and 0 <= exit_pos[1] < height):
            raise ValueError("Exit position must be within the maze dimensions.")
        if entry == exit_pos:
            raise ValueError("Entry and exit positions cannot be the same.")
        return cls(width, height, entry, exit_pos, output_file, perfect)

def main() -> None:
    config_file_path = "config.txt"
    try:
        maze_config = MazeConfig.from_config(config_file_path)
        print("Maze configuration loaded successfully:")
        print(f"Width: {maze_config.width}")
        print(f"Height: {maze_config.height}")
        print(f"Entry: {maze_config.entry}")
        print(f"Exit: {maze_config.exit_pos}")
        print(f"Output File: {maze_config.output_file}")
        print(f"Perfect Maze: {maze_config.perfect}")
    except Exception as e:
        print(f"Error loading configuration: {e}")

if __name__ == "__main__":
    main()