# Should use 900x1600 , and change name LD to "suppver_v"
import pygetwindow as gw

# Get windows with name "suppver_v"
def moveTo():
    windows = gw.getWindowsWithTitle('supper_v')

    # Move to 0,0
    if len(windows) != 0:
        print(windows[0])
        print("Move to")
        windows[0].moveTo(0,0)
