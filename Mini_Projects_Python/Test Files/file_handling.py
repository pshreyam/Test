import json
settings={}
settings['users']={'name':'Hari','age':15,'color':'fair'}
settings['config']={'world':'global','terrain':'green'}
obj=open("users.json",'w')
json.dump(settings,obj)
