LOTW_USER_FIELDS = {
    'callsign': 0, # user callsign used
    'activity_date': 1,  # last activity date
    'activity_time': 2  # last activity time
}


class LotwUserActivity(object):
    def __init__(self, data):
        super(LotwUserActivity, self).__init__()

        if not isinstance(data, list):
            raise ValueError("Expect data to be a list")

        self.callsign = data[LOTW_USER_FIELDS['callsign']]
        self.activity_date = data[LOTW_USER_FIELDS['activity_date']]
        self.activity_time = data[LOTW_USER_FIELDS['activity_time']]

    def to_dict(self):
        return self.__dict__
