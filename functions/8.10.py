strings_list = ['Hello Hello', 'Hello again Hello', 'This is list of Hello strings']
sent_messages = []



def send_messages():
	for string_list in strings_list:
		string_list = strings_list.pop()
		sent_messages.append(string_list)
send_messages()

print(sent_messages)
print(strings_list)
