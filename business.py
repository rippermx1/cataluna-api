from firebase import Service, Calendar


class Business:
    def __init__(self):
        self.service = Service()
        self.calendar = Calendar()

    def get_all_services(self):
        try:
            return self.service.get_all()
        except Exception as e:
            print(e)
            return None

    def get_avaliable_calendar_hours(self, date):
        try:
            return self.calendar.get_hours(date)
        except Exception as e:
            print(e)
            return None

    def confirm_calendar_hour(self, date, hour):
        try:
            return self.calendar.confirm_hour(date, hour)
        except Exception as e:
            print(e)
            return None
