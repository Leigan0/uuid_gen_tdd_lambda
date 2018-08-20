from event_data_extractor import EventDataExtractor

def handle(event, context):
    print(event)
    dataExtractor = EventDataExtractor(event)
    return dataExtractor.get_data()
