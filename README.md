# facesnap
## Open lid, take a pick

![build](https://github.com/jpodivin/facesnap/actions/workflows/main.yml/badge.svg)
![pep8](https://github.com/jpodivin/facesnap/actions/workflows/flake8.yml/badge.svg)

Ever wondered if anyone was touching your laptop while you were away?
If you are like me, you did, and you have probably rigged some sort script
to make sure you know who it was. 

I've recreated the one I used to run in python and turned it into a proper service.
Once installed and running, the facesnap will take 3 pictures,
whenever someone opens a lid of your laptop and store them in the `~/facesnaps` directory.

The delay is set to 1 sec, to increase likelyhood that camera is facing the persons
face, and not something else. 

## Installation

### Prerequisites
Facesnap listens to system messages using pydbus and PyGObject.
Unfortunately, installing PyGObject takes a bit more than a rootless pip. 
Fortunately, the folks behind PyGObject have provided simple [instructions](https://pygobject.readthedocs.io/en/latest/getting_started.html) compatible with all major distros.

### Installing facesnap
In order to get facesnap up and running as service for the root user you need to install the script itself and the unit file to register it with systemd.
Either with sudo, which is easier, but not recommended on the security grounds.
The upside of this approach, if you want to call it that way,
is that pics will get stored in home of the `root`.

And will thus remain only accesible to people with root access.  

```
sudo pip install .
sudo ./installservice.sh
```

Or you can install facesnap as a normal user, which will require couple of tweeks
to the `facesnap.service` file. 

For one the `ExecStart` key must be set to place where you have installed the facesnap.py script. You should also add `User` and `Group` keys.

No matter the method, you will need to reload the units and start the service for the changes to take effect.

```
sudo systemctl daemon-reload
sudo systemctl enable facesnap.service
sudo systemctl start facesnap.service
```

## Adjust the behavior

I would encourage you to survey the script before installation,
but I'm sure you are doing it already. 

So I'll instead suggest that you should consider if the settings are to your liking. For example you might want the images to be stored elswhere, or for them to be taken after shorter delay.

If you are fancy, you can insert a face reckognition algorithm to only store pictures
of actual faces, or to discern your own face, from the faces of others.
The opencv is already in requirements, and not just because of the friendly API.
