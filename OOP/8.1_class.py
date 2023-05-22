class Phone:
    color = 'black'
    features = ['camera', 'sensor', 'water proof']

    def call(self):
        print("cring cring cring")

    def send_sms(self, number, text):
        sms = f"sending sms: {text} to {number}"
        return sms

my_phone = Phone()
my_phone.call()
sms = my_phone.send_sms('01715529212', 'I missed to miss you')
print(sms)