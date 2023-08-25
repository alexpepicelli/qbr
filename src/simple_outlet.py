from pylsl import StreamInfo, StreamOutlet

outlet = None


def main():
    h = hash("PythonStream")
    info = StreamInfo("PythonStream", "Markers", 1, 0, 'string', h)
    global outlet
    outlet = StreamOutlet(info)


def push(string):
    if outlet is not None:
        outlet.push_sample(string)


main()
