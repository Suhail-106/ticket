from django.http import JsonResponse
from django.shortcuts import render
from .models import Ticket
import qrcode
from django.conf import settings
import os

def home(request):
    return render(request, "index.html")

def redeem_ticket(request, code):
    try:
        ticket = Ticket.objects.get(code=code)

        if ticket.is_redeemed:
            return JsonResponse({"status": "already used"})

        ticket.is_redeemed = True
        ticket.save()

        return JsonResponse({"status": "successfully redeemed"})

    except Ticket.DoesNotExist:
        return JsonResponse({"status": "invalid ticket"})
    



def generate_ticket(request):
    ticket = Ticket.objects.create()

    os.makedirs(settings.MEDIA_ROOT, exist_ok=True)

    # 🔥 FULL URL QR me daal
    qr_data = f"http://127.0.0.1:8000/redeem/{ticket.code}/"

    img = qrcode.make(qr_data)

    path = os.path.join(settings.MEDIA_ROOT, f"{ticket.code}.png")
    img.save(path)

    return JsonResponse({
        "code": str(ticket.code),
        "qr": f"/media/{ticket.code}.png"
    })