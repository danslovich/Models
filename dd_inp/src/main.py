#!/usr/bin/env python
import threading
import rospy
from std_msgs.msg import String
import sys, select, termios, tty

class inpPub(threading.Thread):
    def __init__(self, rate):
        super(inpPub, self).__init__()
        self.publisher   = rospy.Publisher('dd_inp', String, queue_size = 1)
        self.condition   = threading.Condition()
        self.done        = False
        self.action      = ''
        if rate != 0.0:
            self.timeout = 1.0 / rate
        else:
            self.timeout = None
        self.start()

    def update(self, action):
        self.action = action
        self.condition.acquire()
        self.publisher.publish(action)
        self.condition.notify()
        self.condition.release()

    def stop(self):
        self.done = True
        self.update('stop')
        self.join()

def getKey(key_timeout):
    tty.setraw(sys.stdin.fileno())
    rlist, _, _ = select.select([sys.stdin], [], [], key_timeout)
    if rlist:
        key = sys.stdin.read(1)
    else:
        key = ''
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key

if __name__=="__main__":
    msg = """
    Reading keyboard input
    ----------------------
               W

               ^
       A     < + >     D
               v

               S
    ----------------------

    CTRL-C to quit
    """

    moveBindings = {
        'w':'forward',
        's':'backward',
        'a':'l_rotate',
        'd':'r_rotate'
    }
    rospy.init_node('dd_inp')
    settings    = termios.tcgetattr(sys.stdin)
    action      = ''
    repeat      = rospy.get_param("~repeat_rate", 0.0)
    key_timeout = rospy.get_param("~key_timeout", 0.0)

    if key_timeout == 0.0:
        key_timeout = None

    pub_thread = inpPub(repeat)

    try:
        print(msg)
        while(1):
            key = getKey(key_timeout)
            if key in moveBindings.keys():
                action = moveBindings[key]
            else:
                if key == '':
                    continue
                if (key == '\x03'):
                    break
                action = 'stop'
            pub_thread.update(action)

    except Exception as e:
        print(e)

    finally:
        pub_thread.stop()
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)