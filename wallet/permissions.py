from rest_framework.permissions import BasePermission,SAFE_METHODS

class IsGETOrPatch(BasePermission):
	def has_permission(self,request,view):
		allowed_methods=['GET','PATCH']
		if request.method in allowed_methods:
			return True
		else:
			return False
