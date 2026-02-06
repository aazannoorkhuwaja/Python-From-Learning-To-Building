def emoji_language(message):
    message=message.split(" ")
    emojies={
        ':)':'😃',
        ':(':'🙃'
    }
    output=''
    for msg in message:
        output+=emojies.get(msg,msg)+' '
    return output


mesg=input('Enter The Language: ' )
print(emoji_language(mesg))