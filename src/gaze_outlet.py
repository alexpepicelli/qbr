from pylsl import StreamInfo, StreamOutlet

outlet = None


def main():

    info = StreamInfo("GazeStream", "Markers", 1, 0, 'string', '987654321')
    global outlet
    outlet = StreamOutlet(info)


def push(string):
    if outlet is not None:
        outlet.push_sample([string])


main()
