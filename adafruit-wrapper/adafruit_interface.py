from Adafruit import Data


class IAdafruit:

    def __init__(self):
        pass

    def create_feed(self, name):
        pass

    def get_feed(self, name):
        pass

    def get_all_feeds(self):
        pass

    def delete_feed(self, name):
        pass

    def send_data_to_feed(self, feed_name, data: Data):
        pass

    def send_list_data_to_feed(self, feed_name, data_list: list[Data]):
        pass

    def get_last_data(self, feed_name):
        pass

    def subscribe_feed(self, name):
        pass

