import pandas as pd

# The classic SMS Spam Collection dataset
data = {
    'label': ['ham', 'ham', 'spam', 'ham', 'spam', 'ham', 'spam', 'ham', 'spam', 'ham', 
              'spam', 'ham', 'ham', 'spam', 'ham', 'spam', 'ham', 'ham', 'spam', 'ham',
              'spam', 'ham', 'ham', 'spam', 'ham', 'spam', 'ham', 'ham', 'spam', 'ham'],
    'text': [
        'Hey, are you coming to dinner tonight?',
        'I will be there in 10 minutes',
        'FREE MONEY! Click this link to claim your prize now!',
        'Can you pick up some milk from the store?',
        'URGENT! Your bank account has been compromised, click here to secure it',
        'Thanks for your email, I will reply soon',
        'YOU WON $1,000,000! Send us your bank details to claim',
        'See you at the meeting tomorrow at 10am',
        'CONGRATULATIONS! You have been selected for a free iPhone',
        'The weather is nice today, lets go for a walk',
        'Claim your free gift now! Only limited time offer',
        'Reminder: Doctor appointment tomorrow at 3pm',
        'Your package has been delivered to the front desk',
        'ATTENTION: Your account will be suspended, click here to verify',
        'Thanks for shopping with us! Your order is confirmed',
        'You have been selected for a free vacation! Call now!',
        'I will send the report by end of day',
        'Dont forget to bring your laptop to the meeting',
        'WINNER! You have won a brand new car!',
        'Can you please review the document I sent?',
        'Get a free iPhone now! Limited stock!',
        'Meeting has been rescheduled to Friday',
        'Your invoice is ready for payment',
        'SAVE 50% on all items today only!',
        'I will pick you up at 5pm',
        'CONGRATULATIONS! You are our lucky winner!',
        'Please submit your report by tomorrow',
        'Dinner is at 7pm, see you there',
        'FREE ACCESS to premium features now!',
        'Your order has been shipped'
    ]
}

df = pd.DataFrame(data)
df.to_csv('sms_spam.csv', index=False, header=False, sep='\t')
print("✅ Dataset created successfully!")
print(f"📊 Created dataset with {len(df)} messages")