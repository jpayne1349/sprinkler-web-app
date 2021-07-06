Project changed. No longer utilizing this. Summer 2021

I found it to be quite difficult to have the Rpi run programs while also listening for incoming web requests.
My attempts at multithreading, multiple servers, etc. were deep dives that eventually I lacked the knowledge to debug.
The closest I got was a implementing a redis-server / worker configuration that allowed for interuption of the scripts while they
were being run. This would have worked well, had I spent the time to really know what I was doing. :D

My current setup moved the Rpi to my office and added an ESP32 to the sprinkler control cabinet. The Rpi runs an MQTT server, 
as well as a Node-Red server. The ESP32 sub/pubs to topics that the Node-Red server oversees. Basically the ESP32 just waits for commands and then executes them. The Node-Red server communicates with my HomePod and exposes control to our iPhones on the Home app. 

There's still some fine tuning to be done involving loss of power events, like autoreconnect instead of a manual reset of the ESP. But functionally, it works well!
