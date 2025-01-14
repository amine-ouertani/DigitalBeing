
from json import dumps
import os
import sys

import emoji

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)


# These might be red in your IDE, since we are adding parent dir to path (above)
import agent_params as param
from agents.openchat.agents.gpt3 import GPT3Agent
#from agents.openchat.agents.rasa import RasaAgent
from agents.openchat.openchat import OpenChat
from agents.repeat.repeat import Repeat

from jsondb import jsondb as jsondb
from tcpServer import tcpServer as _server
from postgres import postgres as _db

import logging

logger = logging.getLogger("app.main")

class DigitalBeing():

    def __init__(self, **kwargs):
        try:
            self.jsondb = jsondb()
            self.jsondb.getAgents()
            self.postgres = _db()
            if (os.getenv('LOAD_DISCORD_LOGGER') == 'True'):
                self._server = _server('127.0.0.1', 7778)
            for model_name in param.SELECTED_AGENTS:
                self.context = self.jsondb.getTopicForAgent(model_name.lstrip())
                print('got self context: ' + self.context)
                if model_name == 'gpt3':
                    self.gpt3_agent = GPT3Agent(engine=param.GPT3_ENGINE, context=self.context)
                #elif model_name == 'rasa':
                #    self.rasa_agent = RasaAgent(param.RASA_MODEL_NAME)
                elif model_name =="repeat":
                    self.repeat_agent = Repeat()
                else:
                    self.agent = OpenChat(model=model_name, device=param.DEVICE, environment=param.ENVIRONMENT)
                    self.agent_env = self.agent.create_environment_by_name(self.agent.environment)

        except:
            logger.exception("__init__")

    def sendDiscordMessage(self, text: str):
        try:
            if (hasattr(self, '_server')):
                self._server.sendMessage(text)
        except:
            logger.exception("sendDiscordMessage")

    def handle_message(self, **kwargs):
        try:
            message = kwargs.get('message')
            chat_history = self.postgres.getHistory(int(os.getenv('CHAT_HISTORY_MESSAGES_COUNT')), kwargs.get('client_name'), kwargs.get('chat_id'))
            createdAt = kwargs.get('createdAt')
            if (message == None):
                if (hasattr(self, '_server')):
                    self._server.sendMessage("Exception invoke_solo_agent: invalid kwarg: message")
                print("Exception invoke_solo_agent: invalid kwarg: message")
                return { 'none': 'none' }
            responses_dict = {}
            for model_name in param.SELECTED_AGENTS:
                if model_name == 'gpt3':
                    if ('\n' in message):
                        message = message.replace('\n', "r''")
                    responses_dict['gpt3'] = self.addEmojis(self.gpt3_agent.invoke_api(message=message))
                #elif model_name == 'rasa':
                #    responses_dict['rasa'] = self.addEmojis(self.rasa_agent.invoke(message=message))
                elif model_name == "repeat":
                    responses_dict['repeat'] = self.addEmojis(self.repeat_agent.handle_message(message))
                else:
                    responses_dict[model_name] = self.addEmojis(self.agent_env.start(self.agent.agent, user_message=message, model_name=model_name, context=self.context))
            
            return responses_dict

        except Exception as err:
            logger.exception("handle_message")
            if (hasattr(self, '_server')):
                self._server.sendMessage("Exception handle_message: " + err)
            return { 'none': 'none' }

    def addEmojis(self, msg):
        msg = msg.strip()
        res = ''
        words = msg.split(' ')
        i = 0
        while i < len(words):
            words[i] = emoji.emojize(words[i])
            i += 1
                    
        print(words)
        for x in words:
            res += x + ' '

        return res

    def handle_slash_command(self, **kwargs):
        try:
            chat_history = self.postgres.getHistory(int(os.getenv('CHAT_HISTORY_MESSAGES_COUNT')), kwargs.get('client_name'), kwargs.get('chat_id'))
            chat_history = { kwargs.get('command') + ' ' + kwargs.get('args'): chat_history }
            chat_history = dumps(chat_history)
            print(chat_history)
            return { 'none': 'not implemented' }
        
        except Exception as err:
            logger.exception("handle_message")
            if (hasattr(self, '_server')):
                self._server.sendMessage("Exception handle_message: " + err)
            return { 'none': 'none' }

    def handle_user_update(self, **kwargs):
        try:
            return { 'none': 'not implemented' }
        
        except Exception as err:
            logger.exception("handle_message")
            if (hasattr(self, '_server')):
                self._server.sendMessage("Exception handle_message: " + err)
            return { 'none': 'none' }

    def handle_message_reaction(self, **kwargs):
        try:
            return { 'none': 'not implemented' }
        
        except Exception as err:
            logger.exception("handle_message")
            if (hasattr(self, '_server')):
                self._server.sendMessage("Exception handle_message: " + err)
            return { 'none': 'none' }

    def get_agents(self):
        try:
            return self.jsondb.getAgents()
        except Exception as err:
            logger.exception("get_agents")
            if (hasattr(self, '_server')):
                self._server.sendMessage("Exception get_agents: " + err)
            print("Exception get_agents: " + err)
            return { 'key': 'none', 'value': 'name' }


    def set_agent_fields(self, **kwargs):
        try:
            name = kwargs.get('name')
            if (name == None):
                if (hasattr(self, '_server')):
                    self._server.sendMessage("Exception set_agent_fields: invalid kwarg: name")
                print("Exception set_agent_fields: invalid kwarg: name")
                return {'name': 'none', 'context': 'none'}
            context = kwargs.get('context')
            if (context == None):
                if (hasattr(self, '_server')):
                    self._server.sendMessage("Exception set_agent_fields: invalid kwarg: context")
                print("Exception set_agent_fields: invalid kwarg: context")
                return {'name': 'none', 'context': 'none'}
            self.jsondb.setAgentName(context.lstrip(), name.lstrip())
            return {'name': name, 'context': context}
        except Exception as err:
            logger.exception()
            if (hasattr(self, '_server')):
                self._server.sendMessage("Exception set_agent_fields: " + err)
            print("Exception set_agent_fields: " + err)
            return {'name': 'none', 'context': 'none'}


    def invoke_solo_agent(self, **kwargs):
        try:
            message = kwargs.get('message')
            if (message == None):
                if (hasattr(self, '_server')):
                    self._server.sendMessage("Exception invoke_solo_agent: invalid kwarg: message")
                print("Exception invoke_solo_agent: invalid kwarg: message")
                return { 'key': 'none', 'value': 'none' }
            model_name = kwargs.get('agent')
            if (model_name == None):
                if (hasattr(self, '_server')):
                    self._server.sendMessage("Exception invoke_solo_agent: invalid kwarg: agent")
                print("Exception invoke_solo_agent: invalid kwarg: agent")
                return { 'key': 'none', 'value': 'none' }
            response_dict = {}
            context = self.jsondb.getTopicForAgent(model_name.lstrip())
            if model_name == 'gpt3':
                response_dict['gpt3'] = self.gpt3_agent.invoke_api(message=message)
            #elif model_name == 'rasa':
            #    response_dict['rasa'] = self.rasa_agent.invoke(message=message)
            else:
                response_dict[model_name] = self.agent_env.start(self.agent.agent, user_message=message, model_name=model_name, context=context)
            return response_dict
        except Exception as err:
            logger.exception()
            if (hasattr(self, '_server')):
                self._server.sendMessage("Exception invoke_solo_agent: " + err)
            print("Exception invoke_solo_agent: " + err)
            return { 'key': 'none', 'value': 'none' }