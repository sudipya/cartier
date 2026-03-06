from pymongo import MongoClient
from config import settings

class Database:
    def __init__(self):
        self.client = MongoClient(settings.MONGO_URI)
        self.db = self.client[settings.DATABASE_NAME]
        self.logs = self.db["attack_logs"]

    def log_attack(self, payload, attack_type, confidence, evidence):
        record = {
            "payload": payload,
            "attack_type": attack_type,
            "confidence": confidence,
            "evidence": evidence
        }
        self.logs.insert_one(record)

    def get_logs(self):
        return list(self.logs.find({}, {"_id": 0}))

db = Database()
