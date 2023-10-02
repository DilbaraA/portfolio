from rest_framework import serializers


class UserSerializers(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.CharField()
    password = serializers.CharField()



# {
#     "username":"user",
#     "email": "none@mail.ru",
#     "password":"123"
# }
