from abc import ABC, abstractmethod
class BankingApp(ABC):
    def database(self):
        print(f"Connect to database successfully")
    @abstractmethod
    def security(self):
        pass 
class Mobile(BankingApp):

    def login_app(self):
        print("Login to Mobile Successfully.")

    def security(self):
        print("Security seems good. No hacking attempts detected.")

if __name__ == "__main__":
    mobile_app = Mobile()
    print(mobile_app)