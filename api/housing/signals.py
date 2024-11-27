'''
Copyright 2023 Ashwattha Phatak, Anish Mulay, Akshay Dongare

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''
# signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import Lease, User
import requests
from django.conf import settings

def send_mail(mail, subject, text):
    if mail == "" or "@gmail.com" not in mail or subject == "" or text == "":
        raise ValueError()
    api_key = settings.API_KEY
    domain = settings.DOMAIN
    from_address = settings.FROM
    api_key = api_key
    domain = domain
    s = f"https://api.mailgun.net/v3/{domain}/messages"
    return requests.post(s,
        auth=("api", api_key),
        data={
            "from": from_address,
            "to": [mail],
            "subject": subject,
            "text": text
            })

@receiver(post_save, sender=Lease)
def send_lease_created_email(sender, instance, created, **kwargs):
    if created:
        tenant = User.objects.get(username=instance.tenant_name)
        owner = User.objects.get(username=instance.ownername)
        subject = f"Lease Created between owner: {owner}, tenant:{tenant}"
        text = f"The lease is created between owner: {owner}, tenant:{tenant} for {instance.flat_identifier}\nDuration - from: {instance.lease_start_date} to {instance.lease_end_date}"
        response1 = send_mail(owner.contact_email, subject, text)
        response2 = send_mail(tenant.contact_email, subject, text)
        if response1.status_code != 200 or response2 != 200:
            print(f"Request failed: response1 status code = {response1.status_code}, response2 status code = {response2.status_code}")
            