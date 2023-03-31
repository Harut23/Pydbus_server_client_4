from pydbus import SessionBus
from gi.repository import GLib
import random
bus = SessionBus()
BUS = "org.example.demo.test"
server_object = bus.get(BUS)
loop = GLib.MainLoop()
INTERVAL = 2


def make_method_call_client_4():

    name_list = ["Harut", "Narek", "Arman", "Davit", "Eduard"]
    name = name_list[random.randint(0, len(name_list)-1)]
    print("name to be sent to server: {}".format(name))
    # Client sends randomly selected "name" data
    reply = server_object.echo_string(name)  # server replies with the name
    print("message echoed from server: {}".format(reply))

    return True



if __name__ =="__main__":
    print("Starting Client Demo ...")
    # call function to make a method call.

    #GLib to run repeating function every 2 secconds
    GLib.timeout_add_seconds(interval=INTERVAL,
                             function=make_method_call_client_4())
    loop.run()
