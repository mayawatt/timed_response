import json
import csv
import pandas as pd

#DONT UNDERSTAND
with open ('./inputjson.json') as get_json:
	read_content = json.load(get_json)

#print(type(read_content['users']))


#takes stimulus data mess like '["<p><font size=\\"+3\\"><u>to wring</u></font></p>","<p><font size=\\"+3\\">wrang</font></p>"]' and returns 'wrang'
#and returns 'to wring'
#UNDERSTOOD
def cleanStim1 (string):
	return( "to" + string.split('to')[1].split('<')[0])


#Takes a string like '["<p><font size=\\"+3\\"><u>to wring</u></font></p>","<p><font size=\\"+3\\">wrang</font></p>"]' 
#and returns 'wrang'
#UNDERSTOOD
def cleanStim2 (string):
	return(string.split(',')[1].split('>')[2].split('<')[0])


# def getMeta (metaMess):
# 	rightDict = metaMess['rawResponses']
# 	print(rightDict)

# stranged = '''{'rt': 65734, 'preamble': '', 'superq': 'Please answer the following questions:', 'rawResponses': {'Q0': {'text': '<strong>What language do you speak most often?</strong>', 'options': ['Afrikaans', 'Albanian', 'Arabic', 'Armenian', 'Basque', 'Bengali', 'Bulgarian', 'Catalan', 'Cambodian', 'Chinese(Mandarin)', 'Croatian', 'Czech', 'Danish', 'Dutch', 'English', 'Estonian', 'Fiji', 'Finnish', 'French', 'Georgian', 'German', 'Greek', 'Gujarati', 'Hebrew', 'Hindi', 'Hungarian', 'Icelandic', 'Indonesian', 'Irish', 'Italian', 'Japanese', 'Javanese', 'Korean', 'Latin', 'Latvian', 'Lithuanian', 'Macedonian', 'Malay', 'Malayalam', 'Maltese', 'Maori', 'Marathi', 'Mongolian', 'Nepali', 'Norwegian', 'Persian', 'Polish', 'Portuguese', 'Punjabi', 'Quechua', 'Romanian', 'Russian', 'Samoan', 'Serbian', 'Slovak', 'Slovenian', 'Spanish', 'Swahili', 'Swedish', 'Tamil', 'Tatar', 'Telugu', 'Thai', 'Tibetan', 'Tonga', 'Turkish', 'Ukrainian', 'Urdu', 'Uzbek', 'Vietnamese', 'Welsh', 'Xhosa'], 'allowMultipleSelections': False, 'required': True, 'placeholder': 'Select language'}, 'A0': 'English', 'Q1': {'text': '<strong>What language do you speak at home?</strong>', 'options': ['Afrikaans', 'Albanian', 'Arabic', 'Armenian', 'Basque', 'Bengali', 'Bulgarian', 'Catalan', 'Cambodian', 'Chinese(Mandarin)', 'Croatian', 'Czech', 'Danish', 'Dutch', 'English', 'Estonian', 'Fiji', 'Finnish', 'French', 'Georgian', 'German', 'Greek', 'Gujarati', 'Hebrew', 'Hindi', 'Hungarian', 'Icelandic', 'Indonesian', 'Irish', 'Italian', 'Japanese', 'Javanese', 'Korean', 'Latin', 'Latvian', 'Lithuanian', 'Macedonian', 'Malay', 'Malayalam', 'Maltese', 'Maori', 'Marathi', 'Mongolian', 'Nepali', 'Norwegian', 'Persian', 'Polish', 'Portuguese', 'Punjabi', 'Quechua', 'Romanian', 'Russian', 'Samoan', 'Serbian', 'Slovak', 'Slovenian', 'Spanish', 'Swahili', 'Swedish', 'Tamil', 'Tatar', 'Telugu', 'Thai', 'Tibetan', 'Tonga', 'Turkish', 'Ukrainian', 'Urdu', 'Uzbek', 'Vietnamese', 'Welsh', 'Xhosa'], 'allowMultipleSelections': False, 'required': True, 'placeholder': 'Select language'}, 'A1': 'English', 'Q2': {'text': '<strong>What is your mother tongue? (i.e. the first language you learned at home during childhood and still understand to this day.)</strong>', 'options': ['Afrikaans', 'Albanian', 'Arabic', 'Armenian', 'Basque', 'Bengali', 'Bulgarian', 'Catalan', 'Cambodian', 'Chinese(Mandarin)', 'Croatian', 'Czech', 'Danish', 'Dutch', 'English', 'Estonian', 'Fiji', 'Finnish', 'French', 'Georgian', 'German', 'Greek', 'Gujarati', 'Hebrew', 'Hindi', 'Hungarian', 'Icelandic', 'Indonesian', 'Irish', 'Italian', 'Japanese', 'Javanese', 'Korean', 'Latin', 'Latvian', 'Lithuanian', 'Macedonian', 'Malay', 'Malayalam', 'Maltese', 'Maori', 'Marathi', 'Mongolian', 'Nepali', 'Norwegian', 'Persian', 'Polish', 'Portuguese', 'Punjabi', 'Quechua', 'Romanian', 'Russian', 'Samoan', 'Serbian', 'Slovak', 'Slovenian', 'Spanish', 'Swahili', 'Swedish', 'Tamil', 'Tatar', 'Telugu', 'Thai', 'Tibetan', 'Tonga', 'Turkish', 'Ukrainian', 'Urdu', 'Uzbek', 'Vietnamese', 'Welsh', 'Xhosa'], 'allowMultipleSelections': False, 'required': True, 'placeholder': 'Select language'}, 'A2': 'Afrikaans', 'Q3': {'text': '<strong>What is your age?</strong>', 'options': ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '28', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73', '75', '75', '76', '77', '78', '79', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '90', '91', '92', '93', '94', '95', '96', '97', '98', '99', '100'], 'allowMultipleSelections': False, 'required': True, 'placeholder': 'Select age'}, 'A3': '18', 'Q4': {'text': '<strong>What is your sex?</strong>', 'options': ['Male', 'Female', 'Other'], 'allowMultipleSelections': False, 'required': True, 'placeholder': 'Select sex'}, 'A4': 'Female'}, 'responses': '{"Q0":{"text":"<strong>What language do you speak most often?</strong>","options":["Afrikaans","Albanian","Arabic","Armenian","Basque","Bengali","Bulgarian","Catalan","Cambodian","Chinese(Mandarin)","Croatian","Czech","Danish","Dutch","English","Estonian","Fiji","Finnish","French","Georgian","German","Greek","Gujarati","Hebrew","Hindi","Hungarian","Icelandic","Indonesian","Irish","Italian","Japanese","Javanese","Korean","Latin","Latvian","Lithuanian","Macedonian","Malay","Malayalam","Maltese","Maori","Marathi","Mongolian","Nepali","Norwegian","Persian","Polish","Portuguese","Punjabi","Quechua","Romanian","Russian","Samoan","Serbian","Slovak","Slovenian","Spanish","Swahili","Swedish","Tamil","Tatar","Telugu","Thai","Tibetan","Tonga","Turkish","Ukrainian","Urdu","Uzbek","Vietnamese","Welsh","Xhosa"],"allowMultipleSelections":false,"required":true,"placeholder":"Select language"},"A0":"English","Q1":{"text":"<strong>What language do you speak at home?</strong>","options":["Afrikaans","Albanian","Arabic","Armenian","Basque","Bengali","Bulgarian","Catalan","Cambodian","Chinese(Mandarin)","Croatian","Czech","Danish","Dutch","English","Estonian","Fiji","Finnish","French","Georgian","German","Greek","Gujarati","Hebrew","Hindi","Hungarian","Icelandic","Indonesian","Irish","Italian","Japanese","Javanese","Korean","Latin","Latvian","Lithuanian","Macedonian","Malay","Malayalam","Maltese","Maori","Marathi","Mongolian","Nepali","Norwegian","Persian","Polish","Portuguese","Punjabi","Quechua","Romanian","Russian","Samoan","Serbian","Slovak","Slovenian","Spanish","Swahili","Swedish","Tamil","Tatar","Telugu","Thai","Tibetan","Tonga","Turkish","Ukrainian","Urdu","Uzbek","Vietnamese","Welsh","Xhosa"],"allowMultipleSelections":false,"required":true,"placeholder":"Select language"},"A1":"English","Q2":{"text":"<strong>What is your mother tongue? (i.e. the first language you learned at home during childhood and still understand to this day.)</strong>","options":["Afrikaans","Albanian","Arabic","Armenian","Basque","Bengali","Bulgarian","Catalan","Cambodian","Chinese(Mandarin)","Croatian","Czech","Danish","Dutch","English","Estonian","Fiji","Finnish","French","Georgian","German","Greek","Gujarati","Hebrew","Hindi","Hungarian","Icelandic","Indonesian","Irish","Italian","Japanese","Javanese","Korean","Latin","Latvian","Lithuanian","Macedonian","Malay","Malayalam","Maltese","Maori","Marathi","Mongolian","Nepali","Norwegian","Persian","Polish","Portuguese","Punjabi","Quechua","Romanian","Russian","Samoan","Serbian","Slovak","Slovenian","Spanish","Swahili","Swedish","Tamil","Tatar","Telugu","Thai","Tibetan","Tonga","Turkish","Ukrainian","Urdu","Uzbek","Vietnamese","Welsh","Xhosa"],"allowMultipleSelections":false,"required":true,"placeholder":"Select language"},"A2":"Afrikaans","Q3":{"text":"<strong>What is your age?</strong>","options":["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","28","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50","51","52","53","54","55","56","57","58","59","60","61","62","63","64","65","66","67","68","69","70","71","72","73","75","75","76","77","78","79","80","81","82","83","84","85","86","87","88","89","90","91","92","93","94","95","96","97","98","99","100"],"allowMultipleSelections":false,"required":true,"placeholder":"Select age"},"A3":"18","Q4":{"text":"<strong>What is your sex?</strong>","options":["Male","Female","Other"],"allowMultipleSelections":false,"required":true,"placeholder":"Select sex"},"A4":"Female"}', 'test_part': 'important', 'trial_type': 'dropdown', 'trial_index': 14, 'time_elapsed': 100611, 'internal_node_id': '0.0-5.0'} '''
# getMeta(stranged)




#loads the word into a list
#DONT UNDERSTAND
listOWords = []
with open ("wordQs.txt", 'r') as common:
	for line in common:
		thisLine = line.rstrip("\n")
		thisLine = thisLine.rstrip(" ")
		listOWords.append(thisLine + ' rt')
		listOWords.append(thisLine + ' response')


#makes dictionary object from the json
dictofUsers = read_content['users']


#given an output location, writes a csv w the exp data 
def writeCsv (outFileName):
	with open(outFileName, 'a') as f:
			fieldnames = ['user' ,'what language do you speak most often?', 'what language do you speak at home?', 'what is your mother tongue?', 'what is your age?', 'what is your sex?']
			fieldnames = fieldnames + listOWords
			print(fieldnames)
			writer = csv.DictWriter(f, fieldnames = fieldnames)
			writer.writeheader()

			for user in read_content['users']:

				usrDict = {}

				# for word in fieldnames:
				# 	usrDict[word] = ''

				profile = dictofUsers[user]
				#print(profile)
				dataInst = json.loads(profile['data'])
				#print(dataInst[11])
				print("  ")
				usrDict['user'] = user 
				usrDict['what language do you speak most often?'] = (dataInst[11]['rawResponses']['A0'])
				usrDict['what language do you speak at home?'] = (dataInst[11]['rawResponses']['A1'])
				usrDict['what is your mother tongue?'] = (dataInst[11]['rawResponses']['A2'])
				usrDict['what is your age?'] = (dataInst[11]['rawResponses']['A3'])
				usrDict['what is your sex?'] = (dataInst[11]['rawResponses']['A4'])

				i = 23

				while i < 166 :
					try:
						#print (dataInst[i])

						atHand = cleanStim2(dataInst[i]['stimulus'])

						if (atHand + ' rt') in fieldnames:
							usrDict[atHand + ' rt'] = dataInst[i]['rt']
							print(dataInst[i]['key_press'])
							if dataInst[i]['key_press'] == 70:
								usrDict[atHand + ' response'] = 'f'
							elif dataInst[i]['key_press'] == 74:
								usrDict[atHand + ' response'] = 'j'

						
					except Exception as e:
						print(e)
						pass

					i = i + 2

				writer.writerow(usrDict)
						


				#print(usrDict)










			# global globalCount
			
			# if globalCount is 0:
			# 	writer.writeheader()

writeCsv('cleandata.csv')