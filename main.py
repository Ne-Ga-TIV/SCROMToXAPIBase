import time
import random
from engine import XAPIGameEngine
from game_objects import Player, Item

if __name__ == "__main__":
    engine = XAPIGameEngine()
    player = Player("Player1")
    player.x, player.y = 0, 0
    engine.add_game_object(player)

    engine.add_controllable_object(player, {
        "w": "up",
        "s": "down",
        "a": "left",
        "d": "right"
    })

    try:
        print("Starting game with grid rendering:\n")

        while engine.running:
            items = []
            while len(items) < player.level:
                x, y = random.randint(0, 5), random.randint(0, 5)
                if (x, y) != (player.x, player.y):
                    items.append(Item(f"Item{len(items)}", x, y))

            for item in items:
                engine.add_game_object(item)

            engine.log_event("kuhiva", "started", f"Level{player.level}")

            while player.items_collected < player.level and player.remaining_moves > 0:
                engine.render_grid(6, 6, [player] + items, player)
                engine.handle_input()

                for item in items[:]:
                    if player.x == item.x and player.y == item.y:
                        print(f"{player.name} collected {item.name}!")
                        engine.log_event("kuhiva", "collected", item.name)
                        engine.remove_game_object(item)
                        items.remove(item)
                        player.items_collected += 1

                engine.update_game_objects(6, 6)

            if player.items_collected < player.level:
                print(f"{player.name} failed to complete the level in time.")
                engine.log_event("kuhiva", "failed", f"Level{player.level}")
                engine.stop()

            duration = round(time.time() - player.start_time, 2)
            engine.log_event("kuhiva", "completed", f"Level{player.level}", {
                "duration": engine.format_duration(duration),
                "extensions": {
                    "http://example.com/extensions/used_moves": player.used_moves
                }
            })
            engine.record_level_history(player.level, duration)

            player.reset_for_next_level()

    except KeyboardInterrupt:
        engine.display_level_history()
        engine.stop()
        print("Game stopped by user.")