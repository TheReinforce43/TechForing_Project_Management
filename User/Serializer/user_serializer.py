from rest_framework import  serializers 
# from User.models import Users 
from django.core.validators import validate_email  
from django.contrib.auth import  authenticate ,get_user_model
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from django.core.exceptions import ValidationError

Users= get_user_model()

class SignUpUserSerializer(serializers.ModelSerializer):

    class Meta:
        model=Users
        fields = ['id', 'email', 'Username', 'phone_number', 'password', 'date_joined','profile_image']
        extra_kwargs = {
            'password': {'write_only': True},
            'phone_number': {'required': False},
            'date_joined': {'required': False},
            'profile_image': {'required': False},
            }

    def validate_email(self,value):

        try:
            validate_email(value)
        
        except ValidationError:
            raise serializers.ValidationError('Invalid Email Format')
        
        return value 
    
    # def validate_phone_number(self,value):

    #     try:
    #         if 
        
    
    def create(self,validated_data):
        print("Validated data:", validated_data)  # Debugging statement
        try:
            user = Users.objects.create_user(
                Username=validated_data['Username'],
                email=validated_data['email'],
                password=validated_data['password'],
                profile_image= validated_data.get('profile_image'),
                date_joined= validated_data.get('date_joined'),
                phone_number = validated_data.get('phone_number'),
        
            )

            return user 
        
        except Exception as e:
            raise serializers.ValidationError('Error Occured: '+ str(e))



# User login serializers 

class LoggedInUserSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)
    access_token = serializers.SerializerMethodField()
    refresh_token = serializers.SerializerMethodField()
    user= SignUpUserSerializer(read_only=True)


    def get_access_token(self,obj):
        return obj['access_token']
    
    def get_refresh_token(self,obj):
        return obj['refresh_token']
    


    def validate(self,data):
        email=data.get('email')
        password=data.get('password')
        
        user = authenticate(email=email,password=password)

        if user and user.is_active:
            refresh = RefreshToken.for_user(user)
            data['access_token'] =str(refresh.access_token)
            data['refresh_token'] =str(refresh)
            data['user'] = SignUpUserSerializer(user).data
            data['success'] = True

        else:
            raise serializers.ValidationError('Invalid Credentials')
        
        return data
    


# User Logout Serializer 


class  UserLogoutSerializer(serializers.Serializer):

    refresh_token =serializers.CharField()


    def validate(self,data):
        refresh_token = data.get('refresh_token')

        if not refresh_token:
            raise serializers.ValidationError('Refresh token is required')
        
        return data 
    
    def save(self,**kwargs):
        refresh_token  = self.validate_data['refresh_token']

        try:
            refresh_token_obj = RefreshToken(refresh_token)
            refresh_token_obj.blacklist()
        except TokenError :
            raise serializers.ValidationError('Invalid or expired token')
            




           




