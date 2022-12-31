from django.http import JsonResponse ,Http404  ,HttpResponse
from django.shortcuts import render
from rest_framework import generics
from rest_framework import status
from rest_framework.permissions import AllowAny
from moonch3api.models import Note ,UserDetail
from django.db.models import Q
from moonch3api.serializers import NoteSerializer ,UserInfoSerializer 

# Create your views here.

#for sysinfo
import platform , os, sys , random 


class HomeSweetHome( generics.GenericAPIView ) :
    permission_classes = (AllowAny,)
    serializer_class = NoteSerializer
    


    def get(self , request , *args  , **kwargs ) :
        u = request.accepted_media_type
        print( dir( u ) , u)
        return JsonResponse({
            'data' : 'data is Empty ',
            'oj' :'',
        } , status=status.HTTP_200_OK)

    def post(self, request ):
        da = request.POST.get('master')
        print(da)
        data = Note.objects.all()
        serialzerdata = NoteSerializer(data , many=True , context={'request': request} )
        return JsonResponse({
            'data' : serialzerdata.data,
        } , status=status.HTTP_200_OK)



class UserNote(generics.ListAPIView ) :
    permission_classes = (AllowAny , )

    def get ( self , request , *args , **kwargs ) :
        data = {
            'Note' : 1,
        }
        return JsonResponse(data , status=status.HTTP_200_OK)


class SystemInfo :
    en = sys.getdefaultencoding()

    def __init__(self , **opt ):
        self.user = 'trsh'

    @classmethod
    def guessNumber(self,**opt):
        data = opt.get('guessme')
        return data

    @classmethod
    def dataSystem ( self, request  , *args , **kwargs ) :
        guess_game_dict = {}
        point = 0
        
        data = {
            'system' : platform.platform() ,
            'header' : request.headers['User-agent'],
            #'cookies' : request.headers['Cookie']
            
        }
        max_num = request.GET.get('max') if request.GET.get('max') != None else 10
        
        try :
            guessnumber = request.GET.get('q') if request.GET.get('q') != None else False
            if guessnumber :
                data.update({'Guess_Game' : guess_game_dict,})
                rdata = random.randint(1,int(max_num))
                guess_game_dict.update({'Max-Number ' : rdata })
                if type(int(guessnumber)) == int :
                    guess_game_dict.update({
                        'answer' : guessnumber,
                    })

                if int(guessnumber) == rdata :
                    point += 10
                    guess_game_dict.update({'ans' : {
                        'message' : 'Waw you did Great' ,
                        'point' : point , 
                    },  })
        except ValueError :
            data.update({
                'message' : 'max Support only integer',
            })
        except Exception as e:
            data.update({
                'messages' : 'this is too Much %s'%(e),
            })

                

        return JsonResponse(data , status = status.HTTP_200_OK)


class Dev( generics.GenericAPIView ):
    dict = {
        'dev' : [ {

            'id' : 'monster_1',
            'name' : 'Trustful shylla',
            'DOB' : 'empty',
        },
        {
            'id' : 'monster_1',
            'name' : 'Trustful shylla',
            'DOB' : 'empty',
        }
        ]
        
        

    }
    def __init__(self , **kw) :
        self.getdev = 1

    def get(self , request , *args , **kwargs) :
        return JsonResponse(self.dict , status=status.HTTP_200_OK)



# get version of development

class Version( generics.GenericAPIView ) :

    def get(self, request , *args , **kwargs ) -> None :
        data = {
            'message' : 'Get method Not allow'
        }

        return JsonResponse( data , status=status.HTTP_202_ACCEPTED)

    def post(self, request , *args , **kwargs) :
        ch = request.POST.get('version')
        if ch == None:
            return JsonResponse({
                'message' : 'data is Empty',
                'eg':'curl http://api.localhost:8000/ver/ --form "v=1"',
            },
            status=status.HTTP_200_OK)

        elif ch != ' '.strip():

            data = {
                'message' : 'Post method Not allow'
            }

            return JsonResponse( data , status=status.HTTP_202_ACCEPTED)

        raise Http404

class UserInfo( generics.GenericAPIView ) :
    permission_classes = (AllowAny,)
    serializer_class = UserInfoSerializer 

    def get(self , request , *args  , **kwargs ) :
        return JsonResponse({
            'data' : 'data is Empty here info ',
            'oj' :'',
        } , status=status.HTTP_200_OK)

    def post(self, request ):
        da = request.POST.get('master')
        if da == 'trsh':
            data = UserDetail.objects.all()
            serialzerdata = UserInfoSerializer(data , many=True , context={'request': request} )
            return JsonResponse({
                'data' : serialzerdata.data,
            } , status=status.HTTP_200_OK)

        return JsonResponse({
                'message' : 'Unauthorized',
            } , status=status.HTTP_400_BAD_REQUEST)
