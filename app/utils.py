from django.core.mail import send_mail

def send_post_created_email(post):
    subject = 'New Post Created'
    greeting = f'Hello,'
    message = f'{greeting}\n\nA new post titled "{post.title}" has been created.'
    from_email = 'waghbhushan805@gmail.com'
    recipient_list = ['kbaviskar001@gmail.com']  # Replace with the recipient's email address

    send_mail(subject, message, from_email, recipient_list)
