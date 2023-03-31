from gi.repository import GLib
from pydbus import SessionBus  # Session or System Bus

bus = SessionBus()
BUS = "https://github.com/Harut23/SearchEngine2022"
loop = GLib.MainLoop()
INTERVAL = 2
message_count = 0



class DBusService_XML:  # method name="echo_string"
    """
    DBus Service XML definition
    type = "i" for integer, "S" string, "d" double, "as" list of string data
    """
    dbus = """
    <node>
        <interface name= "{}">
            <method name="echo_string">
                <arg type="s" name = "input" direction="in">
                </arg>
                <arg type="s" name="output" direction="out">
                </arg>
            </method>
        <interface>
    </node>
    """.format(BUS)


    def echo_string(self, input_string):
        "Echo the string"

        # return the input received
        return input_string


if __name__ == "__main__":

    bus.publish(BUS, DBusService_XML())
    loop.run()

