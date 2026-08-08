#!/usr/bin/env python3

def main() -> None:
	try:
		with open("config.txt", "r") as file:
			for line in file:
				line = line.strip()
				if line and not line.startswith("#"):
					key, value = line.split("=")
					print(f"{key.strip()} = {value.strip()}")
	except FileNotFoundError as e:
		print(f"Error: {e}")


if __name__ == "__main__":
	main()