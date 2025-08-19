import sys
import rpyc


class RemoteEV3:
    def __init__(self, ip="192.168.10.113", port=18861):
        self.ip = ip
        self.port = port

    def connect(self):
        self.c = rpyc.connect(self.ip, self.port)

    def disconnect(self):
        self.c.root.close()

    def execute(self, command, *args):
        commands = {
            "output": self.c.root.change_output,
            "run": self.c.root.run_forever,
            "run_abs": self.c.root.run_abs_pos,
            "run_timed": self.c.root.run_timed,
            "run_direct": self.c.root.run_direct,
            "reset": self.c.root.reset,
            "stop": self.c.root.stop,
        }
        try:
            commands[command.lower()](*args)
        except TypeError:
            print("Wrong arguments given")
        except KeyError:
            print("Command not recognized")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        print(sys.argv)
        ip = sys.argv[0]
    ev3 = RemoteEV3()
    ev3.connect()
    print("Awaiting commands:")
    while True:
        try:
            command = input(">").split()
            assert command != []
            command = [int(x) if x.isdigit() else x for x in command]
        except AssertionError:
            print("No input given")
            continue

        if command[0] == "close":
            break

        ev3.execute(*command)
