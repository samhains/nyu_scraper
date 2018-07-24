import requests
import boto3

from bs4 import BeautifulSoup
#Next, log in to the server
import boto3

from botocore.exceptions import ClientError

# Replace sender@example.com with your "From" address.
# This address must be verified with Amazon SES.
SENDER = "sdhains2@gmail.com"
import time 
# Replace recipient@example.com with a "To" address. If your account
# is still in the sandbox, this address must be verified.
RECIPIENT = "sam@samhains.com"

# Specify a configuration set. If you do not want to use a configuration
# set, comment the following variable, and the
# ConfigurationSetName=CONFIGURATION_SET argument below.
# CONFIGURATION_SET = "ConfigSet"

# If necessary, replace us-west-2 with the AWS Region you're using for Amazon SES.
AWS_REGION = "us-west-2"

# The subject line for the email.
SUBJECT = "Amazon SES Test (SDK for Python)"

# The email body for recipients with non-HTML email clients.
BODY_TEXT = ("Amazon SES Test (Python)\r\n"
             "This email was sent with Amazon SES using the "
             "AWS SDK for Python (Boto)."
            )

# The HTML body of the email.
BODY_HTML = """<html>
<head></head>
<body>
</body>
</html>
            """

# The character encoding for the email.
CHARSET = "UTF-8"

# Create a new SES resource and specify a region.
client = boto3.client('ses',region_name=AWS_REGION)

def send_email(body_text, subject):
# Try to send the email.
	try:
	    #Provide the contents of the email.
	    response = client.send_email(
		Destination={
		    'ToAddresses': [
			RECIPIENT,
		    ],
		},
		Message={
		    'Body': {
			'Html': {
			    'Charset': CHARSET,
			    'Data': BODY_HTML,
			},
			'Text': {
			    'Charset': CHARSET,
			    'Data': body_text,
			},
		    },
		    'Subject': {
			'Charset': CHARSET,
			'Data': subject,
		    },
		},
		Source=SENDER,
		# If you are not using a configuration set, comment or delete the
		# following line
		# ConfigurationSetName=CONFIGURATION_SET,
	    )
	# Display an error if something goes wrong.
	except ClientError as e:
	    print(e.response['Error']['Message'])
	else:
	    print("Email sent! Message ID:"),
	    print(response['MessageId'])

def check_nyu():
    url = "https://m.albert.nyu.edu/app/catalog/classsection/NYUNV/1188/22604"

    r  = requests.get(url)

    data = r.text

    soup = BeautifulSoup(data, "html.parser")

    for link in soup.find_all(text="Closed"):
        if link == "Closed":
		timestr = time.strftime("%Y%m%d-%H%M%S") 
		with open("/home/ubuntu/Code/nyu_scraper/test.txt", "a") as myfile:     
			myfile.write("{} : CLOSED\n".format(timestr))
        else:
		with open("/home/ubuntu/Code/nyu_scraper/test.txt", "a") as myfile:     
			myfile.write("{} : OPEN\n".format(timestr))
		send_email("waitlist open", "waitlist open")

check_nyu()
