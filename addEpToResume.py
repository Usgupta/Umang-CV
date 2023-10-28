import shutil
import datetime
import git
from PyPDF2 import PdfMerger, PdfReader
repo = git.Repo(search_parent_directories=True)
branch = repo.active_branch

print("creating resume pdf now")

yr = datetime.datetime.now().year
# original = r'UMANG GUPTA RESUME.pdf'

original = r'UMANG GUPTA RESUME ' + str(yr) + '.pdf'
epfile = 'EP_Letter.pdf'
# shutil.copyfile(original, target)
# link = 'https://github.com/Usgupta/Umang-CV/blob/'+branch.name+'/'+target
merger = PdfMerger()
merger.append(PdfReader(open(original, 'rb')))
merger.append(PdfReader(open(epfile, 'rb')))
new = r'UMANG_GUPTA_RESUME_' + str(yr) + '.pdf'
merger.write(new)

# print("resume pdf created, here is the link: " + link)
