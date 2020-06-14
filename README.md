netatmo-api-python
==================
1. Clone all files
2. Add your API-Key and login to a fresh netatmo.credentials-File
3. Run "show-stations.py" go get the ID of a station, if you want one special Station
4. Put the Station-ID into the netatmo.credentials
5. Run execute-code.py

If you don't add the Station-ID, the script will take all Station or the first one.

__________________________________________________________

Simple API to access Netatmo weather station data from any python script
For more detailed information see http://dev.netatmo.com

I have no relation with the netatmo company, I wrote this because I needed it myself,
and published it to save time to anyone who would have same needs.

### Install ###

To install lnetatmo simply run:

    python setup.py install

  or

    pip install lnetatmo

Depending on your permissions you might be required to use sudo.
Once installed you can simple add lnetatmo to your python scripts by including:

    import lnetatmo

**New features** (see usage for details)

cameras (Welcome and Presence) : 
 - get live jpeg snapshot with `homeData.getLiveSnapshot(camera="{name}")`
 - get best access url (local if possible else vpn) with `homeData.url(camera="{name}")` and it works despite the is_local property of the camera being mostly false (the camera IP is catched only on camera start and never updated even if the home IP change)

Presence : switch camera on or off with `homeData.presenceStatus("on|off", camera="{name}")`
