from app.repositories.UserRepository import UserRepository

class UserModel():
	
	def __init__(self):
		pass


	def checkUser(self, name, email):
		userRepo=UserRepository()
		hasUser=False
		userCount=userRepo.checkUser(name=name, email=email)
		
		if(userCount==0):
			hasUser=True
		
		return hasUser


	def createUser(self, name, email, password):
		userRepo=UserRepository()
		userRepo.createUser(name=name, email=email, password=password)

	
	def checkAndGetUserInfo(self, email, password):
		userRepo=UserRepository()
		userInfo=userRepo.getUserInfo(email=email, password=password)
		if userInfo:
			return userInfo[0]
		return False