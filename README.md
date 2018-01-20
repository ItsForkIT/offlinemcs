# OfflineMCS

## Forks

```
git clone https://github.com/ItsForkIT/offlinemcs.git

```

## Installation steps :
```
$ sudo pip2 install -r requirements.txt
$ python manage.py runserver

```
![Installation steps](img/offlineMCS.gif)

## Adding new data to the Dashboard

### There is a folder outside the `offlineMCS` folder which folder is sync with the blackbox so whenever any new data came we just need sync the dashboard 


## Setting the Sync Folder 

```

Make a DMS/sync folder outside the offlineMCS store the file in this format 
< Type_of_Data_format >_50_< Type_of_Data >_< Phone_Number >_< Destination >_< lat >_< long >_< date_time >_50

```

## Config

###1 : SYNC_URL 

`offlinemcs/offlineMCS/settings.py` set folder `SYNC_URL = os.path.abspath(BASE_DIR + "/../< sync_folder >/")`

###2 : MEDIA_ROOT Folder

`offlinemcs/offlineMCS/settings.py` set folder `MEDIA_ROOT = '../< media_root_folder >/'` 
