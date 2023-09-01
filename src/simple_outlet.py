from pylsl import StreamInfo, StreamOutlet

outlet = None


def main():

    info = StreamInfo("PythonStream", "Markers", 1, 0, 'string', '123456789')
    global outlet
    outlet = StreamOutlet(info)


def push(string):
    if outlet is not None:
        outlet.push_sample([string])


main()
