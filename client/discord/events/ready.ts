import { deleteMessageFromHistory, wasHandled } from "../chatHistory";

module.exports = async (client) => {
    await client.users.fetch(process.env.LOG_DM_USER_ID).then((user) => {
        client.log_user = user
    }).catch((error) => { console.log(error) });

    await client.guilds.cache.forEach((server) => {
        if (!server.deleted) {
            console.log('fetching messages from server: ' + server.name)
            client.api.applications(client.user.id).guilds(server.id).commands.post({
                data: {
                    name: "continue",
                    description: "makes the agent continue"
                }
            });
            client.api.applications(client.user.id).guilds(server.id).commands.post({
                data: {
                    name: "single_continue",
                    description: "test"
                }
            });
            client.api.applications(client.user.id).guilds(server.id).commands.post({
                data: {
                    name: "say",
                    description: "makes the agent say something",
                    options: [{
                        name: 'text',
                        description: 'text',
                        type: 3,
                        required: true
                    }]
                }
            });

            server.channels.cache.forEach(async (channel) => {
                if (channel.type === 'text' && channel.deleted === false && channel.permissionsFor(client.user.id).has(['SEND_MESSAGES', 'VIEW_CHANNEL'])) {
                    channel.messages.fetch({limit: 100}).then(async messages => {
                        messages.forEach(async function (msg) {
                            if (msg.deleted === true) await deleteMessageFromHistory(channel.id, msg.id)
                            else await wasHandled(channel.id, msg.id, msg.author.username, msg.content, msg.createdTimestamp)
                        })
                    })
                }
            })
        }
    });
    
    console.log('client is ready')
}