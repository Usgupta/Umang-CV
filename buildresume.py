import shutil
import datetime
import git

repo = git.Repo(search_parent_directories=True)
branch = repo.active_branch

print("creating resume pdf now")

yr = datetime.datetime.now().year
original = r'UMANG GUPTA RESUME.pdf'

target = r'UMANG GUPTA RESUME ' + str(yr) + '.pdf'

shutil.copyfile(original, target)
link = 'https://github.com/Usgupta/Umang-CV/blob/'+branch.name+'/'+target

print("resume pdf created, here is the link: " + link)
