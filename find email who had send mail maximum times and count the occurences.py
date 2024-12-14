# WAP to read mbox-short.txt and find email who had send mail maximum times and count the occurences
email_counts = {}
max_count = 0
max_email = ""

f = open("mbox-short.txt", "r")
data = f.readlines()

for i in data:
    if i.startswith("From:"): 
        words = i.split()
        email = words[1]  
        
        # Count occurrences of each email address
        if email in email_counts:
            email_counts[email] += 1
        else:
            email_counts[email] = 1

# Find the email with the maximum occurrences
for email, count in email_counts.items():
    if count > max_count:
        max_count = count
        max_email = email

print(f"The Most Repetitive Email is: {max_email} with {max_count} Occurrences.")
