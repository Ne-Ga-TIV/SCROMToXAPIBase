import asyncio
import aiohttp
import json
import os
from os import system
from pynput import keyboard
from tincan import Statement, Agent, Verb, Activity, Result

os.environ.setdefault("TERM", "xterm")

class XAPIGameEngine:
    def __init__(self):
        self.game_objects = []
        self.lrs_endpoint = "https://snake-game.lrs.io/xapi/statements"
        self.lrs_auth = ("kuhiva", "uchiow")
        self.running = True
        self.input_handler = {}
        self.listener = None
        self.level_history = []

    def add_game_object(self, game_object):
        self.game_objects.append(game_object)

    def remove_game_object(self, game_object):
        if game_object in self.game_objects:
            self.game_objects.remove(game_object)

    def clear_screen(self):
        system("clear" if os.name != "nt" else "cls")

    def add_controllable_object(self, game_object, controls):
        for key, direction in controls.items():
            self.register_input(key, lambda dir=direction: game_object.move(dir))

    def format_duration(self, seconds):
        return f"PT{int(seconds)}S"

    def log_xapi_statement(self, actor_name, verb_id, object_id, result=None):
        actor = Agent(mbox=f"mailto:{actor_name}@example.com", name=actor_name)
        verb = Verb(id=f"http://adlnet.gov/expapi/verbs/{verb_id}", display={"en-US": verb_id})
        obj = Activity(id=f"http://example.com/objects/{object_id}", definition={
            "name": {"en-US": object_id},
            "description": {"en-US": f"Activity related to {object_id}"}
        })

        statement = Statement(actor=actor, verb=verb, object=obj)
        if result:
            statement.result = Result(**result)

        asyncio.run(self._send_to_lrs(statement))

    async def _send_to_lrs(self, statement):
        headers = {
            "X-Experience-API-Version": "1.0.3",
            "Content-Type": "application/json"
        }
        statement_dict = json.loads(statement.to_json())
        async with aiohttp.ClientSession(auth=aiohttp.BasicAuth(*self.lrs_auth)) as session:
            async with session.post(self.lrs_endpoint, json=statement_dict, headers=headers) as response:
                if response.status in (200, 204):
                    print(f"[LRS]: Sent: {statement_dict}")
                else:
                    print(f"[LRS]: Failed with status {response.status}, response: {await response.text()}")

    def log_event(self, actor_name, verb, obj, result=None):
        self.log_xapi_statement(actor_name, verb, obj, result)

    def update_game_objects(self, grid_width, grid_height):
        for obj in self.game_objects:
            obj.update(grid_width, grid_height)

    def render_grid(self, width, height, objects, player):
        self.clear_screen()
        grid = [["." for _ in range(width)] for _ in range(height)]
        for obj in objects:
            if hasattr(obj, 'x') and hasattr(obj, 'y') and hasattr(obj, 'symbol'):
                if 0 <= obj.y < height and 0 <= obj.x < width:
                    grid[obj.y][obj.x] = obj.symbol
        for row in grid:
            print(" ".join(row))
        print(f"\nRemaining moves: {player.remaining_moves}\n")

    def register_input(self, key, callback):
        self.input_handler[key] = callback

    def handle_input(self):
        def on_press(key):
            try:
                if key.char in self.input_handler:
                    self.input_handler[key.char]()
                    raise keyboard.Listener.StopException
                elif key == keyboard.Key.esc:
                    self.stop()
                    raise keyboard.Listener.StopException
            except AttributeError:
                pass

        self.listener = keyboard.Listener(on_press=on_press, suppress=True)
        self.listener.start()
        self.listener.join()

    def record_level_history(self, level, duration):
        self.level_history.append({"level": level, "duration": duration})

    def display_level_history(self):
        print("\nLevel History:")
        for record in self.level_history:
            print(f"Level {record['level']} completed in {record['duration']} seconds.")

    def stop(self):
        self.running = False
        if self.listener:
            self.listener.stop()
