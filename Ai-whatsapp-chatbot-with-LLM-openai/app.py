# from flask import Flask, request
# app = Flask(__name__)
 
# @app.route('/receive_msg', methods=['POST','GET'])
# def webhook():
#    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
#        if not request.args.get("hub.verify_token")== "your verification token is here":
#            return "Verification token missmatch", 403
#        return request.args['hub.challenge'], 200
#    return "Hello world", 200
 
# if __name__ == "__main__":
#    app.run(debug=True)
#above code run first for verification then eun below code
# _________________________________________________________________________________________________________

# from flask import Flask, request
# import requests
 
# app = Flask(__name__)
 
# @app.route('/')
# def index():
#    return "Hello"
 
# def send_msg(msg):
#    headers = {
#        'Authorization': 'Bearer your authorization given by meta',
#    }
#    json_data = {
#        'messaging_product': 'whatsapp',
#        'to': 'reciever number is here',
#        'type': 'text',
#        "text": {
#            "body": msg
#        }
#    }
#    response = requests.post('https://graph.facebook.com/v17.0/number id is here/messages', headers=headers, json=json_data)
#    print(response.text)
 
 
# @app.route('/receive_msg', methods=['POST','GET'])
# def webhook():
#    print(request)
#    res = request.get_json()
#    print(res)
#    try:
#        if res['entry'][0]['changes'][0]['value']['messages'][0]['id']:
#            send_msg("Thank you for the response.")
#    except:
#        pass
#    return '200 OK HTTPS.'
 
  
# if __name__ == "__main__":
#    app.run(debug=True)

# _________________________________________________________________________________________________________

# from flask import Flask, request
# import openai
# import os
# from dotenv import load_dotenv
# from system import context

# openai.api_key=os.getenv('OPENAI_API_KEY')


# app = Flask(__name__)
 
# def send_msg(msg,receiver_number):

#    headers = {
#        'Authorization': "Bearer os.getenv('VERIFICATION_TOKEN')" 
#    }
#    json_data = {
#        'messaging_product': 'whatsapp',
#        'to': receiver_number,
#        'type': 'text',
#        "text": {
#            "body": msg
#        }
#    }
#    response = requests.post("https://graph.facebook.com/v17.0/number id is here/messages", headers=headers, json=json_data)
#    print(response.text)
 


# @app.route('/receive_msg', methods=['POST','GET'])
# def webhook():
#    res = request.get_json()
#    print(res)
#    message=[]
#    system_msg={"role":"system","content":context}
#    message.append(system_msg)   
#    try:
#        if res['entry'][0]['changes'][0]['value']['messages'][0]['id']:
#             chat_gpt_input=res['entry'][0]['changes'][0]['value']['messages'][0]['text']['body']
#             user_msg={"role": "user", "content": chat_gpt_input}
#             message.append(user_msg)
#             completion = openai.ChatCompletion.create(
#             model="gpt-3.5-turbo",
#             messages=message
#         )
#             response = completion['choices'][0]['message']['content']
#             assistant_msg = {"role": "assistant", "content": response}
#             message.append(assistant_msg)
#             print("ChatGPT Response=>",response)
#             receiver_number=res['entry'][0]['changes'][0]['value']['contacts'][0]['wa_id']
#             send_msg(response,receiver_number)
#    except:
#        pass
#    return '200 OK HTTPS.'
 

# if __name__ == "__main__":
#    app.run(debug=True)


#    ______________________________________________________________________


# from flask import Flask, request
# import requests
# import openai
# import os
# from system import context

# openai.api_key=os.getenv('OPENAI_API_KEY')

# app = Flask(__name__)
 
# def send_msg(msg,receiver_number):

#    headers = {
#        'Authorization': 'Bearer ---',
#    }
#    json_data = {
#        'messaging_product': 'whatsapp',
#        'to': receiver_number,
#        'type': 'text',
#        "text": {
#            "body": msg
#        }
#    }
#    response = requests.post('https://graph.facebook.com/v17.0/132277916635812/messages', headers=headers, json=json_data)
#    print(response.text)
 

# @app.route('/receive_msg', methods=['POST','GET'])
# def webhook():
#    res = request.get_json()
#    print(res)
#    try:
#        if res['entry'][0]['changes'][0]['value']['messages'][0]['id']:
#             chat_gpt_input=res['entry'][0]['changes'][0]['value']['messages'][0]['text']['body']
#             completion = openai.ChatCompletion.create(
#             model="gpt-3.5-turbo",
#             messages=[{"role":"user","content":context},
#                 {"role": "user", "content": chat_gpt_input}],
#                 max_tokens=50
#             )
#             response = completion['choices'][0]['message']['content']
#             print("ChatGPT Response=>",response)
#             receiver_number=res['entry'][0]['changes'][0]['value']['contacts'][0]['wa_id']
#             send_msg(response,receiver_number)
#    except:
#        pass
#    return '200 OK HTTPS.'
 
  
# if __name__ == "__main__":
#    app.run(debug=True)


# _____________________________________________________________________________________________________


from flask import Flask, request
import requests
import openai
import os
from system import context

# Set up your OpenAI API key
openai.api_key = os.getenv('OPENAI_API_KEY')

app = Flask(__name__)

# Verification token for WhatsApp integration
VERIFY_TOKEN = "---"

def send_msg(msg, receiver_number):
    headers = {
        'Authorization': 'Bearer ---',
    }
    json_data = {
        'messaging_product': 'whatsapp',
        'to': receiver_number,
        'type': 'text',
        "text": {
            "body": msg
        }
    }
    response = requests.post('https://graph.facebook.com/v17.0/number id/messages', headers=headers, json=json_data)
    print(response.text)

@app.route('/receive_msg', methods=['POST', 'GET'])
def webhook():
    if request.method == 'GET':
        # Handle the subscription verification request
        hub_mode = request.args.get("hub.mode")
        hub_challenge = request.args.get("hub.challenge")
        if hub_mode == "subscribe" and hub_challenge:
            hub_verify_token = request.args.get("hub.verify_token")
            if hub_verify_token == VERIFY_TOKEN:
                return hub_challenge, 200
            else:
                return "Verification token mismatch", 403
    elif request.method == 'POST':
        # Handle incoming WhatsApp messages
        res = request.get_json()
        print(res)
        try:
            if res['entry'][0]['changes'][0]['value']['messages'][0]['id']:
                chat_gpt_input = res['entry'][0]['changes'][0]['value']['messages'][0]['text']['body']
                completion = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": context},
                              {"role": "user", "content": chat_gpt_input}],
                    max_tokens=50
                )
                response = completion['choices'][0]['message']['content']
                print("ChatGPT Response =>", response)
                receiver_number = res['entry'][0]['changes'][0]['value']['contacts'][0]['wa_id']
                send_msg(response, receiver_number)
        except Exception as e:
            print("Error:", e)

    return '200 OK HTTPS.'

if __name__ == "__main__":
    app.run(debug=True)
