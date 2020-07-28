from github import Github

me = Github().get_user('OnikenX')

#https://developer.github.com/v3/repos/hooks/
hooks = Github().get_repo('OnikenX/Planet_Bound').get_hooks()
print(hooks)
names = []
for hook in hooks:
	print(hook)
	names.append(hook.name)

#get a single hook
for name in names:
	print(name)
