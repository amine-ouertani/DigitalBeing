import { getRandomEmptyResponse, startsWithCapital } from "../../utils"
import { addMessageToHistory, exitConversation, getChatHistory, isInConversation, moreThanOneInConversation, onMessageResponseUpdated, prevMessage, prevMessageTimers, sentMessage } from "../chatHistory"
import { botName, username_regex } from "../telegram-client"

export async function onMessage(bot, msg, messageResponseHandler) {
    addMessageToHistory(msg.chat.id, msg.message_id, msg.from.username === undefined ? msg.from.first_name : msg.from.username, msg.text)
    console.log(JSON.stringify(msg))
    const date = Date.now() / 1000
    const msgDate = msg.date
    const diff = date - msgDate
    const hours_diff = Math.ceil(diff/3600)
    const mins_diff = Math.ceil((diff-hours_diff)/60)
    if (mins_diff > 12 || (mins_diff <= 12 && hours_diff > 1)) return
    
    let content = msg.text
    const _sender = msg.from.username === undefined ? msg.from.first_name : msg.from.username
    addMessageToHistory(msg.chat.id, msg.message_id, _sender, content)
    let addPing = false
    if (msg.chat.type == 'supergroup') {
        if (content === '') content = '{sent media}'
        let isReply = false
        if (msg.reply_to_message !== undefined) {
            if (msg.reply_to_message.from.username === botName) isReply = true
            else {
                exitConversation(_sender)
                const _replyTo = msg.reply_to_message.from.username === undefined ? msg.reply_to_message.from.first_name : msg.reply_to_message.from.username
                exitConversation(_replyTo)
                return
            }
        }
        let _prev = undefined
        if (!msg.from.is_bot) {
            _prev = prevMessage[msg.chat.id]
            prevMessage[msg.chat.id] = _sender
            if (prevMessageTimers[msg.chat.id] !== undefined) clearTimeout(prevMessageTimers[msg.chat.id])
            prevMessageTimers[msg.chat.id] = setTimeout(() => prevMessage[msg.chat.id] = '', 120000)
        }
        addPing = (_prev !== undefined && _prev !== '' && _prev !== _sender) || moreThanOneInConversation()

        const isMention = msg.entities !== undefined && msg.entities.length === 1 && msg.entities[0].type === 'mention' && content.includes('@' + process.env.TELEGRAM_BOT_NAME)
        const otherMention = msg.entities !== undefined && msg.entities.length > 0 && msg.entities[0].type === 'mention'  && !content.includes('@' + process.env.TELEGRAM_BOT_NAME)
        let startConv = false
        let startConvName = ''
        if (!isMention && !otherMention) {
            const trimmed = content.trimStart()
            if (trimmed.toLowerCase().startsWith('hi')) {
                const parts = trimmed.split(' ')
                if (parts.length > 1) {
                    if (!startsWithCapital(parts[1])) {
                        startConv = true
                    }
                    else {
                        startConv = false
                        startConvName = parts[1]
                    }
                }
                else {
                    if (trimmed.toLowerCase() === 'hi') {
                        startConv = true
                    } 
                }
            }
        }
        if (otherMention) {
            exitConversation(_sender)
            for(let i = 0; i < msg.entities.length; i++) {
                if (msg.entities[i].type === 'mention') {
                    const _user = msg.text.slice(msg.entities[i].offset + 1, msg.entities[i].length)
                    exitConversation(_user)
                }
            }
        }
        if (!startConv) {
            if (startConvName.length > 0) {
                exitConversation(_sender)
                exitConversation(startConvName)
            }
        }

        const isUserNameMention = content.toLowerCase().replace(',', '').replace('.', '').replace('?', '').replace('!', '').match(username_regex)
        const isInDiscussion = isInConversation(_sender)
        if (!content.startsWith('!') && !otherMention) {
            if (isMention) content = '!ping ' + content.replace('!', '').trim()
            else if (isUserNameMention) content = '!ping ' + content.replace(username_regex, '').trim()   
            else if (isInDiscussion || startConv || isReply) content = '!ping ' + content
        }

        if (!otherMention && content.startsWith('!ping')) sentMessage(_sender)
    }
    else {
        content = '!ping ' + content
    }

    if (content === '!ping ' || !content.startsWith('!ping')) return

    const args = {}
    args['grpc_args'] = {};

    args['parsed_words'] = content.slice('!'.length).trim().split(/ +/g);
    
    args['command_info'] = [
        'ping',
        [ 'HandleMessage' ],
        [ 'sender', 'message', 'client_name', 'chat_id', 'createdAt' ],
        'ping all agents'
      ]
    args['grpc_args']['sender'] = _sender
    if (args['command_info']) {
        args['command'] = args['command_info'][0];
        args['grpc_args']['message'] = content.replace("!" + args['command'], "");
        args['grpc_method'] = args['command_info'][1][0];
        args['grpc_method_params'] = args['command_info'][2];
    }

    args['grpc_args']['client_name'] = 'telegram'
    args['grpc_args']['chat_id'] = msg.chat.id + ''

    const dateNow = new Date();
    var utc = new Date(dateNow.getUTCFullYear(), dateNow.getUTCMonth(), dateNow.getUTCDate(), dateNow.getUTCHours(), dateNow.getUTCMinutes(), dateNow.getUTCSeconds());
    const utcStr = dateNow.getDate() + '/' + (dateNow.getMonth() + 1) + '/' + dateNow.getFullYear() + ' ' + utc.getHours() + ':' + utc.getMinutes() + ':' + utc.getSeconds()
    args['grpc_args']['createdAt'] = utcStr

    await messageResponseHandler(args, (response) => {
        console.log(JSON.stringify(response))
        Object.keys(response.response).map(function(key, index) {
            console.log('response: ' + response.response[key])
            if (response.response[key] !== undefined && response.response[key].length > 0) {
                let text = response.response[key]
                while (text === undefined || text === '' || text.replace(/\s/g, '').length === 0) text = getRandomEmptyResponse()
                if (addPing) bot.sendMessage(msg.chat.id,`<a href="tg://user?id=${msg.from.id}">${msg.from.first_name}</a> ${text}`, {parse_mode: 'HTML'}).then(function (_resp) {
                    onMessageResponseUpdated(_resp.chat.id, msg.message_id, _resp.message_id)
                    addMessageToHistory(_resp.chat.id, _resp.message_id, process.env.BOT_NAME, text)
                    }).catch(console.error)
                else bot.sendMessage(msg.chat.id,text).then(function (_resp) {
                    onMessageResponseUpdated(_resp.chat.id, msg.message_id, _resp.message_id)
                    addMessageToHistory(_resp.chat.id, _resp.message_id, process.env.BOT_NAME, text)
                }).catch(console.error)       
           }
            else {
                let emptyResponse = getRandomEmptyResponse()
                while (emptyResponse === undefined || emptyResponse === '' || emptyResponse.replace(/\s/g, '').length === 0) emptyResponse = getRandomEmptyResponse()
                if (addPing) bot.sendMessage(msg.chat.id,`<a href="tg://user?id=${msg.from.id}">${msg.from.first_name}</a> ${emptyResponse}`, {parse_mode: 'HTML'}).then(function (_resp) {
                    onMessageResponseUpdated(_resp.chat.id, msg.message_id, _resp.message_id)
                    addMessageToHistory(_resp.chat.id, _resp.message_id, process.env.BOT_NAME, emptyResponse)
                    }).catch(console.error)           
                else bot.sendMessage(msg.chat.id,emptyResponse).then(function (_resp) {
                    onMessageResponseUpdated(_resp.chat.id, msg.message_id, _resp.message_id)
                    addMessageToHistory(_resp.chat.id, _resp.message_id, process.env.BOT_NAME, emptyResponse)
                    }).catch(console.error)
            }
        });          
    }).catch(err => console.log(err))
}