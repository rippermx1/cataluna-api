import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import uuid
import os
import json

firebase_credentials = os.getenv('FIREBASE_CREDENTIALS')
cert = json.loads(
    firebase_credentials) if firebase_credentials else './default.json'
app = firebase_admin.initialize_app(credentials.Certificate(cert))


class FirebaseDatabase:
    def __init__(self):
        self.db = firestore.client(app)
        self.ref = None

    def create(self, service):
        pass

    def get(self, id):
        pass

    def get_all(self):
        pass

    def update(self, id, service):
        pass


class Service(FirebaseDatabase):
    SERVICES = 'services'

    def __init__(self):
        super().__init__()
        self.collection = self.db.collection(f'{self.SERVICES}')

    def create(self, service):
        doc = None
        index = 1
        try:
            service['uuid'] = uuid.uuid4().hex
            doc = self.collection.add(service)
            return doc[index]
        except Exception as e:
            print(e)
            return None

    def get(self, id):
        try:
            doc = self.collection.document(id).get()
            print(doc.to_dict())
            return doc.to_dict() if doc else None
        except Exception as e:
            print(e)
            return None

    def get_all(self):
        try:
            docs = self.collection.stream()
            services = []
            for doc in docs:
                services.append(doc.to_dict())
            return services
        except Exception as e:
            print(e)
            return None

    def update(self, id, service):
        try:
            self.collection.document(id).update(service)
        except Exception as e:
            print(e)
            return None


class Calendar(FirebaseDatabase):
    CALENDAR = 'calendar'
    YEARS = 'years'
    MONTHS = 'months'
    DAYS = 'days'
    HOURS = 'hours'

    def __init__(self):
        super().__init__()
        self.collection = self.db.collection(f'{self.CALENDAR}')

    def create_year(self, year):
        try:
            return self.collection.document(year).set({})
        except Exception as e:
            print(e)
            return None

    def create_month(self, year, month):
        try:
            return self.collection.document(year).collection(
                self.MONTHS).document(month).set({})
        except Exception as e:
            print(e)
            return None

    def create_day(self, year, month, date):
        try:
            return self.collection.document(year).collection(
                self.MONTHS).document(month).collection(
                self.DAYS).document(date).set({})
        except Exception as e:
            print(e)
            return None

    def create_hour(self, year, month, date, hour, data):
        try:
            return self.collection.document(year).collection(
                self.MONTHS).document(month).collection(
                self.DAYS).document(date).collection(
                self.HOURS).document(str(hour)).set(data)
        except Exception as e:
            print(e)
            return None

    def get(self, id):
        try:
            doc = self.collection.document(id).get()
            print(doc.to_dict())
            return doc.to_dict() if doc else None
        except Exception as e:
            print(e)
            return None

    def get_hours(self, date):
        try:
            year = date.split('-')[0]
            month = date.split('-')[1]
            month = month.lstrip('0')
            print(year, month)
            docs = self.collection.document(year).collection(
                self.MONTHS).document(month).collection(
                self.DAYS).document(date).collection(
                self.HOURS).stream()
            hours = []
            for doc in docs:
                if doc.to_dict()['label'] not in ['13:00 PM', '14:00 PM']:
                    hours.append(doc.to_dict())
            return hours
        except Exception as e:
            print(e)
            return None

    def confirm_hour(self, date, hour):
        try:
            print(date, hour)
            year = date.split('-')[0]
            month = date.split('-')[1]
            month = month.lstrip('0')
            print(year, month)
            self.collection.document(year).collection(
                self.MONTHS).document(month).collection(
                self.DAYS).document(date).collection(
                self.HOURS).document(hour).update({'available': False})
            return True
        except Exception as e:
            print(e)
            return None

    def update(self, id, schedule):
        try:
            self.collection.document(id).update(schedule)
        except Exception as e:
            print(e)
            return None
