import json
from django.utils import timezone
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.db.transaction import atomic, non_atomic_requests

from .models import WebhookMessage


@csrf_exempt
@require_POST
@non_atomic_requests
def test(request):
    payload = json.loads(request.body)
    WebhookMessage.objects.create(
        received_at=timezone.now(),
        payload=payload,
    )
    process_webhook_payload(payload)
    return HttpResponse("Webhook received!")
    # return HttpResponse(payload, content_type="application/json")

@atomic
def process_webhook_payload(payload):
    # TODO: business logic
    print("Payload received from Webhook is: ", payload)
    print("Processed payload...")
