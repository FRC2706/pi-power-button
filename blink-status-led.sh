#! /bin/sh

### BEGIN INIT INFO
# Provides:          blink-status-led.py.py
# Required-Start:    $remote_fs $syslog
# Required-Stop:     $remote_fs $syslog
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
### END INIT INFO

# If you want a command to always run, put it here

# Carry out specific functions when asked to by the system
case "$1" in
  start)
    echo "Starting blink-status-led.py"
    /usr/local/bin/blink-status-led.py &
    ;;
  stop)
    echo "Stopping blink-status-led.py"
    pkill -f /usr/local/bin/blink-status-led.py
    ;;
  *)
    echo "Usage: /etc/init.d/blink-status-led.sh {start|stop}"
    exit 1
    ;;
esac

exit 0
