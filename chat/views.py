from django.shortcuts import render,redirect
from chat.models import room,messages
from django.http import HttpResponse,JsonResponse


def home (request):
    return render(request,'home.html')

def Room(request,Roomname):
    username=request.GET.get('username')
    room_details=room.objects.get(name=Roomname)

    return render(request,'room.html',
    {
        'room_details':room_details,
        'username':username,
        'roomname':Roomname
    })

def checkview(request):
    if request.method=='POST':
        room_name=request.POST['room_name']
        username=request.POST['username']

        if room.objects.filter(name=room_name).exists():
           return redirect('/'+room_name+'/?username='+username)
        else:
            new_room=room.objects.create(name=room_name)
            new_room.save()
            return redirect('/'+room_name+'/?username='+username)

        
def send(request):
    username=request.POST['username']
    room_id=request.POST['room_id']
    message=request.POST['message']

    new_message=messages.objects.create(roomid=room_id,message=message,user=username)
    new_message.save()
    return HttpResponse('Message sent Successfully')

def getmessages(request,Roomname):
    room_details=room.objects.get(name=Roomname)
    tempmessage=messages.objects.filter(roomid=room_details.id)
    return JsonResponse({"messages":list(tempmessage.values())})