
import thingspeak

channel_id = 1702971 # PUT CHANNEL ID HERE
write_key  = 'PKX85O86NQ6BIQZS' # PUT YOUR WRITE KEY HERE

ch = thingspeak.Channel(id=channel_id, api_key=write_key)

temp = int(input("Enter Air Quality: "))
ch.update({'field1':temp})

print(ch.get())
